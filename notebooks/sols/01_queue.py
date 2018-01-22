print("Problem 5")

class Queue:

    def __init__(self):
        self.q = []

    def insert(self, item):
        self.q.append(item)

    def remove(self):
        if len(self.q) > 0:
            item = self.q[0]
            del self.q[0]
            return item
        else:
            print("The queue is empty")
