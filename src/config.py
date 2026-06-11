import pygame
from perguntas import *

# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Projeto Final - Pygame"

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212,212,212)

CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"





#criando a tela inicial


class Enunciado:
    def __init__(self, posicao:tuple, dimensoes:tuple, texto, cor_fundo, cor_texto):
        x, y = posicao #desempacotamento da tupla para facilitar a leitura
        largura, altura = dimensoes #desempacotamento da tupla para facilitar a leitura
        self.texto = texto
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.rect = pygame.Rect(x, y, largura, altura) #cria um retângulo com as coordenadas e dimensões fornecidas
    
    def desenhar(self, tela, fonte):
        pygame.draw.rect(tela, self.cor_fundo, self.rect) #desenha o retângulo de fundo

        texto_surface = fonte.render(self.texto, True, self.cor_texto) #renderiza o texto
        texto_rect = texto_surface.get_rect(center=self.rect.center) #centraliza o texto dentro do retângulo
        tela.blit(texto_surface, texto_rect) #desenha o texto na tela


import pygame

class Alternativa:
    def __init__(self, posicao, dimensoes, texto, cor_normal, cor_hover, cor_texto):
        x, y = posicao
        largura, altura = dimensoes
        
        # Cria o retângulo oficial que define onde o botão fica na tela
        self.rect = pygame.Rect(x, y, largura, altura)
        
        self.texto = texto
        self.cor_normal = cor_normal
        self.cor_hover = cor_hover
        self.cor_texto = cor_texto
        
        # A cor atual começa como a cor normal do botão
        self.cor_atual = cor_normal

    def atualizar(self, posicao_mouse):
        # Verifica se o mouse está em cima do retângulo (Efeito Hover do CSS)
        if self.rect.collidepoint(posicao_mouse):
            self.cor_atual = self.cor_hover  # Muda para a cor de destaque
        else:
            self.cor_atual = self.cor_normal  # Volta para a cor padrão

    def desenhar(self, tela, fonte):
        # 1. Desenha o retângulo usando a cor_atual (que muda no atualizar)
        pygame.draw.rect(tela, self.cor_atual, self.rect)
        
        # 2. Renderiza e centraliza o texto da alternativa dentro do botão
        texto_surface = fonte.render(self.texto, True, self.cor_texto)
        texto_rect = texto_surface.get_rect()
        texto_rect.center = self.rect.center
        
        # 3. Desenha o texto na tela
        tela.blit(texto_surface, texto_rect)

    def foi_clicado(self, posicao_mouse):
        # Retorna True se o clique do mouse aconteceu dentro deste botão
        return self.rect.collidepoint(posicao_mouse)
    


Alternativa1 = Alternativa((100, 400), (200,50), pergunta1.alternativas[0], CINZA, BRANCO, PRETO)



alternativas_atuais = [] # Lista para armazenar as alternativas atuais, que pode ser atualizada a cada pergunta

#imprime as alternativas na tela, usando um loop para criar um botão para cada alternativa da pergunta atual, num formato 2x2
for i in range(4): #atribui um valor de posição diferente para cada alternativa, usando o índice i para calcular a posição vertical

    alternativas_atuais.append(Alternativa((100, 400 + i*60), (200,50), pergunta1.alternativas[i], CINZA, BRANCO, PRETO))