if __name__ == '__main__':
    distancia = float(input('Digite a distanca em Km:'))
    combustivel = float(input('Digite o combustivel em L:'))

    cosumo_medio = distancia / combustivel
    print('{:.3f} Km/L'.format(cosumo_medio))