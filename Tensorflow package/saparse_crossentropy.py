import tensorflow as tf
import matplotlib.pyplot as plt

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

print(train_image.shape, train_label.shape)
print(test_image.shape, test_label.shape)

# plt.imshow(train_image[0])
# plt.show()

train_image = train_image/255
test_image = test_image/255

print(train_image.shape)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
history = model.fit(train_image, train_label, epochs=5)
model.evaluate(test_image, test_label)

plt.plot(history.epoch, history.history.get('acc'))
plt.show()