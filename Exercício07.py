if __name__ == '__main__':
    while True:
        num = int(input('Digite um número entre 1 e 10 para saber sua tabuada:'))

        if num < 1:
            print("Digite um número valido!")

        elif num > 10:
                print("Digite um número valido!")

        else:
            for c in range(1, 11):
                print('{} x {} = {}'.format(num, c, num * c))
