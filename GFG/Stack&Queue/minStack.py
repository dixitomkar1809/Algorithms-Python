# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given N elements and your task is to Implement a Stack in which you can get minimum element in O(1) time.
'''

# Time Complexity = O(1)

import sys

class MinStack:
    def __init__(self, capacity):
        self.stack = [float('-inf')] * capacity
        self.minStack = [float('-inf')] * capacity
        self.size = 0
        self.capacity = capacity

    def push(self, val):
        if (self.isFull()):
            return False
        if self.size == 0:
            self.stack[self.size] = val
            self.minStack[self.size] = val
            self.size += 1
        else:
            self.stack[self.size] = val
            if self.minStack[self.size - 1] > self.stack[self.size]:
                self.minStack[self.size] = self.stack[self.size]
            else:
                self.minStack[self.size] =  self.minStack[self.size - 1]
            self.size += 1
        return True
    
    def pop(self):
        if self.isEmpty():
            return None
        val = self.stack[self.size-1]
        self.size -= 1
        return val

    def getMin(self):
        if self.isEmpty():
            return None
        return self.minStack[self.size-1]

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[self.size-1]

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity


if __name__=="__main__":
    ms = MinStack(5)
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())
    print(ms.pop())
    print(ms.top())
    print(ms.getMin())