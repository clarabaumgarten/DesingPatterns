class Judge():
    name = None

    def setName(self, name):
        Judge.name = name
    
    def getName(self):
        return Judge.name


if __name__ == "__main__":
    avatar = Judge()
    avatar.setName("Avatar")
    avatar2 = Judge()

    print("Differents objects (avatar == avatar2): ", avatar == avatar2)
    print("\nBut, the same names: ", avatar2.getName(), avatar.getName())
    
    avatar2.setName("Juíz")

    print("But, the same names: ", avatar2.getName(), avatar.getName())
    print("\nDifferent objects with the same info")