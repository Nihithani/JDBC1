#Queue Using Single Stacks

class QueueUsingSingleStacks:
    def __init__(self):
        self.stack=[]
    def enqueue(self,item):
        self.stack.append(item)
    def dequeue(self):
        if not self.stack:
            return "Queue is empty"
        elif len(self.stack)==1:
            return self.stack.pop()
        else:
            front=self.stack.pop()
            dequeue_item=self.dequeue()
            self.stack.append(front)
            return dequeue_item
    def peek(self):
        if not self.stack:
            return "Queue is empty"
        return self.stack[0]
    def is_empty(self):
        return not self.stack
queue=QueueUsingSingleStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())