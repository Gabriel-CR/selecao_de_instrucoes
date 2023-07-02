# Instruções

## Execução

Para executar o código você deve ativar o ambiente virtual venv, nele contém a biblioteca graphviz utilizada para renderizar a árvore em forma de imagem. Para fazer isso basta executar o comando abaixo:

```bash
source venv/bin/activate
```

Após isso, basta executar o arquivo main.py:

```bash
python3 main.py
```

Caso queira desativar o ambiente virtual, basta executar o comando abaixo:

```bash
deactivate
```

Se por algum motivo desejar instalar a biblioteca graphviz ou não conseguir utilizar o venv use o comando:

```bash
pip install graphviz
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
