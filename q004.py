# implement a recently used cache
# note this question was more to talk about the data structures involved but I will
# implemented myself just for practice ;)


# implementation of a very basic linked list
class Node:
  def __init__(previousNode,nextNode,key,value):
    self.previousNode = previousNode
    self.nextNode = nextNode
    self.key = key
    self.value = value

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def addNodeToFront(self, node):
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      node.previousNode = None
      node.nextNode = self.head
      self.head.previousNode = node
      self.head = node
  
  def removeNode(self, node):
    if node.key == self.tail.key:
      if self.tail.key == self.head.key:
        self.tail = None
        self.head = None
      else:
        self.tail.previousNode.nextNode = None
        self.tail = self.tail.previousNode
    elif node.key == self.head.key:
      self.head = self.head.nextNode
      if self.head != None:
        self.head.previousNode = None
    else:
      node.previousNode.nextNode = node.nextNode
      node.nextNode.previousNode = node.previousNode  
    node.nextNode = None
    node.previousNode = None
  
  def removeTail(self):
    node = self.tail
    self.removeNode(node)

# the cache that is managing a list of items and tried to minimize the use of a provided item Manager
class Cache:
  def __init__(self, size, itemManager):
    self.size = size
    self.itemManager = itemManager
    self.items = [] # hashMap pointing ot the items in the linked list
    self.ddlist = DoublyLinkedList()

  def get(self, key):
    if self.items.has_key(key):
      node = self.items[key]
      # need to move the node to the front of the list
      self.ddlist.removeNode(node)
      self.ddlist.addNodeToFront(node)
      return node.value
    else:
      # if the node is not in the cache we need to request it from the itemManager
      # if the cache is already full we need to evict the least recently used item
      if len(self.items) == self.size:
        del self.items[self.tail.key]
        self.ddlist.removeTail()  
      node = Node(None, None, key, self.itemManager.get(key))
      self.items[key] = node
      self.ddlist.add(node)
      return node.value
