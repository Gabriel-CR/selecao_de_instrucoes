# Instruções

## Execução

Para executar o código você deve ativar o ambiente virtual venv, e instalar a biblioteca graphviz, utilizada para renderizar a árvore em forma de imagem. Para fazer isso basta executar os comandos abaixo:

```bash
source venv/bin/activate
pip install graphviz
```

Após isso, basta executar o arquivo main.py:

```bash
python3 main.py
```

Caso queira desativar o ambiente virtual, execute o comando abaixo:

```bash
deactivate
```

## Entradas

As entradas devem ser em formato linear, por exemplo:

```bash
MOVE(MEM(+(MEM(+(FP,CONST a)),*(TEMP i,CONST 4))),MEM(+(FP,CONST X)))
```

Note que não há espaços entre os tokens, tendo isso em vista, uma entrada errada seria:

```bash
+(CONST 1, CONST 2)
```

O erro está no espaço após a vírgula, uma entrada válida para o nosso programa seria colocar espaços apenas ao usar CONST ou TEMP, por exemplo:

```bash
+(CONST 1,CONST 2)
```

```bash
+(TEMP i,CONST 2)
```

## Uso do programa

Após a execução do código irá aparecer a seguinte mensagem no terminal:

```bash
Digite a questão
>
```

Vocẽ deve digitar:

- q1: para executar a questão 1
- q2: para executar a questão 2
- q3: para executar a questão 3

Qualquer valor diferente destes será considerado um erro e aparecerá a seguinte mensagem:

```bash
Digite a questão
> q4
[ERRO]: digite q1, q2, ou q3 para as questões
		q4 não é válido para a opção questão
```

Em caso de sucesso, será exibido a mensagem:

```bash
Digite a questão
> q1
Digite a forma linear
>
```

Você deve digitar a forma linear da árvore, por exemplo:

```bash
Digite a questão
> q1
Digite a forma linear
> MOVE(MEM(+(MEM(+(FP,CONST a)),*(TEMP i,CONST 4))),MEM(+(FP,CONST X)))
```

Em seguida será exibido o resultado da questão selecionada, dado a forma linear digitada, para cada questão o resultado será diferente, por exemplo:

- Para a questão 1: será exibido a árvore em forma de imagem
- Para a questão 2: será exibido os padrões selecionados (na forma linear) seguido pelo custo da solução gerada
- Para a questão 3: será exibido o código equivalente aos padrões selecionados na questão 2

## Github

Se necessário, o código está disponível em: https://github.com/Gabriel-CR/selecao_de_instrucoes
