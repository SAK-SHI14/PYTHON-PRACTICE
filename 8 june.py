#inheritence in python
class Bird:
  def make_sound(self):
    print("Generic bird sound")

class Parrot(Bird):
  def make_sound(self):
    print("Squawk!")

class Sparrow(Bird):
  def make_sound(self):
    print("Chirp!")

class Falcon(Bird):
  def make_sound(self):
    print("Screech!")

class AfricanGreyParrot(Parrot):  # AfricanGreyParrot inherits from Parrot
  pass

birds = [Bird(), Parrot(), Sparrow(), Falcon(), AfricanGreyParrot()]
for bird in birds:
  bird.make_sound()