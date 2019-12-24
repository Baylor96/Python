import tensorflow as tf
import numpy as np

dataset1 = tf.data.Dataset.from_tensor_slices([1,2,3,4,5,6,7])

for ele in dataset1:
    print(ele)

dataset2 = tf.data.Dataset.from_tensor_slices([[1,2], [3,4], [5,6]])
print(dataset2)
for ele in dataset2:
    print(ele.numpy())

dataset_dic = tf.data.Dataset.from_tensor_slices({
    'a':[1,2,3,4],'b':[6,7,8,9],'c':[12,13,14,15]
})
print(dataset_dic)
for ele in dataset_dic:
    print(ele)

dataset_np = tf.data.Dataset.from_tensor_slices(np.array([1,2,3,4,5,6,7]))
for ele in dataset_np.take(4):
    print(ele.numpy())
print(next(iter(dataset_np.take(1))))
dataset_np_shuffle = dataset_np.shuffle(7)
dataset_np_shuffle = dataset_np_shuffle.repeat(count=3)
dataset_np_shuffle = dataset_np_shuffle.batch(3)
for ele in dataset_np_shuffle:
    print(ele.numpy())

dataset_square = dataset_np.map(tf.square)
for ele in dataset_square:
    print(ele.numpy())