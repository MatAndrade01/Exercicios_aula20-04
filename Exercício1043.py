if __name__ == '__main__':
    A = float(input('Digite um nomero:'))
    B = float(input('Digite um número:'))
    C = float(input('Digite um número:'))

    if A > B and A > C:
        soma = B + C
        print(soma)

        if soma > A:
            perimetro = A + B + C
            print('Perimetro = {:.2f}'.format(perimetro))

        if soma <= A:
            area = ((A + B) * C) / 2
            print('Area = {:.2f}'.format(area))


    if B > A and B > C:
        soma = A + C
        print(soma)

        if soma > B:
            perimetro = A + B + C
            print('Perimetro = {:.2f}'.format(perimetro))

        if soma <= B:
            area = ((A + B) * C) / 2
            print('Area = {:.2f}'.format(area))


    if C > A and C > B:
        soma = A + B
        print(soma)

        if soma > C:
            perimetro = A + B + C
            print('Perimetro = {:.2f}'.format(perimetro))

        if soma <= C:
            area = ((A + B) * C) / 2
            print('Area = {:.2f}'.format(area))



