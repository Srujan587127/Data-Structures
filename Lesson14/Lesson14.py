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
        self.items.sort(key = lambda p: self.priorties[p.priority])

    def display(self):
        if not self.items:
            print("\nEmergency queue is empty")
            return
        
        print("\nEmergency queue is empty.")
        for i, patient in  enumerate(self.items[:20], 1):
            print(
                i, "." patient_name, "-ID:", patient.patient_id, "-", patient.priority
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

