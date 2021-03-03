class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__
def showClass(self):
    print(f"{self.nomeClasse}= seu nome é {self.nome}")


class Aluno(Pessoa): #subclass
    
    
    def mostraAluno(self): #subclass
           print(f"{self.nomeClasse}= seu nome é {self.nome}")

class Professor(Pessoa): #subclass
    def mostraProfessor(self):
           print(f"{self.nomeClasse}= seu nome é {self.nome}")