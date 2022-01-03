titulo = ('OPERAÇÕES')
print('*'*60)
print('{:^60}'.format(titulo))
print('*'*60)

print('''
    Operações disponíveis: 
    
    ADIÇÃO -------------------(1)
    SUBTRAÇÃO --------------(2)
    MULTIPLICAÇÃO ---------(3)
    DIVISÃO -------------------(4)
    POTENCIAÇÃO ------------(5)
    DIVISÃO INTEIRA ---------(6)
    RESTO DA DIVISÃO -------(7)
''')
op = int(input('Qual operação deseja efetuar: '))
print('')

if op == 1:
    print('A operação escolhida foi a ADIÇÃO:')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    s = n1 + n2
    print('')
    print('A soma de {} + {} é igual a {}.'.format(n1, n2, s))

elif op == 2:
    print('A operação escolhida foi a SUBTRAÇÃO.')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    s = n1 - n2
    print('')
    print('A subtração de {} - {} é igual a {}.'.format(n1, n2, s))

elif op == 3:
    print('A operação escolhida foi a MULTIPLICAÇÃO.')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    s = n1 * n2
    print('')
    print('A multiplicação de {} * {} é igual a {}.'.format(n1, n2, s))

elif op == 4:
    print('A operação escolhida foi a DIVISÃO.')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    s = n1 / n2
    print('')
    print('A divisão de {} / {} é igual a {}.'.format(n1, n2, s))

elif op == 5:
    print('A operação escolhida foi a POTENCIAÇÃO.')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    s = n1 ** n2
    print('')
    print('A potenciação de {} ** {} é igual a {}.'.format(n1, n2, s))

elif op == 6:
    print('A operação escolhida foi a DIVISÃO INTEIRA.')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    s = n1 // n2
    print('')
    print('A divisão inteira de {} // {} é igual a {}.'.format(n1, n2, s))

elif op == 7:
    print('A operação escolhida foi a RESTO DA DIVISÃO.')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    s = n1 % n2
    print('')
    print('O resto da divisão de {} % {} é igual a {}.'.format(n1, n2, s))

else:
    print('Opção inválida!')
    print('')

print('')
print('Obrigado por usar o nosso programa!')


