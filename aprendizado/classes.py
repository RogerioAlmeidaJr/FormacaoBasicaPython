class Dog:
    def __init__(self, nome = 'Spike', raca = 'PitBull'):

        self.nome = nome
        self.raca = raca

    def dados(self):
        print(self.nome + " é um cachorro da raça " + self.raca)

cachorro = Dog('Frank', 'Pinscher')
cachorroDefault = Dog()

cachorro.dados()
cachorroDefault.dados()