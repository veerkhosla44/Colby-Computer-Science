'''categorical_analysis.py
Run analyses with categorical data
Veer Khosla
CS 251: Data Analysis and Visualization
Fall 2023
'''
import numpy as np
import analysis


class CatAnalysis(analysis.Analysis):
    def __init__(self, data):
        '''CatAnalysis constructor

        (This method is provided to you and should not require modification)

        Parameters:
        -----------
        data: `CatData`.
            `CatData` object that stores the dataset.
        '''
        super().__init__(data)

    def cat_count(self, header):
        '''Counts the number of samples that have each level of the categorical variable named `header`

        Example:
            Column of self.data for `cat_var1`: [0, 1, 2, 0, 0, 1, 0, 0]
            This method should return `counts` = [5, 2, 1].

            If the string level corresponding to `0` is 'Missing' and `exclude_missing` = True then this method returns:
            `counts` = [2, 1].

        Parameters:
        -----------
        header: str. Header of the categorical variable whose levels should be returned.

        Returns:
        -----------
        ndarray. shape=(num_levels,). The number of samples that have each level of the categorical variable named `header`
        list of strs. len=num_levels. The level strings of the categorical variable  `header` associated with the counts.

        NOTE:
        - Your implementation should rely on logical indexing. Using np.unique is not allowed here.
        - A single loop over levels is totally fine here.
        - `self.data` stores categorical levels as INTS so it is helpful to work with INT-coded levels when doing the counting.
        The method should, however, return the STRING-coded levels (e.g. for plotting).
        '''
        # Check if string_levels is None
        string_levels = self.data.get_cat_levels_str(header)
        if string_levels is None:
            raise ValueError(f"String levels for '{header}' could not be obtained.")

        countList = np.zeros(len(string_levels))
        level_strings_result = []

        for i, level in enumerate(string_levels):
            countList[i] = np.sum(self.data.data[:, self.data.header2col[header]] == i)
            level_strings_result.append(level)

        return countList, level_strings_result

    def cat_mean(self, numeric_header, categorical_header):
        '''Computes the mean of values of the numeric variable `numeric_header` for each of the different categorical
        levels of the variable `categorical_header`.

        POSSIBLE EXTENSION. NOT REQUIRED FOR BASE PROJECT

        Example:
            Column of self.data for `numeric_var1` = [4, 5, 6, 1, 2, 3]
            Column of self.data for `cat_var1` = [0, 0, 0, 1, 1, 1]

            If `numeric_header` = "numeric_var1" and `categorical_header` = "cat_var1", this method should return
            `means` = [5, 2].
            (1st entry is mean of all numeric var values with corresponding int level of 0,
             2nd entry is mean of all numeric var values with corresponding int level of 1)

        Parameters:
        -----------
        numeric_header: str. Header of the numeric variable whose values should be averaged.
        categorical_header: str. Header of the categorical variable whose levels determine which values of the
            numeric variable that should be averaged.

        Returns:
        -----------
        ndarray. shape=(num_levels,). Means of values of the numeric variable `numeric_header` for each of the different
            categorical levels of the variable `categorical_header`.
        list of strs. len=num_levels. The level strings of the categorical variable  `categorical_header` associated with
            the counts.

        NOTE:
        - Your implementation should rely on logical indexing. Using np.unique is not allowed here.
        - A single loop over levels is totally fine here.
        - As above, it is easier to work with INT-coded levels, but the STRING-coded levels should be returned.
        - Since your numeric data has nans in it, you should use np.nanmean, which ignores any nan values. Otherwise, the
        according to np.mean, the mean of any collection of numbers that include at least one nan will always be nan.
        You can easily swap np.mean with np.nanmean: https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html
        '''
        string_levels = self.data.get_cat_levels_str(categorical_header)
        if string_levels is None:
            raise ValueError(f"String levels for '{categorical_header}' could not be obtained.")

        means = np.zeros(len(string_levels), dtype=float)

        for i, level in enumerate(string_levels):
            indices = self.data.data[:, self.data.header2col[categorical_header]] == i
            values = self.data.data[indices, self.data.header2col[numeric_header]]
            means[i] = np.nanmean(values)

        return means, string_levels
    

    def cat_var(self, numeric_header, categorical_header):
        '''Computes the variance of values of the numeric variable `numeric_header` for each of the different categorical
        levels of the variable `categorical_header`.

        Parameters:
        -----------
        numeric_header: str. Header of the numeric variable whose values should be used for variance calculation.
        categorical_header: str. Header of the categorical variable whose levels determine the groups for variance calculation.

        Returns:
        -----------
        ndarray. shape=(num_levels,). Variance of values of the numeric variable `numeric_header` for each of the different
            categorical levels of the variable `categorical_header`.
        list of strs. len=num_levels. The level strings of the categorical variable `categorical_header` associated with the variances.

        NOTE:
        - Your implementation should rely on logical indexing.
        - You can use np.nanvar to calculate the variance while ignoring NaN values.
        '''
        string_levels = self.data.get_cat_levels_str(categorical_header)
        if string_levels is None:
            raise ValueError(f"String levels for '{categorical_header}' could not be obtained.")

        variances = np.zeros(len(string_levels), dtype=float)

        for i, level in enumerate(string_levels):
            indices = self.data.data[:, self.data.header2col[categorical_header]] == i
            values = self.data.data[indices, self.data.header2col[numeric_header]]
            variances[i] = np.nanvar(values)

        return variances, string_levels


    def cat_count2(self, header1, header2):
        '''Counts the number of samples that have all combinations of levels coming from two categorical headers
        (`header1` and `header2`).

        POSSIBLE EXTENSION. NOT REQUIRED FOR BASE PROJECT

        Parameters:
        -----------
        header1: str. Header of the first categorical variable
        header2: str. Header of the second categorical variable

        Returns:
        -----------
        ndarray. shape=(header1_num_levels, header2_num_levels). The number of samples that have each combination of
            levels of the categorical variables `header1` and `header2`.
        list of strs. len=header1_num_levels. The level strings of the categorical variable  `header1`
        list of strs. len=header2_num_levels. The level strings of the categorical variable  `header2`

        Example:

        header1_level_strs: ['a', 'b']
        header2_level_strs: ['y', 'z']

        counts =
                [num samples with header1 value 'a' AND header2 value 'y', num samples with header1 value 'a' AND header2 value 'z']
                [num samples with header1 value 'b' AND header2 value 'y', num samples with header1 value 'b' AND header2 value 'z']

        NOTE:
        - To combine two logical arrays element-wise, you can use the & operator or np.logical_and
        '''
        levels_header1 = self.data.get_cat_levels_str(header1)
        levels_header2 = self.data.get_cat_levels_str(header2)

        if levels_header1 is None or levels_header2 is None:
            raise ValueError(f"String levels for '{header1}' or '{header2}' could not be obtained.")

        counts = np.zeros((len(levels_header1), len(levels_header2)), dtype=int)

        for i, level1 in enumerate(levels_header1):
            for j, level2 in enumerate(levels_header2):
                counts[i, j] = np.sum((self.data.data[:, self.data.header2col[header1]] == i) &
                                    (self.data.data[:, self.data.header2col[header2]] == j))

        return counts, levels_header1, levels_header2

    

