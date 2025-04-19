'''test03_read_cat_data.py
Test `Data` class constructor and `read` method with a focus on categorical data
CS 251: Data Analysis and Visualization
Fall 2023
Oliver W. Layton
'''
import numpy as np

from data import Data


def read_data_constructor(iris_filename):
    iris_data = Data(iris_filename)
    _read_iris_common(iris_data)


def read_data_separately(iris_filename):
    iris_data = Data()
    print('Before calling read...')
    print(f"Your iris headers are:\n  {iris_data.headers}\nand should be:\n  None (or []).\n")

    iris_data.read(iris_filename)

    print('After calling read...')
    _read_iris_common(iris_data)


def _read_iris_common(iris_data):
    print(f'Your file path is:\n  {iris_data.filepath}\nand should be:\n  data/iris.csv\n')
    print(f"Your iris headers are\n  {iris_data.headers}\nand should be\n  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']\n")
    print(f"Your iris variable name-to-column mapping is\n  {iris_data.header2col}\nand should be\n  {{'sepal_length': 0, 'sepal_width': 1, 'petal_length': 2, 'petal_width': 3, 'species': 4}}\n")
    print(f"Your iris categorical variable name-to-level mapping is\n  {iris_data.cats2levels}\nand should be\n  {{'species': ['setosa', 'versicolor', 'virginica']}}\n")
    print(f'Your data is a ndarray? {isinstance(iris_data.data, np.ndarray)}')
    print(f'Your data has {iris_data.data.shape[0]} samples and {iris_data.data.shape[1]} variables/dimensions.\nIt should have 150 samples and 5 variables/dimensions.')

    non_numeric = [val for val in iris_data.data.flatten() if isinstance(val, str)]
    if len(non_numeric) > 0:
        print()
        print('Your self.data ndarray contains non-numeric values and it should not.')
        if len(non_numeric) <= 10:
            print(f'  Here are the non-numeric values in self.data:\n  {non_numeric}')
        else:
            print(f'  Here are the first 10 non-numeric values in self.data:\n  {non_numeric[:10]}')
        print("  If you see 'setosa', did you forget to convert categorical variables from strings to ints in self.data?")


def read_data_spaces(test_filename):
    test_data = Data(test_filename)
    print(f'Your test data looks like:\n', test_data.data)
    print('You should see:')
    print('Your test data looks like:\n [[ 1.  2.  3.  4.]\n [ 5.  6.  7.  8.]\n [ 9. 10. 11. 12.]]')
    print('Pay attention to the data type! The numbers should be floats (not have quotes around them).')


def read_mixed_data(test_filename):
    test_data = Data(test_filename)

    print(f'Your file path is:\n  {test_data.filepath}\nand should be:\n  data/test_data_mixed_spaces.csv\n')
    print(f"Your headers are\n  {test_data.headers}\nand should be\n  ['age', 'fav_color', 'shoe_size', 'height', 'fav_pastime', 'spirit_animal', 'fav_food']\n")
    print(f"Your variable name-to-column mapping is\n  {test_data.header2col}\nand should be\n  {{'age': 0, 'fav_color': 1, 'shoe_size': 2, 'height': 3, 'fav_pastime': 4, 'spirit_animal': 5, 'fav_food': 6}}\n")
    print(f"Your categorical variable name-to-level mapping is")
    for key, value in test_data.cats2levels.items():
        print(f'  {key}: {value}')
    print(f'and should be')
    print('''  fav_color : ['Purple', 'Yellow', 'Black']
  fav_pastime : ['Painting with Toes', 'Sock Puppetry', 'Stilt Walking']
  spirit_animal : ['Penguin', 'Koala', 'Frog']
  fav_food : ['Pizza', 'Broccoli', 'Spaghetti', 'Pineapple']
          ''')

    print(f'Your test data looks like:\n', test_data.data)
    print('You should see:')
    expected_data = ''' [[ 30.    0.    7.5 160.    0.    0.    0. ]
 [ 22.    1.    9.  175.    0.    1.    1. ]
 [ 25.    0.   10.5 180.    0.    0.    1. ]
 [ 28.    1.    6.5 155.    1.    1.    1. ]
 [ 35.    0.    8.  170.    1.    2.    2. ]
 [ 29.    1.    7.  165.    1.    2.    0. ]
 [ 31.    0.   11.  185.    2.    0.    1. ]
 [ 27.    1.    6.  158.    2.    1.    2. ]
 [ 23.    2.    7.5 162.    2.    2.    3. ]]'''
    print(f'Your test data looks like:\n{expected_data}')
    print('Pay attention to the data type! The numbers should be floats (not have quotes around them).')


if __name__ == '__main__':
    print('---------------------------------------------------------------------------------------')
    print('Beginning test 1 (Read data in constructor)...')
    print('---------------------------------------------')
    data_file = 'data/iris.csv'
    read_data_constructor(data_file)
    print('---------------------------------------------')
    print('Finished test 1!')
    print('---------------------------------------------------------------------------------------')

    print('---------------------------------------------------------------------------------------')
    print('Beginning test 2 (Read data separately)...')
    print('---------------------------------------------')
    read_data_separately(data_file)
    print('---------------------------------------------')
    print('Finished test 2!')
    print('---------------------------------------------------------------------------------------')

    print('---------------------------------------------------------------------------------------')
    print('Beginning test 3 (Data with spaces)...')
    print('---------------------------------------------')
    spaces_filename = 'data/test_data_spaces.csv'
    read_data_spaces(spaces_filename)
    print('---------------------------------------------')
    print('Finished test 3!')
    print('---------------------------------------------------------------------------------------')

    print('---------------------------------------------------------------------------------------')
    print('Beginning test 4 (Data with spaces, multiple numeric and categorical variables)...')
    print('---------------------------------------------')
    mixed_filename = 'data/test_data_mixed_spaces.csv'
    read_mixed_data(mixed_filename)
    print('---------------------------------------------')
    print('Finished test 4!')
    print('---------------------------------------------------------------------------------------')
