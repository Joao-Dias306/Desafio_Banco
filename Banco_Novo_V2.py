#Bibliotecas 

import textwrap

import datetime

import pytz


# Variáveis e constantes do sistema bancario

def menu():
    Menu = ('''
        Menu
    [1]\tDeposito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [0]\tSair
        
    Digite o número da transação que deseja efetuar:
    '''
    )
    return input(textwrap.dedent(Menu))

# Em um def tudo que esta antes do '/' deve ser somente passado por sua posicao. Entao ele nao aceitaria se Saldo fosse Saldo=Saldo 

def depositar(Saldo, Valor_Depositado, Extrato, Dia_do_Saque, /):
    if Valor_Depositado > 0:
        Saldo += Valor_Depositado
        Data_transacao = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
        Data_transacao_Brasil = Data_transacao.strftime('%d/%m/%Y -- %H:%M:%S')
        Data_transacao_Brasil_Dia = Data_transacao.strftime('%d/%m/%Y')
        Dia_do_Saque.append(Data_transacao_Brasil_Dia)   
        Extrato += f'Valor depositado de R${Valor_Depositado:.2f}\nTransação realizada no dia: {Data_transacao_Brasil}\n'
        print(f'Valor de R${Valor_Depositado} depositado!!!')

        return Saldo, Extrato, Dia_do_Saque
    
    else:
        print(f'Valor de deposito Inválido. R${Valor_Depositado} não é um valor aceito. \n Por favor digite novamente.')

# Em um def depois de '*' as variaveis sao obrigadas a serem nomeadas como Saldo=Saldo.

def sacar(*, Saldo, Valor_Sacado, Extrato, Limite_Valor_Saques, Numero_Saques, LIMITE_MAXIMO_SAQUES_DIARIOS, Dia_do_Saque):
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
        Data_transacao = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
        Data_transacao_Brasil_Dia = Data_transacao.strftime('%d/%m/%Y')                    
        Data_transacao_Brasil = Data_transacao.strftime('%d/%m/%Y -- %H:%M:%S')
        Extrato += f'Valor sacado de R${Valor_Sacado:.2f}\nTransação realizada no dia: {Data_transacao_Brasil}\n'
        Dia_do_Saque.append(Data_transacao_Brasil_Dia)                    
        print(f'Valor de R${Valor_Sacado} sacado!!!')
        Numero_Saques += 1

    else:
        print(f'Valor digitado Inválido, por favor digite um número.')
    
    return Saldo, Extrato, Dia_do_Saque

def exibir_extrato(Saldo, /, *, Extrato):

    print('\n ================= EXTRATO =================')
    print('Não foram realizadas movimentações.' if not Extrato else Extrato)
    print(f'\nSaldo: R$ {Saldo:.2f}\n')
    print('\n ===========================================')

def filtrar_usuarios(cpf, Usuarios):

# CompreeCompreensão de lista

    Usuarios_Filtrados = [Usuario for Usuario in Usuarios if Usuario['cpf'] == cpf]
    return Usuarios_Filtrados[0] if Usuarios_Filtrados else None

def criar_usuario(Usuarios):
    cpf = input('Informe o CPF (somente números): ')
    Usuario = filtrar_usuarios(cpf, Usuarios)

    if Usuario:
        print('Já existe usuário com esse CPF!')
        return
    
    Nome = input('Informe o nome completo: ')
    Data_de_Nascimento = input('Informe a data de nascimento (dd-mm-aaaa):')
    enderco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado) :')
    Usuarios.append({'Nome' : Nome, 'Data_Nacimento' : Data_de_Nascimento, 'Endereço' : enderco, 'cpf' :cpf})

    print('\nUsuário criado com sucesso!\n')

def criar_conta(AGENCIA, Numero_da_Conta, Usuarios):
    cpf = input('Informe o CPF do usuário: ')
    Usuario = filtrar_usuarios(cpf, Usuarios)

    if Usuario:
        print('Conta criada com sucesso!!!')
        return {'Agencia' : AGENCIA, 'Numero_da_Conta' : Numero_da_Conta}
    
    print('Usuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(Contas):
    for Conta in Contas:
        Linha = f'''
            Agência:\t{Conta['Agencia']}
            C/C:\t\t{Conta['Numero_da_Conta']}
        '''
        print('=' * 100)
        print(textwrap.dedent(Linha))

def main():

    AGENCIA = '0001'

    Dia_do_Saque = [0]
    
    Extrato = ''

    LIMITE_MAXIMO_SAQUES_DIARIOS = 3

    Saldo = 0

    Numero_Saques = 0

    Limite_Valor_Saques = 500

    Usuarios = []

    Contas = []

    Numero_da_Conta = 1

    # Código base para criação do sistema menu do banco

    def Checagem_de_Limite_Diario():

        Data_transacao = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
        Data_transacao_Brasil_Dia = Data_transacao.strftime('%d/%m/%Y')

        if Dia_do_Saque[-1] == Data_transacao_Brasil_Dia:
            if len(Dia_do_Saque) > 10:
                return 'Ultrapassou'



    while True:

        Valor_Digitado = menu()

    #Checa se o valor digitado é um número ou não. Sendo um número ele procede com o código normalmente.
    #Não sendo um número ele vai pedir que o usuário digite novamente.

        if Valor_Digitado.isnumeric():
            
            Valor_Digitado = int(Valor_Digitado)

            if Valor_Digitado == 1:
                Resultado_da_Checagem = Checagem_de_Limite_Diario()

                if Resultado_da_Checagem == 'Ultrapassou':
                    print(f'Excedido o número de transações permitidas para Hoje!!')            

                else:
                    Valor_Depositado = float(input('Digite o valor que deseja depositar: '))

                    Saldo, Extrato, Dia_do_Saque = depositar(Saldo, Valor_Depositado, Extrato, Dia_do_Saque)
                    
                    # Garantir que o valor depositado seja somente positivo.
            
            elif Valor_Digitado == 2:

                Resultado_da_Checagem = Checagem_de_Limite_Diario()

                if Resultado_da_Checagem == 'Ultrapassou':
                    print(f'Excedido o número de transações permitidas para Hoje!!')

                else: 
                    Valor_Sacado = float(input('Digite o valor que Você deseja sacar.'))

                    Saldo, Extrato, Dia_do_Saque = sacar(
                        Saldo=Saldo,
                        Valor_Sacado=Valor_Sacado,
                        Extrato=Extrato,
                        Limite_Valor_Saques=Limite_Valor_Saques,
                        Numero_Saques=Numero_Saques,
                        LIMITE_MAXIMO_SAQUES_DIARIOS=LIMITE_MAXIMO_SAQUES_DIARIOS,
                        Dia_do_Saque=Dia_do_Saque
                    )

                    # Variáveis condicionais para poder sacar o dinheiro.

            elif Valor_Digitado == 3:
                exibir_extrato(Saldo, Extrato=Extrato)

            elif Valor_Digitado == 4:
    
                    Conta = criar_conta(AGENCIA, Numero_da_Conta, Usuarios)

                    if Conta:
                        Contas.append(Conta)
                        Numero_da_Conta += 1
            
            elif Valor_Digitado == 5:
                listar_contas(Contas)

            elif Valor_Digitado == 6:
                criar_usuario(Usuarios)

            elif Valor_Digitado == 0:
                break

            else:
                print(f'Valor digitado Inválido, por favor digite um número.')
        
        else:
            print(f'Valor digitado Inválido, por favor digite um número.')

main()