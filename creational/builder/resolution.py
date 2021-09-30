from classes.builder.Builders import FemaleBox, MaleBox


if __name__ == "__main__":
    femaleBox = FemaleBox()
    femaleBox.makeBox()
    print(femaleBox.getBox())
    print(femaleBox.getBox().getTotalPrice())
    femaleBox.getBox().reset()

    print("------------")

    maleBox = MaleBox()
    maleBox.makeBox()

    toys = maleBox.getBox().getToys()
    print(maleBox.getBox().getTotalPrice())
