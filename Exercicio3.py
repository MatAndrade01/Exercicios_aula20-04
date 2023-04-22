if __name__ == '__main__':
    soma = 0
    quantidade_de_positivos = 0
    quantidade_de_negativos = 0
    while True:
        num = float(input("Digite um número (ou 0 para sair):"))
        if num == 0:
            break
        soma += num
        if num > 0:
            quantidade_de_positivos += 1
        else:
            quantidade_de_negativos += 1

    total_numeros = quantidade_de_positivos + quantidade_de_negativos
    media = soma / total_numeros

    percentual_positivo = (quantidade_de_positivos / total_numeros) * 100
    percentual_negativo = (quantidade_de_negativos / total_numeros) * 100

print('A média foi de : {}'.format(media))
print('A quantidade de valores positivos foi de: {}'.format(quantidade_de_positivos))
print('A quantidade de valores negativos foi de: {}'.format(quantidade_de_negativos))
print('O percentual dos valores positivos foram de: {:.2f}%'.format(percentual_positivo))
print('O percentual dos valores negativos foram de: {:.2f}%'.format(percentual_negativo))