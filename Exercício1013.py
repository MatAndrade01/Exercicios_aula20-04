if __name__ == '__main__':
    A = int(input('Digite um número:'))
    B = int(input('Digite um número:'))
    C = int(input('Digite um número:'))

    maiorAB = (A + B + abs(A - B)) / 2
    maiorABC = (maiorAB + C + abs(maiorAB - C)) / 2

    print('{} é o maior'.format(maiorABC))

