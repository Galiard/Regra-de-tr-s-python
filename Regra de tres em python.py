while True:
    print('Que tipo de REGRA DE TRÊS DESEJA FAZER ? ')
    print('''
    [0] com o X na parte DIREITA INFERIOR

    [1] com o X na parte DIREITA SUPERIOR

    [2] com o X na parte ESQUERDA INFERIOR

    [3] com o X na parte ESQUERDA SUPERIOR''')
    print('-='*22)
    escolha = ' '
    while escolha not in '0123':
        escolha = str(input(': ')).strip().upper()[0]
        if escolha not in '0123':
            print('Escolha invalida... TENTE NOVAMENTE')
            print('-='*22)
    if escolha == '0':
        valor1 = float(input('Digite o valor 1 : '))
        valor2 = float(input('Digite o valor 2 : '))
        valor3 = float(input('Digite o valor 3 : '))
        #valor4 = x
        resultado = valor2*valor3
        valorx = resultado/valor1
        print(f'O valor de X é : {valorx}')
        
    if escolha == '1':
        valor1 = float(input('Digite o valor 1 : '))
        valor2 = float(input('Digite o valor 2 : '))
        valor3 = float(input('Digite o valor 3 : '))
        #valor4 = x
        resultado = valor1*valor3
        valorx = resultado/valor2
        print(f'O valor de X é : {valorx}')
    if escolha == '2':
        valor1 = float(input('Digite o valor 1 : '))
        valor2 = float(input('Digite o valor 2 : '))
        valor3 = float(input('Digite o valor 3 : '))
        #valor4 = x
        resultado = valor1*valor3
        valorx = resultado/valor2
        print(f'O valor de X é : {valorx}')
    if escolha == '3':
        valor1 = float(input('Digite o valor 1 : '))
        valor2 = float(input('Digite o valor 2 : '))
        valor3 = float(input('Digite o valor 3 : '))
        #valor4 = x
        resultado = valor1*valor2
        valorx = resultado/valor3
        print(f'O valor de X é : {valorx}')
    print('-='*22)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja fazer mais uma operação? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Até a proxima... te vejo em bréve')

