"""
Strings
"""


#####################################################################################################################


"""
String slicing

Slicing operations select a range of characters from a string.
"""

string_1 = "abcdefghijkl"

print(string_1[5:])    # fghijkl
print(string_1[6:10])  # ghij
print(string_1[:8])    # abcdefgh

# Third number inside brackets is a step value. Slice contains every 2nd character.
print(string_1[0:len(string_1):2])  # acegik

# Use negative numbers as indices in slicing expressions to reference positions relative to the end of the string.
print(string_1[-5:])  # hijkl

print()


#####################################################################################################################


"""
Testing, searching, & manipulating strings

Python provides operators and methods for testing strings, searching the contents of strings, and getting
  modified copies of strings.
"""


"""
Testing strings with `in` and `not in`
"""
string_2 = 'asdfhgjkltyui'
search = 'asdf'
if search in string_2:
    print('Found', search)
search = 'hjkl'
if search not in string_2:
    print('Didn\'t find', search)

print()


"""
String testing methods
"""
string_3 = '1200'
print(string_3.isdigit())  # True
print(string_3.isalpha())  # False
print(string_3.isspace())  # False
print()

string_3 = '123abc'
print(string_3.isalpha())  # False
print(string_3.isalnum())  # True

print()

# More string operations: https://www.w3schools.com/python/python_ref_string.asp


"""
String modification methods

Although strings are immutable in Python, meaning they cannot be modified, they do have a number of methods
  that return modified versions of themselves.
"""
string_4 = "  ASDFiulasdfiu  "
print(string_4.lower())               # "  sadfiulasdfiu  "
print(string_4.lstrip())              # "ASDFiulasdfiu  "
print(string_4.lstrip().lstrip('A'))  # "SDFiulasdfiu  "
print(string_4.rstrip())              # "  ASDFiulasdfiu"
print(string_4.rstrip().rstrip('u'))  # "  ASDFiulasdfi"
print(string_4.strip())               # "ASDFiulasdfiu"
print(string_4.strip(' '))            # "ASDFiulasdfiu"
print('racecar'.strip('ra'))          # "cec"
print(string_4.upper())               # "  ASDFIULASDFIU  "

print()

# More string operations: https://www.w3schools.com/python/python_ref_string.asp


"""
Searching and replacing
"""
string_5 = 'searching and replacing'
print(string_5.endswith('ing'))       # True
print(string_5.find('ear'))           # 1
print(string_5.replace('ing', 'HI'))  # "searchHI and replacHI"
print(string_5.startswith('sea'))     # True
print()


"""
Repetition operator
"""
string_6 = 'repetitions'
print(string_6 * 3)
print()
for i in range(1, 10):
    print('*' * i)
for i in range(8, 0, -1):
    print('*' * i)
print()


"""
Splitting
"""
string_7 = 'One two three four'
word_list = string_7.split()  # ['One', 'two', 'three', 'four']
print(word_list)
print()

"""
By default, the split method uses spaces as separators.
You can specify a different separator by passing it in as an argument to the split method.
"""
date = '01/01/2023'
print(date.split('/'))  # ['01', '01', '2023']
print()


#####################################################################################################################


"""
Comparing strings
"""
string_8 = "abc"
string_9 = "def"
print(string_8 == string_9)  # False
print(string_8 != string_9)  # True
print(string_8 > string_9)   # False
print(string_8 < string_9)   # True
print(string_8 >= string_9)  # False
print(string_8 <= string_9)  # True
