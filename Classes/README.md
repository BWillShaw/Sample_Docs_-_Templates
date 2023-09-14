

---

# Python Class Exercises

Learn Python classes through hands-on exercises. Each exercise focuses on different aspects of classes in Python and provides real-world applications for each concept.

---

## Class Template in Python

Here is a generic template to start building a class in Python:

```python
class ClassName:
    # Class attribute
    class_attribute = "I am a class attribute"

    # Initializer / Instance attributes
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Instance method
    def instance_method(self):
        return f"Hello, I am an instance method. I have access to {self.attribute1}."

    # Class method
    @classmethod
    def class_method(cls):
        return f"Hello, I am a class method. I have access to {cls.class_attribute}."

    # Static method
    @staticmethod
    def static_method():
        return "Hello, I am a static method. I don't have access to any class or instance attributes."

# Create an instance
instance = ClassName("attribute1_value", "attribute2_value")

# Call instance method
print(instance.instance_method())

# Call class method
print(ClassName.class_method())

# Call static method
print(ClassName.static_method())
```

---

## Table of Contents

1. [Person Class - Basics](#exercise-1-person-class---basics)
2. [BankAccount Class - Basics](#exercise-2-bankaccount-class---basics)
3. [Rectangle Class - Encapsulation and Method Overloading](#exercise-3-rectangle-class---encapsulation-and-method-overloading)
4. [Animal and Dog Classes - Inheritance](#exercise-4-animal-and-dog-classes---inheritance)
5. [Car Class - Composition](#exercise-5-car-class---composition)
6. [Library and Book Classes - Aggregation](#exercise-6-library-and-book-classes---aggregation)
7. [Student Class with Class Methods](#exercise-7-student-class-with-class-methods)
8. [Product Class with Class Variables](#exercise-8-product-class-with-class-variables)
9. [User Class - Special Methods](#exercise-9-user-class---special-methods)
10. [Event Class - Polymorphism](#exercise-10-event-class---polymorphism)

---

### Exercise 1: Person Class - Basics

**Concepts:** Class Definition, `__init__`, Basic Methods  
**Objective:**  
Create a class named `Person` that stores a person's first name, last name, and age.

**Real-world application:**  
A foundational class for any system that models human users, like a social network or an employee database.

---

### Exercise 2: BankAccount Class - Basics

**Concepts:** Instance Methods, Attributes  
**Objective:**  
Create a simple `BankAccount` class.

**Real-world application:**  
Financial applications, banking software.

---

### Exercise 3: Rectangle Class - Encapsulation and Method Overloading

**Concepts:** Encapsulation, Method Overloading  
**Objective:**  
Create a `Rectangle` class with attributes `length` and `width`. Implement methods to calculate the area and perimeter. Overload the `__str__` method to print the dimensions.

**Real-world application:**  
Geometric calculations in graphic design software, architectural software.

---

### Exercise 4: Animal and Dog Classes - Inheritance

**Concepts:** Inheritance  
**Objective:**  
Create an `Animal` class with a method `make_sound()`. Create a `Dog` class that inherits from `Animal` and overrides the `make_sound` method.

**Real-world application:**  
Modeling real-world objects and their relationships, such as in a zoo management system.

---

### Exercise 5: Car Class - Composition

**Concepts:** Composition  
**Objective:**  
Create a `Car` class and an `Engine` class. A `Car` should contain an instance of `Engine`.

**Real-world application:**  
Automotive management systems, simulation software.

---

### Exercise 6: Library and Book Classes - Aggregation

**Concepts:** Aggregation  
**Objective:**  
Create `Library` and `Book` classes where a library can contain multiple books, but the books can exist independently of the library.

**Real-world application:**  
Library management systems, inventory management.

---

### Exercise 7: Student Class with Class Methods

**Concepts:** Class Methods  
**Objective:**  
Create a `Student` class that keeps track of the number of student instances using class attributes and class methods.

**Real-world application:**  
Educational platforms, school management systems.

---

### Exercise 8: Product Class with Class Variables

**Concepts:** Static Methods  
**Objective:**  
Create a `Product` class with a method to change the global discount rate for all products, applicable via a static method.

**Real-world application:**  
E-commerce platforms, inventory systems.

---

### Exercise 9: User Class - Special Methods

**Concepts:** Special Methods (`__eq__`, `__hash__`)  
**Objective:**  
Create a `User` class where two instances are considered equal if they have the same username. Implement the `__eq__` and `__hash__` methods.

**Real-world application:**  
User management systems, authentication and authorization systems.

---

### Exercise 10: Event Class - Polymorphism

**Concepts:** Polymorphism  
**Objective:**  
Create an `Event` class and several subclasses like `Meeting` and `Workshop`. Each should have a `get_details` method that returns different information based on the event type.

**Real-world application:**  
Event management software, calendar applications.

---

