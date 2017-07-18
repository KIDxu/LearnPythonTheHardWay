# Is-A, Has-A, Objects, and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## make a class named Dog that is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## class Dog has-a function __init__ that takes self and name parameters
        self.name = name

## make a class named Cat tht is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## class Cat has-a function __init__ that takes self and name parameters
        self.name = name

class Person(object):
    def __init__(self, name):
        ## person has a name
        self.name = name

        ## person has-a pet of some kind
        self.pet = None

## make a class Employee that is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## ???? seem to link class Person and its __init__ function
        super(Employee, self).__init__(name) # superclass,take mother-class Person and its init function
        ## Employee has salary
        self.salary = salary

## make a class Fish
class Fish(object):
    pass

## make a class Salmon that is-a Fish
class Salmon(Fish):
    pass

## make a class Halibut that is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## frank is-a Employee with salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
