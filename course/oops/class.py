

class dog(object):
    # __init__ is known as constructor
    # we can replace self with anything,assigning name and age to that object
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def speak(Dog):
        print("My name is {} and age is {} months".format(Dog.name,Dog.age))
        
    def bark(self):
        print("If {} didn't get his food he will start barking".format(self.name))



class Mammal(object):
    # attributes
    name = ""
    position = 0
    #constructors
    def __init__(self,name,num):
        self.name = name
        self.position = num
        
    #destructor
    def __del__(self):
        print("Destructor is called")
    #methods
    def details(self):
        print("My name is {} , position is {}".format(self.name,self.position))

judo = dog('judo',6)
judo.speak()
judo.bark()

Whale = Mammal('Humman',120)
Whale.details()