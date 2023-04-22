if __name__ == '__main__':
    intervalo_01 = 0
    intervalo_02 = 0
    intervalo_03 = 0
    intervalo_04 = 0

    while True:
        num = float(input('Digite um número (ou digite 0 para sair)'))

        if num == 0:
            break
        if num >= 0 and num <= 25:
            intervalo_01 += 1
        elif num >= 26 and num <= 50:
            intervalo_02 += 1
        elif num >= 51 and num <= 75:
            intervalo_03 =+ 1
        else:
            intervalo_04 += 1

print("Quantidade de números no intervalo de [0 - 25] foi de : {}".format(intervalo_01))
print("Quantidade de números no intervalo de [26 - 50] foi de : {}".format(intervalo_02))
print("Quantidade de números no intervalo de [51 - 75] foi de : {}".format(intervalo_03))
print("Quantidade de números no intervalo de [76 - 100] foi de : {}".format(intervalo_04))