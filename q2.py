from node import Node
from q1 import linear_to_tree
import utils as ut

def select_instruction(linear):
    root = linear_to_tree(linear)
    select(root)
    print(root.custo[0])
    print(root.custo[1])
    return root


"""
    Programação dinâmica para escolher a melhor instrução
"""
def select(root):
    # se for uma folha retorna o valor
    if root.left is None and root.right is None:
        root.escolhido = True
        root.custo = (ut.turn_linear(root), 1)
        return root

    # se for uma operação de + - * /
    if root.data in ['+', '-', '*', '/']:
        # testar colocando so o no atual e chamando recursivamente para os filhos
        op_1 = None
        op_2 = None
        op_3 = None

        # testar colocando o no atual e o filho da esquerda
        if root.left is not None:
            op_1 = select(root.left)

        # testar colocando o no atual e o filho da direita
        if root.right is not None:
            op_2 = select(root.right)

        # testar colocando o no atual sem os filhos
        op_3 = root
        root.custo = ([
            root.data,
            ut.turn_linear(root.left),
            ut.turn_linear(root.right)
                      ],
            op_1.custo[1] + op_2.custo[1] + 1
        )

        # calcular o melhor custo
        if op_1.custo[1] < op_2.custo[1] and op_1.custo[1] < op_3.custo[1]:
            root.escolhido = False
            return op_1
        elif op_2.custo[1] < op_1.custo[1] and op_2.custo[1] < op_3.custo[1]:
            root.escolhido = False
            return op_2
        else:
            root.escolhido = True
            return op_3

    # return root


