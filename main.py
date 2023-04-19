# exercise 1-4
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = SLLNode(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        return str([node for node in self])

    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def insert(self, prev_data, data):
        if self.head is None:
            return False
        current = self.head
        while current is not None:
            if current.data == prev_data:
                break
            current = current.next
        else:
            return False

        new_node = SLLNode(data)
        new_node.next = current.next
        current.next = new_node
        return True

    def clear(self):
        self.head = None

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current.data
            current = current.next
        else:
            return False

    def delete(self, data):
        current = self.head
        prev_node = None
        found = False
        while current and not found:
            if current.data == data:
                found = True
            else:
                prev_node = current
                current = current.next
        if found:
            if prev_node == None:
                self.head = current.next
            else:
                prev_node.next = current.next
            self.size -= 1


my_list = SinglyLinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.insert(2, 4)

print(my_list)

print(my_list.get_data(3))
print(my_list.get_data(5))

print(my_list.size)

my_list.delete(3)

print(my_list.size)
print(my_list)

my_list.clear()

print(my_list)
print()

# exercise 5

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DLLNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        return str([node for node in self])

    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def insert(self, prev_data, data):
        new_node = DLLNode(prev_data)
        if data == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif data == self.size:
            self.append(prev_data)
        else:
            current = self.head
            for i in range(data - 1):
                current = current.next
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
        self.size += 1

    def clear(self):
        self.head = None

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current.data
            current = current.next
        else:
            return False

    def delete(self, data):
        if data == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        elif data == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for i in range(data):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1


my_list = DoublyLinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.insert(4, 1)

print(my_list)

print(my_list.get_data(4))
print(my_list.get_data(5))

print(my_list.size)

my_list.delete(2)

print(my_list.size)

print(my_list)

my_list.clear()

print(my_list)
print()

# exercise 6
class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

my_list = MyStack()

my_list.push(5)
my_list.push(6)
my_list.push(7)
my_list.push(8)

print(my_list.stack)
print(my_list.size())
print(my_list.top())
print(my_list.pop())
print(my_list.stack)
print(my_list.size())
print()

# exercise 7
class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def show_left(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        return self.queue[-1]

    def show_right(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)

my_list = MyQueue()

my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(5)

print(my_list.queue)
print(my_list.size())
print(my_list.show_right())
print(my_list.show_left())
print(my_list.pop())
print(my_list.queue)
print(my_list.size())