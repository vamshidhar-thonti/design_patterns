# Violates the LSP

class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        print("I can't fly")

# Fix

class Bird:
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class NonflyingBird(Bird):
    def fly(self):
        print("I cannot fly")

class Penguin(NonflyingBird):
    pass