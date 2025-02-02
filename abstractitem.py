from abc import ABC,abstractmethod

class AbstractItem(ABC):
    def __init__(self,name,rating=None):  #food menu rating is not present so none is initialized
        self.Name = name
        self.Rating = rating

    @abstractmethod
    def DisplayItem(self, start):pass


