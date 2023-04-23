if __name__ == '__main__':
    salario_novo = 0
    reajuste = 0
    salario = float(input('Digite seu salário:'))

    if salario <= 400.00:
        reajuste = salario * 15 /100
        salario_novo = reajuste + salario
        print('Novo salário: R${:.2f}\nReajuste ganho: R${:.2f}\nEm percentual: 15%'.format(salario_novo, reajuste))

    if salario >= 400.01 and salario <= 800.00:
        reajuste = salario * 12 / 100
        salario_novo = reajuste + salario
        print('Novo salário: R${:.2f}\nReajuste ganho: R${:.2f}\nEm percentual: 12%'.format(salario_novo, reajuste))

    if salario >= 800.01 and salario <= 1200.00:
        reajuste = salario * 10 / 100
        salario_novo = reajuste + salario
        print('Novo salário: R${:.2f}\nReajuste ganho: R${:.2f}\nEm percentual: 10%'.format(salario_novo, reajuste))

    if salario >= 1200.01 and salario <= 2000.00:
        reajuste = salario * 7 /100
        salario_novo = reajuste + salario
        print('Novo salário: R${:.2f}\nReajuste ganho: R${:.2f}\nEm percentual: 7%'.format(salario_novo, reajuste))

    if salario > 2000.00:
        reajuste = salario * 4 / 100
        salario_novo = reajuste + salario
        print('Novo salário: R${:.2f}\nReajuste ganho: R${:.2f}\nEm percentual: 4%'.format(salario_novo, reajuste))
