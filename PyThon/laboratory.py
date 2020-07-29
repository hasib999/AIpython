import datetime

class ageCalculation:
    
    "Calculating Age"

    def __init__(self):
        self.time=datetime.datetime.now()

        self.uName=''
        self.uAge=''
    
    
    def userInput(self):
        self.uName=input("What is Your Name: ")
        self.uAge=int(input("How Old Are You: "))

    def calculateAge(self):
        user100=self.time.year-self.uAge+100
        print("Hi there", self.uName,"You will be 100 years old in the year of ",user100)
    


userAge=ageCalculation()
print(userAge.__doc__)

userAge.userInput()
userAge.calculateAge()


