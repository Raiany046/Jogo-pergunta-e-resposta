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
        largura, altura = 580, 140

        self.texto = texto
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.rect = pygame.Rect(x, y, largura, altura)

    def desenhar(self, tela, fonte):

        pygame.draw.rect(
            tela,
            self.cor_fundo,
            self.rect,
            border_radius=15
        )

        palavras = self.texto.split()

        linhas = []
        linha_atual = ""

        for palavra in palavras:

            teste = linha_atual + palavra + " "

            if fonte.size(teste)[0] <= self.rect.width - 30:
                linha_atual = teste
            else:
                linhas.append(linha_atual)
                linha_atual = palavra + " "

        linhas.append(linha_atual)

        altura_linha = fonte.get_height()
        altura_total = len(linhas) * altura_linha

        y = self.rect.centery - altura_total // 2

        for linha in linhas:

            texto_surface = fonte.render(
                linha,
                True,
                self.cor_texto
            )

            texto_rect = texto_surface.get_rect(
                centerx=self.rect.centerx
            )

            texto_rect.y = y

            tela.blit(texto_surface, texto_rect)

            y += altura_linha


class Alternativa:
    def __init__(self, posicao, texto, cor_normal, cor_hover, cor_texto):
        x, y = posicao
        largura,altura = 350,160
        
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
        pygame.draw.rect(
            tela,
            self.cor_atual,
            self.rect,
            border_radius=15)
        
        # 2. Renderiza e centraliza o texto da alternativa dentro do botão
        texto_surface = fonte.render(self.texto, True, self.cor_texto)
        texto_rect = texto_surface.get_rect()
        texto_rect.center = self.rect.center
        
        # 3. Desenha o texto na tela
        tela.blit(texto_surface, texto_rect)

    def foi_clicada(self, posicao_mouse):
        # Retorna True se o clique do mouse aconteceu dentro deste botão
        return self.rect.collidepoint(posicao_mouse)
    


# --- GEOGRAFIA ---

pergunta_geo_1 = Pergunta(
    "Qual é o maior oceano do planeta?",
    ("Oceano Atlântico", "Oceano Índico", "Oceano Pacífico", "Oceano Ártico"),
    "Geografia",
    alternativa_correta="Oceano Pacífico",
    dificuldade="facil"
)

pergunta_geo_2 = Pergunta(
    "Qual destes países NÃO faz parte da União Europeia?",
    ("França", "Suíça", "Alemanha", "Itália"),
    "Geografia",
    alternativa_correta="Suíça",
    dificuldade="medio"
)

pergunta_geo_3 = Pergunta(
    "Qual é a capital da Austrália?",
    ("Sydney", "Melbourne", "Canberra", "Brisbane"),
    "Geografia",
    alternativa_correta="Canberra",
    dificuldade="medio"
)

pergunta_geo_4 = Pergunta(
    "Qual é o rio mais longo do mundo?",
    ("Rio Nilo", "Rio Amazonas", "Rio Yangtze", "Rio Mississippi"),
    "Geografia",
    alternativa_correta="Rio Amazonas",
    dificuldade="dificil"
)


# --- HISTÓRIA ---

pergunta_hist_1 = Pergunta(
    "Em que ano teve início a Primeira Guerra Mundial?",
    ("1914", "1918", "1939", "1945"),
    "História",
    alternativa_correta="1914",
    dificuldade="medio"
)

pergunta_hist_2 = Pergunta(
    "Quem foi o primeiro presidente do Brasil?",
    ("Getúlio Vargas", "Marechal Deodoro da Fonseca", "Dom Pedro II", "Prudente de Morais"),
    "História",
    alternativa_correta="Marechal Deodoro da Fonseca",
    dificuldade="medio"
)

pergunta_hist_3 = Pergunta(
    "Qual civilização antiga construiu as pirâmides de Gizé?",
    ("Incas", "Astecas", "Egípcios", "Romanos"),
    "História",
    alternativa_correta="Egípcios",
    dificuldade="facil"
)

pergunta_hist_4 = Pergunta(
    "Quem foi o principal líder da Revolução Russa de 1917?",
    ("Karl Marx", "Vladimir Lenin", "Joseph Stalin", "Leon Trotsky"),
    "História",
    alternativa_correta="Vladimir Lenin",
    dificuldade="dificil"
)


# --- CONHECIMENTOS GERAIS ---

pergunta_cg_1 = Pergunta(
    "Quantos ossos tem o corpo humano adulto?",
    ("206", "186", "300", "214"),
    "Conhecimentos Gerais",
    alternativa_correta="206",
    dificuldade="medio"
)

pergunta_cg_2 = Pergunta(
    "Quem pintou a famosa obra 'Mona Lisa'?",
    ("Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"),
    "Conhecimentos Gerais",
    alternativa_correta="Leonardo da Vinci",
    dificuldade="facil"
)

pergunta_cg_3 = Pergunta(
    "Qual é o elemento mais abundante no universo?",
    ("Oxigênio", "Hidrogênio", "Hélio", "Carbono"),
    "Conhecimentos Gerais",
    alternativa_correta="Hidrogênio",
    dificuldade="dificil"
)

pergunta_cg_4 = Pergunta(
    "Qual rede social é conhecida pelo limite original de 140 caracteres e o símbolo de um pássaro?",
    ("Instagram", "Facebook", "Twitter (X)", "TikTok"),
    "Conhecimentos Gerais",
    alternativa_correta="Twitter (X)",
    dificuldade="facil"
)

lista_perguntas = [
    pergunta_geo_1,
    pergunta_geo_2,
    pergunta_geo_3,
    pergunta_geo_4,
    pergunta_hist_1,
    pergunta_hist_2,
    pergunta_hist_3,
    pergunta_hist_4,
    pergunta_cg_1,
    pergunta_cg_2,
    pergunta_cg_3,
    pergunta_cg_4
]