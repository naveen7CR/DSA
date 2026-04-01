# Data Structures 
# class DoublyLinkedListNode:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, value):
#         new_node = DoublyLinkedListNode(value)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node

#     def prepend(self, value):
#         new_node = DoublyLinkedListNode(value)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     def delete(self, value):
#         current = self.head
#         while current:
#             if current.value == value:
#                 if current.prev:
#                     current.prev.next = current.next
#                 else:
#                     self.head = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#                 else:
#                     self.tail = current.prev
#                 return
#             current = current.next


class Node:
    def __init__(self,Data):
        self.prev=None
        self.next=None
        self.data=Data
        curnode=self.head
        while curnode.next!=None:
            print(curnode.data,end=" ")
            curnode=curnode.next
            
          


