class Node:
  value = None
  next = None

  def __init__(self, val=None) -> None:
    self.value = val


class Stack:
  top: Node = None

  def __len__(self):
    return self.size()

  def __iter__(self):
    self.current = self.top
    self.length = self.size()
    return self

  def __next__(self):
    if self.length != 0:
      value = self.current.value
      self.current = self.current.next
      self.length -= 1
      return value
    else:
      raise StopIteration

  def size(self):
    current = self.top
    count = 0
    while current.next != None:
      count += 1
      current = current.next
    count += 1
    return count

  def is_empty(self):
    return self.top == None

  def push(self, value):
    new_node = Node(value)
    if self.top == None:
      self.top = new_node
    else:
      temp = self.top
      self.top = new_node
      self.top.next = temp

  def pop(self):
    self.top = self.top.next

  def peek(self):
    return self.top.value

  def to_string(self):
    current = self.top

    print("[", end="")
    while current.next != None:
      print(f"{current.value}, ", end="")
      current = current.next
    print(f"{current.value}]")
