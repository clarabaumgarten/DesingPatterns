class Judge():
    __instance = None

    def __init__(self, name):
        if Judge.__instance == None:
            Judge.__instance = self
            Judge.name = name
        else:
            raise Exception("Singleton, please")

    def setName(self, name):
        Judge.name = name

    def getName(self):
        return Judge.name

    def getInstance():
        if Judge.__instance == None:
            Judge()
        
        return Judge.__instance

if __name__ == "__main__":
    avatar = Judge("Avatar")
    avatar2 = Judge.getInstance()

    print("Is the same instance: ",avatar2 == avatar)
    print(avatar.name, avatar2.name)

    avatar2.setName("Júiz")
    print("\nSet avatar2 name to Júiz")

    print(avatar2.name, avatar.name)
    print("\nJust the same class instance | Single one object")