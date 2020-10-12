import time
import random

class Wait:
    @staticmethod
    def randomWait(min,max):
        sec = random.uniform(min, max)
        time.sleep(sec)