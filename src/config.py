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





    


Alternativa1 = Alternativa((100, 400), (200,50), pergunta1.alternativas[0], CINZA, BRANCO, PRETO)



alternativas_atuais = [] # Lista para armazenar as alternativas atuais, que pode ser atualizada a cada pergunta

#imprime as alternativas na tela, usando um loop para criar um botão para cada alternativa da pergunta atual, num formato 2x2
for i in range(4): #atribui um valor de posição diferente para cada alternativa, usando o índice i para calcular a posição vertical

    alternativas_atuais.append(Alternativa((100, 400 + i*60), (200,50), pergunta1.alternativas[i], CINZA, BRANCO, PRETO))