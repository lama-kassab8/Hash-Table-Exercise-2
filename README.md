# Hash Table Implementation (Quadratic Probing)

This project is a simple implementation of a **hash table** in Python using **quadratic probing** for collision resolution.  
It also supports **rehashing** when the load factor exceeds `0.7`.

---

## Features
- Insert key-value pairs
- Search for a value by key
- Delete a key-value pair
- Automatic rehashing (table size doubles when load factor > 0.7)
- Collision resolution with **quadratic probing**

---

## How It Works
1. Each key is hashed into an index using Python's built-in `hash()` function.
2. If a collision occurs, the algorithm checks indices using the formula:
   (index + i^2) % table_size
   where `i` increases until a free slot is found.
3. If the table gets too full (load factor > 0.7), it **rehashes** into a larger table.


