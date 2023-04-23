if __name__ == '__main__':
    print('Codigo 1 = cachorro quente R$ 4.00\nCodigo 2 = x-salada R$ 4.50\nCodigo 3 = x-bacon R$ 5.00\nCodigo 4 = torrada simples R$ 2.00\nCodigo 5 = Refrigerante R$ 1.50')
    codigo = int(input('Digite o codigo do alimento:'))
    quantidade = int(input('Digite a quantidade:'))

    if codigo == 1:
        total = quantidade * 5.00
        print('Total = {:.2f}'.format(total))

    if codigo == 2:
        total = quantidade * 4.50
        print('Total = {:.2f}'.format(total))

    if codigo == 3:
        total = quantidade * 5.00
        print('Total = {:.2f}'.format(total))

    if codigo == 4:
        total = quantidade * 2.00
        print('Total = {:.2f}'.format(total))

    if codigo == 5:
        total = quantidade * 1.50
        print('Total = {:.2f}'.format(total))
