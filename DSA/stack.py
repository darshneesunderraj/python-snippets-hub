"""
stack.py

Simple implementation of a Stack using Python list.

Features:
- push
- pop
- peek
- is_empty
- display
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add item to the top of the stack"""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top item of the stack"""
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    def peek(self):
        """Return the top item without removing it"""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def display(self):
        """Display the stack from top to bottom"""
        print("Stack (top -> bottom):", self.stack[::-1])


# Sample usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Popped:", s.pop())
    print("Top element:", s.peek())
    s.display()



