while True:
    print('Valores negativos encerrarão o programa.')
    n = int(input('Digite um numero inteiro para que a tabuada do mesmo seja exibida: '))
    if n<0:
        break
    else:
        print('=' * 20)
        print(f'| Tabuada de {n} ')
        print('=' * 20)
        for c in range(0, 11):
            print(f'|{c:2} x {n} = {c*n}')
        print('='*20)