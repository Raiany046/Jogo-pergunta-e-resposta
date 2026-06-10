import pygame
import random

# CLASSE PERGUNTA

class Pergunta:
    def __init__(
        self,
        pergunta,
        alternativas,
        materia,
        dificuldade,
        id=None,
        alternativa_correta=None
    ):

        self.pergunta = pergunta
        self.alternativas = alternativas
        self.materia = materia
        self.dificuldade = dificuldade
        self.id = id
        self.alternativa_correta = alternativa_correta


# PERGUNTAS

perguntas = [

    Pergunta(
        "Qual é a capital da França?",
        ("Paris", "Londres", "Roma", "Madri"),
        "Geografia",
        "facil",
        id=1,
        alternativa_correta="Paris"
    ),

    Pergunta(
        "Qual é a fórmula da água?",
        ("H2O", "CO2", "O2", "NaCl"),
        "Química",
        "facil",
        id=2,
        alternativa_correta="H2O"
    ),

    Pergunta(
        "Quem escreveu Dom Quixote?",
        (
            "Miguel de Cervantes",
            "William Shakespeare",
            "Jorge Luis Borges",
            "Gabriel Garcia Marquez"
        ),
        "Literatura",
        "media",
        id=3,
        alternativa_correta="Miguel de Cervantes"
    )
]

random.shuffle(perguntas)

# PYGAME

pygame.init()

LARGURA = 900
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tá Sabendo?")

fonte = pygame.font.SysFont(None, 36)
fonte_titulo = pygame.font.SysFont(None, 48)


indice_pergunta = 0
pergunta_atual = perguntas[indice_pergunta]

resultado = ""
pontuacao = 0
vidas = 3

botoes = []

# FUNÇÃO DESENHAR

def desenhar():

    tela.fill((255, 255, 255))

    titulo = fonte_titulo.render(
        f"Matéria: {pergunta_atual.materia}",
        True,
        (0, 0, 255)
    )

    tela.blit(titulo, (40, 20))

    texto_pergunta = fonte.render(
        pergunta_atual.pergunta,
        True,
        (0, 0, 0)
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

        pygame.draw.rect(tela, (70, 110, 220), rect)

        texto_alt = fonte.render(
            alternativa,
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto_alt,
            (65, 193 + i * 80)
        )

        botoes.append((rect, alternativa))

    

    texto_pontos = fonte.render(
        f"Pontuação: {pontuacao}",
        True,
        (0, 0, 0)
    )

    tela.blit(texto_pontos, (700, 20))


    texto_vidas = fonte.render(
        f"Vidas: {vidas}",
        True,
        (255, 0, 0)
    )

    tela.blit(texto_vidas, (700, 70))


    if resultado == "Acertou!":
        cor = (0, 180, 0)

    elif resultado == "Errou!":
        cor = (220, 0, 0)

    else:
        cor = (0, 0, 0)

    texto_resultado = fonte.render(
        resultado,
        True,
        cor
    )

    tela.blit(texto_resultado, (50, 520))

    pygame.display.flip()

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
                    if alternativa == pergunta_atual.alternativa_correta:
                        resultado = "Acertou!"
                        if pergunta_atual.dificuldade == "facil":
                             pontuacao += 10
                        elif pergunta_atual.dificuldade == "media":
                             pontuacao += 20
                        elif pergunta_atual.dificuldade == "dificil":
                             pontuacao += 30
                    else:
                        resultado = "Errou!"
                        vidas -= 1
                    desenhar()
                    pygame.time.delay(1500)
                    # GAME OVER

                    if vidas <= 0:

                        tela.fill((255, 255, 255))

                        texto = fonte_titulo.render(
                            "VOCÊ PERDEU! :(",
                            True,
                            (255, 0, 0)
                        )

                        tela.blit(texto, (300, 250))

                        pygame.display.flip()

                        pygame.time.delay(3000)

                        rodando = False
                        break 
                    # PRÓXIMA PERGUNTA

                    indice_pergunta += 1

                if indice_pergunta < len(perguntas):

                        pergunta_atual = perguntas[indice_pergunta]
                        resultado = ""

                else:

                  tela.fill((255, 255, 255))

                  if vidas == 3:
                    mensagem ="VOCE FOI MUITO BEM! :)"
                       
                    

                  if vidas == 2:
                    mensagem ="VOCE FOI BEM! ;)"
                     

                  if vidas == 1:
                    mensagem ="VOCE PODE MELHORAR!"
                     
                

                  texto_final = fonte_titulo.render(
                   mensagem,
                   True,
                   (0, 250, 0)
                   )

                  texto_pontos = fonte.render(
                  f"Pontuacao Final: {pontuacao}",
                   True,
                  (0, 0, 0)
                  )

                  tela.blit(texto_final, (250, 200))
                  tela.blit(texto_pontos, (300, 300))

                  pygame.display.flip()

                  pygame.time.delay(3000)

                  rodando = False 
                  break

    if rodando:
        desenhar()

pygame.quit()