class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def get_marks(self):
        return self.marks
    

    def set_marks(self, new_marks):
        self.marks = new_marks

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)
print(f"For student {name}, current marks are {marks}.")

new_marks = int(input("Enter New marks: "))
s1.set_marks(new_marks)

print("Updated Marks: ", s1.get_marks)

