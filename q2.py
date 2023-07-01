from node import Node
from q1 import linear_to_tree
import utils as ut


def select_instruction(linear, show=False):
    root = linear_to_tree(linear)
    select(root)
    return root


# Programação dinâmica para escolher a melhor instrução
def select(root):
    # se for uma folha retorna o valor
    if root.left is None and root.right is None:
        root.custo = (ut.turn_linear(root), 1)
        return

    # MOVE
    if root.data == 'MOVE':
        if root.left.data == 'MEM':
            if root.left.left.data == '+' and 'CONST' in root.left.left.right.data:
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                aux.left.left = Node(root.left.left.data)
                aux.left.left.right = Node(root.left.left.right.data)
                if root.right is not None:
                    select(root.right)
                if root.left.left.left is not None:
                    select(root.left.left.left)
                root.custo = (ut.turn_linear(aux), 1)
                return
            if root.left.left.data == '+' and 'CONST' in root.left.left.left.data:
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                aux.left.left = Node(root.left.left.data)
                aux.left.left.left = Node(root.left.left.left.data)
                if root.right is not None:
                    select(root.right)
                if root.left.left.right is not None:
                    select(root.left.left.right)
                root.custo = (ut.turn_linear(aux), 1)
                return
            if root.left.data == 'MEM' and 'CONST' in root.left.left.data:
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                aux.left.left = Node(root.left.left.data)
                if root.right is not None:
                    select(root.right)
                root.custo = (ut.turn_linear(aux), 1)
                return
            if root.right.data != 'MEM':
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                if root.left.left is not None:
                    select(root.left.left)
                if root.right is not None:
                    select(root.right)
                root.custo = (ut.turn_linear(aux), 1)
                return
        # MOVEM
        aux = Node(root.data)
        aux.left = Node(root.left.data)
        aux.right = Node(root.right.data)
        if root.left.left is not None:
            select(root.left.left)
        if root.right.left is not None:
            select(root.right.left)
        root.custo = (ut.turn_linear(aux), 2)
        return

    # LOAD
    if root.data == "MEM":
        if root.left.data == '+' and 'CONST' in root.left.right.data:
            aux = Node(root.data)
            aux.left = Node(root.left.data)
            aux.left.right = Node(root.left.right.data)
            if root.left.left is not None:
                select(root.left.left)
                root.custo = (ut.turn_linear(aux), 1)
                return
            root.custo = (ut.turn_linear(aux), 1)
            return
        if root.left.data == '+' and 'CONST' in root.left.left.data:
            aux = Node(root.data)
            aux.left = Node(root.left.data)
            aux.left.left = Node(root.left.left.data)
            if root.left.right is not None:
                select(root.left.right)
                root.custo = (ut.turn_linear(aux), 1)
                return
            root.custo = (ut.turn_linear(aux), 1)
            return
        if 'CONST' in root.left.data:
            root.custo = (ut.turn_linear(root), 1)
            return
        select(root.left)
        root.custo = ('MEM', 1)
        return

    # se for uma operação de + - * /
    if root.data in ['+', '-', '*', '/']:
        # ADDI
        if root.data == '+' and "CONST" in root.right.data:
            aux = Node(root.data)
            aux.right = root.right
            # calcular o custo do lado left
            if root.left is not None:
                select(root.left)
            root.custo = (ut.turn_linear(aux), 1)
            return
        if root.data == '+' and "CONST" in root.left.data:
            aux = Node(root.data)
            aux.left = root.left
            if root.right is not None:
                select(root.right)
            root.custo = (ut.turn_linear(aux), 1)
            return
        # SUBI
        if root.data == '-' and "CONST" in root.right.data:
            aux = Node(root.data)
            aux.right = root.right
            if root.left is not None:
                select(root.left)
            root.custo = (ut.turn_linear(aux), 1)
            return
        # ADD, MUL, SUB, DIV
        if root.left is not None:
            select(root.left)
        if root.right is not None:
            select(root.right)
        root.custo = (root.data, 1)
        return
