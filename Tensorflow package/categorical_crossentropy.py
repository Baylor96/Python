import tensorflow as tf
import numpy as np

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

train_label_onehot = tf.keras.utils.to_categorical(train_label)
test_label_onehot = tf.keras.utils.to_categorical(test_label)

train_image = train_image/255
test_image = test_image/255

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
histroy = model.fit(train_image, train_label_onehot, epochs=5)

predict = model.predict(test_image)
print(predict[0],np.argmax(predict[0]))
