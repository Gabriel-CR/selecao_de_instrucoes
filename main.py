import q1 as mt
import q2 as sl
import utils as ut


if __name__ == '__main__':
    res = sl.select_instruction("MOVE(MEM(*(CONST 1,CONST 2)),+(CONST 3,CONST 4))")
    print(res.custo[0])
    print(res.custo[1])



