
# https://towardsdatascience.com/circular-queue-or-ring-buffer-92c7b0193326

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = [None]*capacity
    self.current = 0

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0
    self.storage[self.current] = item
    self.current += 1
    
  def get(self):
    a_list = []
    for item in self.storage:
      if item != None:
        a_list.append(item)
    return a_list