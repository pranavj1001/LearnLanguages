class HashTable(object):
    
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.value = [None] * self.size
        
    def insert(self, key, value):
        
        hashValue = self.hash(key, len(self.slots))
        
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.value[hashValue] = value
            
        else:
            
            if self.slots[hashValue] == key:
                self.value[hashValue] = value
                
            else:
                
                nextSlot = self.rehash(hashValue, len(self.slots))
                
                while self.slots[nextSlot] is not None and self.slots[nextSlot] is not key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))
                    
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.value[nextSlot] = value
                
                else:
                    self.value[nextSlot] = value
        
    def hash(self, key, size):
        return key%size
    
    def rehash(self, oldHash, size):
        return (oldHash + 1) % size
    
    def get(self, key):
        
        startSlot = self.hash(key, len(self.slots))
        value = None
        stop = False
        found = False
        pos = startSlot
        
        while self.slots[pos] is not None and not found and not stop:
            
            if self.slots[pos] == key:
                found = True
                value = self.value[pos]
                
            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == startSlot:
                    stop = True
                    
        return value