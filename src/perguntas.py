class Pergunta:
    def __init__(self, pergunta: str, alternativas: tuple, materia: str, id=None, alternativa_correta=None, dificuldade=None):

        # A classe Pergunta representa uma pergunta de múltipla escolha, 
        # contendo a pergunta em si, as alternativas disponíveis, 
        # a matéria relacionada, um identificador único e a alternativa correta.
        #na hora de criar a pergunta, você coloca
        self.pergunta = pergunta
        self.id = id(self)
        self.alternativas = alternativas
        self.materia = materia
        self.alternativa_correta = alternativa_correta
        self.dificuldade = dificuldade


pergunta1 = Pergunta(
    "Qual é a capital da França?",
    ("Paris", "Londres", "Roma", "Madri"),
    "Geografia",
    id = 1,
    alternativa_correta="Paris",
    dificuldade="facil"
)

pergunta2 = Pergunta(
    "Qual é a fórmula da água?",    
    ("H2O", "CO2", "O2", "NaCl"),
    "Química",
    id = 2,
    alternativa_correta="H2O",
    dificuldade="facil"
)

pergunta3 = Pergunta(
    "Quem escreveu 'Dom Quixote'?",
    ("Miguel de Cervantes", "William Shakespeare", "Jorge Luis Borges", "Gabriel García Márquez"),
    "Literatura",
    id = 3,
    alternativa_correta="Miguel de Cervantes",
    dificuldade="facil"
)

perguntas = [pergunta1, pergunta2, pergunta3]