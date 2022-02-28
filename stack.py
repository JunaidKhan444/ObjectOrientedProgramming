class Stack:
    
    def __init__(self):
        self.stack = []
        self.top = 0
    
    def push(self,num):
        
        self.top = self.top + 1
        self.stack.append(num)

    def stackElemnts(self):
        print(self.stack)

    def pop(self):
        if self.top == 0:
             print("Stack is Empty")
        else:
            self.top = self.top - 1
            #print(self.top)
            print("Number Popped")
            print(self.stack.pop())

obj = Stack()

obj.push(1)
obj.push(10)
obj.pop()
obj.push(100)

obj.stackElemnts()