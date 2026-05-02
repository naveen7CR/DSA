# Data Structures 
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


# class Node:
#     def __init__(self,Data):
#         self.prev=None
#         self.next=None
#         self.data=Data
#         curnode=self.head
#         while curnode.next!=None:
#             print(curnode.data,end=" ")
#             curnode=curnode.next
            
          
# selection sorting
# arr =  [12 , 8 , 7 , 3 , 19 , 98 , 20  ]

# def selectionSort(arr):
#     n = len(arr)
#     for i in range(0, n):
#         smallInx = i
#         for j in range(i+1 , n):
#             if arr[j] < arr[smallInx]:
#                 smallInx = j
#         arr[i], arr[smallInx] = arr[smallInx], arr[i]
#     return arr
# print(selectionSort(arr))


# bubbleSort = [12 , 8 , 7 , 3 , 19 , 98 , 20  ]
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print(bubbleSort(bubbleSort))

# matrix:

# Toggle case function
# def toggle_case(s):
#     return ''.join(c.upper() if c.islower() else c.lower() for c in s)

# print(toggle_case("world"))

# from collection import defaultdict
# def createAdjustmentList():
#     n  = int(input("Enter the number of adjustments: "))
#     adj_list = defaultdict(list)
#     for _ in range(n):
#         node = input("Enter the node: ")
#         adj_list[node]

#     edges = int(input("Enter the number of edges: "))

#     isDirected = int(input("enter 1 for directed graph otherwise 0: "))

#     for _ in range(edges):
#         s = input("Enter the source node: ")
#         d = input("Enter the destination node: ")
#         adj_list[s] = d
#         if isDirected == 0:
#             adj_list[d] = s
#     return adj_list

# myAdjList = createAdjList()
# print(myAdjList)
  


# # INORDER TRAVERSA
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def inorder_recursive(root):
#     result = []

#     def traverse(node):
#         if node is none:
#             return
        
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val=val
#         self.left=left
#         self.right=right

# def inorder_recursive(root):
#     result = []
#     def traverse(node):
#         if not node:
#             return
#         traverse(node.left)
#         result.append(node.val)
#         traverse(node.right)
#     traverse(root)
#     return result



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def postorder_recursive(root):
    result= []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result


# def inorder_iterative(root):
#     result=[]
#     stack=[]
#     curr=root
#     while curr or stack:
#         while curr:
#             stack.append(curr)
#             curr=curr.left
#         curr=stack.pop()
#         result.append(curr.val)
#         curr=curr.right
#     return result


def inorder_recursive(root):
    result=[]
    def transverse(node):
        if not node:
            return
        transverse(node.left)
        result.append(node.val)
        transverse(node.right)
    transverse(root)
    return result




def postorder_recursive(root):
    result=[]
    def transverse(node):
        if not node:
            return
        transverse(node.left)
        transverse(node.right)
        result.append(node.val)
    transverse(root)
    return result









