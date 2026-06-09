import sys
import os

# Esse bloco diz para o Python olhar a pasta pai (raiz) antes de buscar os imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Seus imports originais continuam aqui embaixo:
from src import funcoes
from src.perguntas import *
import random



vidas = 3
pontuacao = 0
random.shuffle(lista_perguntas)

for pergunta in lista_perguntas:  
    print(pergunta.enunciado)
    resposta = input('Resposta: ').lower()
    
    if resposta == pergunta.alternativa_correta:
        if pergunta.dificuldade == 'facil':
            pontuacao += 10
        elif pergunta.dificuldade == 'media':
            pontuacao += 20
        elif pergunta.dificuldade == 'dificil':
            pontuacao += 30   
    else:
        print('Você errou, perdeu uma vida!')
        vidas -= 1
        if vidas == 0:
            print('Game Over')
            break  # Interrompe o loop se as vidas acabarem
else:
    print(f'Você venceu! Pontuação final: {pontuacao}')

print("Fim do programa.")