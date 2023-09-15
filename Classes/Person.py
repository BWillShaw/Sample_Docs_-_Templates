

from tkinter import FIRST


class Person:
    species = "human" # species created as class attribute
    
    def __init__(self, first_name = None, last_name = None, age = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def identify(self):
        return f"\nMy name is {first_name} {last_name} and I am {age} years old!"
    
    def import_txt(self, file_path):
        global staff
        with open(file_path, "r") as txt_file:
            lines = txt_file.readlines()
            for line in lines:
                first_name, last_name, age = line.strip().split(",")
                self.first_name = first_name
                self.last_name = last_name
                self.age = age
                staff.append(Person(first_name, last_name, age))
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}"
                
if __name__ == "__main__":
    
    staff = []

    first_name = input("\nPlease enter your first name: ").lower()
    last_name = input("\nPlease enter your last name: ").lower()
    age = input("\nPlease enter your age: ")
    
    person_obj = Person(first_name, last_name, age)
    staff.append(person_obj)
    
    person_obj.import_txt(r"C:\Users\brand\source\repos\Sample_Docs_-_Templates\Classes\People.txt")
    
    print("\n")
    for person in staff:
        print(person)
    
    print("\n")
    print(*staff)
    

