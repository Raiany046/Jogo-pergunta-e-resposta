import random
from perguntas import *
from funcoes import *
import sys
import pygame

pygame.init()
pontuacao_total = carregar_pontuacao()
btn_dica = pygame.Rect(634, 5, 135, 30) 

# --- Configurações da Janela ---
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA)) 
pygame.display.set_caption("Tá sabendo?")

# --- Cores (RGB) - Visual Moderno/Dark Mode ---
COR_FUNDO = (20, 24, 38)          # Azul escuro profundo
COR_TEXTO = (240, 244, 248)       # Off-white
COR_BOTAO = (0, 180, 216)         # Ciano bonito e equilibrado
COR_BOTAO_HOVER = (0, 204, 255)   # Ciano mais brilhante

cores = {
    'branco': (255, 255, 255),
    'azul_claro': (0, 180, 216),
    'verde': (46, 196, 182),
    'amarelo': (255, 191, 0),
    'vermelho': (231, 76, 60),
    'preto': (15, 17, 26),
}

# --- Fontes ---
fonte_titulo = pygame.font.SysFont("Trebuchet MS", 68, bold=True)
fonte_sub_titulo = pygame.font.SysFont("Trebuchet MS", 38, bold=True)
fonte_botao = pygame.font.SysFont("Arial", 26, bold=True)

# --- Configurações do Botão Principal (Menu 1) ---
largura_botao = 220
altura_botao = 65
x_botao = (LARGURA - largura_botao) // 2
y_botao = (ALTURA - altura_botao) // 2 + 50 
retangulo_botao = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

# --- Configurações dos Botões de Categorias (Menu 2) ---
largura_cat = 380
altura_cat = 60
x_cat = (LARGURA - largura_cat) // 2

btn_geo = pygame.Rect(x_cat, 220, largura_cat, altura_cat)
btn_hist = pygame.Rect(x_cat, 300, largura_cat, altura_cat)
btn_cg = pygame.Rect(x_cat, 380, largura_cat, altura_cat)

# Botão de Sair do Jogo no Menu de Categorias
btn_sair_jogo = pygame.Rect(x_cat, 460, largura_cat, altura_cat)

# --- Configuração do Botão Menu Principal (Tela Final) ---
btn_menu = pygame.Rect(300, 440, 200, 60)

def desenhar_tela_inicial():
    tela.fill(COR_FUNDO)

    texto_titulo = fonte_titulo.render("Tá sabendo?", True, COR_TEXTO)
    x_titulo = (LARGURA - texto_titulo.get_width()) // 2
    tela.blit(texto_titulo, (x_titulo, 100))

    posicao_mouse = pygame.mouse.get_pos()
    cor_atual = COR_BOTAO_HOVER if retangulo_botao.collidepoint(posicao_mouse) else COR_BOTAO

    pygame.draw.rect(tela, cor_atual, retangulo_botao, border_radius=12)

    texto_botao = fonte_botao.render("Jogar", True, COR_TEXTO)
    x_txt = retangulo_botao.x + (retangulo_botao.width - texto_botao.get_width()) // 2
    y_txt = retangulo_botao.y + (retangulo_botao.height - texto_botao.get_height()) // 2
    tela.blit(texto_botao, (x_txt, y_txt))

def desenhar_hud(tela, pontuacao, vidas):
    fonte_hud = pygame.font.SysFont("Arial", 30, bold=True)
    texto_pontos = fonte_hud.render(f"Pontos: {pontuacao}", True, (255,255,255))
    tela.blit(texto_pontos, (40, 10))

    for i in range(vidas):
        pygame.draw.circle(tela, (255, 0, 0), (450 + i * 30, 25), 10)

def desenhar_menu_categorias():
    tela.fill(COR_FUNDO)
    texto_titulo = fonte_sub_titulo.render("Escolha uma Categoria", True, cores['amarelo'])
    x_titulo = (LARGURA - texto_titulo.get_width()) // 2
    tela.blit(texto_titulo, (x_titulo, 100))
        
    texto_pontos = fonte_botao.render(f"Pontos Salvos: {pontuacao_total}", True, cores['branco'])
    x_pontos = (LARGURA - texto_pontos.get_width()) // 2
    tela.blit(texto_pontos, (x_pontos, 160))

    posicao_mouse = pygame.mouse.get_pos()

    cor_geo = COR_BOTAO_HOVER if btn_geo.collidepoint(posicao_mouse) else COR_BOTAO
    pygame.draw.rect(tela, cor_geo, btn_geo, border_radius=12)
    txt_geo = fonte_botao.render("Geografia", True, COR_TEXTO)
    tela.blit(txt_geo, (btn_geo.x + (largura_cat - txt_geo.get_width()) // 2, btn_geo.y + 15))

    cor_hist = COR_BOTAO_HOVER if btn_hist.collidepoint(posicao_mouse) else COR_BOTAO
    pygame.draw.rect(tela, cor_hist, btn_hist, border_radius=12)
    txt_hist = fonte_botao.render("História", True, COR_TEXTO)
    tela.blit(txt_hist, (btn_hist.x + (largura_cat - txt_hist.get_width()) // 2, btn_hist.y + 15))

    cor_cg = COR_BOTAO_HOVER if btn_cg.collidepoint(posicao_mouse) else COR_BOTAO
    pygame.draw.rect(tela, cor_cg, btn_cg, border_radius=12)
    txt_cg = fonte_botao.render("Conhecimentos Gerais", True, COR_TEXTO)
    tela.blit(txt_cg, (btn_cg.x + (largura_cat - txt_cg.get_width()) // 2, btn_cg.y + 15))

    # Desenho do Botão "Sair do Jogo"
    cor_sair = cores['vermelho'] if btn_sair_jogo.collidepoint(posicao_mouse) else (180, 50, 50)
    pygame.draw.rect(tela, cor_sair, btn_sair_jogo, border_radius=12)
    txt_sair = fonte_botao.render("Sair do Jogo", True, COR_TEXTO)
    tela.blit(txt_sair, (btn_sair_jogo.x + (largura_cat - txt_sair.get_width()) // 2, btn_sair_jogo.y + 15))


relogio = pygame.time.Clock()

# --- LOOP 1: Tela Inicial (Roda apenas 1 vez ao abrir o jogo) ---
rodando_menu = True
while rodando_menu:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if retangulo_botao.collidepoint(evento.pos):
                rodando_menu = False 

    desenhar_tela_inicial()
    pygame.display.flip()
    relogio.tick(60)


# --- LOOP PRINCIPAL DO JOGO ---
jogo_ativo = True

while jogo_ativo:
    # --- LOOP 2: Seleção de Categorias ---
    rodando_menu_categorias = True
    categoria_selecionada = ""

    while rodando_menu_categorias:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if btn_geo.collidepoint(evento.pos):
                    categoria_selecionada = "Geografia"
                    rodando_menu_categorias = False
                elif btn_hist.collidepoint(evento.pos):
                    categoria_selecionada = "História" 
                    rodando_menu_categorias = False
                elif btn_cg.collidepoint(evento.pos):
                    categoria_selecionada = "Conhecimentos Gerais"
                    rodando_menu_categorias = False
                
                # Se clicar em "Sair", zera a pontuação no arquivo e fecha o app
                elif btn_sair_jogo.collidepoint(evento.pos):
                    pontuacao_total = 0            
                    salvar_pontuacao(0)            
                    pygame.quit()
                    sys.exit()

        desenhar_menu_categorias()
        pygame.display.flip()
        relogio.tick(60)

    # --- Filtragem e Reset de Variáveis para a Nova Partida ---
    perguntas_filtradas = [p for p in lista_perguntas if p.materia == categoria_selecionada]
    if len(perguntas_filtradas) == 0:
        perguntas_filtradas = lista_perguntas

    random.shuffle(perguntas_filtradas)

    # MODIFICADO AQUI: A partida agora começa com os pontos acumulados anteriormente, permitindo gastá-los!
    pontuacao = pontuacao_total 
    
    vidas = 3
    indice = 0
    pergunta_carregada = False
    minhas_alts = []
    tempo_inicial = pygame.time.get_ticks()
    dica_usada = False

    rodando_jogo = True

    # --- LOOP 3: O Jogo em si ---
    while rodando_jogo:
        tela.fill(COR_FUNDO)
        posicao_mouse = pygame.mouse.get_pos()

        if indice >= len(perguntas_filtradas):
            rodando_jogo = False
            break

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for alt in minhas_alts:
                    if alt.cor_normal != COR_FUNDO and alt.foi_clicada(posicao_mouse):
                        resposta_clicada = alt.texto
                        if resposta_clicada == perguntas_filtradas[indice].alternativa_correta:
                            pontuacao = pontuar(perguntas_filtradas[indice], pontuacao)
                        else:
                            vidas = perder_vida(vidas)
                            if vidas <= 0:
                                rodando_jogo = False

                        indice += 1
                        pergunta_carregada = False  
                        tempo_inicial = pygame.time.get_ticks()
                        break
                
                if btn_dica.collidepoint(evento.pos):
                    if pontuacao >= 2 and not dica_usada:
                        pontuacao -= 2
                        dica_usada = True
                        
                        erradas = []
                        for alt in minhas_alts:
                            if alt.texto != perguntas_filtradas[indice].alternativa_correta:
                                erradas.append(alt)
                        
                        for alt in erradas[:2]:
                            alt.cor_normal = COR_FUNDO
                            alt.cor_hover = COR_FUNDO
                            alt.cor_texto = COR_FUNDO

        if not rodando_jogo:
            break

        if not pergunta_carregada and indice < len(perguntas_filtradas):
            minhas_alts = [] 
            dica_usada = False 
            for i, alternativa in enumerate(perguntas_filtradas[indice].alternativas):
                if i == 0: posicao = (40, 220)
                elif i == 1: posicao = (410, 220)
                elif i == 2: posicao = (40, 400)
                elif i == 3: posicao = (410, 400)
                
                minhas_alts.append(Alternativa(posicao, alternativa, cores['azul_claro'], cores['verde'], cores['preto']))
            
            pergunta_carregada = True

        if indice < len(perguntas_filtradas):
            enunciado_atual = Enunciado(perguntas_filtradas[indice].enunciado, cores['amarelo'], cores['preto'])
            enunciado_atual.desenhar(tela, fonte_botao)

        for alt in minhas_alts:
            alt.atualizar(posicao_mouse)
            alt.desenhar(tela, fonte_botao)
            
        if gerenciar_cronometro(tela, fonte_botao, tempo_inicial, 15): 
            vidas = perder_vida(vidas)
            indice += 1
            pergunta_carregada = False
            tempo_inicial = pygame.time.get_ticks()
            
        cor_dica_atual = COR_BOTAO_HOVER if btn_dica.collidepoint(posicao_mouse) else cores['verde']
        pygame.draw.rect(tela, cor_dica_atual, btn_dica, border_radius=10)

        texto_dica = fonte_botao.render("Dica (-2)", True, cores['branco'])
        tela.blit(texto_dica, (btn_dica.x + (btn_dica.width - texto_dica.get_width()) // 2, 
                               btn_dica.y + (btn_dica.height - texto_dica.get_height()) // 2))

        desenhar_hud(tela, pontuacao, vidas)
        pygame.display.flip()
        relogio.tick(60)

    # --- FIM DA PARTIDA ATUAL ---
    # MODIFICADO AQUI: A pontuação total agora passa a ser o resultado final dessa partida (com os acertos ou gastos)
    pontuacao_total = pontuacao
    salvar_pontuacao(pontuacao_total)
        
    # --- LOOP 4: Tela de Resultado (Fim de Jogo) ---
    mensagem = mensagem_final(vidas)
    tela_resultado = True

    while tela_resultado:
        posicao_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if btn_menu.collidepoint(evento.pos):
                    tela_resultado = False 

        tela.fill(COR_FUNDO)

        titulo = fonte_sub_titulo.render("Fim de Jogo", True, cores['amarelo'])
        tela.blit(titulo, (260, 80))

        texto_pontos = fonte_botao.render(f"Pontuação Atual: {pontuacao}", True, cores['branco'])
        tela.blit(texto_pontos, (300, 180))

        texto_vidas = fonte_botao.render(f"Vidas restantes: {vidas}", True, cores['branco'])
        tela.blit(texto_vidas, (260, 220))

        for i in range(max(0, vidas)): 
            pygame.draw.circle(tela, cores['vermelho'], (320 + i * 35, 280), 12)

        texto_msg = fonte_botao.render(mensagem, True, cores['branco'])
        x_msg = (LARGURA - texto_msg.get_width()) // 2
        tela.blit(texto_msg, (x_msg, 340))

        cor_btn_menu = COR_BOTAO_HOVER if btn_menu.collidepoint(posicao_mouse) else COR_BOTAO
        pygame.draw.rect(tela, cor_btn_menu, btn_menu, border_radius=12)

        texto = fonte_botao.render("Menu Principal", True, COR_TEXTO)
        tela.blit(texto, (btn_menu.x + (btn_menu.width - texto.get_width()) // 2, 
                          btn_menu.y + (btn_menu.height - texto.get_height()) // 2))

        pygame.display.flip()
        relogio.tick(60)

pygame.quit()