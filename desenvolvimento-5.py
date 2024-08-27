# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        operacao = input("Digite o número para a operação correspondente: ")
        
        if operacao == '0':
            print("Encerrando a calculadora.")
            break
        elif operacao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if operacao == '1':
                    resultado = num1 + num2
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif operacao == '2':
                    resultado = num1 - num2
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif operacao == '3':
                    resultado = num1 * num2
                    print(f"Resultado: {num1} * {num2} = {resultado}")
                elif operacao == '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado: {num1} / {num2} = {resultado}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
            except ValueError:
                print("Erro: Você deve digitar números válidos.")
        else:
            print("Essa opção não existe.")

calculadora()
