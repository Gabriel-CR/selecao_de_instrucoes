import q1 as mt
import q2 as sl
import utils as ut
from viewTree import ViewTree


if __name__ == '__main__':
    # t = mt.linear_to_tree("MOVE(MEM(+(MEM(+(FP,CONST A)),*(TEMP i,CONST 4))),MEM(+(FP,CONST X)))")
    # a = ViewTree(t)
    # dando erro, debugar para arrumar
    sl.select_instruction("MOVE(MEM(+(MEM(+(FP,CONST A)),*(TEMP i,CONST 4))),MEM(+(FP,CONST x)))")
    # sl.select_instruction("+(MEM(+(FP,CONST A)),*(TEMP i,CONST 4))")



