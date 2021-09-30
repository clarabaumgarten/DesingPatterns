from abc import ABC, abstractmethod
from classes.toys.Toy import Barbie, Polly, Ken, HotWheels
from classes.toys.KidsBox import KidsBox


class AbstractBuilder(ABC):
    @abstractmethod
    def makeBox():
        pass


class FemaleBox(AbstractBuilder):
    _box = KidsBox()

    def makeBox(self):
        barbie = Barbie("Barbie", 50, 20, 5)
        polly = Polly("Polly", 35, 20, 5)
        self._box.addToy(barbie)
        self._box.addToy(polly)
    
    def getBox(self):
        return self._box

    def reset(self):
        self._box.reset()


class MaleBox(AbstractBuilder):
    _box = KidsBox()

    def makeBox(self):
        ken = Ken("Ken", 50, 20, 5)
        hotWheels = HotWheels("HotWheels", 20, 20, 5)
        self._box.addToy(ken)
        self._box.addToy(hotWheels)
    
    def getBox(self):
        return self._box

    def reset(self):
        self._box.reset()
