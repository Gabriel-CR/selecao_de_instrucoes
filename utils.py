def findParent(linearInstructions):
    for i in range(len(linearInstructions)):
        if linearInstructions[i] == '(':
            return i


def parentBalanced(linearInstructions):
    posicao = findParent(linearInstructions)
    if posicao == None:
        return (linearInstructions, None)
    else:
        return (linearInstructions[:posicao], linearInstructions[posicao + 1:-1])


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


if __name__ == "__main__":
    print(turn_list("MEM(+(CONST 1,CONST 2))"))
    print(turn_list("+(CONST 1,CONST 2)"))
    print(turn_list("CONST 1,CONST 2"))
    print(turn_list("+(CONST 1,+(CONST 2,CONST 3))"))
