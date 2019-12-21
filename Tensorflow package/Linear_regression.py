import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

# print('Tensorflow Version: %s' % tf.__version__)

data = pd.read_excel('D:\ljy\lasif data\Income.xlsx')

# plt.scatter(data.Education, data.Income)
# plt.show()

x = data.Education
y = data.Income

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))

# print(model.summary())

model.compile(optimizer='adam', loss='mse')
history = model.fit(x, y, epochs=5000)
