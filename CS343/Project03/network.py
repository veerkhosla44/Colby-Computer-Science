'''network.py
Represents  a neural network (collection of layers)
Saad Khan and Veer Khosla
CS343: Neural Networks
Project 3: Convolutional Neural Networks
'''
import time
import numpy as np

import layer
import filter_ops
import accelerated_layer


class Network:
    '''Represents a neural network with some number of layers of various types.
    To create a specific network, create a subclass (e.g. ConvNet4) then
    add layers to it. For this project, the focus will be on building the
    ConvNet4 network.
    '''
    def __init__(self, reg=0, verbose=True):
        '''Method is pre-filled for you (shouldn't require modification).'''
        # Python list of Layer object references that make up out network
        self.layers = []
        # Regularization strength
        self.reg = reg
        # Whether we want network-related debug/info print outs
        self.verbose = verbose

        # Python list of ints. These are the indices of layers in `self.layers`
        # that have network weights.
        self.wt_layer_inds = []

        # Indices of all dropout layers in the layers list
        self.dropout_layer_inds = []

        # Are we currently training?
        self.in_train_mode = False

        # As in former projects, Python list of loss, training/validation
        # accuracy during training recorded at some frequency (e.g. every epoch)
        self.loss_history = []
        self.train_acc_history = []
        self.validation_acc_history = []


    def is_training(self):
        '''Is the CNN currently training?

        Returns:
        --------
        bool. Whether net is training.
        '''
        pass

    def compile(self, optimizer_name, **kwargs):
        '''Tells each network layer how weights should be updated during backprop
        during training (e.g. stochastic gradient descent, adam, etc.)

        This method is pre-filled for you (shouldn't require modification).

        NOTE: This NEEDS to be called AFTER creating your ConvNet4 object,
        but BEFORE you call `fit()` to train the net (otherwise, how does your
        net know how to update the weights?).

        Parameters:
        ----------
        optimizer_name: string. Name of optimizer class to use to update wts.
            See optimizer::create_optimizer for specific ones supported.
        **kwargs: Any number of optional parameters that get passed to the
            optimizer of your choice. e.g. learning rate.
        '''
        # Only set an optimizer for each layer with weights
        for l in [self.layers[i] for i in self.wt_layer_inds]:
            l.compile(optimizer_name, **kwargs)

    def set_dropout_layers_mode(self, in_train_mode=False):
        '''Relays whether we are in training mode to dropout layers only.

        Parameters:
        -----------
        in_train_mode: bool.
            Are we currently training the net?

        TODO:
        1. Update the network's mode.
        2. Update each of the dropout layer's mode.
        '''
        
        self.in_train_mode = in_train_mode
        for ind in self.dropout_layer_inds:
            self.layers[ind].set_mode(in_train_mode)

        

    def forward(self, inputs, y):
        '''Do forward pass through whole network

        Parameters:
        ----------
        inputs: ndarray.
            Inputs coming into the input layer of the net. shape=(B, n_chans, img_y, img_x)
        y: ndarray.
            int-coded class assignments of training mini-batch. 0,...,numClasses-1 shape=(B,) for mini-batch size B.

        Returns:
        -------
        loss: float.
            REGULARIZED loss.

        TODO:
        1. Call the forward method of each layer in the network.
            Make the output of the previous layer the input to the next.
        2. Compute and get the loss from the LAST network layer.
        2. Compute and get the weight regularization via `self.wt_reg_reduce()` (implement this next)
        4. Return the sum of the loss and the regularization term.
        '''
        # Initialize the input for the first layer
        current_input = inputs

        # Call the forward method of each layer in the network
        for layer in self.layers:
            current_input = layer.forward(current_input)

        # Compute the loss from the last layer
        loss = self.layers[-1].loss(y) 

        # Compute the weight regularization term
        reg_term = self.wt_reg_reduce()

        # Return the sum of the loss and the regularization term
        return loss + reg_term
        
        

    def wt_reg_reduce(self):
        '''Computes the loss weight regularization for all network layers that have weights

        Returns:
        -------
        wt_reg: float. Regularization for weights from all layers across the network.

        NOTE: You only can compute regularization for layers with wts!
        Layer indicies with weights are maintained in `self.wt_layer_inds`.
        The network regularization `wt_reg` is simply the sum of all the regularization terms
        for each individual layer.
        '''
        wt_reg = 0
        for ind in self.wt_layer_inds:
            layer = self.layers[ind]
            wt_reg += 0.5 * layer.reg * np.sum(layer.wts ** 2)
        return wt_reg


    def backward(self, y):
        '''Initiates the backward pass through all the layers of the network.

        Parameters:
        ----------
        y: ndarray. int-coded class assignments of training mini-batch. 0,...,numClasses-1
            shape=(B,) for mini-batch size B.

        Returns:
        -------
        None

        TODO:
        1. Initialize d_upstream, d_wts, d_b to None.
        2. Loop through the network layers in REVERSE ORDER, calling the `Layer` backward method.
            Remember that the output of layer.backward() becomes the d_upstream to the next layer down.
            We don't care about d_wts, d_b in this method (computed/stored in Layer).
        '''
        d_upstream = None
        d_wts = None
        d_b = None

        for layer in reversed(self.layers):
            d_upstream,_,_ = layer.backward(d_upstream, y)
            

    def predict(self, inputs):
        '''Classifies novel inputs presented to the network using the current
        weights.

        Parameters:
        ----------
        inputs: ndarray. shape=shape=(num test samples, n_chans, img_y, img_x)
            This is test data.

        Returns:
        -------
        pred_classes: ndarray. shape=shape=(num test samples)
            Predicted classes (int coded) derived from the network.

        TODO:
        1. Do the forward pass thru the net.
        2. Before doing the forward pass, configure the dropout layers to operate in predict/test mode.
        3. Afer doing the forward pass, configure the dropout layers to operate in whatever mode they were at the start
        of this method.
        '''

        # Set dropout layers to predict mode
        dropout_mode = self.in_train_mode
        self.set_dropout_layers_mode(False)
        # Perform a forward pass through all layers
        # Do a forward sweep through the network
        prev_ins = inputs

        for l in self.layers:
            prev_ins = l.forward(prev_ins)
        #now we want to go to our output layer activations 
        #and see what classes they are for

        # Set dropout layers back to their original mode
        self.set_dropout_layers_mode(dropout_mode)

        output = self.layers[-1]
        activation = output.net_act
        pred_classes = np.argmax(activation, axis = 1)
        return pred_classes

    def accuracy(self, inputs, y, samp_sz=500, mini_batch_sz=15):
        '''Computes accuracy using current net on the inputs `inputs` with classes `y`.

        This method is pre-filled for you (shouldn't require modification).

        Parameters:
        ----------
        inputs: ndarray. shape=shape=(num samples, n_chans, img_y, img_x)
            We are testing the classification accuracy on these data.
        y: ndarray. int-coded class assignments of training mini-batch. 0,...,numClasses-1
            shape=(N,) for mini-batch size N.
        samp_sz: int. If the number of samples is bigger than this number,
            we take a random sample from `inputs` of this size. We do this to
            keep performance of this method reasonable.
        mini_batch_sz: Because it might be tricky to hold all the training
            instances in memory at once, process and evaluate the accuracy of
            samples from `input` in mini-batches. We merge the accuracy scores
            across batches so the result is no different than processing all at
            once.
        '''
        n_samps = len(inputs)

        # Do we subsample the input?
        if n_samps > samp_sz:
            rng = np.random.default_rng(0)
            subsamp_inds = rng.choice(n_samps, samp_sz)
            n_samps = samp_sz
            inputs = inputs[subsamp_inds]
            y = y[subsamp_inds]

        # How many mini-batches do we split the data into to test accuracy?
        n_batches = int(np.ceil(n_samps / mini_batch_sz))
        # Placeholder for our predicted class ints
        y_pred = np.zeros(len(inputs), dtype=np.int32)

        # Compute the accuracy through the `predict` method in batches.
        # Strategy is to use a 1D cursor `b` to extract a range of inputs to process (a mini-batch)
        for b in range(n_batches):
            low = b*mini_batch_sz
            high = b*mini_batch_sz+mini_batch_sz
            # Tolerate out-of-bounds as we reach the end of the num samples
            if high > n_samps:
                high = n_samps

            # Get the network predicted classes and put them in the right place
            y_pred[low:high] = self.predict(inputs[low:high])

        # Accuracy is the average proportion that the prediction matchs the true int class
        acc = np.mean(y_pred == y)

        return acc

    def fit(self, x_train, y_train, x_validate, y_validate, mini_batch_sz=256, n_epochs=1, acc_freq=10, print_every=50, verbose=False):
        '''Trains the neural network on data

        Parameters:
        ----------
        x_train: ndarray. shape=(num training samples, n_chans, img_y, img_x).
            Training data.
        y_train: ndarray. shape=(num training samples,).
            Training data classes, int coded.
        x_validate: ndarray. shape=(num validation samples, n_chans, img_y, img_x).
            Every so often during training (see acc_freq param), we compute
            the accuracy of the network in classifying the validation set
            (out-of-training-set generalization). This is the data we use.
        y_validate: ndarray. shape=(num validation samples,).
            Validation data classes, int coded.
        mini_batch_sz: int.
            Mini-batch training size.
        n_epochs: int.
            Number of training epochs.
        print_every: int.
            Controls the frequency (in iterations) with which to wait before printing out the loss
            and iteration number.
            NOTE: Previously, you used number of epochs rather than iterations to measure the frequency
            of print-outs. Use the simpler-to-implement units of iterations here because CNNs are
            more computationally intensive and you may want print-outs during an epoch.
        acc_freq: int. Should be equal to or a multiple of `print_every`.
            How many training iterations (weight updates) we wait before computing accuracy on the
            full training and validation sets?
            NOTE: This is is a computationally intensive process for the big network so make sure
            that you only COMPUTE training and validation accuracies this often
            (i.e DON'T compute them every iteration).

        Returns:
        --------
        self.loss_history: list.
            Record of training loss computed over each mini-batch of training for every epoch.
        self.train_acc_history. list.
            Record of accuracy on training set computed on entire training set computed every `acc_freq` training iters.
        self.validation_acc_history
            Record of accuracy on val set computed on val training set computed every `acc_freq` training iters.

        TODO: Complete this method's implementation.
        - It should follow the familar format for a training loop: Randomly sampling to get a mini-batch,
        doing the forward and backward pass, computing the loss, updating the wts/biases.
        - Add support for `print_every` and `acc_freq`.
        - Use the Python time module to print out the runtime (in minutes) for iteration 0 only.
        Also printout the projected time for completing ALL training iterations. (For simplicity, you don't need to
        consider the time taken for computing train and validation accuracy).
        - Remember to configure Dropout layer(s) appropriately: they should be in training mode while training and not
        in training mode when training is over.
        '''

        # Set dropout layers to training mode
        self.set_dropout_layers_mode(True)

        iterations = 0
        num_batch_loops = x_train.shape[0] // mini_batch_sz

        for epoch in range(n_epochs):
            for batch in range(num_batch_loops):
                start_time = time.time()

                rng = np.random.default_rng()

                # Get random batch
                samples = rng.integers(0, x_train.shape[0], mini_batch_sz)
                batch_X, batch_y = x_train[samples], y_train[samples]

                # Forward pass and loss calculation
                loss = self.forward(batch_X, batch_y)
                self.loss_history.append(loss)

                # Backward pass
                self.backward(batch_y)
                iterations += 1

                # Update weights for each layer
                for layer in self.layers:
                    layer.update_weights()

                # Print initial timing information
                if iterations == 1:
                    elapsed_time = time.time() - start_time
                    projected_time = (n_epochs * num_batch_loops * elapsed_time) / 60
                    print(f"Time for 0th iteration: {elapsed_time:.2f} seconds")
                    print(f"Projected time to finish: {projected_time:.2f} minutes")

                # Print progress at specified intervals
                if (iterations - 1) % print_every == 0:
                    print(f"Iteration {iterations - 1} ------- Loss: {self.loss_history[-1]:.4f}")

                # Check and print accuracy at specified intervals
                if (iterations - 1) % acc_freq == 0:
                    train_acc = self.accuracy(x_train, y_train)
                    val_acc = self.accuracy(x_validate, y_validate)
                    self.train_acc_history.append(train_acc)
                    self.validation_acc_history.append(val_acc)
                    print(f"Train accuracy: {train_acc:.4f}")
                    print(f"Validation accuracy: {val_acc:.4f}")

        # Print final results
        final_loss = self.loss_history[-1]
        final_train_acc = self.accuracy(x_train, y_train)
        print(f"Final loss: {final_loss:.4f}")
        print(f"Final train accuracy: {final_train_acc:.4f}")

        # Set dropout layers to predict mode
        self.set_dropout_layers_mode(False)


class ConvNet4(Network):
    '''A minimal convolutional neural network.
    Makes a ConvNet4 network with the following layers: Conv2D -> MaxPool2D -> Flatten -> Dense -> Dense

    0. Convolution (net-in), Relu (net-act).
    1. Max pool 2D (net-in), linear (net-act).
    2. Flatten (net-in), linear (net-act).
    3. Dense (net-in), Relu (net-act).
    4. Dense (net-in), soft-max (net-act).
    '''
    def __init__(self, input_shape=(3, 32, 32), n_kers=(32,), ker_sz=(7,), dense_interior_units=(100,),
                 pooling_sizes=(2,), pooling_strides=(2,), n_classes=10, wt_scale=1e-2, reg=0, r_seed=None,
                 verbose=False):
        '''ConvNet4 constructor. The job of this method is to build the network as a collection of connected layers
        (in order) in `self.layers`.

        Parameters:
        -----------
        input_shape: tuple. By default: (n_chans, img_y, img_x)
            Shape of a SINGLE input sample (no mini-batch).
        n_kers: tuple.
            Number of kernels/units in the 1st convolution layer. Format is (32,), which is a tuple rather than just an
            int. The reasoning is that if you wanted to create another Conv2D layer, say with 16 units, n_kers would
            then be (32, 16). Thus, this format easily allows us to make the net deeper.
        ker_sz: tuple.
            x/y size of each convolution filter. Format is (7,), which means make 7x7 filters in the FIRST Conv2D layer.
            If we had another Conv2D layer with filters size 5x5, it would be ker_sz=(7,5)
        dense_interior_units: tuple. Same format as above.
            Number of hidden units in each dense layer.
            NOTE: Does NOT include the output layer, which has # units = # classes.
        pooling_sizes: tuple.  Same format as above.
            Pooling extent in the i-th MaxPool2D layer.
        pooling_strides: tuple.  Same format as above.
            Pooling stride in the i-th MaxPool2D layer.
        n_classes: int.
            Number of classes in the input. This will become the number of units in the Output Dense layer.
        wt_scale: float.
            Global weight scaling to use for all layers with weights
        reg: float.
            Regularization strength
        r_seed: int or None.
            Random seed for setting weights and bias parameters.
        verbose: bool. Do we want to term network-related debug print outs on?
            NOTE: This is different than per-layer verbose settings, which are turned manually on below.

        NOTE:
        - Remember to define self.wt_layer_inds as the list indicies in self.layers that have weights.
        - Number your layers starting at 0.
        '''
        super().__init__(reg, verbose)
        
        self.layers = []
        
        self.layers.append(layer.Conv2D(number=0, name='Conv2D_1', n_kers=n_kers[0], ker_sz=ker_sz[0], wt_scale=wt_scale, activation='relu', verbose=verbose, r_seed=r_seed))
        
        self.layers.append(layer.MaxPool2D(number=1, name='MaxPool2D_1', pool_size=pooling_sizes[0], strides=pooling_strides[0], activation='linear', verbose=verbose))
        
        self.layers.append(layer.Flatten(number=2, name='Flatten_1', verbose=verbose))
        
        self.layers.append(layer.Dense(number=3, name='Dense_1', units=dense_interior_units[0], n_units_prev_layer=n_kers[0] * (input_shape[1] // pooling_strides[0]) * (input_shape[2] // pooling_strides[0]), wt_scale=wt_scale, activation='relu', verbose=verbose, r_seed=r_seed))
        
        self.layers.append(layer.Dense(number=4, name='Dense_2', units=n_classes, n_units_prev_layer=dense_interior_units[0], wt_scale=wt_scale, activation='softmax', verbose=verbose, r_seed=r_seed))
        
        self.wt_layer_inds = [0, 3, 4]

        






class ConvNet4Accel(Network):
    '''A ConvNet4 network with the following layers: Conv2D -> MaxPool2D -> Flatten -> Dense -> Dense.
    This has the same architecture as ConvNet4, but uses ACCELERATED versions of your network layers (where available).

    0. Convolution (net-in), Relu (net-act).
    1. Max pool 2D (net-in), linear (net-act).
    2. Flatten (net-in), linear (net-act).
    3. Dense (net-in), Relu (net-act).
    4. Dense (net-in), soft-max (net-act).
    '''
    def __init__(self, input_shape=(3, 32, 32), n_kers=(16,), ker_sz=(7,), dense_interior_units=(100,),
                 pooling_sizes=(2,), pooling_strides=(2,), n_classes=10, wt_scale=1e-2, reg=0.0, r_seed=None,
                 verbose=False):
        '''ConvNet4Accel constructor. The job of this method is to build the network as a collection of connected
        layers (in order) in `self.layers`.

        Parameters:
        -----------
        input_shape: tuple. By default: (n_chans, img_y, img_x)
            Shape of a SINGLE input sample (no mini-batch).
        n_kers: tuple.
            Number of kernels/units in the 1st convolution layer. Format is (32,), which is a tuple rather than just an
            int. The reasoning is that if you wanted to create another Conv2D layer, say with 16 units, n_kers would
            then be (32, 16). Thus, this format easily allows us to make the net deeper.
        ker_sz: tuple.
            x/y size of each convolution filter. Format is (7,), which means make 7x7 filters in the FIRST Conv2D layer.
            If we had another Conv2D layer with filters size 5x5, it would be ker_sz=(7,5)
        dense_interior_units: tuple. Same format as above.
            Number of hidden units in each dense layer.
            NOTE: Does NOT include the output layer, which has # units = # classes.
        pooling_sizes: tuple.  Same format as above.
            Pooling extent in the i-th MaxPool2D layer.
        pooling_strides: tuple.  Same format as above.
            Pooling stride in the i-th MaxPool2D layer.
        n_classes: int.
            Number of classes in the input. This will become the number of units in the Output Dense layer.
        wt_scale: float.
            Global weight scaling to use for all layers with weights
        reg: float.
            Regularization strength
        r_seed: int or None.
            Random seed for setting weights and bias parameters.
        verbose: bool. Do we want to term network-related debug print outs on?
            NOTE: This is different than per-layer verbose settings, which are turned manually on below.

        NOTE: This should be the same as your ConvNet4, except you should use accelerated layers (where available).
        '''
        super().__init__(reg, verbose)

        n_chans, h, w = input_shape
        
        self.layers = []
        
        self.layers.append(accelerated_layer.Conv2DAccel(number=0, name='Conv2D_1', n_kers=n_kers[0], ker_sz=ker_sz[0], wt_scale=wt_scale, activation='relu', verbose=verbose, r_seed=r_seed))
        
        self.layers.append(accelerated_layer.MaxPool2DAccel(number=1, name='MaxPool2D_1', pool_size=pooling_sizes[0], strides=pooling_strides[0], activation='linear', verbose=verbose))
        
        self.layers.append(layer.Flatten(number=2, name='Flatten_1', verbose=verbose))
        
        self.layers.append(layer.Dense(number=3, name='Dense_1', units=dense_interior_units[0], n_units_prev_layer=n_kers[0] * (input_shape[1] // pooling_strides[0]) * (input_shape[2] // pooling_strides[0]), wt_scale=wt_scale, activation='relu', verbose=verbose, r_seed=r_seed))
        
        self.layers.append(layer.Dense(number=4, name='Dense_2', units=n_classes, n_units_prev_layer=dense_interior_units[0], wt_scale=wt_scale, activation='softmax', verbose=verbose, r_seed=r_seed))
        
        self.wt_layer_inds = [0, 3, 4]

class ConvNet4AccelV2(Network):
    '''A ConvNet4 network with the following layers: Conv2D -> MaxPool2D -> Flatten -> Dense -> Dropout -> Dense.
    This has the same architecture as ConvNet4/ConvNet4Accel, but adds a Dropout layer before the output layer.

    0. Convolution (net-in), Relu (net-act).
    1. Max pool 2D (net-in), linear (net-act).
    2. Flatten (net-in), linear (net-act).
    3. Dense (net-in), Relu (net-act).
    4. Dropout (net-in), linear (net-act).
    5. Dense (net-in), soft-max (net-act).

    NOTE: Where available, the ACCELERATED versions of your network layers should be used in this network.
    '''
    def __init__(self, input_shape=(3, 32, 32), n_kers=(16,), ker_sz=(7,), dense_interior_units=(100,),
                 pooling_sizes=(2,), pooling_strides=(2,), n_classes=10, wt_scale=1e-2, reg=0.0, dropout_rate=0.0,
                 r_seed=None, verbose=False):
        '''ConvNet4AccelV2 constructor. The job of this method is to build the network as a collection of connected
        layers (in order) in `self.layers`.

        Parameters:
        -----------
        input_shape: tuple. By default: (n_chans, img_y, img_x)
            Shape of a SINGLE input sample (no mini-batch).
        n_kers: tuple.
            Number of kernels/units in the 1st convolution layer. Format is (32,), which is a tuple rather than just an
            int. The reasoning is that if you wanted to create another Conv2D layer, say with 16 units, n_kers would
            then be (32, 16). Thus, this format easily allows us to make the net deeper.
        ker_sz: tuple.
            x/y size of each convolution filter. Format is (7,), which means make 7x7 filters in the FIRST Conv2D layer.
            If we had another Conv2D layer with filters size 5x5, it would be ker_sz=(7,5)
        dense_interior_units: tuple. Same format as above.
            Number of hidden units in each dense layer.
            NOTE: Does NOT include the output layer, which has # units = # classes.
        pooling_sizes: tuple.  Same format as above.
            Pooling extent in the i-th MaxPool2D layer.
        pooling_strides: tuple.  Same format as above.
            Pooling stride in the i-th MaxPool2D layer.
        n_classes: int.
            Number of classes in the input. This will become the number of units in the Output Dense layer.
        wt_scale: float.
            Global weight scaling to use for all layers with weights
        reg: float.
            Regularization strength
        dropout_rate: float.
            Proportion of units whose activations we "drop" during training when processing each mini-batch.
        r_seed: int or None.
            Random seed for setting weights and bias parameters.
        verbose: bool. Do we want to term network-related debug print outs on?
            NOTE: This is different than per-layer verbose settings, which are turned manually on below.

        NOTE:
        - Remember to define self.wt_layer_inds as the list indicies in self.layers that have weights.
        - (NEW) Remember to define self.dropout_layer_inds as the list of layer indicies that are Dropout layers.
        '''
        super().__init__(reg, verbose)

        n_chans, h, w = input_shape

        self.layers = []
        
        # Convolution layer
        self.layers.append(accelerated_layer.Conv2DAccel(
            number=0, name='Conv2D_1', n_kers=n_kers[0], ker_sz=ker_sz[0], wt_scale=wt_scale, 
            activation='relu', verbose=verbose, r_seed=r_seed))
        
        # Max Pooling layer
        self.layers.append(accelerated_layer.MaxPool2DAccel(
            number=1, name='MaxPool2D_1', pool_size=pooling_sizes[0], strides=pooling_strides[0], 
            activation='linear', verbose=verbose))
        
        # Flatten layer
        self.layers.append(layer.Flatten(
            number=2, name='Flatten_1', verbose=verbose))
        
        # Dense layer
        self.layers.append(layer.Dense(
            number=3, name='Dense_1', units=dense_interior_units[0], 
            n_units_prev_layer=n_kers[0] * (h // pooling_strides[0]) * (w // pooling_strides[0]), 
            wt_scale=wt_scale, activation='relu', verbose=verbose, r_seed=r_seed))
        
        # Dropout layer
        self.layers.append(layer.Dropout(
            number=4, name='Dropout_1', rate=dropout_rate, verbose=verbose, r_seed=r_seed))
        
        # Output Dense layer
        self.layers.append(layer.Dense(
            number=5, name='Dense_2', units=n_classes, 
            n_units_prev_layer=dense_interior_units[0], 
            wt_scale=wt_scale, activation='softmax', verbose=verbose, r_seed=r_seed))
        
        # Define indices for weight and dropout layers
        self.wt_layer_inds = [0, 3, 5]
        self.dropout_layer_inds = [4]
        
