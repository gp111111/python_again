from random import choice

class Randomwalk():
    """a class used to generate the randomwalk data"""
    def __init__(self,num_points=5000):
        """initialize the attributes of randomwalk"""
        self.num_points = num_points

        #所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step() #调用当前对象的方法
            y_step = self.get_step()

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
    
    def get_step(self):
        """sure the step of x and y"""
        axis_direction = choice([-1,1])
        axis_distance = choice([0,1,2,3,4])
        axis_step = axis_direction * axis_distance
        return axis_step

