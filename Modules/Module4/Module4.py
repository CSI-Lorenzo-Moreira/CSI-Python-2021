meal = "Coffee and bread"
print("What did you have for breakfast?")
print (meal)
meal = "Bacon cheeseburger"
print("What did you have for lunch?")
print(meal)
meal = "no"
print("Have you had dinner?")
print(meal)


def greetStudent(name):
    print(f"Hello {name}!")
greetStudent("lorenzo moreira")

var:str = "representing a value"
mynumber:float = 3.5
myfunctionalstring = f"Combine an existing string {var} with a number: such as {mynumber} or {1}"
print(myfunctionalstring)
print(f"or use the print directly {mynumber}")


def my_string(person,age,food):
    print("Oh, you are " +person+ "." + " You're " +age+ " years old right? " + "Anyways, I have heard that the " +food+ " is pretty good here.")
my_string(input("Input your name: "), input("Input your age: "), input("Input what you want to eat: "))