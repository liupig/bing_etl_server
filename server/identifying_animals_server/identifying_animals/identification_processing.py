# coding=utf-8
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from server.identifying_animals_server.identifying_animals.model import inference

MODULE_PATH = "./server/identifying_animals_server/identifying_animals/model.ckpt-46000"


def get_image(name):
    filename = os.path.join(f"./static/images/{name}")
    image = Image.open(filename)
    image = image.resize([208, 208])
    image = np.array(image)
    return image


def evaluate_one_image(filename):
    image_array = get_image(filename)
    with tf.Graph().as_default():
        BATCH_SIZE = 1
        N_CLASSES = 2
        image = tf.cast(image_array, tf.float32)
        image = tf.image.per_image_standardization(image)
        image = tf.reshape(image, [1, 208, 208, 3])
        logit = inference(image, BATCH_SIZE, N_CLASSES)
        logit = tf.nn.softmax(logit)

        x = tf.placeholder(tf.float32, shape=[208, 208, 3])
        saver = tf.train.Saver()

        with tf.Session() as sess:
            saver.restore(sess, MODULE_PATH)
            prediction = sess.run(logit, feed_dict={x: image_array})
            max_index = np.argmax(prediction)
            if max_index == 0:
                result = {"result": "cat", "probability": "%.6f" % prediction[:, 0]}
            else:
                result = {"result": "dag", "probability": "%.6f" % prediction[:, 1]}

        return result
