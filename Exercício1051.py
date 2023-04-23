if __name__ == '__main__':
    imposto = 0
    diferenca = 0
    renda = float(input('Digite o valor da sua renda:'))

    if renda <= 2000.00:
        print('Isento')

    if renda > 2000.01 and renda <= 3000.00:
        diferenca = renda - 2000.00
        imposto = diferenca * 0.08
        print('R$ {:.2f}'.format(imposto))

    if renda > 3000.01 and renda <= 4500.00:
        imposto = 1000.00 * 0.08
        diferenca = renda - 3000.00
        imposto = imposto + diferenca * 0.18
        print('R$ {:.2f}'.format(imposto))

    if renda > 4500.00:
        imposto = 1000.00 * 0.08 + 1500 * 0.18
        diferenca = renda - 4500.00
        imposto = imposto + diferenca * 0.28
        print('R$ {:.2f}'.format(imposto))

