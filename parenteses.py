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
