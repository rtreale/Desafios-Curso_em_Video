num = int(input('Digite um valor inteiro: '))
print('*='*13+'*')
print(f'A tabuada do número {num} é:')
for c in range(0, 11):
    print(f'[{num}] x [{c}] = [{num*c}]')
print('*='*13+'*')