class Dog:
    species = "canine"
    num_dogs=0



    def __init__(self,name,breed,location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs+=1
    
    @classmethod
    def register_stray(cls):
        return cls("coming soon","unknown","unknown")
        

    def add_trick(self,new_tricks):
        self.tricks.append(new_tricks)
    
    def bark(self):
        print("Bow Bow Bow",self.name)
    
    def learn(self,new_tricks):
        if new_tricks not in self.tricks:
            self.tricks.append(new_tricks)
    
    def perform(self,trick):
        if trick in self.tricks:
            print(f'{self.name} performs {trick}')
        else:
            print(f'{self.name} does not performs {trick}')



kaiser = Dog("kaiser","Pub","America")
kaiser.learn("sit")
kaiser.learn("stand")
#print(Dog.num_dogs)
meatloaf = Dog("meatloaf","pug",18475)
meatloaf.learn("sit")
meatloaf.learn("jump")
#print(Dog.num_dogs)
#print(kaiser.name)
#print(kaiser.breed)
#print(kaiser.location)
#kaiser.add_trick("sit")
#kaiser.add_trick("stand")
#print(kaiser.tricks)
#kaiser.bark()

#kaiser.perform("sit")
#meatloaf.perform("stand")
#meatloaf.perform("sit")

stary1 = Dog.register_stray()
print(stary1.name)
print(stary1.location)
