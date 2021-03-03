from associacao import Pessoa,Celular

smart = Celular("Xiaomix", 1500)
p1 = Pessoa("Clotilde",45,"Rua 666 casa 2")
print(f"{p1.nome} mora no endereço {p1.endereco} e tem {p1.idade} anos")
p1.celular = smart
print(f"{p1.nome} possui um celular da marca {p1.celular.marca} e ele custou {p1.celular.valor}")