lista=list()
listaCliente=dict()

def mascara(f):
    print('='*30)
    print(f'{f.__name__.upper()}'.center(30))
    print('='*30)
    return f()
# ####################################################################################################

def lerMenu(menu):
    for x in range(0, len(menu)):
        lista.append(menu[x][1])
        print(menu[x])

# ####################################################################################################

def validarOption():
    while True:
        option=int(input('Opção: '))
        if str(option) not in lista:
            print('Opção invalida!')
        else:
            return option

# ####################################################################################################

@mascara
def menu_Principal():
    menu=['[1] CRIAR CONTA', '[2] ACESSAR CONTA']
    lerMenu(menu)
    option=validarOption()
    print('='*30)
    return(option)

# ####################################################################################################
@mascara
def menu():
    menu=['[1] DEPOSITAR', '[2] SACAR', '[3] EXTRATO', '[4] SAIR']
    lerMenu(menu)

# ####################################################################################################
def criarConta():
    nome=str(input('Nome completo: '))
    #dataNascimento=int(input('Data nascimento: '))
    cpf=int(input( 'CPF: '))
    #endereco=str(input('Endereço: '))
    #numEndereco=str(input('Numero: '))
    #email=str(input('E-mail: '))
    with open('listaCPF.txt', 'a') as arq:
        arq.write(f'{nome}, {cpf}\n')

    with open('listaCPF.txt', 'r') as arq:
        for linha in arq:
            print(linha)
# ####################################################################################################
def menuAcessaConta():
    pass