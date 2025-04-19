'''filter_ops.py
Implements the convolution and max pooling operations.
Applied to images and other data represented as an ndarray.
Veer Khosla and Saad Khan
CS343: Neural Networks
Project 3: Convolutional neural networks
'''
import numpy as np
import math

def conv2_gray(img, kers, verbose=True):
    '''
    Does a 2D convolution operation on GRAYSCALE `img` using kernels `kers`.
    Uses 'same' boundary conditions.

    Parameters:
    -----------
    img: ndarray. Grayscale input image to be filtered. shape=(height, width)
    kers: ndarray. Convolution kernels. shape=(Num kers, kernel_height, kernel_width)
    verbose: bool. If True, prints shape information for debugging.

    Returns:
    -----------
    filtered_img: ndarray. Filtered image after applying convolution. shape=(Num kers, height, width)
    '''
    img_height, img_width = img.shape
    num_kernels, kernel_height, kernel_width = kers.shape

    if verbose:
        print(f'Image dimensions: height={img_height}, width={img_width}')
        print(f'Number of kernels: {num_kernels}, kernel dimensions: height={kernel_height}, width={kernel_width}')

    # Ensure kernels are square
    if kernel_height != kernel_width:
        print('Kernels must be square!')
        return None

    # Initialize output for the filtered image
    filtered_img = np.zeros((num_kernels, img_height, img_width))
    
    # Calculate padding for 'same' output size
    padding = math.ceil((kernel_width - 1) / 2)

    # Pad the image with zeros
    padded_img = np.pad(img, ((padding, padding), (padding, padding)), mode='constant', constant_values=0)

    # Perform convolution for each kernel
    for k in range(num_kernels):
        kernel = np.flipud(np.fliplr(kers[k]))  # Flip kernel for convolution

        for i in range(img_height):
            for j in range(img_width):
                # Extract the region of interest and apply the kernel
                region = padded_img[i:i + kernel_height, j:j + kernel_width]
                filtered_img[k, i, j] = np.sum(region * kernel)

    if verbose:
        print(f"Filtered image shape: {filtered_img.shape}")

    return filtered_img

def conv2(img, kers, verbose=True):
    '''
    Does a 2D convolution operation on COLOR or grayscale `img` using kernels `kers`.
    Uses 'same' boundary conditions.

    Parameters:
    -----------
    img: ndarray. Input image to be filtered. shape=(n_chans, height, width)
         where n_chans is 1 for grayscale images and 3 for RGB color images
    kers: ndarray. Convolution kernels. shape=(num_kernels, n_chans, kernel_height, kernel_width)
    verbose: bool. If True, prints shape information for debugging.

    Returns:
    -----------
    filtered_img: ndarray. Filtered image after applying convolution. shape=(num_kernels, height, width)
    '''
    n_chans, img_height, img_width = img.shape
    
    # Check and adapt kernel dimensions if necessary
    if len(kers.shape) == 3:  # If kers is (num_kernels, kernel_height, kernel_width)
        kers = np.expand_dims(kers, axis=1)  # Expand to (num_kernels, 1, kernel_height, kernel_width)
    
    num_kernels, ker_chans, kernel_height, kernel_width = kers.shape

    if verbose:
        print(f'Image dimensions: channels={n_chans}, height={img_height}, width={img_width}')
        print(f'Number of kernels: {num_kernels}, kernel dimensions: height={kernel_height}, width={kernel_width}')

    # Ensure kernels are square and handle single-channel kernels for multi-channel images
    if kernel_height != kernel_width:
        print('Kernels must be square!')
        return None
    if ker_chans == 1 and n_chans > 1:
        # Replicate the single-channel kernel across all image channels
        kers = np.tile(kers, (1, n_chans, 1, 1))

    # Initialize output for the filtered image, now with shape (num_kernels, n_chans, img_height, img_width)
    filtered_img = np.zeros((num_kernels, n_chans, img_height, img_width))
    
    # Calculate padding for 'same' output size
    padding = math.ceil((kernel_width - 1) / 2)

    # Pad each channel of the image independently
    padded_img = np.pad(img, ((0, 0), (padding, padding), (padding, padding)), mode='constant', constant_values=0)

    # Perform convolution for each kernel
    for k in range(num_kernels):
        # Process each color channel independently
        for c in range(n_chans):
            kernel = np.flipud(np.fliplr(kers[k, c]))  # Flip kernel for convolution
            
            # Convolve this channel and add to the output for the current kernel
            for i in range(img_height):
                for j in range(img_width):
                    # Extract the region of interest and apply the kernel
                    region = padded_img[c, i:i + kernel_height, j:j + kernel_width]
                    filtered_img[k, c, i, j] = np.sum(region * kernel)

    if verbose:
        print(f"Filtered image shape: {filtered_img.shape}")

    return filtered_img

def conv2nn(imgs, kers, bias, verbose=True):
    '''General 2D convolution operation suitable for a convolutional layer of a neural network.
    Uses 'same' boundary conditions.

    Parameters:
    -----------
    imgs: ndarray. Input IMAGES to be filtered. shape=(BATCH_SZ, n_chans, img_y, img_x)
        where batch_sz is the number of images in the mini-batch
        n_chans is 1 for grayscale images and 3 for RGB color images
    kers: ndarray. Convolution kernels. shape=(n_kers, N_CHANS, ker_sz, ker_sz)
        NOTE: Each kernel should be square and [ker_sz < img_y] and [ker_sz < img_x]
    bias: ndarray. Bias term used in the neural network layer. Shape=(n_kers,)
        i.e. there is a single bias per filter. Convolution by the c-th filter gets the c-th
        bias term added to it.
    verbose: bool. I suggest making helpful print statements showing the shape of various things
        as you go. Only execute these print statements if verbose is True.

    What's new (vs conv2):
    -----------
    - Multiple images (mini-batch support)
    - Kernels now have a color channel dimension too
    - Collapse (sum) over color channels when computing the returned output images
    - A bias term

    Returns:
    -----------
    output: ndarray. `imgs` filtered with all `kers`. shape=(BATCH_SZ, n_kers, img_y, img_x)

    Hints:
    -----------
    - You may need additional loop(s).
    - Summing inside your loop can be made simpler compared to conv2.
    - Adding the bias should be easy.
    '''
    batch_sz, n_chans, img_y, img_x = imgs.shape
    n_kers, n_ker_chans, ker_y, ker_x = kers.shape

    # Verbose output to check shape matches
    if verbose:
        print(f'batch_sz={batch_sz}, n_chan={n_chans}, img_x={img_y}, img_y={img_x}')
        print(f'n_kers={n_kers}, n_ker_chans={n_ker_chans}, ker_y={ker_y}, ker_x={ker_x}')
    
    # Check that kernel channels match image channels
    if n_chans != n_ker_chans:
        print('Number of kernel channels does not match input num channels!')
        return None

    # Check that kernel is square
    if ker_y != ker_x:
        print('Kernels must be square!')
        return None

    # Initialize output with the shape (batch_sz, n_kers, img_y, img_x)
    output = np.zeros((batch_sz, n_kers, img_y, img_x))

    # Calculate padding for 'same' output size
    padding_y = (ker_y) // 2
    padding_x = (ker_x) // 2

    # Pad each image independently on height and width dimensions
    padded_imgs = np.pad(imgs, ((0, 0), (0, 0), (padding_y, padding_y), (padding_x, padding_x)), mode='constant')

    # Perform convolution
    for b in range(batch_sz):
        for k in range(n_kers):
            # Apply bias for each filter
            output[b, k, :, :] += bias[k]
            for c in range(n_chans):
                # Flip kernel for convolution
                kernel = np.flipud(np.fliplr(kers[k, c]))
                # Convolve
                for i in range(img_y):
                    for j in range(img_x):
                        region = padded_imgs[b, c, i:i + ker_y, j:j + ker_x]
                        output[b, k, i, j] += np.sum(region * kernel)

    if verbose:
        print(f'Output shape: {output.shape}')
    
    return output


def get_pooling_out_shape(img_dim, pool_size, strides):
    '''Computes the size of the output of a max pooling operation along one spatial dimension.

    Parameters:
    -----------
    img_dim: int. Either img_y or img_x
    pool_size: int. Size of pooling window in one dimension: either x or y (assumed the same).
    strides: int. Size of stride when the max pooling window moves from one position to another.

    Returns:
    -----------
    int. The size in pixels of the output of the image after max pooling is applied, in the dimension
        img_dim.
    '''
    return (img_dim - pool_size) // strides + 1


def max_pool(inputs, pool_size=2, strides=1, verbose=True):
    ''' Does max pooling on inputs. Works on single grayscale images, so somewhat comparable to
    `conv2_gray`.

    Parameters:
    -----------
    inputs: Input to be filtered. shape=(height img_y, width img_x)
    pool_size: int. Pooling window extent in both x and y.
    strides: int. How many "pixels" in x and y to skip over between successive max pooling operations
    verbose: bool. I suggest making helpful print statements showing the shape of various things
        as you go. Only execute these print statements if verbose is True.

    Returns:
    -----------
    outputs: Input filtered with max pooling op. shape=(out_y, out_x)
        NOTE: out_y, out_x determined by the output shape formula. The input spatial dimensions are
        not preserved (unless pool_size=1...but what's the point of that? :)

    NOTE: There is no padding in the max-pooling operation.

    Hints:
    -----------
    - You should be able to heavily leverage the structure of your conv2_gray code here
    - Instead of defining a kernel, indexing strategically may be helpful
    - You may need to keep track of and update indices for both the input and output images
    - Overall, this should be a simpler implementation than `conv2_gray`
    '''
    img_y, img_x = inputs.shape

    img_height, img_width = inputs.shape

    # Calculate output dimensions
    out_height = (img_height - pool_size) // strides + 1
    out_width = (img_width - pool_size) // strides + 1

    if verbose:
        print(f'Input shape: height={img_height}, width={img_width}')
        print(f'Output shape: out_height={out_height}, out_width={out_width}')

    # Initialize output array for max-pooled image
    pooled_img = np.zeros((out_height, out_width))

    # Perform max pooling
    for i in range(out_height):
        for j in range(out_width):
            # Define the region for max pooling
            region = inputs[i * strides:i * strides + pool_size, j * strides:j * strides + pool_size]
            pooled_img[i, j] = np.max(region)  # Apply max operation within the pooling window

    return pooled_img


def max_poolnn(inputs, pool_size=2, strides=1, verbose=True):
    ''' Max pooling implementation for a MaxPool2D layer of a neural network

    Parameters:
    -----------
    inputs: Input to be filtered. shape=(mini_batch_sz, n_chans, height img_y, width img_x)
        where n_chans is 1 for grayscale images and 3 for RGB color images
    pool_size: int. Pooling window extent in both x and y.
    strides: int. How many "pixels" in x and y to skip over between successive max pooling operations
    verbose: bool. I suggest making helpful print statements showing the shape of various things
        as you go. Only execute these print statements if verbose is True.

    Returns:
    -----------
    outputs: Input filtered with max pooling op. shape=(mini_batch_sz, n_chans, out_y, out_x)
        NOTE: out_y, out_x determined by the output shape formula. The input spatial dimensions are
        not preserved (unless pool_size=1...but what's the point of that?)

    What's new (vs max_pool):
    -----------
    - Multiple images (mini-batch support)
    - Images now have a color channel dimension too

    Hints:
    -----------
    - If you added additional nested loops, be careful when you reset your input image indices
    '''

    mini_batch_sz, n_chans, img_y, img_x = inputs.shape

    # Calculate output dimensions
    out_y = (img_y - pool_size) // strides + 1
    out_x = (img_x - pool_size) // strides + 1

    if verbose:
        print(f'Input shape: mini_batch_sz={mini_batch_sz}, n_chans={n_chans}, height={img_y}, width={img_x}')
        print(f'Output shape: mini_batch_sz={mini_batch_sz}, n_chans={n_chans}, height={out_y}, width={out_x}')

    # Initialize output array for max-pooled image
    pooled_img = np.zeros((mini_batch_sz, n_chans, out_y, out_x))

    # Perform max pooling
    for b in range(mini_batch_sz):
        for c in range(n_chans):
            for i in range(out_y):
                for j in range(out_x):
                    # Define the region for max pooling
                    region = inputs[b, c, i*strides:i*strides+pool_size, j*strides:j*strides+pool_size]
                    pooled_img[b, c, i, j] = np.max(region)  # Apply max operation within the pooling window

    return pooled_img
