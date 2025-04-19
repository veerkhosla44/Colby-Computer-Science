'''categorical_data.py
Manages and provides functionality for working with categorical data
Veer Khosla
CS 251: Data Analysis and Visualization
Fall 2023
'''
import numpy as np

import data


class CatData(data.Data):
    '''`Data` class with expanded support for categorical data
    '''
    def __init__(self, filepath=None, headers=None, data=None, header2col=None, cats2levels=None):
        '''CatData constructor

        Parameters:
        -----------
        filepath: str or None. Path to data .csv file
        headers: Python list of strings or None. List of strings that explain the name of each column of data.
        data: ndarray or None. shape=(N, M).
            N is the number of data samples (rows) in the dataset and M is the number of variables (cols) in the dataset.
        header2col: Python dictionary or None.
                Maps header (var str name) to column index (int).
                Example: "sepal_length" -> 0
        cats2levels: Python dictionary or None.
        '''
        super().__init__(filepath, headers, data, header2col, cats2levels)
        self.original_data = self.data.copy()


    def get_cat_levels_str(self, header):
        '''Get the list of categorical level strings associated with the `header`

        Example:
            Categorical variable names -> Level strings:
                "cat_var1" -> ["a", "b", "c"]
                "cat_var2" -> ["z", "y", "x"]
            If `header` = "cat_var1" then this method returns ["a", "b", "c"].

        Parameters:
        -----------
        header: str. Header of the categorical variable whose levels should be returned.

        Returns:
        -----------
        ndarray of strs. categorical level strings associated with the `header`.

        NOTE: You should cast your list of levels associated with `header` as an ndarray. To do this, remember we can use
        np.array. So instead of returning blah (where blah is the list of levels) you would return np.array(blah).
        '''
        if header in self.cats2levels:
            return np.array(self.cats2levels[header])
        else:
            return None

    def get_cat_levels_int(self, header):
        '''Get the list of int-coded categorical levels associated with the `header`

        Example:
            Categorical variable names -> Level strings:
                "cat_var1" -> ["a", "b", "c"]
                "cat_var2" -> ["z", "y", "x"]
            If `header` = "cat_var2" then this method returns [0, 1, 2].

        Parameters:
        -----------
        header: str. Header of the categorical variable whose levels should be returned.

        Returns:
        -----------
        ndarray of ints. int-coded categorical levels associated with the `header`
        '''
        if header in self.header2col:
            col_index = self.header2col[header]
            col_data = self.data[:, col_index]

            if np.issubdtype(col_data.dtype, np.integer):
                return np.unique(col_data).astype(int)
            else:
                int_col_data = col_data.astype(int)
                return np.unique(int_col_data).astype(int)
        else:
            return np.array([])

    def int2strlevels(self, header, int_levels):
        '''Convert the int-coded levels of the categorical variable named `header` into strings

        Example:
            Categorical variable names -> Level strings:
                "cat_var1" -> ["a", "b", "c"]
                "cat_var2" -> ["z", "y", "x"]
            If `header` = "cat_var2" and `int_levels` = [2, 0] then this method returns ["x", "z"].

        Parameters:
        -----------
        header: str. Header of the categorical variable whose levels should be converted.
        int_levels: list. ints levels associated with the categorical variable named `header`

        Returns:
        -----------
        list of strs. string representations of the int-coded categorical levels `int_levels` associated with `header`
        '''
        string_levels = self.get_cat_levels_str(header)
        strLevels = []

        for level in int_levels:
            strLevels.append(string_levels[level])

        return strLevels

    def str2intlevels(self, header, str_levels):
        '''Convert the string-coded levels of the categorical variable named `header` into ints

        Example:
            Categorical variable names -> Level strings:
                "cat_var1" -> ["a", "b", "c"]
                "cat_var2" -> ["z", "y", "x"]
            If `header` = "cat_var1" and `str_levels` = ["c", "b", "a"] then this method returns [2, 1, 0].

        Parameters:
        -----------
        header: str. Header of the categorical variable whose levels should be converted.
        str_levels: list. str levels associated with the categorical variable named `header`

        Returns:
        -----------
        list of ints. int representations of the string-coded categorical levels `str_levels` associated with `header`
        '''
        string_levels = self.get_cat_levels_str(header)
        intLevels = []

        string_levels = string_levels.tolist()
        for level in str_levels:
            intLevels.append(string_levels.index(level))
        
        return intLevels

    def reset_dataset(self):
        '''Restores the `self.data` ndarray to the original dataset — i.e. removes any filtering of the dataset.

        TODO:
        1. Add a line of code to the constructor that creates an instance variable that represents the original, unmodified
        dataset (e.g. as it was read in from the CSV file). Assign it to a COPY of `self.data`.
        2. In this method, assign `self.data` to a COPY of the original dataset that you set in the constructor.
        '''
        self.data = self.original_data.copy()


    def filter(self, header, strlevel):
        '''Filters dataset to select samples (i.e. rows) only for which the value of the categorical variable `header`
        is equal to `strlevel`. The filtered dataset should replace `self.data`.

        Parameters:
        -----------
        header: str. Header of the categorical variable that we are using to filter the dataset
        strlevel: str. The level string associated with the categorical variable named `header` that we are using to
            filter the dataset.

        NOTE:
        - Remember that the level passed in as a parameter is a STRING but the dataset ndarray (`self.data`) stores
        categorical values as INTs.
        - Logical indexing requires that the array being used to index another has shape=`(N,)` instead of shape=`(N,1)`.
        Therefore, `np.squeeze` might be helpful...
        '''
        
        int_level = self.cats2levels[header].index(strlevel)
        mask = self.data[:, self.header2col[header]] == int_level
        self.data = self.data[mask]
