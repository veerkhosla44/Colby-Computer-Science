'''mlp.py
Constructs, trains, tests 2 layer multilayer layer perceptron networks
Veer Khosla and Saad Khan
CS 343: Neural Networks
Fall 2024
Project 2: Multilayer Perceptrons
'''
import numpy as np


class MLP:
    '''MLP is a class for multilayer perceptron network.

    The structure of our MLP will be:

    Input layer (X units) ->
    Hidden layer (Y units) with Rectified Linear activation (ReLu) ->
    Output layer (Z units) with softmax activation

    Due to the softmax, activation of output neuron i represents the probability that the current input sample belongs
    to class i.
    '''
    def __init__(self, num_input_units, num_hidden_units, num_output_units):
        '''Constructor to build the model structure and intialize the weights. There are 3 layers:
        input layer, hidden layer, and output layer. Since the input layer represents each input
        sample, we don't learn weights for it.

        Parameters:
        -----------
        num_input_units: int. Num input features
        num_hidden_units: int. Num hidden units
        num_output_units: int. Num output units. Equal to # data classes.
        '''
        self.num_input_units = num_input_units
        self.num_hidden_units = num_hidden_units
        self.num_output_units = num_output_units

        self.initialize_wts(num_input_units, num_hidden_units, num_output_units)

    def get_y_wts(self):
        '''Returns a copy of the hidden layer wts'''
        return self.y_wts.copy()

    def initialize_wts(self, M, H, C, std=0.1, r_seed=None):
        ''' Randomly initialize the hidden and output layer weights and bias term

        Parameters:
        -----------
        M: int. Num input features
        H: int. Num hidden units
        C: int. Num output units. Equal to # data classes.
        std: float. Standard deviation of the normal distribution of weights
        r_seed: None or int. Random seed for weight and bias initialization.

        Returns:
        -----------
        No return

        TODO:
        - Initialize self.y_wts, self.y_b and self.z_wts, self.z_b
        with the appropriate size according to the normal distribution with standard deviation
        `std` and mean of 0. For consistency with the test code, initialize the parameters in the following order:
                self.y_wts
                self.y_b
                self.z_wts
                self.z_b
          - For wt shapes, they should be be equal to (#prev layer units, #associated layer units)
            for example: self.y_wts has shape (M, H)
          - For bias shapes, they should equal the number of units in the associated layer.
            for example: self.y_b has shape (H,)
        '''
        rng = np.random.default_rng(seed=0)
        
        self.y_wts = rng.normal(loc=0, scale=std, size=(M, H))
        self.y_b = rng.normal(loc=0, scale=std, size=H)
        self.z_wts = rng.normal(loc=0, scale=std, size=(H, C))
        self.z_b = rng.normal(loc=0, scale=std, size=C)



    def accuracy(self, y, y_pred):
        '''Computes the accuracy of classified samples. Proportion correct

        Parameters:
        -----------
        y: ndarray. int-coded true classes. shape=(Num samps,)
        y_pred: ndarray. int-coded predicted classes by the network. shape=(Num samps,)

        Returns:
        -----------
        float. accuracy in range [0, 1]
        '''
        return np.sum(y == y_pred)/y.size

    def one_hot(self, y, num_classes):
        '''One-hot codes the output classes for a mini-batch

        Parameters:
        -----------
        y: ndarray. int-coded class assignments of training mini-batch. 0,...,numClasses-1
        num_classes: int. Number of unique output classes total

        Returns:
        -----------
        y_one_hot: One-hot coded class assignments.
            e.g. if y = [0, 2, 1] and num_classes = 4 we have:
            [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
        '''
        y_one_hot = np.zeros((y.shape[0], num_classes))
        i = 0
        for ing in y.astype(int):  
            y_one_hot[i,ing] = 1
            i+=1
        
        return y_one_hot
    
    def predict(self, features):
        '''Predicts the int-coded class value for network inputs ('features').

        NOTE: Loops of any kind are NOT ALLOWED in this method!

        Parameters:
        -----------
        features: ndarray. shape=(mini-batch size, num features)

        Returns:
        -----------
        y_pred: ndarray. shape=(mini-batch size,).
            This is the int-coded predicted class values for the inputs passed in.
            NOTE: You can figure out the predicted class assignments without applying the
            softmax net activation function — it will not affect the most active neuron.
        '''
        # Calculate the input to the hidden layer
        y_net_in = np.dot(features, self.y_wts) + self.y_b

        # Apply ReLU activation function
        y_net_act = np.maximum(0, y_net_in)

        # Calculate the input to the output layer
        z_net_in = np.dot(y_net_act, self.z_wts) + self.z_b

        # Predict the class labels
        y_pred = np.argmax(z_net_in, axis=1)

        # Return the predicted labels
        return y_pred



    def forward(self, features, y, reg=0):
        '''Performs a forward pass of the net (input -> hidden -> output).
        This should start with the features and progate the activity to the output layer, ending with the cross-entropy
        loss computation.

        Don't forget to add the regularization to the loss!

        NOTE: Implement all forward computations within this function
        (don't divide up into separate functions for net_in, net_act). Doing this all in one method is not good design,
        but as you will discover, having the forward computations (y_net_in, y_net_act, etc) easily accessible in one
        place makes the backward pass a lot easier to track during implementation. In future projects, we will rely on
        better OO design.

        NOTE: Loops of any kind are NOT ALLOWED in this method!

        Parameters:
        -----------
        features: ndarray. net inputs. shape=(mini-batch-size N, Num features M)
        y: ndarray. int coded class labels. shape=(mini-batch-size N,)
        reg: float. regularization strength.

        Returns:
        -----------
        y_net_in: ndarray. shape=(N, H). hidden layer "net in"
        y_net_act: ndarray. shape=(N, H). hidden layer activation
        z_net_in: ndarray. shape=(N, C). output layer "net in"
        z_net_act: ndarray. shape=(N, C). output layer activation
        loss: float. REGULARIZED loss derived from output layer, averaged over all input samples

        NOTE:
        - To regularize loss for multiple layers, you add the usual regularization to the loss
          from each set of weights (i.e. 2 in this case).
        '''
        # Calculate the input to the hidden layer
        y_net_in = np.dot(features, self.y_wts) + self.y_b

        # Apply ReLU activation function (rectified linear unit)
        y_net_act = np.maximum(0, y_net_in)

        # Calculate the input to the output layer
        z_net_in = np.dot(y_net_act, self.z_wts) + self.z_b

        # Apply the softmax function for the output layer activation
        exp_values = np.exp(z_net_in - np.max(z_net_in, axis=1, keepdims=True))  # Stability improvement
        z_net_act = exp_values / np.sum(exp_values, axis=1, keepdims=True)

        # Compute the regularized loss
        N = y.shape[0]
        correct_log_probs = -np.log(z_net_act[range(N), y])
        data_loss = np.sum(correct_log_probs) / N
        reg_loss = 0.5 * reg * (np.sum(self.z_wts ** 2) + np.sum(self.y_wts ** 2))
        loss = data_loss + reg_loss

        return y_net_in, y_net_act, z_net_in, z_net_act, loss

    def backward(self, features, y, y_net_in, y_net_act, z_net_in, z_net_act, reg=0):
        '''Performs a backward pass (output -> hidden -> input) during training to update the weights. This function
        implements the backpropogation algorithm.

        This should start with the loss and progate the activity backwards through the net to the input-hidden weights.

        I added dz_net_act for you to start with, which is your cross-entropy loss gradient.
        Next, tackle dz_net_in, dz_wts and so on.

        I suggest numbering your forward flow equations and process each for relevant gradients in reverse order until
        you hit the first set of weights.

        Don't forget to backpropogate the regularization to the weights! (I suggest worrying about this last)

        Parameters:
        -----------
        features: ndarray. net inputs. shape=(mini-batch-size, Num features)
        y: ndarray. int coded class labels. shape=(mini-batch-size,)
        y_net_in: ndarray. shape=(N, H). hidden layer "net in"
        y_net_act: ndarray. shape=(N, H). hidden layer activation
        z_net_in: ndarray. shape=(N, C). output layer "net in"
        z_net_act: ndarray. shape=(N, C). output layer activation
        reg: float. regularization strength.

        Returns:
        -----------
        dy_wts, dy_b, dz_wts, dz_b: The following backwards gradients
        (1) hidden wts, (2) hidden bias, (3) output weights, (4) output bias
        Shapes should match the respective wt/bias instance vars.

        NOTE:
        - Regularize each layer's weights like usual.
        '''
        N = features.shape[0]  # Number of samples in the mini-batch

        # One-hot encode the true labels
        y_one_hot = self.one_hot(y, z_net_act.shape[1])

        # Output layer gradients
        dz_net_act = (z_net_act - y_one_hot) / N  # Cross-entropy loss gradient
        dz_wts = np.dot(y_net_act.T, dz_net_act) + reg * self.z_wts  # Regularize output weights
        dz_b = np.sum(dz_net_act, axis=0)

        # Backpropagate to the hidden layer
        dy_net_act = np.dot(dz_net_act, self.z_wts.T)
        dy_net_in = dy_net_act * (y_net_in > 0)  # ReLU derivative

        # Hidden layer gradients
        dy_wts = np.dot(features.T, dy_net_in) + reg * self.y_wts  # Regularize hidden weights
        dy_b = np.sum(dy_net_in, axis=0)

        return dy_wts, dy_b, dz_wts, dz_b

    def fit(self, features, y, x_validation, y_validation, n_epochs=500, lr=0.0001, mini_batch_sz=256, reg=0,
            r_seed=None, verbose=2, print_every=100):
        '''Trains the network to data in `features` belonging to the int-coded classes `y`.
        Implements stochastic mini-batch gradient descent

        Changes from `fit` in `SoftmaxLayer`:
        -------------------------------------
        1. Record accuracy on the validation set (`x_validation`, `y_validation`) after each epoch training.
        2. Record accuracy on training set after each epoch training.

        (see note below for more details)

        Parameters:
        -----------
        features: ndarray. shape=(Num samples N, num features).
            Features over N inputs.
        y: ndarray.
            int-coded class assignments of training samples. 0,...,numClasses-1
        x_validation: ndarray. shape=(Num samples in validation set, num features).
            This is used for computing/printing the accuracy on the validation set at the end of each epoch.
        y_validation: ndarray.
            int-coded class assignments of validation samples. 0,...,numClasses-1
        n_epochs: int.
            Number of training epochs
        lr: float.
            Learning rate
        mini_batch_sz: int.
            Batch size per epoch. i.e. How many samples we draw from features to pass through the model per training epoch
            before we do gradient descent and update the wts.
        reg: float.
            Regularization strength used when computing the loss and gradient.
        r_seed: None or int.
            Random seed for weight and bias initialization.
        verbose: int.
            0 means no print outs. Any value > 0 prints Current epoch number and training loss every
            `print_every` (e.g. 100) epochs.
        print_every: int.
            If verbose > 0, print out the training loss and validation accuracy over the last epoch
            every `print_every` epochs.
            Example: If there are 20 epochs and `print_every` = 5 then you print-outs happen on
            after completing epochs 0, 5, 10, and 15 (or 1, 6, 11, and 16 if counting from 1).

        Returns:
        -----------
        loss_history: Python list of floats. len=`n_epochs * n_iter_per_epoch`.
            Recorded training loss for each mini-batch of training.
        train_acc_history: Python list of floats. len=`n_epochs`.
            Recorded accuracy on every epoch on the training set.
        validation_acc_history: Python list of floats. len=`n_epochs`.
            Recorded accuracy on every epoch on the validation set.

        NOTE:
        The flow of this method should follow the one that you wrote in `SoftmaxLayer`. The main differences are:
        0) Remember to update weights and biases for ALL layers!
        1) Record the accuracy:
            - on training set: Compute it on the ENTIRE training set only after completing an epoch.
            - on validation set: Compute it on the ENTIRE validation set only after completing an epoch.
        2) As in `SoftmaxLayer`, loss on training set should be recorded for each mini-batch of training.
        3) Every `print_every` epochs, print out (if `verbose` is `True`):
        '''
        if r_seed is not None:
            np.random.seed(r_seed)

        loss_history = []
        train_acc_history = []
        validation_acc_history = []

        N = features.shape[0]  # Total number of training samples

        for epoch in range(n_epochs):
            # Shuffle the training data
            indices = np.arange(N)
            np.random.shuffle(indices)
            features = features[indices]
            y = y[indices]

            # Mini-batch gradient descent
            for start_idx in range(0, N, mini_batch_sz):
                end_idx = min(start_idx + mini_batch_sz, N)
                batch_features = features[start_idx:end_idx]
                batch_y = y[start_idx:end_idx]

                # Forward pass
                y_net_in, y_net_act, z_net_in, z_net_act, loss = self.forward(batch_features, batch_y, reg)
                loss_history.append(loss)

                # Backward pass
                dy_wts, dy_b, dz_wts, dz_b = self.backward(batch_features, batch_y, y_net_in, y_net_act, z_net_in, z_net_act, reg)

                # Update weights and biases
                self.y_wts -= lr * dy_wts
                self.y_b -= lr * dy_b
                self.z_wts -= lr * dz_wts
                self.z_b -= lr * dz_b

            # Compute accuracy on the training set
            train_accuracy = self.accuracy(y, self.predict(features))
            train_acc_history.append(train_accuracy)

            # Compute accuracy on the validation set
            validation_accuracy = self.accuracy(y_validation, self.predict(x_validation))
            validation_acc_history.append(validation_accuracy)

            # Print progress
            if verbose > 0 and (epoch % print_every == 0 or epoch == n_epochs - 1):
                print(f"Epoch {epoch + 1}/{n_epochs}, Loss: {loss:.4f}, Training Accuracy: {train_accuracy:.4f}, Validation Accuracy: {validation_accuracy:.4f}")

        return loss_history, train_acc_history, validation_acc_history

