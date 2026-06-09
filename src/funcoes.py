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

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)