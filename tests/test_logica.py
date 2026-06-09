import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #só pra conseguir rodar o código aqui mesmo



from src.funcoes import *
from src.perguntas import *
import random



vidas = 3
pontuacao = 0

random.shuffle(lista_perguntas) #organiza a lista aleatoriamente pra randomizar as perguntas 

for pergunta in lista_perguntas:  
    print(pergunta.enunciado)
    resposta = input('Resposta: ').lower()
    
    if resposta == pergunta.alternativa_correta:
        pontuacao = pontuar(pergunta, pontuacao, resposta) 

    else:
        print('Você errou, perdeu uma vida!')
        vidas = perder_vida(vidas) 
        
    # Checa o Game Over
    if vidas == 0:
        print('Game Over')
        break  
else:
    print(f'Você venceu! Pontuação final: {pontuacao}')

print("Fim do programa.")