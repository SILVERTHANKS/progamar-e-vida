print('poo'.center(32,'='))
class Pessoa():
    def __init__(self, nome, telefone, cep):
        self.nome = nome
        self.telefone = telefone
        self.cep=cep
    def dados(self):
       print(f'Nome: {self.nome}\nTelefone: {self.telefone}\nCEP: {self.cep}')

p1=Pessoa('carlos', '38888-888','12345-785')
p2=Pessoa('Duda', '3357-1231','12345-666')


pessoas=[p1, p2]


for pessoa in pessoas:
    pessoa.dados()
     