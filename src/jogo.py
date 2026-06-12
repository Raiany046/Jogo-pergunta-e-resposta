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



#começa a rodar o jogo
tela.fill(COR_FUNDO) #limpa a tela para começar o jogo


random.shuffle(lista_perguntas)
pontuacao = 0
vidas = 0

indice = 0
pergunta_carregada = False
minhas_alts = []

# (Certifique-se de que 'minhas_alts = []' foi criada antes de entrar aqui)

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
                        indice += 1
                        pergunta_carregada = False  # Próxima pergunta será carregada
                        tempo_inicial = pygame.time.get_ticks()
                    else:
                        vidas = perder_vida(vidas)
                        indice += 1
                        pergunta_carregada = False  # Próxima pergunta será carregada
                        tempo_inicial = pygame.time.get_ticks()
                        if vidas == 0:
                            rodando = False

    # 3. Gerenciamento de Carga (Instancia as alternativas uma vez por pergunta)
    if not pergunta_carregada:

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
    for pergunta in range(len(lista_perguntas)):
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