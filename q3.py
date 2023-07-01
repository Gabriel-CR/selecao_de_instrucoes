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


def get_code(padrao):
    if MOVEM(padrao):
        return f"MOVEM \tM[rj] <- M[ri]"

    if STORE(padrao):
        return f"STORE \tM[rj + c] <- ri"

    if LOAD(padrao):
        return f"LOAD \tr1 <- M[rj + c]"

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
    num_registrador = 1
    for padrao in padroes:
        print(padrao)
        # print(get_code(padrao))

