"""
Created on Tuesday Sep. 26 2023
@author: Nuocheng Yang, MingzheChen
@github: https://github.com/YangNuoCheng, https://github.com/mzchen0 
"""
import random
from collections import deque

class UERMemory(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = deque(maxlen=self.capacity)

    def remember(self, sample):
        self.memory.append(sample)

    def sample(self, n, seeds = 1):
        random.seed(seeds)
        n = min(n, len(self.memory))
        sample_batch = random.sample(self.memory, n)

        return sample_batch