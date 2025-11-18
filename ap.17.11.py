class Stack:
    def __init__(self):
        self.inner_list = []
        print("Stack is created")

    def push(self, elem):
        self.inner_list.append(elem)

    def size(self):
        
        return len(self.inner_list)

    def is_empty(self):
        return len(self.inner_list) == 0

    def peek(self):
        if self.is_empty():
            raise Exception("No elements in the stack")
        last_ind = len(self.inner_list) - 1
        return self.inner_list[last_ind]

    def pop(self):
        if self.is_empty():
            raise Exception("No elements in the stack")
        return self.inner_list.pop()




s1 = Stack()

s1.push(5)
s1.push("5")
s1.push("No elements in the stac")
s1.push("555")
print(s1.peek())
s1.push("432")
s1.push(0)

print(s1.size())
print(s1.is_empty())

print(s1.pop())
print(s1.size())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())  





# queue


class Queue:
    def __init__(self):
        self.inner_list = []
        print("Queue is created")

    def enqueue(self, elem):
        self.inner_list.append(elem)

    def size(self):
        return len(self.inner_list)

    def is_empty(self):
        return len(self.inner_list) == 0

    def peek(self):
        if self.is_empty():
            raise Exception("No elements in the queue")
        return self.inner_list[0]   

    def dequeue(self):
        if self.is_empty():
            raise Exception("No elements in the queue")
        return self.inner_list.pop(0)   


q1 = Queue()

q1.enqueue(10)
q1.enqueue("hello")
q1.enqueue(50)
q1.enqueue("test")
print(q1.peek())

q1.enqueue(999)

print(q1.size())
print(q1.is_empty())

print(q1.dequeue())
print(q1.size())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())   # will raise exception if empty
