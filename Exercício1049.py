if __name__ == '__main__':
    vertebrado_ou_ivertebrado = int(input('O seu animal é vertebrado(1) ou invertebrado(2)?'))

    if vertebrado_ou_ivertebrado == 1:
        print('Seu animal é vertebrado.')
        classe = int(input('O seu animal pertence a qual classe? Ave(1) ou Mamífero(2):'))

        if classe == 1:
            print('A classe do seu animal é Ave.')
            alimentacao = int(input('Seu animal é Carnivoro(1) ou Onivoro(2)?'))

            if alimentacao == 1:
                print('Seu animal é uma Aguia!')

            if alimentacao == 2:
                print('Seu animal é uma Pomba!')

        if classe == 2:
            print('A classe do seu animal é Mamífero.')
            alimentacao = int(input('Seu animal é Onivoro(1) ou Herbivoro(2)?'))

            if alimentacao == 1:
                print('Seu animal é um Homem!')

            if alimentacao == 2:
                print('Seu animal é uma Vaca!')

    if vertebrado_ou_ivertebrado == 2:
        print('Seu animal é Invertebrado.')
        classe = int(input('O seu animal pertence a qual classe? Inseto(1) ou Anelidio(2)'))

        if classe == 1:
            print('A classe do seu animal é Inseto.')
            alimentacao = int(input('Seu animal é Hematofago(1) ou Herbivoro(2)?'))

            if alimentacao == 1:
                print('Seu animal é uma Pulga!')

            if alimentacao == 2:
                print('Seu animal é uma Largata!')

        if classe == 2:
            print('A classe do seu animal é Anelidio.')
            alimentacao = int(input('Seu animal é Hematofago(1) ou Onivoro(2)?'))

            if alimentacao == 1:
                print('Seu animal é uma Sanguessuga!')

            if alimentacao == 2:
                print('Seu animal é uma Minhoca!')
