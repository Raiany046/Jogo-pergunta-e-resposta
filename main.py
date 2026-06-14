import pygame
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from dados import salvar_recorde, carregar_recorde

BASE_DIR = os.path.dirname(__file__)

# CLASSE PERGUNTA

class Pergunta:
    def __init__(self, pergunta, alternativas, materia,
                 id=None, alternativa_correta=None):

        self.pergunta = pergunta
        self.id = id
        self.alternativas = alternativas
        self.materia = materia
        self.alternativa_correta = alternativa_correta


pergunta1 = Pergunta(
    "Qual é a capital da França?",
    ("Paris", "Londres", "Roma", "Madri"),
    "Geografia",
    id=1,
    alternativa_correta="Paris"
)

pergunta2 = Pergunta(
    "Qual é a fórmula da água?",
    ("H2O", "CO2", "O2", "NaCl"),
    "Química",
    id=2,
    alternativa_correta="H2O"
)

pergunta3 = Pergunta(
    "Quem escreveu Dom Quixote?",
    (
        "Miguel de Cervantes",
        "William Shakespeare",
        "Jorge Luis Borges",
        "Gabriel Garcia Marquez"
    ),
    "Literatura",
    id=3,
    alternativa_correta="Miguel de Cervantes"
)

perguntas = [pergunta1, pergunta2, pergunta3]

# PYGAME


pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tá Sabendo?")

fonte = pygame.font.SysFont(None, 36)
fonte_pequena = pygame.font.SysFont(None, 28)

indice_pergunta = 0
pergunta_atual = perguntas[indice_pergunta]

resultado = ""
botoes = []

# PONTUAÇÃO E RECORDE
ARQUIVO_RECORDE = os.path.join(BASE_DIR, "data", "recorde.txt")
PONTOS_POR_ACERTO = 10
pontuacao = 0
recorde = carregar_recorde(ARQUIVO_RECORDE)


# FUNÇÃO DESENHAR


def desenhar():

    tela.fill((255, 255, 255))

    titulo = fonte.render(
        f"Matéria: {pergunta_atual.materia}",
        True,
        (0, 0, 255)
    )
    tela.blit(titulo, (50, 20))

    texto_pergunta = fonte.render(
        pergunta_atual.pergunta,
        True,
        (0, 0, 0)
    )

    tela.blit(texto_pergunta, (50, 70))

    botoes.clear()

    for i, alternativa in enumerate(pergunta_atual.alternativas):

        rect = pygame.Rect(
            50,
            150 + i * 70,
            400,
            50
        )

        pygame.draw.rect(tela, (100, 100, 200), rect)

        texto_alt = fonte.render(
            alternativa,
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto_alt,
            (60, 160 + i * 70)
        )

        botoes.append((rect, alternativa))

    texto_resultado = fonte.render(
        resultado,
        True,
        (0, 150, 0) if "Acertou" in resultado else (200, 0, 0)
    )

    tela.blit(texto_resultado, (50, 500))

    pygame.display.flip()


# TELA FINAL


def desenhar_tela_fim():

    tela.fill((255, 255, 255))

    novo_recorde = pontuacao > recorde

    msg_titulo = "Novo Recorde!" if novo_recorde else "Fim de Jogo!"
    cor_titulo = (200, 100, 0) if novo_recorde else (0, 0, 180)

    titulo = fonte.render(msg_titulo, True, cor_titulo)
    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 150))

    txt_pontos = fonte.render(
        f"Sua pontuação: {pontuacao} pontos",
        True,
        (0, 0, 0)
    )
    tela.blit(txt_pontos, (LARGURA // 2 - txt_pontos.get_width() // 2, 230))

    recorde_exibido = pontuacao if novo_recorde else recorde
    txt_recorde = fonte.render(
        f"Recorde: {recorde_exibido} pontos",
        True,
        (200, 150, 0)
    )
    tela.blit(txt_recorde, (LARGURA // 2 - txt_recorde.get_width() // 2, 290))

    acertos = pontuacao // PONTOS_POR_ACERTO
    txt_acertos = fonte_pequena.render(
        f"Você acertou {acertos} de {len(perguntas)} pergunta(s).",
        True,
        (80, 80, 80)
    )
    tela.blit(txt_acertos, (LARGURA // 2 - txt_acertos.get_width() // 2, 350))

    pygame.display.flip()


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
                        pontuacao += PONTOS_POR_ACERTO
                        resultado = f"Acertou! +{PONTOS_POR_ACERTO} pontos"
                    else:
                        resultado = "Errou!"
                    desenhar()
                    pygame.time.delay(1500)

                    indice_pergunta += 1

                    if indice_pergunta < len(perguntas):
                        pergunta_atual = perguntas[indice_pergunta]
                        resultado = ""

                    else:
                        if pontuacao > recorde:
                            recorde = pontuacao
                            salvar_recorde(ARQUIVO_RECORDE, recorde)

                        desenhar_tela_fim()
                        pygame.time.delay(3000)
                        rodando = False

    desenhar()

pygame.quit()