if __name__ == '__main__':
    primeiro = int(input('Digite o primeiro termo:'))
    razão = int(input('Digite a razão:'))
    for c in range(1, 11):
        print(primeiro * razão ** c)