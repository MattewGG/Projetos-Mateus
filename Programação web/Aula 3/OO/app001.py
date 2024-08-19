class Animal: 
    def __init__(self, nome, especie):
        self.nome = nome 
        self.especie = especie
    
    def emitir_som(self):
        print(f'{self.nome} faz um som!')


cachorro = Animal("Rambo", "Cachorro")

gato = Animal("Feliz", "Gato")

print(f"{cachorro.nome} é um cachorro, {gato.nome} é um gato.")


#*** Heramca


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} late")

print("****")

cachorro = Cachorro("Rambo", "cachorro")
                    
cachorro.emitir_som()


#*** Hernaça gato

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} Mia!")

gato = Gato("Felix", "Gato")
print(gato.nome)
gato.emitir_som()


animais = [Cachorro('Rex', "Cachorro"), 
           Gato('Arnaldo', "Gato")]

print("******")
for Animal in animais:
    Animal.emitir_som()