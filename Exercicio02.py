if __name__ == '__main__':
    somaaltura = 0
    maioraltura = 0
    nomedamaioraltura = 0
    for c in range(1, 16):
        print("-----{}ºCandidato------".format(c))
        nome = str(input("Nome:")).strip()
        altura = float(input("Altura:"))
        somaaltura = maioraltura + altura
        if c == 1:
            maioraltura = altura
            nomedamaioraltura = nome
        if altura > maioraltura:
            maioraltura = altura
            nomedamaioraltura = nome
print("A maior alura é {} metros de altura e pertence a {}".format(maioraltura, nomedamaioraltura))




