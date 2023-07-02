import q1 as mt
import q2 as sl
import q3 as pd
from viewTree import ViewTree


def menu():
    print("Digite a questão")
    questao = input("> ")

    if questao not in ['q1', 'q2', 'q3']:
        print("[ERRO]: digite q1, q2, ou q3 para as questões\n"
              f"\t\t{questao} não é válido para a opção questão")
    else:
        print("Digite a forma linear")
        linear = input("> ")

        if questao == 'q1':
            tree = mt.linear_to_tree(linear)
            print("[AVISO] A imagem da árvore deve aparecer automaticamente na tela,\n"
                  "caso isso não ocorra entre na pasta output e abra a imagem tree.png")
            ViewTree(tree)
        elif questao == 'q2':
            sl.select_instruction(linear, True)
        elif questao == 'q3':
            padroes = sl.select_instruction(linear)
            pd.gen_code(padroes)


if __name__ == '__main__':
    # MOVE(MEM(+(MEM(+(FP,CONST a)),*(TEMP i,CONST 4))),MEM(+(FP,CONST X)))
    menu()
