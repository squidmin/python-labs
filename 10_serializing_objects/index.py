import pickle

"""
Serializing objects

Serializing objects is the process of converting the object to a stream of bytes that can be saved for later
  retrieval. In Python, object serialization is called "pickling."
"""

dict_1 = {'name': 'test_name', 'age': 'test_val_2', 'weight': 'test_weight_3'}
output_file_1 = open('test_info_1.dat', 'wb')
pickle.dump(dict_1, output_file_1)
output_file_1.close()


def main():
    again = 'y'
    output_file_2 = open('test_info_2.dat', 'wb')

    while again.lower() == 'y':
        save_data(output_file_2)
        again = input('Enter more data? (y/n): ')

    output_file_2.close()


def save_data(file):
    person = {}
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    pickle.dump(person, file)


main()
