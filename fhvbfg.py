class Dog:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def bark(self):
        print(f"{self.name} says woof!")

    def get_age(self):
        return self.age

    def dog_info(self):
        print(f"{self.name} is {self.age} years old.")


dog1 = Dog("Buddy", 5)
dog2 = Dog("Bella", 3)


dog1.bark()           
dog2.bark()            

print(dog1.get_age())  
print(dog2.get_age())  


dog1.dog_info()        
dog2.dog_info()       

