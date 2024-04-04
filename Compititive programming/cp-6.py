#printboundary

class Node:
    def __init__(self, data):
        self.data =data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear= new_node
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            data=self.front.data
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            return data
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.front.data
    def display(self):
        current =self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print("queue elements:")
queue.display()
print("peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Queue elements after dequeue:")
queue.display()


#reverse order traversal
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val=value
        self.left=None
        self.right=None
def reverse_level_order(root):
    if not root:
        return[]
    result=[]
    queue= deque([root])
    while queue:
        level_size=len(queue)
        current_level=[]
        for _ in range(level_size):
            node=queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.insert(0, current_level)
    return result
root =TreeNode(1)
root.left= TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
reverse_order=reverse_level_order(root)
print("level order traversal in reverse form:")
for level in reverse_order:
    print(level)

#climbing strairs

def climbstairs(n):
    if n==0 or n==1 or n==2:
        return n
    else:
        res, step_1, step_2 =0, 1, 2
        for i in range(2, n):
            res= step_2+step_1
            step_1=step_2
            step_2=res
        return res
 

#diagonal traversal

from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val=value
        self.left=None
        self.right=None
def diagonal_traversal(root):
    if not root:
        return[]
    result=[]
    queue=deque([(root, 0)])
    while queue:
        node, level =queue.popleft()
        if level ==len(result):
            result.append([])
        result[level].append(node.val)
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level))
    return result
root =TreeNode(8)
root.left= TreeNode(3)
root.right=TreeNode(10)
root.left.left=TreeNode(1)
root.left.right=TreeNode(6)
root.right.right=TreeNode(14)
root.right.right.left=TreeNode(13)
root.left.right.left=TreeNode(4)
root.left.right.right=TreeNode(7)
diagonal_order= diagonal_traversal(root)
print("diagonal traversal of the binary tree:")
for level in diagonal_order:
    print(level)


#fibonacci
#fibonacci using dynamic programming
def fibonacci(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2)
    return f[n]
print(fibonacci(5))




#fibonacci using recursion
def fibonacci(n):
    print(n)
    if n<= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)



#function for nth fibonacci number
def fibonacci(n):
    a=0
    b=1
    if n<0:
        print("incorrect input")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
print(fibonacci(9))





#reverse polish notation

def evalRPN(tokens):
    l=0
    stack=[]
    opers={'+':lambda x,y: x+y,
           '-':lambda x,y:x-y,
           '*':lambda x,y:x*y,
           '/':lambda x,y: int(x/y)
           }
    while l<len(tokens):
        if tokens[l] not in opers:
            stack.append(int(tokens[l]))
        else:
            cur=opers[tokens[l]](stack[-2],stack[-1])
            stack=stack[:-2]
            stack.append(cur)
        l+=1
    return stack[0]
tokens=["2","1","+","3","*"]
print(evalRPN(tokens))


#spiral level order
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val=value
        self.left=None
        self.right=None
def spiral_level_order(root):
    if not root:
        return[]
    result=[]
    queue= deque([root])
    left_to_right=True
    while queue:
        level_size=len(queue)
        current_level=deque()
        for _ in range(level_size):
            node=queue.popleft()
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(current_level))
        left_to_right=not left_to_right
    return result
root =TreeNode(1)
root.left= TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
spiral_order=spiral_level_order(root)
print("level order traversal in spiral form:", spiral_order)



#tribonacci

#tribonacci series

def tribonacci(n):
    if n<=1:
        return n
    elif n==2:
        return 1
    first,second,third=0,1,1
    for _ in range(3,n+1):
        first,second,third=second,third,first+second+third
    return third
num=int(input("enter which tribonacci number you want to know?"))
print(tribonacci(num))
    
