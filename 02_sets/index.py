'''
Creating a set
'''
print('--- Example: Creating a set ---')
set_1 = set()
print(repr(set_1))

set_2 = set(['a', 'b'])
print(repr(set_2))

set_3 = set('abc')
print(repr(set_3))

print(set('aaabc'))  # Duplicates will be removed, per set semantics.

set_4 = set(['one', 'two', 'three'])
print(repr(set_4))

print()


#####################################################################################################################


'''
Getting the number of elements in a set
'''
print('--- Example: Getting the number of elements in a set ---')
print(len(set_2))
print()


#####################################################################################################################


'''
Adding and removing elements
'''
print('--- Example: Adding and removing elements ---')
print('"set_1", before adding elements: ' + repr(set_1))
set_1.add('x')
print('"set_1", after adding elements: ' + repr(set_1))
print()

print('"set_1", before updating elements: "' + repr(set_1))
set_1.update(['i', 'j', 'k'])  # Add a group of items
set_1.update(set_2)  # Add the items of one set to another
print('"set_1", after updating elements: "' + repr(set_1))
print()

print('"set_1", before deleting elements: ' + repr(set_1))
set_1.remove('a')  # Throws a KeyError when it can't locate the target data.
set_1.discard('b')  # Doesn't throw a KeyError when it can't locate the target data.
print('"set_1", after deleting elements: ' + repr(set_1))
print()


#####################################################################################################################


'''
Using a for loop to iterate over a set
'''
print('--- Example: Adding and removing elements ---')
for var in set_1:
  print(var)
print()


#####################################################################################################################


'''
Using the "in" and "not in" operators to test for a value in a set
'''
print('--- Example: Using the "in" and "not in" operators to test for a value in a set ---')
if 'c' in set_3:
  print('"c" was located in "set_3"...')
print()

if -1 not in set_3:
  print('-1 was not located in "set_3"...')
print()


#####################################################################################################################


'''
Finding the union of sets
'''
print('--- Example: Finding the union of sets ---')
print('set_1 == ' + repr(set_1))
print('set_3 == ' + repr(set_3))
print('set_1 | set_3 == ' + repr(set_1 | set_3))            # set_a | set_b
print('set_1.union(set_3) == ' + repr(set_1.union(set_3)))  # set_a.union(set_3)
print()


#####################################################################################################################


'''
Finding the intersection of sets
'''
print('--- Example: Finding the intersection of sets ---')
print('set_1 == ' + repr(set_1))
print('set_3 == ' + repr(set_3))
print('set_1 & set_3 == ' + repr(set_1 & set_3))                          # set_a & set_b
print('set_1.intersection(set_3) == ' + repr(set_1.intersection(set_3)))  # set_a.intersection(set_3)
print()


#####################################################################################################################


'''
Finding the difference of sets

Note: The difference of set_1 and set_2 are the elements that appear in set_1 but do not appear in set_2.
'''
print('--- Example: Finding the intersection of sets ---')
print('set_1 == ' + repr(set_1))
print('set_3 == ' + repr(set_3))
print('set_1 - set_3 == ' + repr(set_1 - set_3))                      # set_a - set_b
print('set_1.difference(set_3) == ' + repr(set_1.difference(set_3)))  # set_a.difference(set_3)
print()


#####################################################################################################################


'''
Finding the symmetric difference of sets

Note: The symmetric difference of two sets is a set that contains the elements that are not shared by the two sets.
'''
print('--- Example: Finding the symmetric difference of sets ---')
print('set_1 == ' + repr(set_1))
print('set_3 == ' + repr(set_3))
print('set_1 ^ set_3 == ' + repr(set_1 ^ set_3))                                          # set_a ^ set_b
print('set_1.symmetric_difference(set_3) == ' + repr(set_1.symmetric_difference(set_3)))  # set_a.symmetric_difference(set_3)
print()


#####################################################################################################################


'''
Finding subsets and supersets
'''
print('--- Example: Finding subsets and supersets ---')
print('set_3 <= set_2 == ' + repr(set_3 <= set_2))
print('set_3.issubset(set_2) == ' + repr(set_3.issubset(set_2)))
print('set_3 >= set_2 == ' + repr(set_3 >= set_2))
print('set_3.issuperset(set_2) == ' + repr(set_3.issuperset(set_2)))
print()
