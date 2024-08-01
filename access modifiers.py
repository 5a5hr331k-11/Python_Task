# Public access modifier:
class user_details:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def displayDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll.no:",self.rollno)

insertDetails = user_details("Sashreeik",15,11011)

insertDetails.displayDetails()

# Private access modifier:
class user_details:
    __name = None
    __age = None
    __rollno = None
    
    def __init__(self,name,age,rollno):
        self.__name = name
        self.__age = age
        self.__rollno = rollno

    def displayDetails(self):
        print("Name:",self.__name)
        print("Age:",self.__age)
        print("Roll.no:",self.__rollno)

insertDetails = user_details("Sashreeik",15,11011)

insertDetails.displayDetails()

# Protected access modifier:
class user_details:
    def __init__(self,name,age,rollno):
        self._name = name
        self._age = age
        self._rollno = rollno

    def displayDetails(self):
        print("Name:",self._name)
        print("Age:",self._age)
        print("Roll.no:",self._rollno)

insertDetails = user_details("Sashreeik",15,11011)

insertDetails.displayDetails()
    
        


    
        


        
