class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__
def showClass(self):
    print(f"{self.nomeClasse}= seu nome é {self.nome}")


class Aluno(Pessoa): #subclass
    def __init__(self,nome,idade,matricula):
        Pessoa.__init__(self,nome,idade)
        self.matricula = matricula
    
    def mostraAluno(self): #subclass
           print(f"{self.nomeClasse}= Aluno: seu nome é {self.nome}")

class Professor(Pessoa): #subclass

        def __init__(self,nome,idade,sal):
            Pessoa.__init__(nome,idade)
            self.salario = sal


    def mostraProfessor(self):
           print(f"{self.nomeClasse}= Professor: seu nome é {self.nome}")