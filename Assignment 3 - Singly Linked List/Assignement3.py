# Assignment-3: Singly Linked List

# 1. Define a class Node to describe a node of a singly linked list.
# 2. Define a class SLL to implement Singly Linked List with _init_() method to create and initialise start reference variable.
# 3. Define a method is_empty() to check if the linked list is empty in SLL class.
# 4. In class SLL, define a method insert_at_start() to insert an element at the starting of the list.
# 5. In class SLL, define a method insert_at_last() to insert an element at the end of the list.
# 6. In class SLL, define a method search() to find the node with specified element value.
# 7. In class SLL, define a method insert_after() to insert a new node after a given node of the list.
# 8. In class SLL, define a method to print all the elements of the list.
# 9. In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
# 10. In class SLL, define a method delete_first() to delete first element from the list.
# 11. In class SLL, define a method delete_last() to delete last element from the list.
# 12. In class SLL, define a method delete_item() to delete specified element from the list.

# Q1. Define a class Node
class Node:
    def __init__(self, item=None, next = None):
        self.item = item
        self.next = next

# Q2. implement Singly Linked List with _init_
class SLL:
    def __init__(self, start = None):
        self.start = start

    #Q3. method to check whether SLL is empty or not
    def is_empty(self):
        return self.start == None
    
    # Q4. implement of insert_at_start
    def insert_at_start(self, data):
        # creating new node for insertion
        new_node = Node(data, self.start)
        self.start = new_node

    # Q5. implement of insert_at_last
    def insert_at_last(self, data):
        # creating new node for insertion
        new_node = Node(data) # here if Next will not referring to anything it will become None by default
        # check whether list is empty or not

        # if list is not empty
        if not self.is_empty():
            temp = self.start
            # checking for last node
            while temp.next is not None:
                # updating temp value to traverse
                temp = temp.next

            temp.next = new_node

        # if list is empty
        else:
            self.start = new_node

    # Q6. implement of search
    def search(self, data):
        # creating Temp variable for traversing
        # traversing from start
        temp = self.start
        # traverse until temp is not None
        while temp is not None:
            # if current item is equal to data/searching value
            if temp.item == data:
                return temp
            
            # if it not equal to searching value then traverse
            temp = temp.next

        # if value not present in list/ list is empty
        return None
    
    # Q7. implement of insert_after
    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(data, temp.next)
            temp.next = new_node

    #Q8. implement of print_list Code Implementation
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    #Q10. implement of delete_first() Code Implementation
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    #Q11. implement of delete_last() Code Implementation
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None

        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    #Q12. implement of delete_item() Code Implementation  
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next

            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)

#Q9. implement of iterator Code Implementation  
class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# driver code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_start(30)
mylist.insert_at_last(50)
mylist.insert_after(mylist.search(50), 100)
mylist.print_list()
mylist.delete_item(30)
print('#####')
mylist.print_list()