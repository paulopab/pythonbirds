class Pessoa:
    def __init__(self, *filhos, nome = None, idade =35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    reuel = Pessoa(nome='Reuel')
    paulo = Pessoa(reuel, nome='paulo')

    print(Pessoa.cumprimentar(paulo))
    print(paulo.nome, paulo.idade)

    for filho in paulo.filhos:
        print(filho.nome)