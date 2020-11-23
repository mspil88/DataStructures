# Doubly Linked List implementation


class Node:
    def __init__(self, prev=None, next=None, value=None):
        self.prev = prev
        self.next = next
        self.value = value

class DLL:
    def __init__(self):
        self.head = None

    #push to front of list
    def push(self, new_value):
        new_node = Node(value=new_value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        new_node.prev = None
        self.head = new_node

    #append to back of list
    def append(self, new_value):
        new_node = Node(value=new_value)
        new_node.next = None
        if self.head is None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    #forward traversal of list
    def print_forwards(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    #backward traversal of list
    def print_backwards(self):
        temp = self.head
        while temp:
            last = temp
            temp = temp.next
        while last:
            print(last.value)
            last = last.prev
    #reverse the list in place
    def reverse_list(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    #deletion based on a key
    def delete(self, key):
        current = self.head
        while current:
            # whilst at the head of the list
            if current.value == key and current == self.head:
                #if there is nothing to the right of the head
                if not current.next:
                    current = None
                    self.head = None
                    return
                #else there is a node to the right of the head
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            elif current.value == key:
                #not at the head but a node to the right
                if current.next:
                    prev = current.prev
                    nxt = current.next
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                #not at the head and there is no node to the right
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next
