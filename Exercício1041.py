if __name__ == '__main__':
    X = float(input('Digite o valor de X:'))
    Y = float(input('Digite o valor de Y:'))

    if X == Y == 0:
        print('Origem')

    if X > 0 and Y == 0:
        print('Eixo X')

    if Y > 0 and X == 0:
        print('Eixo Y')

    if X > 0 and Y > 0:
        print('Q1')

    if X < 0 and Y > 0:
        print('Q2')

    if X < 0 and Y < 0:
        print('Q3')

    if X > 0 and Y < 0:
        print('Q4')
