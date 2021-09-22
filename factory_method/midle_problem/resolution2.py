from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def some(self):
        character = self.factory_method()
        print(character.show_moves())
        print(character.heal())
        print(character.change_costumes())


class MilitaryCreator(Creator):
    def factory_method(self):
        return Military()


class PirateCreator(Creator):
    def factory_method(self):
        return Pirate()


class WizardCreator(Creator):
    def factory_method(self):
        return Wizard()


class FighterCreator(Creator):
    def factory_method(self):
        return Fighter()


class Character(ABC):
    @abstractmethod
    def show_moves(self):
        pass

    @abstractmethod
    def heal(self):
        pass

    @abstractmethod
    def change_costumes(self):
        pass


class Military(Character):
    def show_moves(self):
        return ["Posição de sentido", "Prestar continência", "Armado"]
    
    def heal(self):
        return "Atadura"
    
    def change_costumes(self):
        return ["Farda", "Roupa de natação"]
    

class Pirate(Character):
    def show_moves(self):
        return ["Relaxado", "Apontando arma antiga com um braço", "Dando gargalhadas"]
    
    def heal(self):
        return "Esteriliza verida com álcool"
    
    def change_costumes(self):
        return "Roupa de velejar"
    

class Wizard(Character):
    def show_moves(self):
        return ["Fazendo magia", "Solta magia com as duas mãos"]
    
    def heal(self):
        return "Poção de cura"
    
    def change_costumes(self):
        return "Roupão e chapéu"


class Fighter(Character):
    def show_moves(self):
        return ["Chutes no ar", "Sequência de socos"]
    
    def heal(self):
        return "Atadura"
    
    def change_costumes(self):
        return "Calção muay thay"


def client(characterType: str):
    if characterType == "wizard":
        return WizardCreator()
    elif characterType == "military":
        return MilitaryCreator()
    elif characterType == "pirate":
        return PirateCreator()
    elif characterType == "fighter":
        return FighterCreator()


if __name__ == "__main__":
    character = input("Qual personagem você escolhe?\n")
    characterConcrete = client(character)
    characterConcrete.some()
