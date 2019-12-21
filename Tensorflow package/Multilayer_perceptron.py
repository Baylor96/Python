import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\ljy\lasif data\tensorflow-data\Advertising.csv')

# plt.figure()
# TV = plt.scatter(data.TV, data.sales)
# radio = plt.scatter(data.radio, data.sales)
# newspaper = plt.scatter(data.newspaper, data.sales)
# plt.legend(handles=[TV, radio, newspaper], labels=['TV','radio','newspaper'])
# plt.show()

x = data.iloc[:, 1:-1]
y = data.iloc[:, -1]

model = tf.keras.Sequential(
    [tf.keras.layers.Dense(10, input_shape=(3, ), activation = 'relu'),
     tf.keras.layers.Dense(1)])

# model.summary()

model.compile(optimizer='adam',loss='mse')
model.fit(x,y,epochs=100)

test_pre = data.iloc[:10, 1:-1]
model.predict(test_pre)
test_true = data.iloc[:10, -1]

print(model.predict(test_pre))
print(test_true)