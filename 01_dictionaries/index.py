"""
Creating a dictionary
"""
print('--- Example: Creating a dictionary ---')
dict_1 = {'field_1': 'test_val_1', 'field_2': 'test_val_2', 'field_3': 'test_val_3'}
print(repr(dict_1))  # Expected output: {'field_1': 'test_val_1', 'field_2': 'test_val_2', 'field_3': 'test_val_3'}
print()


#####################################################################################################################


"""
Retrieving a value from a dictionary
"""
print('--- Example: Retrieving a value from a dictionary ---')
print(repr(dict_1['field_2']))  # Expected output: 'test_val_2'
print()


#####################################################################################################################


"""
KeyError exception
"""
# print(repr(dict_1['not_a_valid_key']))  # This will throw a KeyError if uncommented.
# print()


#####################################################################################################################


"""
Using the 'in' and 'not in' operators to test for a value in a dictionary
"""
print('--- Example: Using the "in" and "not in" operators to test for a value in a dictionary ---')
present = 'field_3'
if present in dict_1:
    print(repr(dict_1[present]))  # Expected output: 'test_val_3'
print()

absent = 'absent'
if absent not in dict_1:
    print('Field wasn\'t found in the dictionary.')
print()


#####################################################################################################################


"""
Adding elements to an existing dictionary
"""
print('--- Example: Adding elements to an existing dictionary ---')
print('dict_1 before adding a value: ' + repr(dict_1))
print()
dict_1['field_4'] = 'test_val_4'
print('dict_1 after adding a value: ' + repr(dict_1))
print()


#####################################################################################################################


"""
Deleting elements
"""
print('--- Example: Deleting elements ---')
print('dict_1 before deleting a value: ' + repr(dict_1))
print()
del dict_1['field_2']
print('dict_1 after deleting a value: ' + repr(dict_1))
print()

# del dict_1['not_a_valid_key']  # KeyError exception is raised if uncommented.


#####################################################################################################################


"""
Getting the number of elements in a dictionary
"""
print('--- Example: Getting the number of elements in a dictionary ---')
print(len(dict_1))
print()


#####################################################################################################################


"""
Mixing data types in a dictionary
"""
print('--- Example: Mixing data types in a dictionary ---')
mixed_up = {'abc': 1, 999: 'yada yada', (3, 6, 9): [3, 6, 9]}
print(repr(mixed_up))
print()


#####################################################################################################################


"""
Creating an empty dictionary
"""
dict_2 = {}
dict_3 = dict()


#####################################################################################################################


"""
Using a for loop to iterate over a dictionary
"""
print('--- Example: Using a for loop to iterate over a dictionary ---')
for key in dict_1:
    print(key, dict_1[key])
print()


#####################################################################################################################


"""
Some dictionary methods
"""

"""
Method         Description
=====================================================================================================================
clear          Clears the contents of a dictionary.
get            Gets the value associated with a specified key. If the key is not found, the method does not raise
                 an exception. Instead, it returns a default value.
items          Returns all the keys in a dictionary and their associated values as a sequence of tuples.
keys           Returns all the keys in a dictionary as a sequence of tuples.
pop            Returns the value associated with a specified key and removes that key-value pair from the dictionary.
                 If the key is not found, the method returns a default value.
popitem        Returns a randomly selected key-value pair as a tuple from the dictionary and removes that key-value
                 pair from the dictionary.
values         Returns all the values in the dictionary as a sequence of tuples.
"""
