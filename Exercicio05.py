if __name__ == '__main__':
    soma = 0
    quantidade_numeros = 0
    quantidade_par = 0
    quantidade_impar = 0
    media_pares = 0
    soma_pares = 0
    while True:
        num = float(input('Digite um número positivo (digite um númeor negativo Ou digite 0 para encerrar o programa)'))

        if num == 0:
            break

        quantidade_numeros += 1
        soma += num

        if num % 2 == 0:
            quantidade_par += 1
            soma_pares += num

        else:
            quantidade_impar += 1

    if quantidade_numeros > 0:
        media_geral = soma / quantidade_numeros

        if quantidade_par > 0:
            media_pares = soma_pares / quantidade_par

        else:
            media_pares = 0

        print("Quantidade de números pares: {}".format(quantidade_par))
        print("Quantidade de números ímpares: {}".format(quantidade_impar))
        print("Média dos valores pares: {}".format(media_pares))
        print("Média geral dos números lidos: {}".format(media_geral))
    else:
        print("Nenhum número foi digitado.")