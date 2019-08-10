class Parent(object):
    def __init__(self):
        print("hey this is parents init")

    def implicit(self):
        print("this is implicit inherit")
    
    def override(self):
        print("hey override in parent")
    
    def altered(self):
        print("PARENT ALTERED()")

class Child(Parent):
    def another_method(self):
        print("this is anoter method")
    
    def override(self):
        print("hey this is IN CHILD")

    def altered(self):
        print("kids altered")
        super(Child, self).altered()
        print("again in kids")


child = Child()
child.another_method()
child.implicit()
child.override()
child.altered()
