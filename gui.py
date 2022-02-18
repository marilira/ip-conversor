import os
from converter import decimal, binario

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_strokes():
    print('-'*40)

def print_title():
    print()
    print('-'*7, 'Conversor de Endereço IP', '-'*7)

def print_options():
    print('\nOpcoes:')
    print('1 - Converter decimal para binario'.rjust(38))
    print('2 - Converter binario para decimal'.rjust(38))
    print('3 - Sair\n'.rjust(13))

def print_result(ip, result, op):
    clear()
    print_title()
    print(f'\nIP Decimal: {ip}'.rjust(30) if op == 1 else f'\nIP Binário: {ip}'.rjust(30))
    print(f'Resultado: {result}\n')
    print_strokes()

def run():
    clear()
    print_title()
    print_options()
    while True:
        operation = int(input('Selecione uma operacao: '))
        if operation == 3:
            break
        else:
            ip = input('\nDigite o endereco IP (A.B.C.D): ')
            r = None
            if operation == 1:
                r = binario(ip)
            else:
                r = decimal(ip)
            print_result(ip, r, operation)
            print_options()
    clear()
    print('\nHave a nice day ;)\n')
    exit()