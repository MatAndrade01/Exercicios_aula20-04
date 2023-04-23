if __name__ == '__main__':
    x1 = float(input('Digite um valor:'))
    y1 = float(input('Digite um valor:'))
    x2 = float(input('Digite um valor:'))
    y2 = float(input('Digite um valor:'))

    operacao1 = (x2 - x1) ** 2
    operacao2 = (y2 - y1) ** 2
    operacao3 = operacao1 + operacao2
    operacao4 = operacao3 ** (1/2)
    print('{:.4f}'.format(operacao4))