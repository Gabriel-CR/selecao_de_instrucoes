import q1 as mt
import q2 as sl
import utils as ut


if __name__ == '__main__':
    res_1 = sl.select_instruction("MEM(+(CONST 1,CONST 2))")
    res_2 = sl.select_instruction("MEM(CONST 1)")
    res_2 = sl.select_instruction("MEM(-(+(CONST 3,CONST 4),CONST 5))")
    res_3 = sl.select_instruction("+(+(CONST 1,CONST 2),CONST 5))")
    res_4 = sl.select_instruction("+(+(CONST 1,CONST 2),-(+(CONST 3,CONST 4),CONST 5))")
    res_5 = sl.select_instruction("+(+(CONST 1,CONST 2),-(+(CONST 3,CONST 4),+(CONST 5,CONST 6)))")
    res_6 = sl.select_instruction("+(*(CONST 1,CONST 2),-(/(CONST 4,CONST 5),CONST 3))")



