import tensorflow as tf
import gzip
import numpy as np
import matplotlib.pyplot as plt


def load_data():

    path = r"D:\ljy\lasif data\fashion-mnist"
    files = [
        'train-labels-idx1-ubyte.gz', 'train-images-idx3-ubyte.gz',
        't10k-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz'
    ]
    paths = []
    for fname in files:
        paths.append(tf.keras.utils.get_file(fname, origin=None, cache_dir=path + fname, cache_subdir=path))

    with gzip.open(paths[0], 'rb') as lbpath:
        y_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(paths[1], 'rb') as imgpath:
        x_train = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(y_train), 28, 28)

    with gzip.open(paths[2], 'rb') as lbpath:
        y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(paths[3], 'rb') as imgpath:
        x_test = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(y_test), 28, 28)

    return (x_train, y_train), (x_test, y_test)

if __name__ == '__main__':

    print(tf.__version__)

    (train_images, train_labels), (test_images, test_labels) = load_data()

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    print(train_images.shape)
    print(len(train_images))
    print(test_images.shape)
    print(len(test_labels))

    plt.figure(figsize=(5,5))
    plt.imshow(train_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.show()