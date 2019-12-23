import tensorflow as tf
import matplotlib.pyplot as plt

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

input = tf.keras.Input(shape=(28, 28))
x = tf.keras.layers.Flatten()(input)
x = tf.keras.layers.Dense(32, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
output = tf.keras.layers.Dense(10, activation='softmax')(x)

input1 = tf.keras.Input(shape=(28,28))
input2 = tf.keras.Input(shape=(28,28))
x1 = tf.keras.layers.Flatten()(input1)
x2 = tf.keras.layers.Flatten()(input2)
x = tf.keras.layers.concatenate([x1, x2])
x = tf.keras.layers.Dense(32, activation='relu')(x)
output = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(inputs=[input1, input2], outputs=output)


model = tf.keras.Model(inputs=input, outputs=output)

model.summary()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
history = model.fit(train_image, train_label, epochs=30, validation_data=(test_image, test_label))

