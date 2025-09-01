def menu():
    print('='*25)
    print('SISTEMA BANCARIO'.center(25))
    print('='*25)
    
    menu=['[1] DEPOSITAR', '[2] SACAR', '[3] EXTRATO', '[4] SAIR']
    
    for num in range(0, len(menu)):
        lista.append(menu[num][1])
        print(menu[num])
    print('='*25)

# ====================================================================================================
def menu_deposito():
    print('='*25)
    print('DEPOSITO'.center(25))
    print('='*25)

# ====================================================================================================
def menu_extrato(extrato, saldo):
    print('='*25)
    print('EXTRATO'.center(25))
    print('='*25)
    print(extrato)
    print()
    print(f'Saldo: R${saldo:.2f}')
    print('='*25)

# ====================================================================================================
def menu_sacar():
    print('='*25)
    print('SAQUE'.center(25))
    print('='*25)

lista=list()
saldo=0
extrato=''
saques=0

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
        