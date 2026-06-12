import time
import pygame

pygame.font.init()
fonte = pygame.font.SysFont("Arial", 48)
relogio = pygame.time.Clock()

def gerenciar_cronometro(tela, fonte, tempo_inicial, tempo_total=15):
    tempo_atual = pygame.time.get_ticks()
    segundos_passados = (tempo_atual - tempo_inicial) // 1000
    tempo_restante = tempo_total - segundos_passados
    
    if tempo_restante <= 0:
        tempo_restante = 0
        
    # 1. RENDER: Cria a "figurinha" do texto
    texto_tempo = fonte.render(f"Tempo: {tempo_restante}", True, (255, 255, 255))
    
    # --- MATEMÁTICA PARA O CANTO SUPERIOR DIREITO ---
    # Pegamos a largura total da tela (ex: 800)
    largura_da_tela = tela.get_width() 
    
    # Subtraímos a largura do texto para ele não ficar escondido, 
    # e tiramos mais uns 20 pixels de margem para não colar na borda.
    posicao_x = largura_da_tela - texto_tempo.get_width() - 20
    posicao_y = 20 # 20 pixels para baixo do topo
    
    # 2. BLIT: Carimba o texto na posição certa
    tela.blit(texto_tempo, (posicao_x, posicao_y))
    
    return tempo_restante == 0

def pontuar(pergunta, pontuacao_atual, resposta):
    '''
    Esta função calcula e RETORNA a pontuação atualizada do jogador.
    '''

    if resposta == pergunta.alternativa_correta:
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



