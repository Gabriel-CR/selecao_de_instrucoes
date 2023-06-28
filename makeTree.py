import utils
from node import Node


def linear_to_tree(expression):
    stack = []  # Pilha para armazenar os nós ancestrais
    root = None  # Nó raiz da árvore
    current_node = None  # Nó atual sendo construído

    lista = utils.turn_list(expression)

    for i in range(len(lista)):
        if current_node is None:
            current_node = Node(lista[i])
            root = current_node
            stack.append(current_node)
        else:
            if lista[i] == '(':
                stack.append(current_node)
            elif lista[i] == ')':
                current_node = stack.pop()
            else:
                current_node = Node(lista[i])
                if stack[-1].left is None:
                    stack[-1].left = current_node
                else:
                    stack[-1].right = current_node

    return root


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.right, level + 1)

    return


if __name__ == "__main__":
    from viewTree import ViewTree

    root = []
    root.append(linear_to_tree("MEM(+(CONST 1,CONST 2))"))
    root.append(linear_to_tree("+(CONST 1,CONST 2)"))
    root.append(linear_to_tree("CONST 1,CONST 2"))
    root.append(linear_to_tree("+(CONST 1,+(CONST 2,CONST 3))"))
    root.append(linear_to_tree("+(CONST 1,+(CONST 2,+(CONST 3,CONST 4)))"))

    viewTree = ViewTree(root[4])


