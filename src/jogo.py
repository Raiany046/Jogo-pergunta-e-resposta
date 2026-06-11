import pygame
import random
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
    texto_titulo = fonte_titulo.render("NOME DO JOGO", True, COR_TEXTO)
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
relogio = pygame.time.Clock()

while rodando_menu:
    # Gerenciamento de eventos
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

    # Desenha os elementos na tela
    desenhar_tela_inicial()

    # Atualiza a tela
    pygame.display.flip()
    
    # Limita o framerate a 60 FPS
    relogio.tick(60)

    