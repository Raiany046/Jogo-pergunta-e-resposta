class Pergunta:
    def __init__(self, enunciado: str, alternativas: tuple, materia: str, id=None, alternativa_correta=None, dificuldade=None):

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


pergunta1 = Pergunta(
    "Qual é a capital da França?",
    ("aris", "londres", "roma", "madri"),
    "Geografia",
    id = 1,
    alternativa_correta="paris",
    dificuldade="facil"
)

pergunta2 = Pergunta(
    "Qual é a fórmula da água?",    
    ("h2o", "co2", "o2", "nacl"),
    "Química",
    id = 2,
    alternativa_correta="h2o",
    dificuldade="facil"
)

pergunta3 = Pergunta(
    "Quem escreveu 'Dom Quixote'?",
    ("miguel de cervantes", "william shakespeare", "jorge Luis Borges", "gabriel garcía márquez"),
    "Literatura",
    id = 3,
    alternativa_correta="Miguel de Cervantes",
    dificuldade="facil"
)

lista_perguntas = [pergunta1, pergunta2, pergunta3]