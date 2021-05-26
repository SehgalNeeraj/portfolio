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

    def draw(self, num_of_balls):
        """[summary]

        Args:
            num_of_balls (int, optional): [description]. Defaults to 0.

        Returns:
            [type]: [description]
        """
        draw_balls = []
        if num_of_balls > len(self.contents):
            num_of_balls = len(self.contents)

        for index in range(num_of_balls):
            random_index = random.randint(0,len(self.contents)-1)
            draw_balls.append(str(self.contents[random_index]))
            del self.contents[random_index]

        return draw_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """[summary]

    Args:
        hat ([type]): [description]
        expected_balls ([type]): [description]
        num_balls_drawn ([type]): [description]
        num_experiments ([type]): [description]

    Returns:
        [type]: [description]
    """
    probability = 0.0
    M = 0
    N = num_experiments
    expected_contents = list()

    for (k, v) in expected_balls.items():
        for index in range(v):
            expected_contents.append(str(k))

    for index in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        flag = True

        for expected_ball in expected_contents:
            if expected_ball not in balls_drawn:
                flag = False
                break
            
            balls_drawn.remove(expected_ball)
            
        if flag:
            M += 1

    probability = float(M/N)
    return (probability)
