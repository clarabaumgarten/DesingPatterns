from abc import ABC, abstractmethod


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
        return "Esteriliza ferida com álcool"
    
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


if __name__ == "__main__":
    character = input("Qual personagem você escolhe?\n")
    
    if character == "wizard":
        print(Wizard().show_moves())
        print(Wizard().heal())
        print(Wizard().change_costumes())
    elif character == "military":
        print(Military().show_moves())
        print(Military().heal())
        print(Military().change_costumes())
    elif character == "pirate":
        print(Pirate().show_moves())
        print(Pirate().heal())
        print(Pirate().change_costumes())
    elif character == "fighter":
        print(Fighter().show_moves())
        print(Fighter().heal())
        print(Fighter().change_costumes())
