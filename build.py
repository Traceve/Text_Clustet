import os
import time
from datetime import timedelta

import numpy as np
import tensorflow as tf
import tensorflow.contrib.keras as kr
from sklearn import metrics

from train_word2vec import train_word2vec

def export_word2vec_vectors(config):
    """
    save vocab_vector to numpy file
    :param config: config
    :return:
    """
    vocab = config.word_to_id
    file_r = codecs.open(config.vector_word_filename, 'r', encoding='utf-8')
    line = file_r.readline()
    voc_size, vec_dim = map(int, line.split(' '))
    embeddings = np.zeros([len(vocab), vec_dim])
    line = file_r.readline()
    while line:
        items = line.split(' ')
        word = items[0]
        vec = np.asarray(items[1:], dtype='float32')
        if word in vocab:
            word_idx = vocab[word]
            embeddings[word_idx] = np.asarray(vec)
        line = file_r.readline()
    np.savez_compressed(config.vector_word_npz, embeddings=embeddings)