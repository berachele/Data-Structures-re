class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

    def get_value(self):
        # returns the node's data 
        return self.value

    def get_next(self):
        # returns the thing pointed at by this node's `next` reference 
        return self.next_node

    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # the first Node in the LinkedList
        self.head = None
        # the last Node in the LinkedList
        self.tail = None

    '''
    Adds `data` to the end of the LinkedList 
    O(1) because this operation doesn't depend on the size of the linked list 
    '''
    def add_to_tail(self, data):
        # wrap the `data` in a Node instance 
        new_node = Node(data)

        # what about the empty case, when both self.head = None and self.tail = None?
        if not self.head and not self.tail:
            # list is empty 
            # update both head and tail to point to the new node 
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case 
        else:
            # call set_next with the new_node on the current tail node 
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list 
            self.tail = new_node

    '''
    Removes the Node that `self.tail` is referring to and returns the 
    Node's data
​
    What's the runtime of this method?
    '''
    def remove_tail(self):
        # if the linked list is empty 
        if self.tail is None:
            return None
        # save the tail Node's data
        data = self.tail.get_value()
        # both head and tail refer to the same Node 
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            # in order to update `self.tail` to point to the
            # the Node _before_ the tail, we need to traverse
            # the whole linked list starting from the head,
            # because we cannot move backwards from any one
            # Node, so we have to start from the beginning
            current = self.head

            # traverse until we get to the Node right 
            # before the tail Node 
            while current.get_next() != self.tail:
                current = current.get_next()

            # `current` is now pointing at the Node right
            # before the tail Node
            self.tail = None
            self.tail = current
            # self.tail.set_next(None)
        
        return data

    '''
    Removes the Node that `self.head` is referring to and returns the 
    Node's data 
    '''
    def remove_head(self):
        if self.head is None:
            return None
        # save the head Node's data
        data = self.head.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None 
            self.head = None
            self.tail = None
        else:
            # we have more than one Node in the linked list 
            # delete the head Node 
            # update `self.head` to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()

        return data

    '''
    Traverses the linked list and returns a boolean indicating whether the 
    specified `data` is in the linked list.
​
    What's the runtime for this method?
    '''
    def contains(self, data):
        # an empty linked list can't contain what we're looking for 
        if not self.head:
            return False

        # get a reference to the first Node in the linked list 
        # we update what this Node points to as we traverse the linked list 
        current = self.head 

        # traverse the linked list so long as `current` is referring 
        # to a Node 
        while current is not None:
            # check if the Node that `current` is pointing at is holding
            # the data we're looking for 
            if current.get_value() == data:
                return True
            # update our `current` pointer to point to the next Node in the linked list
            current = current.get_next()
        
        # we checked the whole linked list and didn't find the data
        return False

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def dequeue(self):
#         self.size -=1
#         if self.__len__() == 0:
#             return None
#         return self.storage.pop(0)

#Queue implementing a Singly Linked List
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.__len__() == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()