class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            x = Node(data)
            x.next = self.head
            self.head = x
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            x = self.head
            self.head = self.head.next
            x.next = None
            return x.data

    def top(self):
        return self.head.data

    def size(self):
        c = 0
        i = self.head
        while i is not None:
            c+=1
            i=i.next
        return c

if __name__ == '__main__':
    stack = Stack() #initializing the stack variable with the stack class
    stack.push(1) #adding 1 to the stack
    stack.push(2) #adding 1 to the stack
    stack.push(3) #adding 1 to the stack 
    stack.push(4) #adding 1 to the stack
    print(stack.isEmpty()) #returns false because it is not empty
    print(stack.pop()) #returns 4: the popped value
    print(stack.top()) #returns 3: the top value
    print(stack.size()) #returns 3: the size of the array