if __name__ == '__main__':
    A = int(input('Digite um valor:'))
    B = int(input('Digite um valor:'))

    divisao =0

    if A > B:
        resto = A % B

        if resto == 0:
            print('São multiplo')

        if resto > 0:
            print('Não são multiplos')

    if B > A:
        resto = B % A

        if resto == 0:
            print('São multiplo')

        if resto > 0:
            print('Não são Multiplos')

