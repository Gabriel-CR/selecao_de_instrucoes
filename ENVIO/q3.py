import utils as ut
import q1 as mt


def ADD(p):
    if p == '+':
        return True
    return False


def MUL(p):
    if p == '*':
        return True
    return False


def SUB(p):
    if p == '-':
        return True
    return False


def DIV(p):
    if p == '/':
        return True
    return False


def ADDI(p):
    linear = ut.turn_list(p)
    linear = [x for x in linear if x not in ['(', ')']]
    if 'CONST' in linear[0]:
        return True
    if linear[0] == '+' and len(linear) > 1:
        return True
    return False


def SUBI(p):
    linear = [x for x in ut.turn_list(p) if x not in ['(', ')']]
    if linear[0] == '-' and len(linear) > 1:
        return True
    return False


def LOAD(p):
    linear = [x for x in ut.turn_list(p) if x not in ['(', ')']]
    if linear[0] == 'MEM':
        return True
    return False


def STORE(p):
    linear = [x for x in ut.turn_list(p) if x not in ['(', ')']]
    if linear[0] == 'MOVE' and linear[1] == 'MEM':
        return True
    return False


def MOVEM(p):
    linear = [x for x in ut.turn_list(p) if x not in ['(', ')']]
    if linear[0] == 'MOVE' and linear[1] == 'MEM' and linear[2] == 'MEM':
        return True
    return False


num_registrador = 0
stack = []
def pos_ordem(node):
    global num_registrador
    global stack
    if node is None:
        return

    # Percorre a subárvore esquerda
    pos_ordem(node.left)
    # Percorre a subárvore direita
    pos_ordem(node.right)

    if node.custo[0] == '':
        return
    if node.custo[0] == 'FP':
        node.code = 'FP'
        stack.append(f"r{num_registrador + 1}")
        num_registrador += 1
        return
    if 'TEMP' in node.custo[0]:
        node.code = f"r{node.custo[0][5:]}"
        return

    if MOVEM(node.custo[0]):
        rj = node.left.left.code
        ri = node.right.left.code
        print(f"MOVEM \tM[{rj}] <- M[{ri}]")
        return
    if STORE(node.custo[0]):
        rj = ''
        c = ''
        ri = node.right.code

        if node.left.left.custo[0] != '':
            rj = node.left.left.code
            c = 0
        elif 'CONST' in node.left.left.data:
            rj = 'r0'
            c = node.left.left.data[6:]
        elif node.left.left.right.custo[0] != '':
            rj = node.left.left.right.code
            c = node.left.left.left.data[6:]
        else:
            rj = node.left.left.left.code
            c = node.left.left.right.data[6:]

        print(f"STORE \tM[{rj} + {c}] <- {ri}")
        return
    if LOAD(node.custo[0]):
        ri = ''
        rj = ''
        c = ''

        if node.left.custo[0] != '':
            ri = f"r{num_registrador + 1}"
            num_registrador += 1
            rj = node.left.code
            c = '0'
        elif 'CONST' in node.left.data:
            ri = f"r{num_registrador + 1}"
            num_registrador += 1
            rj = 'r0'
            c = node.left.data[6:]
        elif node.left.right.custo[0] != '':
            rj = node.left.right.code
            if rj[0] == 'r' and len(rj) > 1:
                ri = rj
            else:
                ri = f"r{num_registrador + 1}"
                num_registrador += 1
            c = node.left.left.data[6:]
        else:
            rj = node.left.left.code
            if rj[0] == 'r' and len(rj) > 1:
                ri = rj
            else:
                ri = f"r{num_registrador + 1}"
                num_registrador += 1
            c = node.left.right.data[6:]

        node.code = ri
        print(f"LOAD \t{ri} <- M[{rj} + {c}]")
        return
    if SUBI(node.custo[0]):
        ri = ''
        rj = node.left.code
        c = node.right.data[6:]

        if rj[0] == 'r' and len(rj) > 1:
            ri = rj
        else:
            ri = f"r{num_registrador + 1}"
            num_registrador += 1

        node.code = ri
        print(f"SUBI \t{ri} <- {rj} - {c}")
        return
    if ADDI(node.custo[0]):
        ri = ''
        rj = ''
        c = ''

        if node.custo[0][:5] == 'CONST':
            print(1)
            ri = f"r{num_registrador + 1}"
            num_registrador += 1
            rj = 'r0'
            c = node.data[6:]
        elif node.right.custo[0] != '':
            print(2)
            rj = node.right.code
            if rj[0] == 'r' and len(rj) > 1:
                print(3)
                ri = rj
            else:
                print(4)
                ri = f"r{num_registrador + 1}"
                num_registrador += 1
            c = node.left.data[6:]
        else:
            print(5)
            rj = node.left.code
            if rj[0] == 'r' and len(rj) > 1:
                print(6)
                ri = rj
            else:
                print(7)
                ri = f"r{num_registrador + 1}"
                num_registrador += 1
            c = node.right.data[6:]

        node.code = ri
        print(f"ADDI \t{ri} <- {rj} + {c}")
        return

    if node.data in ['+', '-', '*', '/']:
        ri = node.left.code if node.left.code != 'ri' else node.right.code
        # num_registrador += 1
        rj = node.left.code
        rk = node.right.code
        if node.data == '+':
            print(f"ADD \t{ri} <- {rj} {node.data} {rk}")
        elif node.data == '-':
            print(f"SUB \t{ri} <- {rj} - {rk}")
        elif node.data == '*':
            print(f"MUL \t{ri} <- {rj} * {rk}")
        elif node.data == '/':
            print(f"DIV \t{ri} <- {rj} / {rk}")

        node.code = ri
        return


def get_code(padrao, node=None):
    if MOVEM(padrao):
        return f"MOVEM \tM[rj] <- M[ri]"
    if STORE(padrao):
        return f"STORE \tM[rj + c] <- ri"
    if LOAD(padrao):
        return f"LOAD \tri <- M[rj + c]"
    if ADDI(padrao):
        return f"ADDI \tri <- rj + c"
    if SUBI(padrao):
        return f"SUBI \tri <- rj - c"
    if ADD(padrao):
        return f"ADD \tri <- rj + rk"
    if MUL(padrao):
        return f"MUL \tri <- rj * rk"
    if SUB(padrao):
        return f"SUB \tri <- rj - rk"
    if DIV(padrao):
        return f"DIV \tri <- rj / rk"

def gen_code(padroes):
    for padrao in padroes:
        c = get_code(padrao)
        if c is not None:
            print(c)
        # else:
        #     print(padrao)
