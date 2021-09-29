from classes.toys.Toy import Toy


class KidsBox():
    _toys = []

    def addToy(self, toy: Toy):
        self._toys.append(toy)
  
    def getTotalPrice(self) -> float:
        sum = 0
        for toy in self._toys:
            sum += toy.getPrice()
        return sum
    
    def getToys(self):
        return self._toys
    
    def reset(self):
        self._toys = []
