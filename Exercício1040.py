if __name__ == '__main__':
    n1 = float(input('Digite a primeira nota:'))
    n2 = float(input('Digite a segunda nota:'))
    n3 = float(input('Digite a terceira nota:'))
    n4 = float(input('Digite a quarta nota:'))

    media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

    if media_ponderada >= 7:
        print('Média = {:.2f}'.format(media_ponderada))
        print('Aluno Aprovado.')

    if media_ponderada < 5:
        print('Média = {:.2f}'.format(media_ponderada))
        print('Aluno Reprovado.')

    if media_ponderada == 5 or media_ponderada <= 6.9:
        print('Média = {:.2f}'.format(media_ponderada))
        print('Aluno em Exame.')

        nota_exame = float(input('Digite a nota do exame:'))
        print('Nota do exame = {:.2f}'.format(nota_exame))

        media_final = (nota_exame + media_ponderada) / 2

        if media_final >= 5:
            print('Aluno Aprovado.')
            print('Média Final = {:.2f}'.format(media_final))

        if media_final <= 4.9:
            print('Aluno Reprovado.')
            print('Média Final = {:.2f}'.format(media_final))
