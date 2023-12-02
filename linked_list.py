class Node():
  value = None
  next = None

  def __init__(self, val=None) -> None:
    self.value = val


class LinkedList():
  head = None
  tail = None

  def __len__(self):
    return self.size()

  def size(self):
    current = self.head
    count = 0

    while current.next != None:
      count += 1
      current = current.next
    count += 1
    return count

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = new_node

  def remove(self, index):
    if index == 0:
      self.head = self.head.next
    current = Node()
    current = self.head
    for _ in range(1, index):
      current = current.next
    temp = current.next.next
    current.next = temp

  def pop(self):
    current = self.head
    while current.next.next != None:
      current = current.next
    self.tail = current
    self.tail.next = None

  def insert(self, index, value):
    new_node = Node(value)
    if index == 0:
      temp = self.head
      self.head = new_node
      self.head.next = temp
    current = self.head
    for _ in range(1, index):
      current = current.next
    temp = current.next
    current.next = new_node
    current.next.next = temp

  def get_value(self, index):
    current = self.head

    for _ in range(0, index):
      current = current.next
    return current.value

  def reverse(self):
    prevoius = None
    current = self.head
    while current.next != None:
      next = current.next
      if current == self.head:
        current.next = None
        prevoius = current
        current = next
      else:
        current.next = prevoius
        prevoius = current
        current = next
    self.tail.next = prevoius
    self.head, self.tail = self.tail, self.head

  def to_string(self):
    current = self.head
    print("[", end="")
    while current.next is not None:
      print(f"{current.value} ,", end="")
      current = current.next
    print(f"{current.value}]", end="")
