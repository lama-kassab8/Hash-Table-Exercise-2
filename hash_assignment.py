class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.count = 0
        self.table = [None] * self.size


    def hash(self, key):
        return hash(key) % self.size


    def insert(self, key, value):
        # check the load factor before inserting 
        if (self.count + 1)/self.size > 0.7: # increase the self.count by 1 because we're about to add a new element and if the load factor crosses the threshold of  0.7, rehash the table
            self.rehash()

        index = self.hash(key) # compute the initial hash index for the key to find where it should be inserted
        i = 0 # start at index zero

        while i < self.size: # keep trying to insert until we insert or check all slots in the table
            probing_index= (index + i**2) % self.size # use the quadratic probing to jump i^2 spots forward
            if self.table[probing_index] is None: # if the spot is empty:
                self.table[probing_index] = (key, value) # insert the key and value in this empty spot
                self.count +=1 # increase the count as one time has been added
                return
            else:
                i +=1 # if the spot we first checked was occupied, check the next spot

        raise Exception("The hash table is full.") # if all spots are occupied, it means the table is too full for a key and value to be added

    def search(self, key):

        index = self.hash(key) # compute the initial hash index for the key to find where it should be inserted
        i = 0 # start at index zero

        while i < self.size: # keep trying to insert until we insert or check all slots in the table
            probing_index= (index + i**2) % self.size # use the quadratic probing to jump i^2 spots forward
            if self.table[probing_index] is None: # if the spot is empty:
                return None # as the key was not found
            
            if self.table[probing_index][0] == key: # if the key in this slot matches the key we're looking for:
                return self.table[probing_index][1] # return its value

            i+=1 # if the spot we checked didn't have the key we were looking for, try the next spot to find the matching key
        
        return None
    

    def delete(self, key):
        index = self.hash(key) # compute the initial hash index for the key to find where it should be inserted
        i = 0 # start at index zero

        while i < self.size: # keep trying to insert until we insert or check all slots in the table
            probing_index= (index + i**2) % self.size # use the quadratic probing to jump i^2 spots forward
            if self.table[probing_index] is None: # if the spot is empty:
                return False # indicate that key was not found and so it cannot be deleted
            
            if self.table[probing_index][0] ==key:
                self.table[probing_index] = None # remove the key value pair by setting it to None
                self.count -=1 # now that the pair of key and value was deleted, the count of items in the hash table is going to decrease by 1
                return True # to indicate that the deletion process was successful
            
            i +=1 # check the next spot, in case the key was not found

        return False # this indicates that the key was not found in the table
            

    def rehash(self):
        original_table= self.table # save the original table in original_table

        self.size = self.size * 2 # make the size of the table double the size of the original table
        self.table= [None] * self.size # make a list with self.size elements and put None in every slot then save this list inside the hash table
        self.count = 0 # reset count because items will be reinserted 

        # the next loop is for inserting all the items in the original table in the newly created table
        for item in original_table:
            if item is not None:
                key, value = item
                self.insert(key,value)


# test run

ht = HashTable()

ht.insert("Alaa", 25)
ht.insert("Basil", 30)
ht.insert("Huda", 22)


print(ht.search("Alass"))    
print(ht.search("Basil"))   
print(ht.search("Sanaa"))    


ht.delete("Basil")
print(ht.search("Basil"))     


ht.insert("David", 40)
ht.insert("Eva", 28)
ht.insert("Seif", 35)
ht.insert("Lana", 32)
ht.insert("Hannah", 29)

print(ht.search("Eva"))    
print(ht.search("Lana"))      


print("Table size:", ht.size)