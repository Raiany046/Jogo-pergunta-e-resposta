import pygame

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

indice_pergunta = 0
pergunta_atual = perguntas[indice_pergunta]

resultado = ""
botoes = []


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
        (0, 150, 0)
    )

    tela.blit(texto_resultado, (50, 500))

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
                        resultado = "Acertou!"
                    else:
                        resultado = "Errou!"
                    desenhar()
                    pygame.time.delay(1500)

                    indice_pergunta += 1

                    if indice_pergunta < len(perguntas):
                        pergunta_atual = perguntas[indice_pergunta]
                        resultado = ""

                    else: 
                        resultado = "Fim do jogo!"
                        desenhar()
                        pygame.time.delay(2000)
                        rodando = False

    desenhar()

pygame.quit()