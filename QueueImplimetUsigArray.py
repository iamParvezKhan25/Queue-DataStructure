# Queue Data Structure Usig Array

class Queue:
    def __init__(self, size):
        self.queue = [] #EmptyList
        self.front = 0
        self.rear = 0
        self.size = size

    def enQueue(self, newData):
        if self.size == self.rear:
            print("Error : Queue is FULL!")
        else:
            self.queue.append(newData)
            self.rear += 1
            print("enQueue : {}".format(newData))

    def deQueue(self):
        if self.front == self.rear:
            print("ERROR : Queue is EMPTY!")
        else:
            exData = self.queue.pop(0) #Delete/POP First Element from List
            self.rear -= 1
            print("deQueue : {}".format(exData))
    
    def queueDisplay(self):
        print(":: Queue Display ::")
        for i in self.queue:
            print(i)

if __name__ == '__main__':

    q = Queue(5) #in Argument Declare Size/Capacity of Queue

    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    q.enQueue(60)
    q.queueDisplay()

    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.queueDisplay()
