class Node():
    def __init__(self,x:int,y:int,parent) -> None:
        self.x = x
        self.y = y
        self.parent = parent
    def to_string(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def hashable(self):
        return str(self.x) + "." + str(self.y)

class Stack():
    def __init__(self) -> None:
        self.data = []

    def add(self, node):
        self.data.append(node)
    
    def empty(self):
        return len(self.data) == 0

    def remove(self) -> Node:
        if self.empty():
            raise Exception("EMPTY")
        node = self.data[-1]
        self.data = self.data[:-1]
        return node
    
    def head(self):
        if not self.empty():
            return self.data[0]
        else:
            return None
    
class Queue(Stack):
    def remove(self):
        if self.empty():
            raise Exception("EMPTY")
        node = self.data[0]
        self.data = self.data[1:]
        return node
    