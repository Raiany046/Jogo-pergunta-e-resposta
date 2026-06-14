import pygame
class Pergunta:
    def __init__(self, enunciado: str, alternativas: tuple, materia: str, alternativa_correta=None, dificuldade=None):

        # A classe Pergunta representa uma pergunta de múltipla escolha, 
        # contendo a pergunta em si, as alternativas disponíveis, 
        # a matéria relacionada, um identificador único e a alternativa correta.
        #na hora de criar a pergunta, você coloca
        self.enunciado = enunciado
        self.id = id
        self.alternativas = alternativas
        self.materia = materia
        self.alternativa_correta = alternativa_correta
        self.dificuldade = dificuldade





class Enunciado:
    def __init__(self, texto, cor_fundo, cor_texto):
        x, y = 40, 40
        largura, altura = 580, 120
        self.texto = texto
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.rect = pygame.Rect(x, y, largura, altura) #cria um retângulo com as coordenadas e dimensões fornecidas
    
    def desenhar(self, tela, fonte):
        pygame.draw.rect(tela, self.cor_fundo, self.rect) #desenha o retângulo de fundo

        texto_surface = fonte.render(self.texto, True, self.cor_texto) #renderiza o texto
        texto_rect = texto_surface.get_rect(center=self.rect.center) #centraliza o texto dentro do retângulo
        tela.blit(texto_surface, texto_rect) #desenha o texto na tela




class Alternativa:
    def __init__(self, posicao, texto, cor_normal, cor_hover, cor_texto):
        x, y = posicao
        largura, altura = 350, 160
        
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

    def foi_clicada(self, posicao_mouse):
        # Retorna True se o clique do mouse aconteceu dentro deste botão
        return self.rect.collidepoint(posicao_mouse)
    


pergunta1 = Pergunta(
    "Qual é a capital da França?",
    ("Paris", "Londres", "Roma", "Madri"),
    "Geografia",
    alternativa_correta="Paris",
    dificuldade="facil"
)

pergunta2 = Pergunta(
    "Qual é a fórmula da água?",    
    ("H2O", "CO2", "O2", "NaCl"),
    "Química",
    alternativa_correta="H2O",
    dificuldade="facil"
)

pergunta3 = Pergunta(
    "Quem escreveu 'Dom Quixote'?",
    ("Miguel de Cervantes", "William Shakespeare", "Jorge Luis Borges", "Gabriel García Márquez"),
    "Literatura",
    alternativa_correta="Miguel de Cervantes",
    dificuldade="facil"
)

pergunta4 = Pergunta(
    "Quem descobriu o Brasil?",    
    ("Pedro Álvares Cabral", "Cristóvão Colombo", "Vasco da Gama", "Fernão de Magalhães"),
    "História",
    alternativa_correta="Pedro Álvares Cabral",
    dificuldade="facil"
)

lista_perguntas = [pergunta1, pergunta2, pergunta3, pergunta4]
