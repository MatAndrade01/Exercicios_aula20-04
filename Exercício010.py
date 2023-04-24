if __name__ == '__main__':
    num = int(input('Digite um número para saber seu fatorial:'))
    resultado = 1

    for c in range(1, num+1):
        resultado *= c
        print('O fatorial de {} foi: {}'.format(num, resultado))
