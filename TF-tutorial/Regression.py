import tensorflow as tf
import numpy as np
from matplotlib.pyplot import scatter, show

# to train a neural network on a simple regression problem
# we create data for a 1-dimensional regression problem

# generate data
inputs = np.linspace(-2 * np.pi, 2 * np.pi, 10000)[:, None]
outputs = np.sin(inputs) + 0.05 * np.random.normal(size=[len(inputs), 1])
scatter(inputs[:, 0], outputs[:, 0], s=0.1, color='k', marker='o')
show()

# create inputs,variables,neural network operations,mean-squared-error loss,gradient descent optimizer, and runs the
# optimizer using mini-batches of the data
sess = tf.Session()


def create_model():
    # create inputs
    input_ph = tf.placeholder(dtype=tf.float32, shape=[None, 1])
    output_ph = tf.placeholder(dtype=tf.float32, shape=[None, 1])
    # create variables three layers
    w0 = tf.get_variable(name='w0', shape=[1, 20], initializer=tf.contrib.layers.fully_connected)
    w1 = tf.get_variable(name='w1', shape=[20, 20], initializer=tf.contrib.layers.fully_connected)
    w2 = tf.get_variable(name='w2', shape=[20, 1], initializer=tf.contrib.layers.fully_connected)

    b0 = tf.get_variable(name='b0', shape=[20], initializer=tf.constant_initializer())
    b1 = tf.get_variable(name='b1', shape=[20], initializer=tf.constant_initializer())
    b2 = tf.get_variable(name='b2', shape=[1], initializer=tf.constant_initializer())

    weights = [w0, w1, w2]
    biases = [b0, b1, b2]
    activations = [tf.nn.relu, tf.nn.relu, None]

    # create computation graph
    layer = input_ph
    for w, b, activation in zip(weights, biases, activations):
        layer = tf.matmul(layer, w) + b
        if activation is not None:
            layer = activation(layer)
    output_pre = layer
    return input_ph, output_ph, output_pre


input_ph, output_ph, output_pre = create_model()

# create loss
mse = tf.reduce.mean(0.5 * tf.square(output_pre - output_ph))

# create optimizer
opt = tf.train.AdamOptimizer().minimize(mse)  # a stochastic gradient descent method


# initialize variables
sess.run(tf.global_variables_initializer())

# create saver to save model variables
saver = tf.train.Saver()

# run training
batch_size = 32
for training_step in range(10000):
    # get a random subset of the training data
    print(training_step)
    indices = np.random.randint(low=0, high=len(inputs), size=batch_size)
    input_batch = inputs[indices]
    output_batch = outputs[indices]

    # run the optimizer and get the mse
    _, mse_run = sess.run([opt, mse], feed_dict={input_ph: input_batch, output_ph: output_batch})
    # print the mse every so often
    if training_step % 1000 == 0:
        print('{0:04d} mse:{1:.3f}'.format(training_step, mse_run))
        saver.save(sess, '/tem/model.ckpt')

# create the model
input_ph, output_ph, output_pre = create_model()

# restore the saved model
saver = tf.train.Saver()
saver.restore(sess, '/tem/model.ckpt' )

output_pre_run = sess.run(output_pre, feed_dict={input_ph: inputs})

scatter(inputs[:, 0], outputs[:, 0], c='k', marker='o', s=0.1)
scatter(inputs[:, 0], output_pre_run[:, 0], c='k', marker='o', s=0.1)

