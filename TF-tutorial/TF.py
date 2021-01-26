import tensorflow as tf

# create the session you will work in
sess = tf_reset()


# define your inputs
# a=tf.constant(1.0)
# b=tf.constant(2.0)
# if shape=[none], means that we do not know the (batch) size of inputs
a = tf.placeholder(dtype=tf.float32, shape=[1], name='a_placeholder')
b = tf.placeholder(dtype=tf.float32, shape=[1], name='b_placeholder')

# create a variable
var_init_value = [[2.0, 4.0, 6.0]]
var = tf.get_variable(name='myvar', shape=[1, 3], dtype=tf.float32, initializer=tf.constant_initializer(var_init_value))

# for everything in global list we want to initialize
init_op = tf.global_variables_initializer()
# do some operations
c = a + b
c_elementwise = a * b
c_matmul = tf.matmul(b, a)
c_elementwise_run, c_matmul_run = sess.run([c_elementwise, c_matmul])

# mean
c_mean = tf.reduce_mean(b)

# get the result
c_run = sess.run(c)
c0_run = sess.run(c, feed_dict={a: [1.0], b: [2.0]})
c1_run = sess.run(c, feed_dict={a: [2.0], b: [4.0]})
print('c={0}'.format(c_run))
print('c0={0}'.format(c0_run))
print('c1={0}'.format(c1_run))
print('c_elementwise:\n{0]'.format(c_elementwise_run))