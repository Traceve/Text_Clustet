import os
class TCNNConfig(object):
    def __init__(self, data_base_dir):
        self.train_dir = os.path.join(data_base_dir, 'train.txt')
        self.vocab_dir = os.path.join(data_base_dir, 'vocab.txt')
        self.vector_word_npz = os.path.join(data_base_dir, 'vector_word.npz')
        self.vector_word_filename = os.path.join(data_base_dir, 'vector_word.txt')
        self.words = None
        self.word_to_id = None