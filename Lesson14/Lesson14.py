class patient:

    def __init__(self, pateint_id,name, age, problem, priority = "Normal"):
        self.patient_id = pateint_id
        self.name = name
        self.age = age
        self.problem = problem
        self.priority = priority

        def display(self):
            print(
                self.patient_id,
                "|",
                self.name,
                "| Age:",
                self.age,
                "|",
                self.problem,
                "|",
                self.priority,
            )
    def to_file_format(self):
        return (
            str(self.patient_id)
            + ","
            + self.name
            + ","
            + str(self.age)
            + ","
            + self.problem
            + ","
            +self.priority 
        )
    
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, patient):
        self.items.append(patient)

    def dequeue(self):

        if len(self.items) == 0:
            return None
        
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self, limit = 20):

        if self.is_empty():
            print("\nQueue is empty")
            return
        
        print("\nWaiting Patients")
         
        amount = min(len(self.items), limit)

        for i in range(amount):

            patient = self.items[i]

            print(i + 1, ",", patient.name, "-ID: ", patient.patient_id)

        if len(self.items) > limit:
            print("...", len(self.items))

class PriorityQueeue:
    priorities = {"Critical": 1, "High": 2, "Medium": 3}

    def __init__(self):
        self.items = []

    def add(self, patient):
        self.items.append(patient)
        self.items.sort(key = lambda p: self.priorities[p.priority])

    def display(self):
        if not self.items:
            print("\nEmergency queue is empty")
            return
        
        print("\nEmergency queue is empty.")
        for i, patient in  enumerate(self.items[:20], 1):
            print(
                i, "." ,patient.name, "-ID:", patient.patient_id, "-", patient.priority
            )

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

class HospitalTree:
    def __init__(self):
        self.root = TreeNode("Hospital")

        departments = {
            "Emergency": ["Tramua Unit", "ICU"],
            "Cardiolgy": ["ECG Room", "Cardiac Ward"],
            "Neurology": ["MRI Room", "CT Scan"],
            'Orthopedics': ["X - Ray Room", "Fracture Ward"],
            "Pharmacy": ["Medicine Counter"]   
                        
        }
        for department, rooms in departments.items():
            node = TreeNode(department)
            for room in rooms:
                node.children.append(TreeNode(room))
            self.root.children.append(node)
    
    def display_recursive(self, node, level = 0):
        print(" "* level + "|--", node.name)
        for child in node.children:
            self.display_recursive(child, level + 1)

    def display(self):
        print("\n=============== HOSPITAL DEPARTMENTS =======================")
        self.display_recursive(self.root)

waiting_queue = Queue()
emergency_queue = PriorityQueeue()
hospital_tree = HospitalTree()
    
while True:

    print("\n======================================")
    print("      HOSPITAL MANAGEMENT SYSTEM        ")
    print("1. Register Patient")
    print("2. Register Emergency Patient")
    print("3. View Waiting Queue")
    print("4. Hospital Departments")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age"))
        problem = input("Enter Problem: ")

        new_patient = patient(
            patient_id,
            name,
            age,
            problem
        )

        waiting_queue.enqueue(new_patient)

        print("\nPatient registered successfully!")

    elif choice == "2":

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        problem = input("Enter Problem: ")

        print("\nPriority")
        print("1.Critical")
        print("2. High")
        print("3. Medium")

        priority_choice = input("Enter priority: ")

        if priority_choice == "1":
            priority = "Critical"

        elif priority_choice == "2":
            priority = "High"

        else:
            priority = "Medium"
        emergency_patient = patient(
            patient_id,
            name,
            age,
            problem,
            priority
        )
        emergency_queue.add(
          emergency_patient  
        )
        print(
            "\nEmergency patient registered successfully!"
        )

    elif choice == "3":
        waiting_queue.display()

        emergency_queue.display()
    elif choice == "4":

        hospital_tree.display()

    elif choice == "5":

        print(
            "\nThank you for using the"
            "Hospital Mangement System!"
        )

        break

    else:
        
        print(
            "\nInvalid choice. Please try again."
        )