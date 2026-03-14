from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("The animal is sleeping")

class dog(animal):
    def sound(self):
        print("Animal is barking")

class cat(animal):
    def sound(self):
        
        print("Animal is sounding Meow")

class cow(animal):
    def sound(self):
        print("Animal is sounding MOO")

d=dog()
c=cat()
co=cow()

d.sound()
c.sound()
co.sound()



class student:
    college_name = "ABC College"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name

    def is_pass(marks):
        if marks>=35:
            print("Pass")
        else:
            print("fail")
    def display(self):
        print("The name of the student is",self.name)
        print("The roll number of the student is",self.roll_no)
    
s1=student("Abhi","123")
s2=student("balu","099")

s1.display()
s2.display()

print(student.college_name)
student.change_college("XYZ College")
print(s1.college_name)

student.is_pass(40)
student.is_pass(30)



"""task given by mentor"""
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f" book name is {self.title} and author is {self.author} and price is {self.price}"

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, price={self.price})"

obj=Book("python","john",100)
print(obj.__str__())
print(obj.__repr__())

obj2=Book("java","jane",200)
print(obj2.__str__())
print(obj2.__repr__())

obj3=Book("c++","jim",300)
print(obj3.__str__())
print(obj3.__repr__())
