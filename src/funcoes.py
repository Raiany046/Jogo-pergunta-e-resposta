import time

def cronometro():
    inicio = time.time()
    for i in range(1, 16):
        print(i)
        time.sleep(1)
    fim = time.time()


def pontuar(pontos, dificuldade):
    if dificuldade == 'facil':
        pontos += 10
    elif dificuldade == 'medio':
        pontos += 20
    elif dificuldade == 'dificil':
        pontos += 30
    return pontos

def perder_vida(vidas):
    vidas -= 1
    return vidas