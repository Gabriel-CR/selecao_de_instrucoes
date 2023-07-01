import q1 as mt
import q2 as sl
import q3 as pd
import utils as ut
from viewTree import ViewTree


if __name__ == '__main__':
    padroes = sl.select_instruction("MOVE(MEM(+(MEM(+(FP,CONST a)),*(TEMP i,CONST 4))),MEM(+(FP,CONST X)))")
    # padroes = sl.select_instruction("+(CONST 1,-(CONST 2,CONST 3))")
    # tree = mt.linear_to_tree("MOVE(MEM(+(MEM(+(FP,CONST a)),*(TEMP i,CONST 4))),MEM(+(FP,CONST X)))")
    ordem, custo = ut.get_ordem(padroes)
    for o in ordem:
        if o != '':
            print(o)

    print(custo)
    # pd.gen_code(padroes.custo[0])





