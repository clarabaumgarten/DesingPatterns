from classes.toys.Toy import Barbie, Ken, Polly, HotWheels
from classes.toys.KidsBox import KidsBox


if __name__ == "__main__":
    barbie = Barbie("Barbie", 50, 20, 5)
    ken = Ken("Ken", 50, 22, 7)
    polly = Polly("Polly", 35, 5, 2)
    hotwheels = HotWheels("HotWheels", 20, 5, 15)

    kidsbox = KidsBox()
    kidsbox.addToy(barbie)
    kidsbox.addToy(ken)

    kidsbox3 = KidsBox()
    kidsbox3.addToy(polly)
    kidsbox3.addToy(hotwheels)

    print(kidsbox.getToys())
    print(kidsbox.getTotalPrice())

    print(kidsbox3.getToys())
    print(kidsbox3.getTotalPrice())
