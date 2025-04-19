'''test04_read_missing_data.py
Test `Data` class constructor and `read` method with a focus on missing data
CS 251: Data Analysis and Visualization
Fall 2023
Oliver W. Layton
'''
from data import Data
import numpy as np
np.set_printoptions(precision=1, suppress=True)


def read_missing_data(test_filename):
    test_data = Data(test_filename)

    print(f'Your file path is:\n  {test_data.filepath}\nand should be:\n  data/test_data_missing.csv\n')
    print(f"Your headers are\n  {test_data.headers}\nand should be\n  ['age', 'fav_color', 'shoe_size', 'fav_sport']\n")
    print(f"Your variable name-to-column mapping is\n  {test_data.header2col}\nand should be\n  {{'age': 0, 'fav_color': 1, 'shoe_size': 2, 'fav_sport': 3}}\n")
    print(f"Your categorical variable name-to-level mapping is\n  {test_data.cats2levels}\nand should be\n  {{'fav_color': ['Missing', 'Purple'], 'fav_sport': ['Juggling', 'Missing']}}\n")

    print(f'Your test data looks like:\n', test_data.data)
    print('You should see:')
    expected_data = ''' [[ nan  0.   7.5  0. ]
 [22.   0.   nan  1. ]
 [25.   1.  10.5  1. ]]'''
    print(f'Your test data looks like:\n{expected_data}')
    print('Pay attention to the data type! The numbers should be floats or nan (not have quotes around them).')


def read_austin_pet_data(test_filename):
    test_data = Data(test_filename)

    print(f'Your file path is:\n  {test_data.filepath}\nand should be:\n  data/austin_pet.csv\n')
    print(f"Your headers are\n  {test_data.headers}\nand should be\n  ['animal_id', 'in_reason', 'in_condition', 'animal_type', 'breed', 'color', 'in_year', 'in_month', 'in_day', 'in_hour', 'found_state', 'sex', 'in_age_years', 'outcome', 'outcome_subtype', 'out_year', 'out_month', 'out_day', 'out_hour', 'out_age_years', 'dob_month', 'dob_day', 'dob_year']\n")
    print(f"Your variable name-to-column mapping is")
    for key, value in test_data.header2col.items():
        print(f'  {key:15}: {value:<2}')
    print(f'and should be')
    expected = '''  animal_id      : 0
  in_reason      : 1
  in_condition   : 2
  animal_type    : 3
  breed          : 4
  color          : 5
  in_year        : 6
  in_month       : 7
  in_day         : 8
  in_hour        : 9
  found_state    : 10
  sex            : 11
  in_age_years   : 12
  outcome        : 13
  outcome_subtype: 14
  out_year       : 15
  out_month      : 16
  out_day        : 17
  out_hour       : 18
  out_age_years  : 19
  dob_month      : 20
  dob_day        : 21
  dob_year       : 22'''
    print(expected)
    print(f'The first row of test data looks like:')
    print(test_data.data[0])
    print('You should see:')
    expected_data = '''[657197.      0.      0.      0.      0.      0.      0.      0.      0.
      0.      0.      0.     nan      0.      0.      0.      0.      0.
      0.      0.      0.      0.      0.]'''
    print(f'{expected_data}')
    print(f'The last row of test data looks like:')
    print(test_data.data[-1])
    print('You should see:')
    expected_data = '''[883557.      2.      1.      1.    389.    315.     11.      9.     20.
     14.      1.      1.      8.      6.      0.     11.     12.     31.
     22.     38.     12.     31.     23.]'''
    print(f'{expected_data}')
    print('Pay attention to the data type! The numbers should be floats or nan (not have quotes around them).')


if __name__ == '__main__':
    print('---------------------------------------------------------------------------------------')
    print('Beginning test 1 (Data with missing data)...')
    print('---------------------------------------------')
    mixed_filename = 'data/test_data_missing.csv'
    read_missing_data(mixed_filename)
    print('---------------------------------------------')
    print('Finished test 1!')
    print('---------------------------------------------------------------------------------------')

    print('---------------------------------------------------------------------------------------')
    print('Beginning test 2 (Large dataset with missing data)...')
    print('---------------------------------------------')
    filename = 'data/austin_pet.csv'
    read_austin_pet_data(filename)
    print('---------------------------------------------')
    print('Finished test 2!')
    print('---------------------------------------------------------------------------------------')
