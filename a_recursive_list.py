class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result
    
    def toNodeNum(self):
        result: list = []
        current = self.first
        value = current.value
        return value



def initialize() -> List:
    return List()


def isEmpty(data: List) -> bool:
    return data.first == None


def addAtIndex(data: List, index: int, value: int) -> List:
    def helper(v: Node, index:int, value: int, i: int):
        if i + 1 == index:
            new_node = Node(value, v.next)
            v.next = new_node
        elif v is None:
            return -1
        else:
            helper(v.next, index, value, i + 1)
        
    if isEmpty(data):
        data.first = Node(value, None)
        data.last = data.first
        return data
    elif index < 0 or index >= len(data):
        return -1
    elif index == 0:
        new_node = Node(value, data.first)
        data.first = new_node
        return data
    else: 
        helper(data.first, index, value, i = 0)
        return data
    

def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    def helper(v: Node, index:int, i: int):
        global new_node
        if i + 1 == index:
            node = v.next
            v.next = node.next
            new_node = node
        elif v is None:
            return -1
        else: 
            helper(v.next, index, i + 1)
    
    if isEmpty(data):
        return -1
    elif index < 0 or index >= len(data):
        return -1
    elif index == 0:
        removed_node = data.first
        data.first = None
        return removed_node, data
    else:
        helper(data.first, index, i = 0)
        return new_node.value, data


def addToFront(data: List, value: int) -> List:
    if data.first is None:
        data.first = Node(value, None)
        return data
    else:
        new_node = Node(value, data.first)
        data.first = new_node
        return data



def addToBack(data: List, value: int) -> List:
    def helper(v:Node):
        if v.next == None:
            last_node = Node(value, None)
            node = v.next
            node.next = last_node
        else:
            helper(v)
    if data.first is None:
        data.first = Node(value,None)
        return data
    else:
        helper(data.first)
        return data


def getElementAtIndex(data: List, index: int) -> Node:
    def helper(v,index,i):
        if i == index:
            return v
        elif i > index:
            raise IndexError("Oops")
        else:
            return helper(v.next,index, i+1)
    if isEmpty(data):
        return None
    elif index < 0 or index == len(data):
        raise IndexError("Oops")
    else:
        return helper(data.first,index,i =0)


l = initialize()
addToFront(l, 2)
addToFront(l, 5)
addToBack(l, 5)


print(l.last.value)

l = l.toPythonList()
print(l)


def clear(data: List) -> List:
    raise NotImplementedError("List.clear() not defined")
