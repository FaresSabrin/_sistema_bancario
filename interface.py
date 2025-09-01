list_numbers=list()

# ######################################################################
def menu():
    print('-'*20)
    print('SISTEMA BANCARIO'.center(20))
    print('-'*20)
    
    options=['[1] DEPOSITAR', '[2] SACAR', '[3] EXTRATO', '[4] SAIR']
    global list_numbers

    for num in range(0, len(options)):
        list_numbers.append(int(options[num][1]))

    for itens in range(0, len(options)):
        print(options[itens])

    print('-'*20)

# ######################################################################
def option():
    while True:
        if validate_option(int(input('Opção: '))) is True:
            break

# ######################################################################
def validate_option(num):
    try:
        if num not in list_numbers:
            print('Opção invalida!')
            return False
    except(ValueError, TypeError):
        print('Opção invalida!')
        return False
    except KeyboardInterrupt:
        print('Opção não informada!')
        return False
    else:
        return True, num