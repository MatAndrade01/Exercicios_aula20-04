if __name__ == '__main__':
    A = float(input('Digite um número:'))
    B = float(input('Digite um número:'))
    C = float(input('Digite um número:'))
    pi = 3.141559
    triangulo = A * C / 2
    circulo = pi * (C * C)
    trapezio = (A + B) * C / 2
    quadrado = B * B
    retangulo = A * B
    print('Triangulo:{:.3f}\nCirculo:{:.3f}\nTrapezio:{:.3f}\nQuadrado:{:.3f}\nRetangulo:{:.3f}\n'.format(triangulo, circulo, trapezio, quadrado, retangulo))

