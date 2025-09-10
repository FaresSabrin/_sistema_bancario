# TODO: por mascara no dia e hora
import os
from time import sleep
from datetime import datetime

list_num_menu=list() # guarda a quantidade de numeros do menu chamado
lista=list()

def mascara(f):
    def wrapper(*args, **kwargs):
        limpaTerminal()
        print('='*30)
        print(f'{f.__name__.upper()}'.center(30))
        print('='*30)
        return f(*args, **kwargs)
    return wrapper

def limpaTerminal(): # limpa o terminal
    os.system('cls' if os.name=='nt' else 'clear')

@mascara
def menu_principal():
    menu={'1':'CRIAR CONTA', '2':'ACESSAR CONTA'}
    lerMenu(menu)
    print('='*30)
    if numeroMenu() == 1:
        cria_conta()
    else:
        acessa_conta()

@mascara
def menu_conta(cliente):
    print(f'Nome: {cliente["nome"].split()[0].capitalize()} - Conta: {cliente["agencia"]}'.center(30))
    menu={'1':'DEPOSITAR', '2':'SACAR','3':'EXTRATO', '4':'SAIR'}
    lerMenu(menu)
    print('='*30)
    num=numeroMenu()
    if num == 1: menu_deposito()
    elif num == 2: menu_sacar()
    elif num == 3: menu_extrato(extrato, saldo)
    elif num == 4: menu_principal()

def lerMenu(menu):
    list_num_menu.clear()
    for x, y in menu.items():
        list_num_menu.append(int(x))
        print(f'[{x}] {y}')

def numeroMenu():
    while True:
        num=int(input('Opção: '))
        if num not in list_num_menu:
            print('Opção invalida!')
        else:
            return num 

def cria_conta():
    formulario(valida_CPF(menu_principal, 'criarConta'))

@mascara
def acessa_conta():
    menu_conta(valida_CPF(menu_principal, 'acessarConta'))
    
@mascara
def formulario(cpf):
    print(f'CPF: {cpf}')
    nome=input('Nome completo: ')
    local=input('Endereço: ')
    fone=input('Telefone: ')
    conta='0001'
    agencia=f'{cpf[0:2]}{cpf[3:5]}{cpf[-2:]}-{fone[-1]}'
    data=datetime.now()
    cliente=f'{nome},{cpf},{local},{fone},{conta},{agencia},{data}'
    with open('listaCPF.txt','a') as arq:
        arq.write(f'{cliente}\n')
        print('Cadastro realizado!')
        print('Voltando ao menu Principal em: ')
        for i in range(10,0,-1):
            print(f'\r{i}  ', end='', flush=True)
            sleep(0.5)
    menu_principal()

@mascara
def valida_CPF(voltar, modo):
    cliente=dict()
    cpf=input('Digite seu CPF: ')
    with open('listaCPF.txt','r') as arq:
        for linha in arq:
            linha=linha.strip()
            nome, cpfCliente, local, fone, conta, agencia, data=linha.split(',')
            cliente[cpfCliente]={
                'nome':nome,
                'local':local,
                'fone':fone,
                'conta':conta,
                'agencia':agencia,
                'data':data
            }

        if modo == 'criarConta':
            if cpf in cliente:
                print(f'CPF ja possui conta! Voltando ao menu: ')
                for i in range(10,0,-1):
                    print(f'\r{i}  ', end='', flush=True)
                    sleep(0.5)
                voltar()
            else:
                return cpf
            
        elif modo == 'acessarConta':
            if cpf in cliente:
                return cliente[cpf]
            else:
                print('CPF não possui conta!\nVoltando ao menu')
                for i in range(10,0,-1):
                    print(f'\r{i}  ', end='', flush=True)
                    sleep(0.5)
                voltar()

@mascara
def menu_deposito():
    valor=float(input('Valor a depositar R$: '))

@mascara
def menu_sacar():
    valor=float(input('Valor a sacar R$: '))

@mascara
def menu_extrato(extrato, saldo):
    print(extrato)
    print(f'Saldo: R${saldo:.2f}')
    

saldo=0
extrato=''
saques=0
menu_principal()
'''
while True:
    menu()
    while True:
        op=input('Opção: ')
        if op not in lista:
            print('Opção invalida!')
        else:
            break

    if op=='1':
        menu_deposito()
        while True:
            valor=float(input('Valor do deposito: '))
            if valor <=0:
                print('Valor invalido!')
            else:
                extrato+= f'{"Deposito":<15} R${valor:.2f}\n'
                saldo+=valor
                print(f'Deposito de R${valor:.2f} realizado com sucesso!')
                break

    elif op=='2':
        while True:
            menu_sacar()
            vl=float(input('Valor do saque: '))

            if vl>saldo:
                print('Saldo insuficiente!')
                break
            elif vl<=0:
                print('Erro no valor informado!')
                break
            elif saques>=3:
                print('Limite de saques')
                break
            elif vl>500:
                print('Valor maximo para saque: R$500')
                break
            else:
                saldo-=vl
                saques+=1
                extrato+=f'{"Saque":<15} R${vl:.2f}\n'
                print(f'Saque de R${vl:.2f} realizado!')
                break
    
    elif op=='3':
        menu_extrato(extrato, saldo)
    else:
        break    
'''