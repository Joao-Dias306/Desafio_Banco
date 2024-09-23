# Variáveis e constantes do sistema bancario

Menu = ('''
    Menu
[1] Deposito
[2] Saque
[3] Extrato
[0] Sair
    
Digite o número da transação que deseja efetuar:
'''
)
Extrato = ''

LIMITE_MAXIMO_SAQUES_DIARIOS = 3

Saldo = 0

Numero_Saques = 0

Limite_Valor_Saques = 500

# Código base para criação do sistema menu do banco

while True:
    Valor_Digitado = input(Menu)

#Checa se o valor digitado é um número ou não. Sendo um número ele procede com o código normalmente.
#Não sendo um número ele vai pedir que o usuário digite novamente.

    if Valor_Digitado.isnumeric():
        
        Valor_Digitado = int(Valor_Digitado)

        if Valor_Digitado == 1:
    
            Valor_Depositado = float(input('Digite o valor que deseja depositar: '))
            
            # Garantir que o valor depositado seja somente positivo.

            if Valor_Depositado > 0:
                Saldo += Valor_Depositado
                Extrato += 'Valor depositado de ' + str(Valor_Depositado) + '\n'
                print(f'Valor de R${Valor_Depositado} depositado!!!')

            else:
                print(f'Valor de deposito Inválido. {Valor_Depositado} não é um valor aceito. \n Por favor digite novamente.')

        
        elif Valor_Digitado == 2:

            Valor_Sacado = float(input('Digite o valor que Você deseja sacar.'))

            # Variáveis condicionais para poder sacar o dinheiro.

            Excedeu_Saldo = Valor_Sacado > Saldo

            Excedeu_Saques = Numero_Saques >= LIMITE_MAXIMO_SAQUES_DIARIOS

            Excedeu_Limite = Valor_Sacado > Limite_Valor_Saques

            if Excedeu_Limite:
                print('Operação Inválida! O valor do saque excede o limite de R$500 por saque.')

            elif Excedeu_Saldo:
                print('Operação Inválida! Você não tem saldo suficiente.')
            
            elif Excedeu_Saques:
                print('Operação Inválida! Número máximo de saques excedido.')

            # Garantindo que o valor sacado seja maior que 0
            elif Valor_Sacado > 0 :
                Saldo -= Valor_Sacado
                Extrato += 'Valor sacado de ' + str(Valor_Sacado) + '\n'
                print(f'Valor de R${Valor_Sacado} sacado!!!')
                Numero_Saques += 1

            else:
                print(f'Valor digitado Inválido, por favor digite um número.')
        
        elif Valor_Digitado == 3:
            print('\n ================= EXTRATO =================')
            print('Não foram realizadas movimentações.' if not Extrato else Extrato)
            print(f'\nSaldo: R$ {Saldo:.2f}\n')

        elif Valor_Digitado == 0:
            break

        else:
            print(f'Valor digitado Inválido, por favor digite um número.')
    
    else:
        print(f'Valor digitado Inválido, por favor digite um número.')
