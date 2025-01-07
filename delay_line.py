import numpy as np

class DelayLine:
    def __init__(self, delay_length: int):
        self.delay_length = delay_length
        self.__delay_buffer = np.zeros((delay_length,))
    
    def process(self, x, y):
        # Perhaps add a check
        for i in range(len(x)):
            y[i] = self.__delay_buffer[-1]
            for j in range(self.delay_length - 1, 0, -1):
                self.__delay_buffer[j] = self.__delay_buffer[j - 1]
            self.__delay_buffer[0] = x[i]

