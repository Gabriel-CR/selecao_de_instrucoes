from node import Node
from q1 import linear_to_tree
import utils as ut

def select_instruction(linear):
    root = linear_to_tree(linear)
    r = select(root)
    print(r.custo[0])
    print(r.custo[1])
    return root


"""
    Programação dinâmica para escolher a melhor instrução
"""
def select(root):
    # se for uma folha retorna o valor
    if root.left is None and root.right is None:
        root.escolhido = True
        root.custo = ([ut.turn_linear(root)], 1)
        return root

    # se for uma operação de + - * /
    if root.data in ['+', '-', '*', '/']:
        # ADDI
        if root.data == '+' and "CONST" in root.right.data:
            aux = Node(root.data)
            aux.right = root.right
            aux.escolhido = True
            # calcular o custo do lado left
            if root.left is not None:
                l = select(root.left)
                aux.custo = ([ut.turn_linear(aux)] + l.custo[0], 1 + l.custo[1])
            else:
                aux.custo = ([ut.turn_linear(aux)], 1)
            return aux
        if root.data == '+' and "CONST" in root.left.data:
            aux = Node(root.data)
            aux.left = root.left
            aux.escolhido = True
            # calcular custo do lado right
            if root.right is not None:
                r = select(root.right)
                aux.custo = ([ut.turn_linear(aux)] + r.custo[0], 1 + r.custo[1])
            else:
                aux.custo = ([ut.turn_linear(aux)], 1)
            return aux
        # SUBI
        if root.data == '-'and "CONST" in root.right.data:
            aux = Node(root.data)
            aux.right = root.right
            aux.escolhido = True
            # calcular o custo do lado l
            if root.left is not None:
                l = select(root.left)
                aux.custo = ([ut.turn_linear(aux)] + l.custo[0], 1 + l.custo[1])
            else:
                aux.custo = ([ut.turn_linear(aux)], 1)
            return aux
        # ADD, MUL, SUB, DIV
        if root.left is not None:
            l = select(root.left)
            root.custo = (root.custo[0] + l.custo[0], root.custo[1] + l.custo[1])
        if root.right is not None:
            r = select(root.right)
            root.custo = (root.custo[0] + r.custo[0], root.custo[1] + r.custo[1])
        root.custo = ([root.data] + root.custo[0], root.custo[1] + 1)
        return root

