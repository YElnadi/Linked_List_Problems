'''
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.
'''



class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def sum_list(head):
    current = head
    sum_list = 0
    while current is not None:
       sum_list += current.val
       current = current.next

    return sum_list


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19