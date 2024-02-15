class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
class linklist:
  def __init__(self):
    self.head = None
  def insert(self,val):
    if self.head == None:
      self.head = Node(val)
      return
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = Node(val)
      return
  def delete_first(self):
    if self.head == None:
      return
    else:
      self.head = self.head.next
  def delete_end(self):
    if self.head == None:
      return
    elif self.head.next == None:
      self.head = None
    else:
      temp = self.head
      prev = None
      while temp.next is not None:
        prev = temp
        temp = temp.next
      prev.next = None

  def delete(self,val):
    if self.head.data == val:
      self.head = self.head.next
      return
    else:
      temp = self.head
      prev = None
      while temp.data != val:
        prev = temp
        temp = temp.next
      prev.next = temp.next
      return

  def ll_sort(self):
    if self.head is None:
      return self.head
    else:
      temp = self.head
      while temp is not None:
        temp1 = temp
        while temp1.next :
          if temp1.data > temp1.next.data:
            next_node = temp1.data
            temp1.data = temp1.next.data
            temp1.next.data = next_node
          temp1 = temp1.next
        temp = temp.next
  def search(self,val):
    temp = self.head
    while temp:
      if temp.data == val:
        return True
      temp = temp.next
    return False
  def insert_in(self,pos,val):
    temp = self.head
    while temp:
      if temp.data == pos:
        temp1 = temp.next
        temp.next = Node(val)
        temp.next.next =temp1
      temp = temp.next
  def display(self):
    temp = self.head
    while temp:
      print(temp.data,end=" -> ")
      temp = temp.next
    print("None")
  
print("Enter 1 for insertion")
print("Enter 2 for delete at first")
print("Enter 3 for delete at end")
print("Enter 4 for delete node")
print("Enter 5 for search")
print("Enter 6 for sort")
print("Enter 7 for insertion in middle")
print("Enter 0 for exit")
ll = linklist()
while True:
  n = int(input("Enter the number"))
  if n == 0:
    break
  elif n == 1:
    a = int(input("Enter the value"))
    ll.insert(a)
    ll.display()
  elif n == 2:
    ll.delete_first()
    ll.display()
  elif n == 3:
    ll.delete_end()
    ll.display()
  elif n == 4:
    a = int(input("Enter the number to delete"))
    ll.delete(a)
    ll.display()
  elif n == 5:
    a = int(input("Enter the number to search"))
    print(f"searching {a} is {ll.search(a)}")
  elif n == 6:
    ll.sort()
    ll.display()
  elif n == 7:
    a = int(input("Enter the value"))
    b = int(input("Enter the index after")) 
    ll.insert_in(b,a)
    ll.display()
  else:
    print("Enter the valid number")

