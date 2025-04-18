'''deep_dream.py
Generate art with a pretrained neural network using the DeepDream algorithm
YOUR NAMES HERE
CS 343: Neural Networks
Project 4: Transfer Learning
Fall 2024
'''
import time
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image


import tf_util


class DeepDream:
    '''Runs the DeepDream algorithm on an image using a pretrained network.
    You should NOT need to import and use Numpy in this file (use TensorFlow instead).
    '''
    def __init__(self, pretrained_net, selected_layers_names):
        '''DeepDream constructor.

        Parameters:
        -----------
        pretrained_net: TensorFlow Keras Model object. Pretrained network configured to return netAct values in
            ALL layers when presented with an input image.
        selected_layers_names: Python list of str. Names of layers in `pretrained_net` that we will readout netAct values
            from in order to contribute to the generated image.

        TODO:
        1. Define instance variables for the pretrained network and the number of selected layers used to readout netAct.
        2. Make an readout model for the selected layers (use function in `tf_util`) and assign it as an instance variable.
        '''
        self.loss_history = None

        self.loss_history = None
        self.net = pretrained_net
        self.numLayers = len(selected_layers_names)
        self.readoutModel = tf_util.make_readout_model(pretrained_net, selected_layers_names)

    def loss_layer(self, layer_net_acts):
        '''Computes the contribution to the total loss from the current layer with netAct values `layer_net_acts`. The
        loss contribution is the mean of all the netAct values in the current layer.

        Parameters:
        -----------
        layer_net_acts: tf tensor. shape=(1, Iy, Ix, K). The netAct values in the current selected layer. K is the
            number of kernels in the layer.

        Returns:
        -----------
        loss component from current layer. float. Mean of all the netAct values in the current layer.
        '''
        return tf.reduce_mean(layer_net_acts)

    def forward(self, gen_img, standardize_grads=True, eps=1e-8):
        '''Performs forward pass through the pretrained network with the generated image `gen_img`.
        Loss is computed based on the SELECTED layers (in readout model).

        Parameters:
        -----------
        gen_img: tf tensor. shape=(1, Iy, Ix, n_chans). Generated image that is used to compute netAct values, loss,
            and the image gradients. The singleton dimension is the batch dimension (N).
        standardize_grads: bool. Should we standardize the image gradients?
        eps: float. Small number used in standardization to prevent possible division by 0 (i.e. if stdev is 0).

        Returns:
        -----------
        loss. float. Sum of the loss components from all the selected layers.
        grads. shape=(1, Iy, Ix, n_chans). Image gradients (`dImage` aka `dloss_dImage`) — gradient of the
            generated image with respect to each of the pixels in the generated image.

        TODO:
        While tracking gradients:
        - Use the readout model to extract the netAct values in the selected layers for `gen_img`.
        - Compute the average loss across all selected layers.
        Then:
        - Obtain the tracked gradients of the loss with respect to the generated image.
        '''
        with tf.GradientTape() as tape:
            tape.watch(gen_img)
            netActs = self.readoutModel(gen_img)
            loss = tf.reduce_mean([self.loss_layer(act) for act in netActs])
        grads = tape.gradient(loss, gen_img)
        if standardize_grads:
            grads = (grads - tf.math.reduce_mean(grads)) / (tf.math.reduce_std(grads) + eps)
        return loss, grads
    
    import time

    def fit(self, gen_img, n_epochs=26, lr=0.01, print_every=25, plot=True, plot_fig_sz=(5, 5), export=True):
        '''Iteratively modify the generated image (`gen_img`) for `n_epochs` with the image gradients using the
            gradient ASCENT algorithm. In other words, run DeepDream on the generated image.

        Parameters:
        -----------
        gen_img: tf tensor. shape=(1, Iy, Ix, n_chans). Generated image that is used to compute netAct values, loss,
            and the image gradients.
        n_epochs: int. Number of epochs to run gradient ascent on the generated image.
        lr: float. Learning rate.
        print_every: int. Print out progress (current epoch) every this many epochs.
        plot: bool. If true, plot/show the generated image `print_every` epochs.
        plot_fig_sz: tuple of ints. The plot figure size (height, width) to use when plotting/showing the generated image.
        export: bool. Whether to export a JPG image to the `deep_dream_output` folder in the working directory
            every `print_every` epochs. Each exported image should have the current epoch number in the filename so that
            the image currently exported image doesn't overwrite the previous one. For example, image_1.jpg, image_2.jpg,
            etc.

        Returns:
        -----------
        self.loss_history. Python list of float. Loss values computed on every epoch of training.

        TODO:
        1. Compute the forward pass on the generated image for `n_epochs`.
        2. Apply the gradients to the generated image using the gradient ASCENT update rule.
        3. Clip pixel values to the range [0, 1] and update the generated image.
            The TensorFlow `assign` function is helpful here because = would "wipe out" the tf.Variable property,
            which is not what we want because we want to track gradients on the generated image across epochs.
        4. After the first epoch completes, always print out how long it took to finish the first epoch and an estimate
        of how long it will take to complete all the epochs (in minutes).

        NOTE:
        - Deep Dream performs gradient ASCENT rather than DESCENT (which we are more used to). The difference is only
        in the sign of the gradients.
        - Clipping is different than normalization!
        '''
        self.loss_history = []
        output_dir = 'deep_dream_output'

        # Ensure the output directory exists
        if export and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        start_time = time.time()

        for epoch in range(1, n_epochs + 1):
            loss, grads = self.forward(gen_img)
            gen_img.assign_add(lr * grads)
            gen_img.assign(tf.clip_by_value(gen_img, 0.0, 1.0))
            self.loss_history.append(loss.numpy())

            if epoch % print_every == 0:
                print(f"Epoch {epoch}/{n_epochs}, Loss: {loss.numpy():.4f}")
                if plot:
                    plt.imshow(gen_img.numpy()[0])
                    plt.axis('off')
                    plt.show()
                if export:
                    img = tf_util.tf2image(gen_img)
                    img.save(f'{output_dir}/epoch_{epoch}.jpg')
            if epoch == 1:
                print(f"Epoch {epoch}/{n_epochs}, Loss: {loss.numpy():.4f}")
                runtime = time.time() - start_time
                estimated_total_time = runtime * n_epochs / 60  # in minutes
                print(f"Runtime after first epoch: {runtime:.2f} seconds")
                print(f"Estimated total time to complete all epochs: {estimated_total_time:.2f} minutes")
                plt.imshow(gen_img.numpy()[0])
                plt.axis('off')
                plt.show()

        return self.loss_history
    
    def fit_multiscale(self, gen_img, n_scales=4, scale_factor=1.3, n_epochs=26, lr=0.01, print_every=1, plot=True,
                   plot_fig_sz=(5, 5), export=True):
        '''Run DeepDream `fit` on the generated image `gen_img` a total of `n_scales` times. After each time, scale the
        width and height of the generated image by a factor of `scale_factor` (round to nearest whole number of pixels).
        The generated image does NOT start out from scratch / the original image after each resizing. Any modifications
        DO carry over across runs.

        Parameters:
        -----------
        gen_img: tf tensor. shape=(1, Iy, Ix, n_chans). Generated image that is used to compute netAct values, loss,
            and the image gradients.
        n_scales: int. Number of times the generated image should be resized and DeepDream should be run.
        n_epochs: int. Number of epochs to run gradient ascent on the generated image.
        lr: float. Learning rate.
        print_every: int. Print out progress (current scale) every this many SCALES (not epochs).
        plot: bool. If true, plot/show the generated image `print_every` SCALES.
        plot_fig_sz: tuple of ints. The plot figure size (height, width) to use when plotting/showing the generated image.
        export: bool. Whether to export a JPG image to the `deep_dream_output` folder in the working directory
            every `print_every` SCALES. Each exported image should have the current scale number in the filename so that
            the image currently exported image doesn't overwrite the previous one.

        Returns:
        -----------
        self.loss_history. Python list of float. Loss values computed on every epoch of training.

        TODO:
        1. Call fit `n_scale` times. Pass along hyperparameters (n_epochs, etc.). Turn OFF plotting and exporting within
        the `fit` method — this method should take over the plotting and exporting (in scale intervals rather than epochs).
        2. Multiplicatively scale the generated image.
            Check out: https://www.tensorflow.org/api_docs/python/tf/image/resize

            NOTE: The output of the built-in resizing process is NOT a tf.Variable (its an ordinary tensor).
            But we need a tf.Variable to compute the image gradient during gradient ascent.
            So, wrap the resized image in a tf.Variable.
        3. After the first scale completes, always print out how long it took to finish the first scale and an estimate
        of how long it will take to complete all the scales (in minutes).
        '''
        self.loss_history = []
        # Create output directory if needed
        output_dir = 'deep_dream_output'
        if export and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        start_time = time.time()

        for scale in range(1, n_scales + 1):

            # Track losses for this scale
            scale_loss_history = []

            # Run gradient ascent for n_epochs on the current scale
            self.fit(gen_img, n_epochs, lr, print_every=9999999999, plot=False, export=False)

            # Append losses for this scale to the overall loss history
            self.loss_history.extend(scale_loss_history)

            # Plot and export image after each scale
            if scale % print_every == 0:
                print(f"Scale {scale}/{n_scales}")
                img = tf_util.tf2image(gen_img)
                if plot:
                    plt.figure(figsize=plot_fig_sz)
                    plt.imshow(img)
                    plt.axis('off')
                    plt.title(f"Scale {scale}")
                    plt.show()
                if export:
                    img = tf_util.tf2image(gen_img)
                    img.save(f"{output_dir}/scale_{scale}.jpg")

            

            # Debugging: Confirm image shape before scaling
            print(f"Before scaling: {gen_img.shape}")

            if scale == 1:
                runtime = time.time() - start_time
                estimated_total_time = runtime * n_scales / 60  # in minutes
                print(f"Runtime after first scale: {runtime:.2f} seconds")
                print(f"Estimated total time to complete all scales: {estimated_total_time:.2f} minutes")

            # Resize the image to the next scale
            new_shape = [int(dim * scale_factor) for dim in gen_img.shape[1:3]]
            gen_img = tf.Variable(tf.image.resize(gen_img, size=new_shape), trainable=True)

            # Debugging: Confirm image shape after scaling
            print(f"After scaling: {gen_img.shape}")

        return self.loss_history

    def animated_multiscale_fit(self, gen_img, n_scales=4, scale_factor=1.3, n_epochs=26, lr=0.01, plot_fig_sz=(5, 5), export=True, fps=30):
        import matplotlib.animation as animation
        from IPython.display import HTML
        from tqdm import tqdm
        images = []
        self.loss_history = []
        
        total_steps = n_scales * n_epochs
        with tqdm(total=total_steps, desc="Processing", unit="step") as pbar:
            for scale in range(1, n_scales + 1):
                for epoch in range(1, n_epochs + 1):
                    loss, grads = self.forward(gen_img)
                    gen_img.assign_add(lr * grads)
                    gen_img.assign(tf.clip_by_value(gen_img, 0.0, 1.0))
                    self.loss_history.append(loss.numpy())
                    images.append(tf_util.tf2image(gen_img))
                    pbar.set_postfix_str(f"Scale {scale}/{n_scales}, Epoch {epoch}/{n_epochs}")
                    pbar.update(1)
                new_shape = [int(dim * scale_factor) for dim in gen_img.shape[1:3]]
                gen_img = tf.Variable(tf.image.resize(gen_img, size=new_shape), trainable=True)
        
        # Use matplotlib to create an animation
        fig, ax = plt.subplots()
        ax.axis('off')
        im = ax.imshow(images[0])
    
        def update(i):
            im.set_array(images[i])
            return [im]
    
        ani = animation.FuncAnimation(fig, update, frames=len(images), interval=1000 // fps, blit=True)
        plt.close(fig)  # Prevents additional static plot display in notebook
        return HTML(ani.to_jshtml())
            
                