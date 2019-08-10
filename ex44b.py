class Other(object):
    def override(self):
        print("hey this is override")

    def implicit(self):
        print("hey this is implicit")

    def altered(self):
        print("hey this is altered")

class Child(object):
    def __init__(self):
        self.other = Other()

    def override(self):
        print("this is just overriden")

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print("altered")
        self.other.altered()
        print("stuff2")


child = Child()
child.implicit()
child.altered()

