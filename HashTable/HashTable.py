# Hash table stores key-value pairs but the key is generated through a hashing function.

# In Python, the Dictionary data types represent the implementation of hash tables.

# Declare a dictionary {'Key': Value}

# Space: O(n)
#Search: avg = O(1) worst = O(n)
#Insert: avg = O(1) worst = O(n)
#Delete: avg = O(1) worst = O(n)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8 # update existing entry
dict['School'] = "DPS School" # Add new entry

# Accessing the dictionary with its key
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict        # delete entire dictionary
