import time

def cronometro():
    inicio = time.time()
    for i in range(1, 16):
        print(i)
        time.sleep(1)
    fim = time.time()


def pontuar(pergunta, pontuacao_atual, resposta):
    # Esta função agora calcula e RETORNA a nova pontuação
    if resposta == pergunta.alternativa_correta:
        if pergunta.dificuldade == 'facil':
            pontuacao_atual += 10
        elif pergunta.dificuldade == 'media':
            pontuacao_atual += 20
        elif pergunta.dificuldade == 'dificil':
            pontuacao_atual += 30
    return pontuacao_atual # Retorna o novo valor para quem chamou

def perder_vida(vidas_atuais):
    # Esta função calcula e RETORNA a quantidade de vidas
    vidas_atuais -= 1
    return vidas_atuais


