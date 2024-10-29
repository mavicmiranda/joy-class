# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


import datetime

def main():
    ano_atual = 2022 
    
    nome_completo = input("Digite seu nome completo: ")
    
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                raise ValueError("Ano fora do intervalo permitido.")
            
            idade = ano_atual - ano_nascimento
            
            print(f"\n{nome_completo}, você completou ou completará {idade} anos em {ano_atual}.")
            break
        
        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, insira um ano válido.")


main()
