import numpy as np

class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next    


class linked_list:
    def __init__(self, head=None):
        self.head = head
    def read(self,index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.value
    def write(self, index, value):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        current_node.value = value
        return
    def insert(self, index, value):
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
        new_node = node(value, current_node.next)
        current_node.next = new_node
        return
    def delete(self, index):
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        return
    def print_all(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next
        return
    def last_element(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        print( current_node.value )
        return

    def reverse(self):
        current_node = self.head
        previous_node = None
        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        return
        

class double_node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class double_linked_list:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def read(self,index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.value

    def write(self, index, value):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        current_node.value = value
        return

    def insert(self, index, value):
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
        new_node = double_node(value, current_node.next, current_node)
        current_node.next = new_node
        return

    def delete(self, index):
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        return
    def print_all_backwards(self):
        current_node = self.tail
        while current_node != None:
            print(current_node.value)
            current_node = current_node.prev
        return



if __name__ == "__main__":
    #create a linked list
    n1 = node(1)
    n2 = node(2)
    n3 = node(3)
    n4 = node(4)
    n5 = node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None


    dn1 = double_node(1)
    dn2 = double_node(2)
    dn3 = double_node(3)
    dn4 = double_node(4)
    dn5 = double_node(5)

    dn1.next = dn2
    dn1.prev = None
    dn2.next = dn3
    dn2.prev = dn1
    dn3.prev = dn1
    dn3.next = dn4
    dn3.prev = dn2
    dn4.next = dn5
    dn4.prev = dn3
    dn5.next = None
    dn5.prev = dn4



    ll = linked_list(n1)
    ll.print_all()

    print('Now for the double nodes \n\r')

    dll = double_linked_list(dn1, dn5)
    dll.print_all_backwards()

    print('Question 3. \n \r')

    ll.last_element()

    print('Question 4. \n \r')
    bwl = linked_list(n1)
    bwl.reverse()
    bwl.print_all()

    print('Question 5. \n \r')
    ll5 = linked_list(n1)
    n3.take_out()
    ll5.print_all()