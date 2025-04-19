'''knn.py
K-Nearest Neighbors algorithm for classification
Veer Khosla
CS 251: Data Analysis and Visualization
Fall 2023
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd


class KNN:
    '''K-Nearest Neighbors supervised learning algorithm'''
    def __init__(self, num_classes):
        '''KNN constructor

        TODO:
        - Add instance variable for `num_classes`
        '''
        self.num_classes = num_classes

        # exemplars: ndarray. shape=(num_train_samps, num_features).
        #   Memorized training examples
        self.exemplars = None
        # classes: ndarray. shape=(num_train_samps,).
        #   Classes of memorized training examples
        self.classes = None

    def train(self, data, y):
        '''Train the KNN classifier on the data `data`, where training samples have corresponding
        class labels in `y`.

        Parameters:
        -----------
        data: ndarray. shape=(num_train_samps, num_features). Data to learn / train on.
        y: ndarray. shape=(num_train_samps,). Corresponding class of each data sample.

        TODO:
        - Set the `exemplars` and `classes` instance variables such that the classifier memorizes
        the training data.
        '''
        self.exemplars = data
        self.classes = y

    def predict(self, data, k):
        '''Use the trained KNN classifier to predict the class label of each test sample in `data`.
        Determine class by voting: find the closest `k` training exemplars (training samples) and
        the class is the majority vote of the classes of these training exemplars.

        Parameters:
        -----------
        data: ndarray. shape=(num_test_samps, num_features). Data to predict the class of
            Need not be the data used to train the network.
        k: int. Determines the neighborhood size of training points around each test sample used to
            make class predictions. In other words, how many training samples vote to determine the
            predicted class of a nearby test sample.

        Returns:
        -----------
        ndarray of nonnegative ints. shape=(num_test_samps,). Predicted class of each test data
        sample.

        TODO:
        - Compute the distance from each test sample to all the training exemplars.
        - Among the closest `k` training exemplars to each test sample, count up how many belong
        to which class.
        - The predicted class of the test sample is the majority vote.
        '''
        num_test_samps = data.shape[0] if isinstance(data, np.ndarray) else data.shape[0]
        predicted_classes = np.zeros(num_test_samps, dtype=int)

        data_array = data.to_numpy() if isinstance(data, pd.DataFrame) else data

        for i in range(num_test_samps):
            distances = np.sqrt(np.sum((self.exemplars - data_array[i])**2, axis=1))
            closest_indices = np.argsort(distances)[:k]
            class_counts = np.zeros(self.num_classes, dtype=int)
            for j in range(k):
                class_counts[int(self.classes[closest_indices[j]])] += 1
            max_count = -1
            max_class = -1
            for j in range(self.num_classes):
                if class_counts[j] > max_count:
                    max_count = class_counts[j]
                    max_class = j

            predicted_classes[i] = max_class

        return predicted_classes

    def accuracy(self, y, y_pred):
        '''Computes accuracy based on percent correct: Proportion of predicted class labels `y_pred`
        that match the true values `y`.

        Parameters:
        -----------
        y: ndarray. shape=(num_data_sams,)
            Ground-truth, known class labels for each data sample
        y_pred: ndarray. shape=(num_data_sams,)
            Predicted class labels by the model for each data sample

        Returns:
        -----------
        float. Between 0 and 1. Proportion correct classification.

        NOTE: Can be done without any loops
        '''
        num_correct = np.sum(y == y_pred)
        total_samples = y.shape[0]
        accuracy = num_correct / total_samples

        return accuracy
    
    def plot_predictions(self, k, n_sample_pts):
        '''Paints the data space in colors corresponding to which class the classifier would
         hypothetically assign to data samples appearing in each region.

        Parameters:
        -----------
        k: int. Determines the neighborhood size of training points around each test sample used to
            make class predictions. In other words, how many training samples vote to determine the
            predicted class of a nearby test sample.
        n_sample_pts: int.
            How many points to divide up the input data space into along the x and y axes to plug
            into KNN at which we are determining the predicted class. Think of this as regularly
            spaced 2D "fake data" that we generate and plug into KNN and get predictions at.

        TODO:
        - Pick a discrete/qualitative color scheme. We suggest, like in the clustering project, to
        use either the Okabe & Ito or one of the Petroff color palettes: https://github.com/proplot-dev/proplot/issues/424
        - Wrap your colors list as a `ListedColormap` object (already imported above) so that matplotlib can parse it.
        - Make an ndarray of length `n_sample_pts` of regularly spaced points between -40 and +40.
        - Call `np.meshgrid` on your sampling vector to get the x and y coordinates of your 2D
        "fake data" sample points in the square region from [-40, 40] to [40, 40].
            - Example: x, y = np.meshgrid(samp_vec, samp_vec)
        - Combine your `x` and `y` sample coordinates into a single ndarray and reshape it so that
        you can plug it in as your `data` in self.predict.
            - Shape of `x` should be (n_sample_pts, n_sample_pts). You want to make your input to
            self.predict of shape=(n_sample_pts*n_sample_pts, 2).
        - Reshape the predicted classes (`y_pred`) in a square grid format for plotting in 2D.
        shape=(n_sample_pts, n_sample_pts).
        - Use the `plt.pcolormesh` function to create your plot. Use the `cmap` optional parameter
        to specify your discrete ColorBrewer color palette.
        - Add a colorbar to your plot
        '''
        cmap = ListedColormap(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

        x_vals = np.linspace(-40, 40, n_sample_pts)
        y_vals = np.linspace(-40, 40, n_sample_pts)
        x, y = np.meshgrid(x_vals, y_vals)

        sample_points = np.column_stack((x.flatten(), y.flatten()))

        predictions = self.predict(sample_points, k)
        predictions = predictions.reshape((n_sample_pts, n_sample_pts))

        plt.figure(figsize=(8, 8))
        plt.pcolormesh(x, y, predictions, cmap=cmap, shading='auto')

        cbar = plt.colorbar()
        cbar.set_ticks(np.arange(0.5, self.num_classes, 1))
        cbar.set_ticklabels(np.arange(self.num_classes))

        plt.title(f'Class Boundaries for K={k}')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()

    def confusion_matrix(self, y, y_pred):
        '''Create a confusion matrix based on the ground truth class labels (`y`) and those predicted
        by the classifier (`y_pred`).

        Parameters:
        -----------
        y: ndarray. shape=(num_data_samps,)
            Ground-truth, known class labels for each data sample
        y_pred: ndarray. shape=(num_data_samps,)
            Predicted class labels by the model for each data sample

        Returns:
        -----------
        ndarray. shape=(num_classes, num_classes).
            Confusion matrix
        '''
        num_classes = self.num_classes
        confusion_matrix = np.zeros((num_classes, num_classes))
        
        for i in range(num_classes):
            for j in range(num_classes):
                confusion_matrix[i, j] = np.sum((y == i) & (y_pred == j))
        
        return confusion_matrix


