from collections import Counter

import jieba
import numpy as np
import tensorflow.contrib.keras as kr

def open_file(filename, mode='r'):
    """
    常用文件操作，可在python2和python3间切换.
    mode: 'r' or 'w' for read or write
    """
    return open(filename, mode, encoding='utf-8', errors='ignore')#以UTF-8的格式代开文件并返回
