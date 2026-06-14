import time
import pygame

pygame.font.init()
fonte = pygame.font.SysFont("Arial", 48)
relogio = pygame.time.Clock()

def gerenciar_cronometro(tela, fonte, tempo_inicial, tempo_total=15):
    tempo_atual = pygame.time.get_ticks()
    segundos_passados = (tempo_atual - tempo_inicial) // 1000
    tempo_restante = max(0, tempo_total - segundos_passados) # Garante que não fique negativo
    
    # --- GEOMETRIA DO CRONÔMETRO (Alinhado com o Enunciado) ---
    # Baseado na nossa tabela: X=640, Y=40, Largura=120, Altura=120
    raio = 60
    centro_x = 640 + raio  # 700
    centro_y = 40 + raio   # 100
    
    # 1. DESENHA O CÍRCULO (Fundo do Cronômetro)
    # Substitua as cores pelas variáveis que você está usando (ex: cores['azul_claro'])
    cor_circulo = (40, 40, 40) # Uma cor de fundo para o círculo
    pygame.draw.circle(tela, cor_circulo, (centro_x, centro_y), raio)
    
    # Opcional: Desenhar uma borda no círculo para dar acabamento
    cor_borda = (255, 255, 255)
    pygame.draw.circle(tela, cor_borda, (centro_x, centro_y), raio, 3) # Espessura 3
    
    # 2. RENDERIZA APENAS O NÚMERO
    texto_tempo = fonte.render(str(tempo_restante), True, (255, 255, 255))
    
    # 3. CENTRALIZA O TEXTO NO CÍRCULO
    # Pegamos o retângulo do texto gerado e jogamos o centro dele para o centro do círculo
    texto_rect = texto_tempo.get_rect()
    texto_rect.center = (centro_x, centro_y)
    
    # 4. BLIT: Desenha o número centralizado
    tela.blit(texto_tempo, texto_rect)
    
    return tempo_restante == 0

def pontuar(pergunta, pontuacao_atual):
    '''
    Esta função calcula e RETORNA a pontuação atualizada do jogador.
    '''

    if pergunta.dificuldade == 'facil':
            pontuacao_atual += 1
    elif pergunta.dificuldade == 'media':
            pontuacao_atual += 2
    elif pergunta.dificuldade == 'dificil':
            pontuacao_atual += 3
    return pontuacao_atual # Retorna o novo valor para quem chamou

def perder_vida(vidas_atuais):
    '''
    Esta função calcula e RETORNA a quantidade de vidas atualizada do jogador.
    '''

    vidas_atuais -= 1
    return vidas_atuais



