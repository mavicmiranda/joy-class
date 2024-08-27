


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
