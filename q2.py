from node import Node
from q1 import linear_to_tree
import utils as ut


def select_instruction(linear):
    root = linear_to_tree(linear)
    r = select(root)
    for padrao in r.custo[0]:
        print(padrao)
    print(f"\nCusto da solução: {r.custo[1]}")


# Programação dinâmica para escolher a melhor instrução
def select(root):
    # se for uma folha retorna o valor
    if root.left is None and root.right is None:
        root.escolhido = True
        root.custo = ([ut.turn_linear(root)], 1)
        return root

    # MOVE
    if root.data == 'MOVE':
        if root.left.data == 'MEM':
            if root.left.left.data == '+' and 'CONST' in root.left.left.right.data:
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                aux.left.left = Node(root.left.left.data)
                aux.left.left.right = Node(root.left.left.right.data)
                aux.escolhido = True
                if root.right is not None:
                    r = select(root.right)
                    aux.custo = (r.custo[0], r.custo[1])
                if root.left.left.left is not None:
                    lll = select(root.left.left.left)
                    aux.custo = (aux.custo[0] + lll.custo[0], aux.custo[1] + lll.custo[1])
                aux.custo = ([ut.turn_linear(aux)] + aux.custo[0], 1 + aux.custo[1])
                return aux
            if root.left.left.data == '+' and 'CONST' in root.left.left.left.data:
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                aux.left.left = Node(root.left.left.data)
                aux.left.left.left = Node(root.left.left.left.data)
                aux.escolhido = True
                if root.right is not None:
                    r = select(root.right)
                    aux.custo = (r.custo[0], r.custo[1])
                if root.left.left.right is not None:
                    llr = select(root.left.left.right)
                    aux.custo = (aux.custo[0] + llr.custo[0], aux.custo[1] + llr.custo[1])
                aux.custo = ([ut.turn_linear(aux)] + aux.custo[0], 1 + aux.custo[1])
                return aux
            if root.left.data == 'MEM' and 'CONST' in root.left.left.data:
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                aux.left.left = Node(root.left.left.data)
                aux.escolhido = True
                if root.right is not None:
                    r = select(root.right)
                    aux.custo = (r.custo[0], r.custo[1])
                aux.custo = ([ut.turn_linear(aux)] + aux.custo[0], 1 + aux.custo[1])
                return aux
            if root.right.data != 'MEM':
                aux = Node(root.data)
                aux.left = Node(root.left.data)
                if root.left.left is not None:
                    ll = select(root.left.left)
                    aux.custo = (ll.custo[0], ll.custo[1])
                if root.right is not None:
                    r = select(root.right)
                    aux.custo = (aux.custo[0] + r.custo[0], aux.custo[1] + r.custo[1])
                aux.custo = ([ut.turn_linear(aux)] + aux.custo[0], 1 + aux.custo[1])
                return aux
        # MOVEM
        aux = Node(root.data)
        aux.left = Node(root.left.data)
        aux.right = Node(root.right.data)
        if root.left.left is not None:
            ll = select(root.left.left)
            aux.custo = (ll.custo[0], ll.custo[1])
        if root.right.left is not None:
            rl = select(root.right.left)
            aux.custo = (aux.custo[0] + rl.custo[0], aux.custo[1] + rl.custo[1])
        aux.custo = ([ut.turn_linear(aux)] + aux.custo[0], 2 + aux.custo[1])
        return aux

    # LOAD
    if root.data == "MEM":
        if root.left.data == '+' and 'CONST' in root.left.right.data:
            aux = Node(root.data)
            aux.left = Node(root.left.data)
            aux.left.right = Node(root.left.right.data)
            aux.escolhido = True
            if root.left.left is not None:
                ll = select(root.left.left)
                aux.custo = ([ut.turn_linear(aux)] + ll.custo[0], 1 + ll.custo[1])
                return aux
            aux.custo = ([ut.turn_linear(aux)], 1)
            return aux
        if root.left.data == '+' and 'CONST' in root.left.left.data:
            aux = Node(root.data)
            aux.left = Node(root.left.data)
            aux.left.left = Node(root.left.left.data)
            aux.escolhido = True
            if root.left.right is not None:
                lr = select(root.left.right)
                aux.custo = ([ut.turn_linear(aux)] + lr.custo[0], 1 + lr.custo[1])
                return aux
            aux.custo = ([ut.turn_linear(aux)], 1)
            return aux
        if 'CONST' in root.left.data:
            root.custo = ([ut.turn_linear(root)], 1)
            return root
        l = select(root.left)
        root.custo = (['MEM'] + l.custo[0], 1 + l.custo[1])
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
        if root.data == '-' and "CONST" in root.right.data:
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
