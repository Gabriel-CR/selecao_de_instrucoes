import q1 as mt
import q2 as sl
import q3 as pd
import utils as ut
from viewTree import ViewTree


if __name__ == '__main__':
    # padroes = sl.select_instruction("+(CONST 2,-(CONST 1,CONST 3))")
    padroes = sl.select_instruction("MOVE(MEM(+(MEM(+(FP,CONST A)),*(TEMP i,CONST 4))),MEM(+(FP,CONST X)))")
    pd.gen_code(padroes.custo[0])





