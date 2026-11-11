class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_bmi_result(self):
        height_in_meters = self.height**0.3048  
        bmi = self.weight/(height_in_meters**2)

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "healthy"
        else:
            return "obese"


name = input("Enter your name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height in feet : "))
weight = float(input("Enter your weight in kg : "))

person = Person(name, age, height, weight)

print("name : ",person.name)
print("age : ",person.age)

print("BMI result : ",person.get_bmi_result())