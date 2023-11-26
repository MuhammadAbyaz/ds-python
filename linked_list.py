class Node():
  value = None
  next = None

  def __init__(self, val=None) -> None:
    self.value = val


class LinkedList():
  head = None
  tail = None

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = new_node

  def to_string(self):
    current = self.head
    print("[", end="")
    while current.next is not None:
      print(f"{current.value} ,", end="")
      current = current.next
    print(f"{current.value}]", end="")

  def remove(self, index):
    pass

  def pop(self):
    pass

  def insert(self, index, value):
    pass

  def get_value(self, index):
    pass
