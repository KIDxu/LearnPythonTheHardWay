# Inheritance vs. Composition
class Parent(object):
    def override(self):
        print "PARENT override()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.override()
son.override()

dad.altered()
son.altered()

## Composition
class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):
    def __init__(self):
        self.other = Other() #Composition

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()
son.implicit()
son.override()
son.altered()
