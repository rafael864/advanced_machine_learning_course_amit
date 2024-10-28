from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def describe(self):
        pass
class dog(animal):
    def make_sound(self):
        print('bark')
    def describe(self):
        print('brown')
class cat(animal):
    def make_sound(self):
        print('purr')
    def describe(self):
        print('white')
class cow(animal):
    def make_sound(self):
        print('low') 
    def describe(self):
        print('black and white')
if __name__=='__main__':
    dog().make_sound()
    dog().describe()
    cat().make_sound()
    cat().describe()
    cow().make_sound()
    cow().describe()