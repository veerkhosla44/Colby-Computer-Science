'''analysis.py
Run statistical analyses and plot Numpy ndarray data
Veer Khosla
CS 251: Data Analysis and Visualization
Fall 2023
'''
import numpy as np
import matplotlib.pyplot as plt
from data import Data

class Analysis:
    def __init__(self, data):
        '''

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        self.data = data

        plt.rcParams.update({'font.size': 18})

    def set_data(self, data):
        '''Method that re-assigns the instance variable `data` with the parameter.
        Convenience method to change the data used in an analysis without having to create a new Analysis object.

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        self.data = data

    def min(self, headers, rows=[]):
        '''Computes the minimum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.
        (i.e. the minimum value in each of the selected columns)

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min over, or over all indices if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''

        data_subset = self.data.select_data(headers, rows)
        return np.min(data_subset, axis = 0)

    
    def max(self, headers, rows=[]):
        '''Computes the maximum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of max over, or over all indices if rows=[]

        Returns
        -----------
        maxs: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''

        data_subset = self.data.select_data(headers, rows)
        return np.max(data_subset, axis=0)
    

    def range(self, headers, rows=[]):
        '''Computes the range [min, max] for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min/max over, or over all indices if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables
        maxes: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        data_subset = self.data.select_data(headers, rows)
        return np.min(data_subset, axis=0), np.max(data_subset, axis=0)

    def mean(self, headers, rows=[]):
        '''Computes the mean for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`).

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of mean over, or over all indices if rows=[]

        Returns
        -----------
        means: ndarray. shape=(len(headers),)
            Mean values for each of the selected header variables

        NOTE: You CANNOT use np.mean here!
        NOTE: There should be no loops in this method!
        '''
        data_subset = self.data.select_data(headers, rows)
        return np.sum(data_subset, axis=0) / data_subset.shape[0]

    def var(self, headers, rows=[]):
        '''Computes the variance for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of variance over, or over all indices if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Variance values for each of the selected header variables

        NOTE:
        - You CANNOT use np.var or np.mean here!
        - There should be no loops in this method!
        '''
        data_subset = self.data.select_data(headers, rows)
        # print("Data Subset:", data_subset)
        n = data_subset.shape[0]
        mean = np.sum(data_subset, axis=0) / n
        # print("Mean:", mean)
        squared_diff = (data_subset - mean) ** 2
        # print("Squared Differences:", squared_diff)
        variance = np.sum(squared_diff, axis=0) / (n - 1)
        # print("Variance:", variance)
        return variance
    
    def std(self, headers, rows=[]):
        '''Computes the standard deviation for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of standard deviation over, or over all indices if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Standard deviation values for each of the selected header variables

        NOTE:
        - You CANNOT use np.var, np.std, or np.mean here!
        - There should be no loops in this method!
        '''
        return np.sqrt(self.var(headers, rows))


    def show(self):
        '''Simple wrapper function for matplotlib's show function.

        (Does not require modification)
        '''
        plt.show()

    def scatter(self, ind_var, dep_var, title):
        '''Creates a simple scatter plot with "x" variable in the dataset `ind_var` and "y" variable in the dataset
        `dep_var`. Both `ind_var` and `dep_var` should be strings in `self.headers`.

        Parameters:
        -----------
        ind_var: str.
            Name of variable that is plotted along the x axis
        dep_var: str.
            Name of variable that is plotted along the y axis
        title: str.
            Title of the scatter plot

        Returns:
        -----------
        x. ndarray. shape=(num_data_samps,)
            The x values that appear in the scatter plot
        y. ndarray. shape=(num_data_samps,)
            The y values that appear in the scatter plot

        NOTE: Do not call plt.show() here.
        '''
        x = self.data.select_data([ind_var])
        y = self.data.select_data([dep_var])
        plt.scatter(x, y)
        plt.xlabel(ind_var)
        plt.ylabel(dep_var)
        plt.title(title)
        return x, y


    def pair_plot(self, data_vars, fig_sz=(12, 12), title=''):
        '''Create a pair plot: grid of scatter plots showing all combinations of variables in `data_vars` in the
        x and y axes.

        Parameters:
        -----------
        data_vars: Python list of str.
            Variables to place on either the x or y axis of the scatter plots
        fig_sz: tuple of 2 ints.
            The width and height of the figure of subplots. Pass as a paramter to plt.subplots.
        title. str. Title for entire figure (not the individual subplots)

        Returns:
        -----------
        fig. The matplotlib figure.
            1st item returned by plt.subplots
        axes. ndarray of AxesSubplot objects. shape=(len(data_vars), len(data_vars))
            2nd item returned by plt.subplots

        TODO:
        1. Make the len(data_vars) x len(data_vars) grid of scatterplots
        2. The y axis of the FIRST column should be labeled with the appropriate variable being plotted there.
        The x axis of the LAST row should be labeled with the appropriate variable being plotted there.
        3. Only label the axes and ticks on the FIRST column and LAST row. There should be no labels on other plots
        (it looks too cluttered otherwise!).
        4. Do have tick MARKS on all plots (just not the labels).
        5. Because variables may have different ranges, your pair plot should share the y axis within columns and
        share the x axis within rows. To implement this, pass in the appropriate string values for the `sharex` and `sharey`
        keyword arguments of plt.subplots.
        '''

        if not isinstance(data_vars, list):
            data_vars = [data_vars]

        # figure and axes for the pair plot
        fig, axes = plt.subplots(len(data_vars), len(data_vars), figsize=fig_sz, sharex='col', sharey='row')
        
        # titles for the columns and rows
        for i, var in enumerate(data_vars):
            axes[len(data_vars) - 1, i].set_xlabel(var)  # x-axis label for the last row
            axes[i, 0].set_ylabel(var)  # y-axis label for the first column

        # scatter plots
        for i in range(len(data_vars)):
            for j in range(len(data_vars)):
                if i != j:
                    x_data = self.data.select_data([data_vars[j]])
                    y_data = self.data.select_data([data_vars[i]])
                    axes[i, j].scatter(x_data, y_data, alpha=0.5)

        #Formatting
        for i in range(len(data_vars) - 1):
            for j in range(len(data_vars)):
                axes[i, j].xaxis.set_visible(False)

        for i in range(len(data_vars)):
            for j in range(1, len(data_vars)):
                axes[i, j].yaxis.set_visible(False)

        if title:
            fig.suptitle(title)

        return fig, axes
    

    def trend_analysis(self, month):
        """
        Perform trend analysis for the given month.
        """
        yearly_avg_temps = []

        for year in range(1973, 2023):
            avg_temp = self.mean([month], rows=[year - 1973])
            yearly_avg_temps.append(avg_temp[0])

        return yearly_avg_temps
    

    def calculate_monthly_average(self, year, month):
        """
        Calculate the monthly average temperature for the specified year and month.
        """
        monthly_avg_temps = {month: [] for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}

        for month in monthly_avg_temps.keys():
            monthly_avg_temp = self.mean([month])
            monthly_avg_temps[month] = monthly_avg_temp

        self.plot_monthly_averages(monthly_avg_temps)


    def monthly_averages_over_time(self):
        """
        Calculate and plot monthly averages over time.
        """
        monthly_avg_temps = {month: [] for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}

        for month in monthly_avg_temps.keys():
            monthly_avg_temps[month] = self.calculate_monthly_average_over_time(month)

        self.plot_monthly_averages(monthly_avg_temps)


    def calculate_monthly_average_over_time(self, month):
        """
        Calculate the monthly average temperature over time for a specific month.
        """
        monthly_avg_temps = []

        for year in range(1973, 2023):
            avg_temp = self.mean([month], rows=[year - 1973])
            monthly_avg_temps.append(avg_temp[0])

        return monthly_avg_temps


    def plot_monthly_averages(self, monthly_avg_temps):
        """
        Plot monthly average temperatures over time.
        """
        months = list(monthly_avg_temps.keys())
        plt.figure(figsize=(12, 6))

        for month in months:
            plt.plot(range(1973, 2023), monthly_avg_temps[month], label=month)


        plt.ylim(0, max([max(monthly_avg_temps[month]) for month in months]))
        plt.legend(loc='center left', bbox_to_anchor=(1, 1))

        plt.xlabel('Year')
        plt.ylabel('Monthly Average Temperature')
        plt.title('Monthly Average Temperatures Over Time')
        plt.legend()
        plt.grid(True)

        plt.show()


    def yearly_average_over_time(self):
        """
        Calculate and plot the yearly average temperatures over time.
        """
        yearly_avg_temps = []

        for year in range(1895, 2023):
            monthly_avg_temps = []

            for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                avg_temp = self.mean([month], rows=[year - 1895])
                monthly_avg_temps.append(avg_temp[0]) 

            # current year
            yearly_avg_temp = np.mean(monthly_avg_temps)
            yearly_avg_temps.append(yearly_avg_temp)

        # scatter plot
        plt.figure(figsize=(12, 6))
        plt.scatter(range(1895, 2023), yearly_avg_temps, marker='o', label='Yearly Average Temperature')
        plt.xlabel('Year')
        plt.ylabel('Yearly Average Temperature')
        plt.title('Yearly Average Temperature Over Time')
        plt.grid(True)
        plt.ylim(30, 50)
        plt.legend()

        plt.show()


    def monthly_means(self):
        monthly_means = {}
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            data_subset = self.data.select_data([month])
            mean_temp = np.mean(data_subset)
            monthly_means[month] = mean_temp

        return monthly_means


    def monthly_ranges(self):
        monthly_ranges = {}
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            data_subset = self.data.select_data([month])

            # range for the current month
            range_temp = np.ptp(data_subset)
            monthly_ranges[month] = range_temp

        return monthly_ranges

    def monthly_stds(self):
        monthly_stds = {}
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            data_subset = self.data.select_data([month])
            std_temp = np.std(data_subset)
            monthly_stds[month] = std_temp

        return monthly_stds
    


    def format_dict(self, input_dict, format_str="{:<2}: {:.2f}"):
        """Format a dictionary for easier reading.
        """
        formatted_str = ""
        for key, value in input_dict.items():
            formatted_str += format_str.format(key, value) + "\n"
        return formatted_str


