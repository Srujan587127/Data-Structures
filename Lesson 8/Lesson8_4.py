class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, person):
        self.queue.append(person)

    def dequeue(self):
        if len (self.queue) > 0:
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
ticket_queue = Queue()

ticket_queue.enqueue("Alice")
ticket_queue.enqueue("Bob")
ticket_queue.enqueue("Charlie")

ticket_queue.enqueue("David")

while not ticket_queue.is_empty():
    person = ticket_queue.dequeue()
    print(person, "bought a ticket. ")