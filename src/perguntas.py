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
 
# ============================================
# PERGUNTAS FÁCEIS - GEOGRAFIA
# ============================================
 
pergunta5 = Pergunta(
    "Qual é a capital do Brasil?",
    ("Brasília", "Rio de Janeiro", "São Paulo", "Salvador"),
    "Geografia",
    alternativa_correta="Brasília",
    dificuldade="facil"
)
 
pergunta6 = Pergunta(
    "Qual é o maior oceano do mundo?",
    ("Oceano Pacífico", "Oceano Atlântico", "Oceano Índico", "Oceano Ártico"),
    "Geografia",
    alternativa_correta="Oceano Pacífico",
    dificuldade="facil"
)
 
pergunta7 = Pergunta(
    "Qual país tem o maior número de habitantes?",
    ("Índia", "China", "EUA", "Indonésia"),
    "Geografia",
    alternativa_correta="Índia",
    dificuldade="facil"
)
 
pergunta8 = Pergunta(
    "Qual é a capital da Itália?",
    ("Roma", "Milão", "Veneza", "Florença"),
    "Geografia",
    alternativa_correta="Roma",
    dificuldade="facil"
)
 
pergunta9 = Pergunta(
    "Qual é o maior deserto do mundo?",
    ("Deserto do Saara", "Deserto de Gobi", "Deserto de Mojave", "Deserto da Antártida"),
    "Geografia",
    alternativa_correta="Deserto da Antártida",
    dificuldade="facil"
)
 
# ============================================
# PERGUNTAS FÁCEIS - HISTÓRIA
# ============================================
 
pergunta10 = Pergunta(
    "Em que ano Colombo chegou à América?",
    ("1492", "1500", "1520", "1480"),
    "História",
    alternativa_correta="1492",
    dificuldade="facil"
)
 
pergunta11 = Pergunta(
    "Quem foi o primeiro presidente dos EUA?",
    ("George Washington", "Thomas Jefferson", "John Adams", "Benjamin Franklin"),
    "História",
    alternativa_correta="George Washington",
    dificuldade="facil"
)
 
pergunta12 = Pergunta(
    "Em que continente fica o Egito?",
    ("África", "Ásia", "Europa", "América"),
    "História",
    alternativa_correta="África",
    dificuldade="facil"
)
 
pergunta13 = Pergunta(
    "Quem foi o inventor da lâmpada incandescente?",
    ("Thomas Edison", "Nikola Tesla", "Benjamin Franklin", "Joseph Swan"),
    "História",
    alternativa_correta="Thomas Edison",
    dificuldade="facil"
)
 
# ============================================
# PERGUNTAS FÁCEIS - CIÊNCIAS
# ============================================
 
pergunta14 = Pergunta(
    "Qual elemento químico tem o símbolo 'O'?",
    ("Oxigênio", "Ouro", "Osmium", "Ósmio"),
    "Química",
    alternativa_correta="Oxigênio",
    dificuldade="facil"
)
 
pergunta15 = Pergunta(
    "Qual é o planeta mais próximo do Sol?",
    ("Mercúrio", "Vênus", "Terra", "Marte"),
    "Astronomia",
    alternativa_correta="Mercúrio",
    dificuldade="facil"
)
 
pergunta16 = Pergunta(
    "Quantos ossos tem o corpo humano adulto?",
    ("206", "186", "226", "196"),
    "Biologia",
    alternativa_correta="206",
    dificuldade="facil"
)
 
pergunta17 = Pergunta(
    "Qual é o maior órgão do corpo humano?",
    ("Pele", "Fígado", "Cérebro", "Coração"),
    "Biologia",
    alternativa_correta="Pele",
    dificuldade="facil"
)
 
# ============================================
# PERGUNTAS FÁCEIS - LITERATURA
# ============================================
 
pergunta18 = Pergunta(
    "Quem escreveu 'Cem Anos de Solidão'?",
    ("Gabriel García Márquez", "Pablo Neruda", "Jorge Luis Borges", "Julio Cortázar"),
    "Literatura",
    alternativa_correta="Gabriel García Márquez",
    dificuldade="facil"
)
 
pergunta19 = Pergunta(
    "Quem escreveu 'O Cortiço'?",
    ("Aluísio Azevedo", "Machado de Assis", "Cruz e Sousa", "Gonçalves Dias"),
    "Literatura",
    alternativa_correta="Aluísio Azevedo",
    dificuldade="facil"
)
 
pergunta20 = Pergunta(
    "Em que país nasceu William Shakespeare?",
    ("Inglaterra", "Escócia", "Irlanda", "País de Gales"),
    "Literatura",
    alternativa_correta="Inglaterra",
    dificuldade="facil"
)
 
# ============================================
# PERGUNTAS MÉDIAS - GEOGRAFIA
# ============================================
 
pergunta21 = Pergunta(
    "Qual é a capital da Austrália?",
    ("Canberra", "Sydney", "Melbourne", "Brisbane"),
    "Geografia",
    alternativa_correta="Canberra",
    dificuldade="medio"
)
 
pergunta22 = Pergunta(
    "Qual é o rio mais comprido do mundo?",
    ("Rio Nilo", "Rio Amazonas", "Rio Yangtze", "Rio Mississippi"),
    "Geografia",
    alternativa_correta="Rio Nilo",
    dificuldade="medio"
)
 
pergunta23 = Pergunta(
    "Qual é a cordilheira mais alta do mundo?",
    ("Himalaia", "Andes", "Alpes", "Montanhas Rochosas"),
    "Geografia",
    alternativa_correta="Himalaia",
    dificuldade="medio"
)
 
pergunta24 = Pergunta(
    "Qual país tem mais ilhas?",
    ("Suécia", "Noruega", "Finlândia", "Canadá"),
    "Geografia",
    alternativa_correta="Suécia",
    dificuldade="medio"
)
 
pergunta25 = Pergunta(
    "Qual é o ponto mais alto do Brasil?",
    ("Pico da Neblina", "Pico do Itatiaia", "Serra do Espinhaço", "Pico de Itabira"),
    "Geografia",
    alternativa_correta="Pico da Neblina",
    dificuldade="medio"
)
 
# ============================================
# PERGUNTAS MÉDIAS - HISTÓRIA
# ============================================
 
pergunta26 = Pergunta(
    "Em que ano caiu o Muro de Berlim?",
    ("1989", "1987", "1991", "1985"),
    "História",
    alternativa_correta="1989",
    dificuldade="medio"
)
 
pergunta27 = Pergunta(
    "Quem foi Napoleão Bonaparte?",
    ("Militar e Imperador Francês", "Revolucionário Russo", "General Alemão", "Líder Italiano"),
    "História",
    alternativa_correta="Militar e Imperador Francês",
    dificuldade="medio"
)
 
pergunta28 = Pergunta(
    "Em que ano foi a Revolução Francesa?",
    ("1789", "1799", "1769", "1809"),
    "História",
    alternativa_correta="1789",
    dificuldade="medio"
)
 
pergunta29 = Pergunta(
    "Qual império construiu o Coliseu em Roma?",
    ("Império Romano", "Império Grego", "Império Persa", "Império Otomano"),
    "História",
    alternativa_correta="Império Romano",
    dificuldade="medio"
)
 
pergunta30 = Pergunta(
    "Em que ano terminou a Segunda Guerra Mundial?",
    ("1945", "1944", "1943", "1946"),
    "História",
    alternativa_correta="1945",
    dificuldade="medio"
)
 
# ============================================
# PERGUNTAS MÉDIAS - CIÊNCIAS
# ============================================
 
pergunta31 = Pergunta(
    "Qual é a velocidade da luz?",
    ("300.000 km/s", "150.000 km/s", "500.000 km/s", "100.000 km/s"),
    "Física",
    alternativa_correta="300.000 km/s",
    dificuldade="medio"
)
 
pergunta32 = Pergunta(
    "Quem formulou a teoria da evolução?",
    ("Charles Darwin", "Jean-Baptiste Lamarck", "Gregor Mendel", "Louis Pasteur"),
    "Biologia",
    alternativa_correta="Charles Darwin",
    dificuldade="medio"
)
 
pergunta33 = Pergunta(
    "Qual é o elemento mais abundante da crosta terrestre?",
    ("Oxigênio", "Silício", "Alumínio", "Ferro"),
    "Química",
    alternativa_correta="Oxigênio",
    dificuldade="medio"
)
 
pergunta34 = Pergunta(
    "Qual gás as plantas usam para fazer fotossíntese?",
    ("Dióxido de carbono", "Oxigênio", "Nitrogênio", "Argônio"),
    "Biologia",
    alternativa_correta="Dióxido de carbono",
    dificuldade="medio"
)
 
pergunta35 = Pergunta(
    "Qual é o planeta mais quente do sistema solar?",
    ("Vênus", "Mercúrio", "Marte", "Júpiter"),
    "Astronomia",
    alternativa_correta="Vênus",
    dificuldade="medio"
)
 
# ============================================
# PERGUNTAS MÉDIAS - LITERATURA
# ============================================
 
pergunta36 = Pergunta(
    "Quem escreveu 'Crime e Castigo'?",
    ("Fiódor Dostoiévski", "Lev Tolstói", "Anton Tchékhov", "Ivan Turguêniev"),
    "Literatura",
    alternativa_correta="Fiódor Dostoiévski",
    dificuldade="medio"
)
 
pergunta37 = Pergunta(
    "Qual obra é de Jorge Amado?",
    ("Capitães da Areia", "O Cortiço", "Dom Casmurro", "Memórias Póstumas de Brás Cubas"),
    "Literatura",
    alternativa_correta="Capitães da Areia",
    dificuldade="medio"
)
 
pergunta38 = Pergunta(
    "Quem escreveu 'Grande Sertão: Veredas'?",
    ("Guimarães Rosa", "Graciliano Ramos", "Jorge Amado", "Clarice Lispector"),
    "Literatura",
    alternativa_correta="Guimarães Rosa",
    dificuldade="medio"
)
 
# ============================================
# PERGUNTAS DIFÍCEIS - HISTÓRIA
# ============================================
 
pergunta39 = Pergunta(
    "Em que ano começou a Guerra dos Cem Anos?",
    ("1337", "1300", "1380", "1320"),
    "História",
    alternativa_correta="1337",
    dificuldade="dificil"
)
 
pergunta40 = Pergunta(
    "Quem foi o primeiro Sacro Imperador Romano?",
    ("Carlos Magno", "Oto I", "Henrique III", "Frederico Barba Roxa"),
    "História",
    alternativa_correta="Carlos Magno",
    dificuldade="dificil"
)
 
pergunta41 = Pergunta(
    "Em que ano foi assinada a Magna Carta?",
    ("1215", "1220", "1200", "1225"),
    "História",
    alternativa_correta="1215",
    dificuldade="dificil"
)
 
pergunta42 = Pergunta(
    "Quem foi o último imperador romano do Ocidente?",
    ("Rômulo Augusto", "Nero", "Constantino", "Flávio Máximo"),
    "História",
    alternativa_correta="Rômulo Augusto",
    dificuldade="dificil"
)
 
pergunta43 = Pergunta(
    "Em que ano foi descoberta a circulação do sangue?",
    ("1628", "1600", "1650", "1620"),
    "História",
    alternativa_correta="1628",
    dificuldade="dificil"
)
 
# ============================================
# PERGUNTAS DIFÍCEIS - CIÊNCIAS
# ============================================
 
pergunta44 = Pergunta(
    "Qual é o número de Avogadro?",
    ("6,022 × 10²³", "3,14 × 10²³", "2,71 × 10²³", "9,8 × 10²³"),
    "Química",
    alternativa_correta="6,022 × 10²³",
    dificuldade="dificil"
)
 
pergunta45 = Pergunta(
    "Qual físico propôs a teoria da relatividade?",
    ("Albert Einstein", "Isaac Newton", "Niels Bohr", "Max Planck"),
    "Física",
    alternativa_correta="Albert Einstein",
    dificuldade="dificil"
)
 
pergunta46 = Pergunta(
    "Qual é o processo de divisão celular que produz gametas?",
    ("Meiose", "Mitose", "Citocinese", "Apoptose"),
    "Biologia",
    alternativa_correta="Meiose",
    dificuldade="dificil"
)
 
pergunta47 = Pergunta(
    "Qual elemento químico foi descoberto por Marie Curie?",
    ("Rádio", "Polônio", "Plutônio", "Urânio"),
    "Química",
    alternativa_correta="Rádio",
    dificuldade="dificil"
)
 
pergunta48 = Pergunta(
    "Qual é a constante de Planck aproximadamente?",
    ("6,63 × 10⁻³⁴", "1,38 × 10⁻²³", "9,11 × 10⁻³¹", "1,6 × 10⁻¹⁹"),
    "Física",
    alternativa_correta="6,63 × 10⁻³⁴",
    dificuldade="dificil"
)
 
# ============================================
# PERGUNTAS DIFÍCEIS - LITERATURA
# ============================================
 
pergunta49 = Pergunta(
    "Qual movimento literário Dante Alighieri representa?",
    ("Dolce Stil Novo", "Romantismo", "Realismo", "Simbolismo"),
    "Literatura",
    alternativa_correta="Dolce Stil Novo",
    dificuldade="dificil"
)
 
pergunta50 = Pergunta(
    "Quem escreveu 'Os Sofrimentos do Jovem Werther'?",
    ("Johann Wolfgang von Goethe", "Friedrich Schiller", "Heinrich Heine", "Thomas Mann"),
    "Literatura",
    alternativa_correta="Johann Wolfgang von Goethe",
    dificuldade="dificil"
)
 
pergunta51 = Pergunta(
    "Qual é a obra principal de Machado de Assis?",
    ("Memórias Póstumas de Brás Cubas", "Dom Casmurro", "Quincas Borba", "Esaú e Jacó"),
    "Literatura",
    alternativa_correta="Memórias Póstumas de Brás Cubas",
    dificuldade="dificil"
)
 
pergunta52 = Pergunta(
    "Quem escreveu 'O Processo'?",
    ("Franz Kafka", "Hermann Hesse", "Thomas Mann", "Bertolt Brecht"),
    "Literatura",
    alternativa_correta="Franz Kafka",
    dificuldade="dificil"
)
 
pergunta53 = Pergunta(
    "Qual poeta escreveu 'Os Lusíadas'?",
    ("Luís de Camões", "Pessoa", "Vinícius de Moraes", "Carlos Drummond de Andrade"),
    "Literatura",
    alternativa_correta="Luís de Camões",
    dificuldade="dificil"
)
 
# ============================================
# PERGUNTAS DIFÍCEIS - GEOGRAFIA
# ============================================
 
pergunta54 = Pergunta(
    "Qual é a capital da Birmânia (Myanmar)?",
    ("Naypyidaw", "Yangon", "Mandalay", "Bagan"),
    "Geografia",
    alternativa_correta="Naypyidaw",
    dificuldade="dificil"
)
 
pergunta55 = Pergunta(
    "Qual é a menor nação do mundo por área?",
    ("Vaticano", "Mônaco", "San Marino", "Liechtenstein"),
    "Geografia",
    alternativa_correta="Vaticano",
    dificuldade="dificil"
)
 
pergunta56 = Pergunta(
    "Qual é o pico mais alto da América do Sul?",
    ("Aconcágua", "Ojos del Salado", "Monte San Valentín", "Nevado Sajama"),
    "Geografia",
    alternativa_correta="Aconcágua",
    dificuldade="dificil"
)
 
pergunta57 = Pergunta(
    "Qual é a profundidade máxima do Oceano Pacífico?",
    ("Fossa das Marianas - 11.000m", "Fossa de Tonga - 10.800m", "Fossa do Japão - 9.220m", "Fossa de Kuril - 10.542m"),
    "Geografia",
    alternativa_correta="Fossa das Marianas - 11.000m",
    dificuldade="dificil"
)
 
pergunta58 = Pergunta(
    "Qual estado brasileiro tem a maior área territorial?",
    ("Amazonas", "Mato Grosso", "Bahia", "Pará"),
    "Geografia",
    alternativa_correta="Amazonas",
    dificuldade="dificil"
)
 
# ============================================
# PERGUNTAS MÉDIAS - MATEMÁTICA
# ============================================
 
pergunta59 = Pergunta(
    "Qual é o valor de Pi aproximadamente?",
    ("3,14159", "2,71828", "1,41421", "1,73205"),
    "Matemática",
    alternativa_correta="3,14159",
    dificuldade="medio"
)
 
pergunta60 = Pergunta(
    "Qual é a raiz quadrada de 144?",
    ("12", "11", "13", "14"),
    "Matemática",
    alternativa_correta="12",
    dificuldade="medio"
)
 
pergunta61 = Pergunta(
    "Quanto é 25% de 200?",
    ("50", "40", "60", "30"),
    "Matemática",
    alternativa_correta="50",
    dificuldade="medio"
)
 
pergunta62 = Pergunta(
    "Qual é o dobro de 345?",
    ("690", "600", "700", "680"),
    "Matemática",
    alternativa_correta="690",
    dificuldade="medio"
)
 
# ============================================
# PERGUNTAS DIFÍCEIS - MATEMÁTICA
# ============================================
 
pergunta63 = Pergunta(
    "Qual matemático é famoso pelo Teorema de Pitágoras?",
    ("Pitágoras", "Euclides", "Arquimedes", "Thales"),
    "Matemática",
    alternativa_correta="Pitágoras",
    dificuldade="dificil"
)
 
pergunta64 = Pergunta(
    "Qual é a fórmula de Bhaskara usada para resolver?",
    ("Equações de segundo grau", "Equações de primeiro grau", "Funções exponenciais", "Logaritmos"),
    "Matemática",
    alternativa_correta="Equações de segundo grau",
    dificuldade="dificil"
)
 
pergunta65 = Pergunta(
    "Qual número é considerado a base dos logaritmos naturais?",
    ("e (2,71828...)", "π (3,14159...)", "φ (1,61803...)", "γ (0,57721...)"),
    "Matemática",
    alternativa_correta="e (2,71828...)",
    dificuldade="dificil"
)
 
pergunta66 = Pergunta(
    "Qual é o último teorema de Fermat?",
    ("xⁿ + yⁿ ≠ zⁿ para n > 2", "x² + y² = z²", "a² - b² = (a+b)(a-b)", "x³ + y³ = z³"),
    "Matemática",
    alternativa_correta="xⁿ + yⁿ ≠ zⁿ para n > 2",
    dificuldade="dificil"
)
 
# ============================================
# PERGUNTAS MÉDIAS - MÚSICA
# ============================================
 
pergunta67 = Pergunta(
    "Quantas notas musicais existem na escala cromática?",
    ("12", "10", "14", "8"),
    "Música",
    alternativa_correta="12",
    dificuldade="medio"
)
 
pergunta68 = Pergunta(
    "Em que país nasceu Ludwig van Beethoven?",
    ("Alemanha", "Áustria", "Itália", "França"),
    "Música",
    alternativa_correta="Alemanha",
    dificuldade="medio"
)
 
pergunta69 = Pergunta(
    "Qual instrumento tem o maior registro de freqüência?",
    ("Piano", "Violino", "Trompa", "Trompete"),
    "Música",
    alternativa_correta="Piano",
    dificuldade="medio"
)
 
# ============================================
# PERGUNTAS DIFÍCEIS - MÚSICA
# ============================================
 
pergunta70 = Pergunta(
    "Quem compôs a 'Nona Sinfonia'?",
    ("Ludwig van Beethoven", "Wolfgang Mozart", "Joseph Haydn", "Johann Sebastian Bach"),
    "Música",
    alternativa_correta="Ludwig van Beethoven",
    dificuldade="dificil"
)
 
pergunta71 = Pergunta(
    "Qual compositor foi 'o pai da ópera'?",
    ("Claudio Monteverdi", "Giuseppe Verdi", "George Frideric Handel", "Wolfgang Amadeus Mozart"),
    "Música",
    alternativa_correta="Claudio Monteverdi",
    dificuldade="dificil"
)
 
# ============================================
# PERGUNTAS MÉDIAS - SPORTS
# ============================================
 
pergunta72 = Pergunta(
    "Em que país foi criado o futebol moderno?",
    ("Inglaterra", "Brasil", "França", "Alemanha"),
    "Esportes",
    alternativa_correta="Inglaterra",
    dificuldade="medio"
)
 
pergunta73 = Pergunta(
    "Quantos jogadores cada time tem em um jogo de basquete?",
    ("5", "6", "7", "4"),
    "Esportes",
    alternativa_correta="5",
    dificuldade="medio"
)
 
# ============================================
# PERGUNTAS FÁCEIS - CULTURA GERAL
# ============================================
 
pergunta74 = Pergunta(
    "Qual cor é o topo da bandeira do Brasil?",
    ("Verde", "Amarelo", "Azul", "Branco"),
    "Cultura Geral",
    alternativa_correta="Verde",
    dificuldade="facil"
)
 
pergunta75 = Pergunta(
    "Quantos continentes existem?",
    ("7", "6", "5", "8"),
    "Geografia",
    alternativa_correta="7",
    dificuldade="facil"
)
 
# ============================================
# COMPILAR LISTA COMPLETA
# ============================================
 
lista_perguntas = [
    pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, 
    pergunta9, pergunta10, pergunta11, pergunta12, pergunta13, pergunta14, pergunta15, pergunta16,
    pergunta17, pergunta18, pergunta19, pergunta20, pergunta21, pergunta22, pergunta23, pergunta24,
    pergunta25, pergunta26, pergunta27, pergunta28, pergunta29, pergunta30, pergunta31, pergunta32,
    pergunta33, pergunta34, pergunta35, pergunta36, pergunta37, pergunta38, pergunta39, pergunta40,
    pergunta41, pergunta42, pergunta43, pergunta44, pergunta45, pergunta46, pergunta47, pergunta48,
    pergunta49, pergunta50, pergunta51, pergunta52, pergunta53, pergunta54, pergunta55, pergunta56,
    pergunta57, pergunta58, pergunta59, pergunta60, pergunta61, pergunta62, pergunta63, pergunta64,
    pergunta65, pergunta66, pergunta67, pergunta68, pergunta69, pergunta70, pergunta71, pergunta72,
    pergunta73, pergunta74, pergunta75
]
 
# ============================================
# INFORMAÇÕES DA LISTA
# ============================================
 
''' print(f"Total de perguntas: {len(lista_perguntas)}")
print(f"Total de categorias: {len(set(p.categoria for p in lista_perguntas))}")
 
# Contagem por dificuldade
dificuldades = {}
for pergunta in lista_perguntas:
    dificuldades[pergunta.dificuldade] = dificuldades.get(pergunta.dificuldade, 0) + 1
 
print("\nPerguntas por dificuldade:")
for dif, qtd in sorted(dificuldades.items()):
    print(f"  {dif.capitalize()}: {qtd}")
 
# Contagem por categoria
categorias = {}
for pergunta in lista_perguntas:
    categorias[pergunta.categoria] = categorias.get(pergunta.categoria, 0) + 1
 
print("\nPerguntas por categoria:")
for cat in sorted(categorias.keys()):
    print(f"  {cat}: {categorias[cat]}")'''