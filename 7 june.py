#OOPS (Object Oriented Programming)
#defining a class
class panda:
    pass
obj = panda()

class Panda:
    attr1 = "mammal"
    def __init__(self, name):
        self.name = name

kungfu = Panda("kungfu")
motu = Panda("motu")

print("kungfu is a {}".format(kungfu.__class__.attr1))
print("motu is a {}".format(motu.__class__.attr1))

print("my name is {}".format(kungfu.name))
print("my name is {}".format(motu.name))