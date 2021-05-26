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

    def draw(self, num_of_balls=0):
        draw_balls = []
        if num_of_balls > len(self.contents):
            num_of_balls = len(self.contents)

        for index in range(num_of_balls):
            random_index = random.randint(0,len(self.contents)-1)
            draw_balls.append(str(self.contents[random_index]))
            del self.contents[random_index]

        return draw_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
