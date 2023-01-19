"""
Tuples

The primary difference between tuples and lists is that tuples are immutable.
"""


#####################################################################################################################


"""
Tuple basics
"""

tuple_1 = (1, 2, 3, 4, 5)

# for i in tuple_1:
#     print(i)

# for i in range(0, len(tuple_1)):
#     print(tuple_1[i])

"""
Tuples support all the same operations as lists, except those that change the contents of the list.

Tuples support the following:
- Subscript indexing (for retrieving element values only)
- Methods such as `index`
- Built-in functions such as `len`, `min`, and `max`
- Slicing expressions
- The `in` operator
- The `+` and `-` operators

Tuples do not support methods such as `append`, `remove`, `insert`, `reverse`, and `sort`.
"""

tuple_2 = (1,)  # Creates tuple with only one element. Trailing comma is necessary to create a tuple.
whoops_an_integer = (1)  # Simply creates an integer.


#####################################################################################################################


"""
Converting between lists and tuples
"""

"""
You can use the built-in `list()` function to convert a tuple to a list and the built-in `tuple()` function to
  convert a list to a tuple.
"""

number_tuple = (1, 2, 3)
number_list = list(number_tuple)
print(number_list)  # [1, 2, 3]

str_list = ['one', 'two', 'three']
str_tuple = tuple(str_list)
print(str_tuple)  # ('one', 'two', 'three')
