if __name__ == '__main__':
    primeiro = int(input('Primeiro termo:'))
    razão = int(input('Razão:'))
    decimotermo = primeiro + (10 - 1) * razão
    for c in range(primeiro, decimotermo + razão, razão):
        print('{} '.format(c), end=' ')
