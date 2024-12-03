class Aluno2:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class equipe:
    def __init__(self, projeto, *equipes):
        self.projeto = projeto
        self.equipes = equipes[:]


class GerenciadorEquipes:
    def __init__(self, ):