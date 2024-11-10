# Balanço de Parênteses I (Beecrowd - Problema 1068)

## Descrição
O problema consiste em verificar o **balanceamento de parênteses** em várias expressões. A tarefa é indicar se a quantidade de parênteses em cada expressão está correta ou não, **ignorando o conteúdo da expressão**. 

### Exemplo de Expressões Corretas
- `a+(b*c)-2-a` → correto
- `(a+b*(2-c)-2+a)*2` → correto

### Exemplo de Expressões Incorretas
- `(a*b-(2+c)` → incorreto
- `2*(3-a))` → incorreto
- `)3+b*(2-c)(` → incorreto

### Regras
- Todo parêntese de fechamento `)` deve ter um parêntese de abertura correspondente `(`.
- Não deve haver parênteses fechados sem um parêntese de abertura prévio.
- A quantidade total de parênteses de abertura e fechamento deve ser igual.

## Entrada
A entrada contém **várias expressões** (1 ≤ N ≤ 10.000), cada uma com até **1000 caracteres**. A entrada é lida até o **EOF (End of File)**.

## Saída
Para cada expressão da entrada, o programa deve imprimir:
- `"correct"` se os parênteses estão balanceados.
- `"incorrect"` se os parênteses estão desequilibrados.

### Exemplo de Entrada
```
a+(b*c)-2-a 
(a+b*(2-c)-2+a)*2 
(a*b-(2+c) 
2*(3-a))  
)3+b*(2-c)(
```

### Exemplo de Saída
```
correct
correct
incorrect
incorrect
incorrect
```

## Solução

### Lógica Utilizada
O problema é resolvido usando o conceito de **pilha**:
1. **Iterar por cada caractere da expressão**:
   - Se for um parêntese de abertura `(`, adicionamos à pilha.
   - Se for um parêntese de fechamento `)`, verificamos:
     - Se a pilha está vazia, significa que há um fechamento sem abertura, então a expressão é `"incorrect"`.
     - Caso contrário, removemos o parêntese de abertura correspondente da pilha.
2. **Após percorrer a expressão**:
   - Se a pilha estiver vazia, a expressão está balanceada (`"correct"`).
   - Se ainda houver itens na pilha, significa que há parênteses de abertura não fechados (`"incorrect"`).

### Implementação em Python
```python
import sys

def verificar_balanceamento(expressao):
    pilha = []
    
    # Percorre cada caractere da expressão
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return "incorrect"
            pilha.pop()
    
    return "correct" if not pilha else "incorrect"

def main():
    # Lê todas as linhas até o EOF
    for linha in sys.stdin:
        expressao = linha.strip()
        if expressao:
            print(verificar_balanceamento(expressao))

if __name__ == "__main__":
    main()
```

### Explicação do Código
- Utilizamos `sys.stdin` para **ler todas as linhas até o EOF**, pois o Beecrowd utiliza essa abordagem para entrada de dados.
- A função `verificar_balanceamento` utiliza uma **pilha** para rastrear os parênteses.
- O programa imprime `"correct"` ou `"incorrect"` para cada expressão analisada.

### Complexidade
- A complexidade é **O(n)** para cada expressão, onde `n` é o número de caracteres da expressão.
- O uso de uma pilha garante que cada caractere seja processado uma única vez, tornando a solução eficiente mesmo para o limite máximo de entradas.

## Como Executar
Para testar o código em um ambiente local:
1. Salve o código em um arquivo, por exemplo, `parenteses.py`.
2. Abra um terminal e execute:
   ```bash
   python3 parenteses.py < input.txt
   ```
   Onde `input.txt` é um arquivo que contém as expressões a serem testadas.

## Notas Finais
Este problema é uma introdução ao uso de estruturas de dados como pilhas para resolver problemas de balanceamento de expressões. É útil em diversas áreas, como análise de expressões matemáticas, análise de código-fonte, entre outros.
