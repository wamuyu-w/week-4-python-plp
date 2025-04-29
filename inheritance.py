class Person:
    def __init__(self, name, age, height, gender, weight):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.weight = weight

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Gender: {self.gender}, Weight: {self.weight}")


class Student(Person):
    def __init__(self, name, age, height, gender, weight, student_id, school):
        super().__init__(name, age, height, gender, weight)
        self.student_id = student_id
        self.school = school

    # Polymorphism
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, School: {self.school}")


# Example usage
p = Person("Alice", 25, "120cm", "Female", "60kg")
s = Student("Bob", 20, "173cm", "Male", "70kg", "ST1234", "CUEA")

print("This is the person:")
p.display_info()

print("\nThis is the student:")
s.display_info()
