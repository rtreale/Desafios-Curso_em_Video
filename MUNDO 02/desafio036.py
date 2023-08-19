valor_financiamento = float(input('Qual valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
parcelas_anuais = int(input('Em quantos anos deseja pagar? '))

parcelas_mensais = valor_financiamento/(parcelas_anuais*12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_financiamento, parcelas_anuais, parcelas_mensais))

if parcelas_mensais > (0.3*salario):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
