
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D
from tensorflow.python.keras.models import Sequential
from tensorflow.python import keras
import numpy as np

num_classes = 10
img_rows, img_cols = 28, 28
seed = 7
np.random.seed(seed)


def model(train_x, train_y, test_x, test_y, epoch):
    conv_model = Sequential()
    # first layer with input shape (img_rows, img_cols, 1) and 12 filters
    conv_model.add(Conv2D(12, kernel_size=(3, 3), activation='relu',
                          input_shape=(img_rows, img_cols, 1)))
    # second layer with 12 filters
    conv_model.add(Conv2D(12, kernel_size=(3, 3), activation='relu'))
    # third layer with 12 filers
    conv_model.add(Conv2D(12, kernel_size=(3, 3), activation='relu'))
    # flatten layer
    conv_model.add(Flatten())
    # adding a Dense layer
    conv_model.add(Dense(100, activation='relu'))
    # adding the final Dense layer with softmax
    conv_model.add(Dense(num_classes, activation='softmax'))

    # compile the model
    conv_model.compile(optimizer=keras.optimizers.Adadelta(),
                       loss='categorical_crossentropy',
                       metrics=['accuracy'])
    print("\n Training the Convolution neural network on MNIST data\n")
    # fit the model
    conv_model.fit(train_x, train_y, batch_size=128, epochs=epoch,
                   validation_split=0.1, verbose=2)
    predicted_train_y = conv_model.predict(train_x)
    print('Train accuracy : ', (sum(np.argmax(predicted_train_y, axis=1)
                                    == np.argmax(train_y, axis=1))/(float(len(train_y)))))
    predicted_test_y = conv_model.predict(test_x)
    print('Test accuracy : ', (sum(np.argmax(predicted_test_y, axis=1)
                                   == np.argmax(test_y, axis=1))/(float(len(test_y)))))
    return conv_model, predicted_train_y, predicted_test_y
