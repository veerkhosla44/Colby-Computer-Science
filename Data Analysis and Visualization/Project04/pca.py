'''pca.py
Performs principal component analysis using the covariance matrix of the dataset
Veer Khosla
CS 251: Data Analysis and Visualization
Fall 2023
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from data_transformations import normalize, center


class PCA:
    '''Perform and store principal component analysis results

    NOTE: In your implementations, only the following "high level" `scipy`/`numpy` functions can be used:
    - `np.linalg.eig`
    The numpy functions that you have been using so far are fine to use.
    '''

    def __init__(self, data):
        '''

        Parameters:
        -----------
        data: pandas DataFrame. shape=(num_samps, num_vars)
            Contains all the data samples and variables in a dataset. Should be set as an instance variable.
        '''
        self.data = data

        # vars: Python list. len(vars) = num_selected_vars
        #   String variable names selected from the DataFrame to run PCA on.
        #   num_selected_vars <= num_vars
        self.vars = None

        # A: ndarray. shape=(num_samps, num_selected_vars)
        #   Matrix of data selected for PCA
        self.A = None

        # normalized: boolean.
        #   Whether data matrix (A) is normalized by self.pca
        self.normalized = None

        # A_proj: ndarray. shape=(num_samps, num_pcs_to_keep)
        #   Matrix of PCA projected data
        self.A_proj = None

        # e_vals: ndarray. shape=(num_pcs,)
        #   Full set of eigenvalues (ordered large-to-small)
        self.e_vals = None
        # e_vecs: ndarray. shape=(num_selected_vars, num_pcs)
        #   Full set of eigenvectors, corresponding to eigenvalues ordered large-to-small
        self.e_vecs = None

        # prop_var: Python list. len(prop_var) = num_pcs
        #   Proportion variance accounted for by the PCs (ordered large-to-small)
        self.prop_var = None

        # cum_var: Python list. len(cum_var) = num_pcs
        #   Cumulative proportion variance accounted for by the PCs (ordered large-to-small)
        self.cum_var = []

        # orig_means: ndarray. shape=(num_selected_vars,)
        #   Means of each orignal data variable
        self.orig_means = None

        # orig_mins: ndarray. shape=(num_selected_vars,)
        #   Mins of each orignal data variable
        self.orig_mins = None

        # orig_maxs: ndarray. shape=(num_selected_vars,)
        #   Maxs of each orignal data variable
        self.orig_maxs = None

    def get_prop_var(self):
        '''(No changes should be needed)'''
        return self.prop_var

    def get_cum_var(self):
        '''(No changes should be needed)'''
        return self.cum_var

    def get_eigenvalues(self):
        '''(No changes should be needed)'''
        return self.e_vals

    def get_eigenvectors(self):
        '''(No changes should be needed)'''
        return self.e_vecs

    def covariance_matrix(self, data):
        '''Computes the covariance matrix of `data`

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_vars)
            `data` is NOT centered coming in, you should do that here.

        Returns:
        -----------
        ndarray. shape=(num_vars, num_vars)
            The covariance matrix of centered `data`

        NOTE: You should do this wihout any loops
        NOTE: np.cov is off-limits here — compute it from "scratch"!
        '''
        mean_data = np.mean(data, axis=0)
        centered_data = data - mean_data

        cov_matrix = np.dot(centered_data.T, centered_data) / (data.shape[0] - 1)

        return cov_matrix

    def compute_prop_var(self, e_vals):
        '''Computes the proportion variance accounted for by the principal components (PCs).

        Parameters:
        -----------
        e_vals: ndarray. shape=(num_pcs,)

        Returns:
        -----------
        Python list. len = num_pcs
            Proportion variance accounted for by the PCs
        '''
        total_var = np.sum(e_vals)
        prop_var = e_vals / total_var

        return prop_var

    def compute_cum_var(self, prop_var):
        '''Computes the cumulative variance accounted for by the principal components (PCs).

        Parameters:
        -----------
        prop_var: Python list. len(prop_var) = num_pcs
            Proportion variance accounted for by the PCs, ordered largest-to-smallest
            [Output of self.compute_prop_var()]

        Returns:
        -----------
        Python list. len = num_pcs
            Cumulative variance accounted for by the PCs
        '''
        cum_var = [np.sum(prop_var[:i+1]) for i in range(len(prop_var))]
        return cum_var
        

    def pca(self, vars, normalize_dataset=False):
        '''Performs PCA on the data variables `vars`

        Parameters:
        -----------
        vars: Python list of strings. len(vars) = num_selected_vars
            1+ variable names selected to perform PCA on.
            Variable names must match those used in the `self.data` DataFrame.
        normalize_dataset: boolean.
            If True, min-max normalize each data variable it ranges from 0 to 1.

        NOTE: Leverage other methods in this class as much as possible to do computations.

        TODO:
        - Select the relevant data (corresponding to `vars`) from the data pandas DataFrame
        then convert to numpy ndarray for forthcoming calculations.
        - If `normalize` is True, normalize the selected data so that each variable (column)
        ranges from 0 to 1 (i.e. normalize based on the dynamic range of each variable).
            - Before normalizing, create instance variables containing information that would be
            needed to "undo" or reverse the normalization on the selected data.
        - Make sure to compute everything needed to set all instance variables defined in constructor,
        except for self.A_proj (this will happen later).
        '''

        # col_indices = [self.vars.index(col) for col in vars]
        
        # selected_data = self.A[:, col_indices]
        
        # self.vars = vars
        # self.A = selected_data

        # if normalize_dataset:
        #     self.orig_maxs = np.max(self.A, axis=0)
        #     self.orig_mins = np.min(self.A, axis=0)
        #     self.orig_means = np.mean(self.A, axis=0)
        #     self.A = (self.A - self.orig_mins) / (self.orig_maxs - self.orig_mins)

        # self.A = center(self.A)
        # cov_matrix = self.covariance_matrix(self.A)
        # self.e_vals, self.e_vecs = np.linalg.eig(cov_matrix)

        # sort_order = np.argsort(self.e_vals)[::-1]
        # self.e_vals = self.e_vals[sort_order]
        # self.e_vecs = self.e_vecs[:, sort_order]

        # self.prop_var = self.compute_prop_var(self.e_vals)
        # self.cum_var = self.compute_cum_var(self.prop_var)

        # self.cum_var = np.array(self.cum_var)

        self.vars = vars
        selected_data = self.data[vars].values

        if normalize:
            max_vals = np.max(selected_data, axis=0)
            min_vals = np.min(selected_data, axis=0)
            dynamic_range = max_vals - min_vals
            normalized_data = (selected_data - min_vals) / dynamic_range
            self.max_vals = max_vals
            self.min_vals = min_vals
            self.dynamic_range = dynamic_range
            self.normalized = True
            self.A = normalized_data
        else:
            self.normalized = False
            self.A = selected_data

        cov_matrix = self.covariance_matrix(self.A)
        e_vals, e_vecs = np.linalg.eig(cov_matrix)
        sorted_indices = np.argsort(e_vals)[::-1]
        sorted_e_vals = e_vals[sorted_indices]
        sorted_e_vecs = e_vecs[:, sorted_indices]

        self.e_vals = sorted_e_vals
        self.e_vecs = sorted_e_vecs

        self.prop_var = self.compute_prop_var(self.e_vals)
        self.cum_var = self.compute_cum_var(self.prop_var)


        

    def pca_all_vars(self, normalize_dataset=False):
        '''
        Perform PCA on all data variables

        Parameters:
        -----------
        normalize_dataset: boolean.
            If True, min-max normalize each data variable so it ranges from 0 to 1.
        '''
        self.pca(vars=self.data.columns.tolist(), normalize_dataset=normalize_dataset)

    def elbow_plot(self, num_pcs_to_keep=None):
        '''Plots a curve of the cumulative variance accounted for by the top `num_pcs_to_keep` PCs.
        x axis corresponds to top PCs included (large-to-small order)
        y axis corresponds to proportion variance accounted for

        Parameters:
        -----------
        num_pcs_to_keep: int. Show the variance accounted for by this many top PCs.
            If num_pcs_to_keep is None, show variance accounted for by ALL the PCs (the default).

        NOTE: Make plot markers at each point. Enlarge them so that they look obvious.
        NOTE: Reminder to create useful x and y axis labels.
        NOTE: Don't write plt.show() in this method
        '''
        if self.cum_var is None:
            raise ValueError('Cant plot cumulative variance. Compute the PCA first.')

        if num_pcs_to_keep is None:
            num_pcs_to_keep = len(self.e_vals)

        plt.plot(range(1, num_pcs_to_keep + 1), self.cum_var[:num_pcs_to_keep], marker='o', markersize=6)
        plt.xlabel('Number of Principal Components')
        plt.ylabel('Cumulative Variance Explained')

    def pca_project(self, pcs_to_keep):
        '''Project the data onto `pcs_to_keep` PCs (not necessarily contiguous)

        Parameters:
        -----------
        pcs_to_keep: Python list of ints. len(pcs_to_keep) = num_pcs_to_keep
            Project the data onto these PCs.
            NOTE: This LIST contains indices of PCs to project the data onto, they are NOT necessarily
            contiguous.
            Example 1: [0, 2] would mean project on the 1st and 3rd largest PCs.
            Example 2: [0, 1] would mean project on the two largest PCs.

        Returns
        -----------
        pca_proj: ndarray. shape=(num_samps, num_pcs_to_keep).
            e.g. if pcs_to_keep = [0, 1],
            then pca_proj[:, 0] are x values, pca_proj[:, 1] are y values.

        NOTE: This method should set the variable `self.A_proj`
        '''

        selected_e_vecs = self.e_vecs[:, pcs_to_keep]
        pca_proj = self.A @ selected_e_vecs
        self.A_proj = pca_proj

        return pca_proj

    def pca_then_project_back(self, data, top_k):
        '''Project the data into PCA space (on `top_k` PCs) then project it back to the data space

        (Week 2)

        Parameters:
        -----------
        top_k: int. Project the data onto this many top PCs.

        Returns:
        -----------
        ndarray. shape=(num_samps, num_selected_vars)

        TODO:
        - Project the data on the `top_k` PCs (assume PCA has already been performed).
        - Project this PCA-transformed data back to the original data space
        - If you normalized, remember to rescale the data projected back to the original data space.
        '''
        selected_e_vecs = self.e_vecs[:, :top_k]
        pca_proj = self.A @ selected_e_vecs
        data_proj = pca_proj @ selected_e_vecs.T

        if self.normalized == True:
            data_proj = (data_proj * self.dynamic_range) + self.min_vals

        return data_proj

    def loading_plot(self):
        '''Create a loading plot of the top 2 PC eigenvectors

        (Week 2)

        TODO:
        - Plot a line joining the origin (0, 0) and corresponding components of the top 2 PC eigenvectors.
            Example: If e_0 = [0.1, 0.3] and e_1 = [1.0, 2.0], you would create two lines to join
            (0, 0) and (0.1, 1.0); (0, 0) and (0.3, 2.0).
            Number of lines = num_vars
        - Use plt.annotate to label each line by the variable that it corresponds to.
        - Reminder to create useful x and y axis labels.
        '''
        if self.e_vecs is None:
            raise ValueError('Principal components not available. Run PCA first.')

        num_vars = self.A.shape[1]
        
        # Limit the loop to the number of principal components (2)
        num_pcs = min(2, num_vars)
        
        top_pcs = self.e_vecs[:, :num_pcs]

        plt.figure(figsize=(10, 6))
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        for i in range(num_pcs):
            # Plot a line from (0, 0) to the corresponding components of the top 2 PC eigenvectors
            plt.plot([0, top_pcs[0, i]], [0, top_pcs[1, i]], label=f'Variable {i + 1}', marker='o', markersize=8)

        for i in range(num_pcs):
            # Annotate each line with the variable label
            plt.annotate(f'Variable {i + 1}', (top_pcs[0, i], top_pcs[1, i]), fontsize=12)

        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.legend()
        plt.title('Loading Plot: Top 2 Principal Components vs. Variables')
        plt.grid(True)
        plt.show()


    def accounted_variance(self, selected_variance):
        if self.cum_var is None:
            return None

        for i, var in enumerate(self.cum_var):
            if var >= selected_variance:
                return i + 1

        return None