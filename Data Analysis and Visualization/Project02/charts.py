'''charts.py
Plotting functions for categorical data
Veer Khosla
CS 251: Data Analysis and Visualization
Fall 2023
'''
import numpy as np
import matplotlib.pyplot as plt


def sidebarplot(values, labels, title, show_counts=True, figsize=(6, 7), sort_by='na', top_k = None, error_bars = False):
    '''Horizontal bar plot with bar lengths `values` (the "x values") with associated labels `labels` on the y axis.

    Parameters:
    -----------
    values: ndarray. shape=(num_levels). Each numeric value to plot as a separate horizontal bar coming out of the y axis.
    labels: list of str. len=num_labels. Labels associated with each bar / numeric value in `values`.
    title: str. Title of the plot.
    show_counts: bool. Whether to show each numeric value as text next to each bar.
    fig_sz: tuple of 2 ints. The width and height of the figure.

    NOTE:
    - Assign the output of plt.barh to a variable named ax. i.e.
        ax = plt.barh(...)
    If show_counts is set to True, then add the code:
        if show_counts:
            plt.bar_label(ax, values)    
    to make the values appear on the plot as text next to each bar.
    - If your values show up next to the bars with many significant digits, add the following line of code to have Numpy
    round each displayed value to the nearest 0.01:
        values = np.round(values, 2)
    '''
    
    if sort_by == 'na':
        sorted_indices = np.argsort(labels)
    elif sort_by == 'va':
        # sort values in descending order
        sorted_indices = np.argsort(values)[::-1]
    else:
        raise ValueError("Invalid sort_by value. Use 'na' for sorting by label or 'va' for sorting by value.")
    
    values = values[sorted_indices]
    labels = [labels[i] for i in sorted_indices]

    if top_k is not None:
        values = values[:top_k]
        labels = labels[:top_k]
    
    fig, ax = plt.subplots(figsize=figsize)
    values = np.round(values, 2)
    ax.barh(labels, values)

    if show_counts:
        ax.bar_label(ax.containers[0])

    if error_bars:
        std_devs = np.random.uniform(0.1, 0.5, len(labels))
        ax.errorbar(values, labels, xerr=std_devs, fmt='o', color='red', label='Std Dev')

    ax.set_title(title)
    plt.show()


def sort(values, labels, sort_by='na'):
    '''Sort the arrays `values` and `labels` in the same way so that corresponding items in either array stay matched up
    after the sort.

    Parameters:
    -----------
    values: ndarray. shape=(num_levels,). One array that should be sorted
    labels: ndarray. shape=(num_levels,). Other array that should be sorted
    sort_by: str. Method by which the arrays should be sorted. There are 3 possible values:
        1. 'na': Keep the arrays as-is, no sorting takes place.
        2. 'value': Reorder both arrays such that the array `values` is sorted in ascending order.
        3. 'label': Reorder both arrays such that the array `labels` is sorted in ascending order.

    Returns:
    -----------
    ndarray. shape=(num_levels,). Sorted `values` array. Corresponding values in `labels` remain matched up.
    ndarray. shape=(num_levels,). Sorted `labels` array. Corresponding values in `values` remain matched up.


    NOTE:
    - np.argsort might be helpful here.
    '''
    if sort_by == 'value':
        sort = np.argsort(values)
        sortValues = values[sort]
        sortLabels = labels[sort]

    elif sort_by == 'label':
        sort = np.argsort(labels)
        sortValues = values[sort]
        sortLabels = labels[sort]

    else:
        sortValues = values
        sortLabels = labels
    
    return sortValues, sortLabels


def grouped_sidebarplot(values, header1_labels, header2_levels, title, figsize=(6, 7)):
    '''Horizontal side-by-side bar plot with bar lengths `values` (the "x values") with associated labels.
    `header1_labels` are the levels of `header`, which appear on the y axis. Each level applies to ONE group of bars next
    to each other. `header2_labels` are the levels that appear in the legend and correspond to different color bars.

    POSSIBLE EXTENTION. NOT REQUIRED FOR BASE PROJECT

    (Useful for plotting numeric values associated with combinations of two categorical variables header1 and header2)

    Parameters:
    -----------
    values: ndarray. shape=(num_levels). Each numeric value to plot as a separate horizontal bar coming out of the y axis.
    labels: list of str. len=num_labels. Labels associated with each bar / numeric value in `values`.
    title: str. Title of the plot.
    show_counts: bool. Whether to show each numeric value as text next to each bar.
    fig_sz: tuple of 2 ints. The width and height of the figure.

    Example:
    -----------
    header1_labels = ['2020', '2021']
    header2_labels = ['Red', 'Green', 'Blue']
    The side-by-side bar plot looks like:

    '2021' 'Red'  ----------
     y=2   'Green'------
           'Blue' ----------------

    '2020' 'Red'  -------------------
     y=1   'Green'-------------------
           'Blue' ---------

    In the above example, the colors also describe the actual colors of the bars.

    NOTE:
    - You can use plt.barh, but there are offset to compute between the bars...
    '''
    fig, ax = plt.subplots(figsize=figsize)
    num_header1_levels, num_header2_levels = values.shape

    bar_width = 0.2
    index = np.arange(num_header2_levels)

    # Create bars for each header1 level
    for i, label in enumerate(header1_labels):
        bar_position = index + i * bar_width
        ax.barh(bar_position, values[i], height=bar_width, label=label)

    ax.set_yticks(index + (bar_width * (num_header1_levels - 1)) / 2)
    ax.set_yticklabels(header2_levels)

    ax.set_xlabel('Values')
    ax.set_title(title)
    ax.legend(title='Header 1 Labels', loc='upper right')

    plt.show()