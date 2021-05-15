def isEmpty(stack):
    return len(stack) == 0

def push(stack,element):
    stack.append(element)
    return stack

def size(stack):
    return len(stack)

def pop(stack):
    return stack.pop()

def top(stack):
    try:
        return stack[-1]
    except IndexError:
        print("Error: stack has overflowed")

if __name__ == '__main__':
    stack = [1, 2, 3, 4]
    print(isEmpty(stack)) #returns false because stack is populated
    print(push(stack, 100)) #returns [1, 2, 3, 4, 100] 
    print(pop(stack)) #returns the popped vaulue 6
    print(top(stack)) #returns 4, the top value on the stack
    print(size(stack)) #returns 5: the size pf the stack