students = ["Alex", "John", "Amelie", "Ava", "Srujan"]

target = input("Enter name for Searching: ")

found = False
for name in students:
    if name == target:
        print("Student Found")
        found = Truebreak


if not found:
    print("Students not found!")