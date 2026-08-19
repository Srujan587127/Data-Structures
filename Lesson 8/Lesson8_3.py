class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
print_queue = Queue()


print_queue.enqueue("Doc1")
print_queue.enqueue("Doc2")
print_queue.enqueue("Doc3")


while not print_queue.is_empty():
    document = print_queue.dequeue()
    print("Printing", document , "...")
