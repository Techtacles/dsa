class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data=None):
        node = Node(data)
        self.data = data
        self.head = node
        self.tail = node
        self.length = 1

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            # Make newNode the new tail
            # We can access .next because it is inheriting from the Node class
            self.tail = newNode
        self.length += 1
        return self

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get(self, index):
        if index < 0 or index > self.get_length():
            print("Provide a valid index within Linkedlist's range")
        if index == 0:
            return self.head
        count = 0
        get_data = None
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            if count == index:
                get_data = itr
        return get_data

    def remove(self, index):
        if index < 0 or index > self.get_length():
            print("Provide a valid index within Linkedlist's range")
        if index == 0:
            self.head = self.head.next
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            count += 1
        return self

    def insert(self, index, data):
        if index < 0 or index > self.get_length():
            print("Provide a valid index within Linkedlist's range")
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                current.next = Node(data)
                break
            count += 1
        return self

    def shift(self):
        self.head = self.head.next
        return self

    def unshift(self, data):
        node = Node(data)
        self.head = node
        return self

    def set(self, index, data):
        if index < 0 or index > self.get_length():
            print("Provide a valid index within Linkedlist's range")
        if index == 0:
            return self.unshift(data)
        node = Node(data)
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = node
                break
        return self


l = LinkedList(3)
l.insert_at_end(4)
l.insert_at_end(5)
l.insert_at_end(6)
l.set(1, 50)
print(l.head.next.__dict__)

