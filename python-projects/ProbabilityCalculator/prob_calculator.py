import copy
import random
from typing import List
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        """[summary]
        """
        self.contents = list()
        for (k, v) in kwargs.items():
            for index in range(v):
                self.contents.append(str(k))


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
