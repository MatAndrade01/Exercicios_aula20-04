if __name__ == '__main__':
    A = str(input('Digite a primeira palavra:')).lower()
    B = str(input('Digite a segunda palavra:')).lower()
    c = str(input('Digite a terceira palavra:')).lower()

    if (A == 'vertebrado') and (B == 'ave') and (c == 'carnivoro'):
        print('Aguia')

    if (A == 'vertebrado') and (B == 'ave') and (c == 'onivoro'):
        print('Pomba')

    if (A == 'vertebrado') and (B == 'mamifero') and (c == 'onivoro'):
        print('Homem')

    if (A == 'vertebrado') and (B == 'mamifero') and (c == 'herbivoro'):
        print('Vaca')

    if (A == 'invertebrado') and (B == 'inseto') and (c == 'hematofago'):
        print('Pulga')

    if (A == 'Invertebrado') and (B == 'inseto') and (c == 'herbivoro'):
        print('Largata')

    if (A == 'Invertebrado') and (B == 'anelidio') and (c == 'hematofago'):
        print('Sanguessuga')

    if (A == 'Invertebrado') and (B == 'anelidio') and (c == 'onivoro'):
        print('minhoca')
