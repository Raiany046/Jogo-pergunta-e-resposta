import pygame
import random
from perguntas import *
from funcoes import verificar_resposta, calcular_pontos, perder_vida, jogador_perdeu

# CLASSE PERGUNTA



random.shuffle(lista_perguntas)

# CONSTANTES

LARGURA = 900
ALTURA = 600

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (70, 110, 220)
VERMELHO = (220, 0, 0)
VERDE = (0, 180, 0)

# PYGAME

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tá Sabendo?")

fonte = pygame.font.SysFont(None, 36)
fonte_titulo = pygame.font.SysFont(None, 48)

indice_pergunta = 0
pergunta_atual = lista_perguntas[indice_pergunta]

resultado = ""
pontuacao = 0
vidas = 3

botoes = []

# DESENHAR

def desenhar():

    tela.fill(BRANCO)

    titulo = fonte_titulo.render(
        f"Matéria: {pergunta_atual.materia}",
        True,
        AZUL
    )

    tela.blit(titulo, (40, 20))

    texto_pergunta = fonte.render(
        pergunta_atual.pergunta,
        True,
        PRETO
    )

    tela.blit(texto_pergunta, (40, 90))

    botoes.clear()

    for i, alternativa in enumerate(pergunta_atual.alternativas):

        rect = pygame.Rect(
            50,
            180 + i * 80,
            600,
            55
        )

        pygame.draw.rect(tela, AZUL, rect)

        texto_alt = fonte.render(
            alternativa,
            True,
            BRANCO
        )

        tela.blit(
            texto_alt,
            (65, 193 + i * 80)
        )

        botoes.append((rect, alternativa))

    texto_pontos = fonte.render(
        f"Pontuação: {pontuacao}",
        True,
        PRETO
    )

    tela.blit(texto_pontos, (700, 20))

    texto_vidas = fonte.render(
        f"Vidas: {vidas}",
        True,
        VERMELHO
    )

    tela.blit(texto_vidas, (700, 70))

    if resultado == "Acertou!":
        cor = VERDE

    elif resultado == "Errou!":
        cor = VERMELHO

    else:
        cor = PRETO

    texto_resultado = fonte.render(
        resultado,
        True,
        cor
    )

    tela.blit(texto_resultado, (50, 520))

    pygame.display.flip()


# TELA FINAL

def mostrar_tela_final():

    tela.fill(BRANCO)

    if vidas == 3:
        mensagem = "VOCÊ FOI MUITO BEM! :)"

    elif vidas == 2:
        mensagem = "VOCÊ FOI BEM! ;)"

    else:
        mensagem = "VOCÊ PODE MELHORAR!"

    texto_final = fonte_titulo.render(
        mensagem,
        True,
        VERDE
    )

    texto_pontos = fonte.render(
        f"Pontuação Final: {pontuacao}",
        True,
        PRETO
    )

    tela.blit(texto_final, (220, 200))
    tela.blit(texto_pontos, (300, 300))

    pygame.display.flip()

    pygame.time.delay(3000)


# PRIMEIRO DESENHO

desenhar()

# LOOP PRINCIPAL

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            for rect, alternativa in botoes:

                if rect.collidepoint(evento.pos):

                    if verificar_resposta(
                        alternativa,
                        pergunta_atual
                    ):

                        resultado = "Acertou!"

                        pontuacao += calcular_pontos(
                            pergunta_atual.dificuldade
                        )

                    else:

                        resultado = "Errou!"

                        vidas = perder_vida(vidas)

                    desenhar()

                    pygame.time.delay(1500)

                    if jogador_perdeu(vidas):

                        tela.fill(BRANCO)

                        texto = fonte_titulo.render(
                            "VOCÊ PERDEU! :(",
                            True,
                            VERMELHO
                        )

                        tela.blit(texto, (250, 250))

                        pygame.display.flip()

                        pygame.time.delay(3000)

                        rodando = False

                        break

                    indice_pergunta += 1

                    if indice_pergunta < len(lista_perguntas):

                        pergunta_atual = lista_perguntas[indice_pergunta]

                        resultado = ""

                    else:

                        mostrar_tela_final()

                        rodando = False

                    break

    if rodando:
        desenhar()

pygame.quit()
