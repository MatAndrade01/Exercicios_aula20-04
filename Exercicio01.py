if __name__ == '__main__':
    soma = 0
    for c in range(1, 501, 2):
        if c % 3 == 0:
            soma = soma + c
    print("A soma desses números é: {}".format(soma))
