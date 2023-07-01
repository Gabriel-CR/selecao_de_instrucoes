from node import Node


def turn_list(linearInstructions):
    aux = ''
    res = []
    for i in linearInstructions:
        if i == '(' or i == ')':
            res.append(aux)
            res.append(i)
            aux = ''
        elif i == ',':
            res.append(aux)
            aux = ''
        else:
            aux += i

    res.append(aux)

    # remove '' da lista
    res = [i for i in res if i != '']

    return res


# função que recebe um Node e retorna a árvore em representação linear
def turn_linear(node):
    if node is None:
        return ''

    if node.left is None and node.right is None:
        return node.data

    if node.left is None:
        return node.data + '(' + turn_linear(node.right) + ')'

    if node.right is None:
        return node.data + '(' + turn_linear(node.left) + ')'

    return node.data + '(' + turn_linear(node.left) + ',' + turn_linear(node.right) + ')'


ordem_comandos = []
custo = 0
def pos_ordem(node):
    if node is None:
        return

    # Percorre a subárvore esquerda
    pos_ordem(node.left)

    # Percorre a subárvore direita
    pos_ordem(node.right)

    # Visita o nó atual
    ordem_comandos.append(node.custo[0])
    global custo
    custo += node.custo[1]


def get_ordem(node):
    pos_ordem(node)
    return (ordem_comandos, custo)


if __name__ == "__main__":
    print(turn_list("MEM(+(CONST 1,CONST 2))"))
    print(turn_list("+(CONST 1,CONST 2)"))
    print(turn_list("CONST 1,CONST 2"))
    print(turn_list("+(CONST 1,+(CONST 2,CONST 3))"))
