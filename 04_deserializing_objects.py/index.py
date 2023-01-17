import pickle

"""
Deserializing objects
"""

input_file = open('test_info.dat', 'rb')
obj = pickle.load(input_file)
print('obj == ' + repr(obj))
print()

def main():
  end_of_file = False
  input_file = open('test_info.dat', 'rb')
  while not end_of_file:
    try:
      person = pickle.load(input_file)
      display_data(person)
    except EOFError:
      end_of_file = True
  
  input_file.close()

def display_data(person):
  print('Name: ', person['name'])
  print('Age: ', person['age'])
  print('Weight: ', person['weight'])
  print()

main()
