class HashTable(object):

    # constructor
    # provides the basic structure of the Hash Table
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.value = [None] * self.size

    # Method to insert an element in the table
    def insert(self, key, value):

        # first find a hash Value
        hashValue = self.hash(key, len(self.slots))

        # if the slot at the above hash Value is empty
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.value[hashValue] = value

        else:

            # if the key of the value which is being inserted
            # already exists then just update the value
            if self.slots[hashValue] == key:
                self.value[hashValue] = value

            # else find a new slot
            else:

                # take the next slot
                nextSlot = self.rehash(hashValue, len(self.slots))

                # loop through the slots
                while self.slots[nextSlot] is not None and self.slots[nextSlot] is not key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                # if we found an empty slot then insert in it
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.value[nextSlot] = value

                # if the key of the value which is being inserted
                # already exists then just update the value
                else:
                    self.value[nextSlot] = value

    # method to find the hash value
    def hash(self, key, size):
        return key%size

    # method to find the next hash value
    def rehash(self, oldHash, size):
        return (oldHash + 1) % size

    # method to get the value associated to a key
    def get(self, key):

        # initially we look for the key's corresponding original slot
        startSlot = self.hash(key, len(self.slots))
        value = None
        stop = False
        found = False
        pos = startSlot

        # loop through the slots
        while self.slots[pos] is not None and not found and not stop:

            # if the slot is found
            if self.slots[pos] == key:
                found = True
                value = self.value[pos]

            # try the next hash
            else:
                pos = self.rehash(pos, len(self.slots))

                # if we reached the first slot where we started from then stop
                if pos == startSlot:
                    stop = True
                    
        return value