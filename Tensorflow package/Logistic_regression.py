import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\ljy\lasif data\tensorflow-data\credit-a.csv', header=None)

# value_c = data.iloc[:, -1].value_counts()
# print(value_c)

x = data.iloc[:, :-1]
y = data.iloc[:, -1].replace(-1, 0)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(10, input_shape=(15,), activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

# model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['acc'])
history = model.fit(x, y, epochs=200)
print(history.history.keys())

plt.plot(history.epoch, history.history.get('loss'))
# plt.plot(history.epoch, history.history.get('acc'))
plt.show()