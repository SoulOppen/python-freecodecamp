import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls):
        self.contents = []
        for color, quantity in balls.items():
            self.contents.extend([color] * quantity)
    def sort(self):
        random.shuffle(self.contents)
    def draw(self,times):
        draw=[]
        for i in range(times):
            self.sort()
            if len(self.contents)>0:
                draw.append(self.contents.pop())
        return draw
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total_positive = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = {}
        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] += 1
            else:
                drawn_balls_count[ball] = 1
        experiment_positive = True
        for  color in list(expected_balls.keys()):
            if color not in list(drawn_balls_count.keys()):
                experiment_positive=False
            elif expected_balls[color] > drawn_balls_count[color]:
                experiment_positive=False
        if experiment_positive:
            total_positive += 1
    return total_positive / num_experiments
hat =Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=30000)
