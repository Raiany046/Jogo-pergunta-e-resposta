import pygame
import random
<<<<<<< HEAD
from perguntas import *
from funcoes import *
import sys



pygame.init()

# --- Configurações da Janela ---
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA)) #define a tela
pygame.display.set_caption("Minha Tela Inicial")

# --- Cores (RGB) ---
COR_FUNDO = (30, 30, 40)        # Um azul escuro acinzentado
COR_TEXTO = (255, 255, 255)      # Branco
COR_BOTAO = (50, 150, 250)       # Azul claro
COR_BOTAO_HOVER = (80, 180, 255) # Azul mais claro para o efeito do mouse

cores = {
    'branco': (255, 255, 255),
    'azul_claro': (50, 150, 250),
    'verde': (50, 250, 50),
    'vermelho': (250, 50, 50),
    'amarelo': (250, 250, 50),  
    'preto': (0, 0, 0),
}

# --- Fontes ---
# Se quiser usar fontes padrão do sistema, usamos SysFont
fonte_titulo = pygame.font.SysFont("Arial", 64, bold=True)
fonte_botao = pygame.font.SysFont("Arial", 32)

# --- Configurações do Botão ---
# pygame.Rect(esquerda, topo, largura, altura)
largura_botao = 200
altura_botao = 60
x_botao = (LARGURA - largura_botao) // 2
y_botao = (ALTURA - altura_botao) // 2
retangulo_botao = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

# --- Configurações do Botão ---
# pygame.Rect(esquerda, topo, largura, altura)
largura_botao = 200
altura_botao = 60
x_botao = (LARGURA - largura_botao) // 2
y_botao = (ALTURA - altura_botao) // 2
retangulo_botao = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)


def desenhar_tela_inicial():
    # 1. Desenha o plano de fundo
    # NOTA: Se quiser usar uma imagem de fundo, descomente as linhas abaixo:
    # imagem_fundo = pygame.image.load("seu_cenario.png")
    # tela.blit(imagem_fundo, (0, 0))
    tela.fill(COR_FUNDO)

    # 2. Desenha o Título do Jogo
    texto_titulo = fonte_titulo.render("Tá sabendo?", True, COR_TEXTO)
    # Centraliza o texto horizontalmente e define a altura (100 pixels do topo)
    x_titulo = (LARGURA - texto_titulo.get_width()) // 2
    tela.blit(texto_titulo, (x_titulo, 100))

    # 3. Detecta a posição do mouse para efeito visual no botão
    posicao_mouse = pygame.mouse.get_pos()
    if retangulo_botao.collidepoint(posicao_mouse):
        cor_atual_botao = COR_BOTAO_HOVER
    else:
        cor_atual_botao = COR_BOTAO

    # 4. Desenha o Botão
    pygame.draw.rect(tela, cor_atual_botao, retangulo_botao, border_radius=12)

    # 5. Desenha o Texto do Botão
    texto_botao = fonte_botao.render("Jogar", True, COR_TEXTO)
    # Centraliza o texto exatamente no meio do retângulo do botão
    x_txt_botao = retangulo_botao.x + (retangulo_botao.width - texto_botao.get_width()) // 2
    y_txt_botao = retangulo_botao.y + (retangulo_botao.height - texto_botao.get_height()) // 2
    tela.blit(texto_botao, (x_txt_botao, y_txt_botao))


# --- Loop Principal da Tela Inicial ---
rodando_menu = True
rodando = True
relogio = pygame.time.Clock()
tempo_inicial = pygame.time.get_ticks()

while rodando_menu:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Verifica o clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # 1 = Botão esquerdo
                if retangulo_botao.collidepoint(evento.pos):
                    print("Botão Jogar clicado! Iniciando o jogo...")
                    rodando_menu = False # Sai do menu e avança no código

    desenhar_tela_inicial()

    pygame.display.flip()
    
    relogio.tick(60)




tela.fill(COR_FUNDO) #limpa a tela para começar o jogo


#variáveis de controle do jogo

random.shuffle(lista_perguntas)
pontuacao = 0
vidas = 0
indice = 0
pergunta_carregada = False
minhas_alts = []
tempo_inicial = pygame.time.get_ticks()


while rodando:
    tela.fill(COR_FUNDO)
    posicao_mouse = pygame.mouse.get_pos()

    # 1. Verificação de parada
    if indice >= len(lista_perguntas):
        rodando = False
        break

    # 2. Loop de Eventos (Captura ações do usuário)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Verifica o clique APENAS quando o evento acontecer
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            # Aqui você verifica se clicou em alguma alternativa
            for alt in minhas_alts:
                if alt.foi_clicada(posicao_mouse):
                    resposta_clicada = alt.texto
                    if resposta_clicada == lista_perguntas[indice].alternativa_correta:
                        pontuacao = pontuar(lista_perguntas[indice], pontuacao)
                    else:
                        vidas = perder_vida(vidas)
                        if vidas == 0:
                            rodando = False

                    indice += 1
                    pergunta_carregada = False  # Próxima pergunta será carregada
                    tempo_inicial = pygame.time.get_ticks()
                    break
            if not rodando or pergunta_carregada is False:
                break

    if not rodando:
        break

    # 3. Gerenciamento de Carga (Instancia as alternativas uma vez por pergunta)
    if not pergunta_carregada and indice < len(lista_perguntas):

        minhas_alts = [] # Limpa as anteriores para carregar as novas

        for i, alternativa in enumerate(lista_perguntas[indice].alternativas):
            if i == 0:
                posicao = (40, 220)
            elif i == 1:
                posicao = (410, 220)
            elif i == 2:
                posicao = (40, 400)
            elif i == 3:
                posicao = (410, 400)
            
            minhas_alts.append(Alternativa(posicao, alternativa, cores['azul_claro'], cores['verde'], cores['preto']))
        
        pergunta_carregada = True

    # 4. Renderização e Atualização Visual (Acontece 60 vezes por segundo)
    if indice < len(lista_perguntas):
        enunciado_atual = Enunciado(lista_perguntas[indice].enunciado, cores['amarelo'], cores['preto'])
        enunciado_atual.desenhar(tela, fonte_botao)

    for alt in minhas_alts:
        alt.atualizar(posicao_mouse)
        alt.desenhar(tela, fonte_botao)
        
    # O cronômetro fica fora do 'for alt', no escopo principal do loop
    if gerenciar_cronometro(tela, fonte, tempo_inicial, 15):
        vidas = perder_vida(vidas)
        indice += 1
        pergunta_carregada = False
        tempo_inicial = pygame.time.get_ticks()

    pygame.display.flip()
    relogio.tick(60)
    
    
pygame.quit()
=======

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


# FUNÇÕES

def calcular_pontos(dificuldade):

    if dificuldade == "facil":
        return 10

    elif dificuldade == "media":
        return 20

    elif dificuldade == "dificil":
        return 30

    return 0


def perder_vida(vidas):
    return vidas - 1


def jogador_perdeu(vidas):
    return vidas <= 0


def verificar_resposta(alternativa, pergunta):
    return alternativa == pergunta.alternativa_correta


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
pergunta_atual = perguntas[indice_pergunta]

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

                    if indice_pergunta < len(perguntas):

                        pergunta_atual = perguntas[indice_pergunta]

                        resultado = ""

                    else:

                        mostrar_tela_final()

                        rodando = False

                    break

    if rodando:
        desenhar()

pygame.quit()
>>>>>>> cd5ddd33b907c68e93f94778ef284e0c65ddebf3
