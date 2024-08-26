from abc import ABC, abstractmethod

class Footballers(ABC):
    def position(self):
        pass
    
class Ronaldo(Footballers):
    def position(self):
        print("Striker")
class Messi(Footballers):
    def position(self):
        print("Right-Winger")
class Neymar(Footballers):
    def position(self):
        print("Left-Winger")
class Mbappe(Footballers):
    def position(self):
        print("Striker")
class Bellingham(Footballers):
    def position(self):
        print("Centre-Midfielder")

por = Ronaldo()
por.position()

arg = Messi()
arg.position()

brz = Neymar()
brz.position()

fra = Mbappe()
fra.position()

eng = Bellingham()
eng.position()




