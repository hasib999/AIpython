
class Queue:
    
    def __init__(self,pop_index):
        self.queue = []
        self.pop_index=pop_index

    def append(self, item):
        self.queue.append(item)

    def sortAppend(self, item,f):
        self.queue.append(item)
        self.queue.sort(key=f)    

    def extend(self, items):
        self.queue.extend(items)     

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(self.pop_index)
        else:
            raise Exception('FIFOQueue is empty')

    def printQueue(self):
        print("Frontier Status After Adding .............")
        print([items.state for items in self.queue])
        
    def __len__(self):
        return len(self.queue)

    def __contains__(self, item):        
        return item in self.queue
    
          
