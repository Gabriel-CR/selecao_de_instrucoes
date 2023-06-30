import q1 as mt
import q2 as sl
import utils as ut


if __name__ == '__main__':
    # res = sl.select_instruction("MEM(+(CONST 1,CONST 2))")
    # res = sl.select_instruction("MEM(CONST 1)")
    # res = sl.select_instruction("MEM(-(+(CONST 3,CONST 4),CONST 5))")
    # res = sl.select_instruction("+(+(CONST 1,CONST 2),CONST 5))")
    # res = sl.select_instruction("+(+(CONST 1,CONST 2),-(+(CONST 3,CONST 4),CONST 5))")
    # res = sl.select_instruction("+(+(CONST 1,CONST 2),-(+(CONST 3,CONST 4),+(CONST 5,CONST 6)))")
    # res = sl.select_instruction("+(*(CONST 1,CONST 2),-(/(CONST 4,CONST 5),CONST 3))")
    # res = sl.select_instruction("MOVE(MEM(+(-(CONST 0,CONST 1),CONST 2)),CONST 3)")
    # res = sl.select_instruction("MOVE(MEM(+(CONST 1,-(CONST 0,CONST 1))),CONST 3)")
    # res = sl.select_instruction("MOVE(MEM(CONST 1),+(CONST 2,CONST 3))")
    res = sl.select_instruction("MOVE(MEM(*(CONST 1,CONST 2)),+(CONST 3,CONST 4))")



