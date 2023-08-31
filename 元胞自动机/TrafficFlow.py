import numpy as np
import numpy.random

# 定义参数
n = 20
v_max = 4
road = np.zeros(n + 2, dtype=int)


class Car:
    speed = 0
    loc = 0

    def __init__(self, _loc):
        self.loc = _loc
        self.speed = 0

    def get_front_car(self):
        for j in range(self.loc + 1, n + 1):
            if road[j]:
                return j
            else:
                continue
        return -1

    def speed_up(self):
        self.speed += 1
        if self.speed > v_max:
            self.speed = v_max

    def break_down(self):
        d = self.get_front_car() - self.loc - 1
        if d >= 0:
            self.speed = min(self.speed, d)

    def speed_down(self):
        p = numpy.random.randint(low=0, high=10, size=1)[0]
        if p <= 1:
            self.speed = max(self.speed - 1, 0)

    def update(self):
        road[self.loc] = 0
        # print('原位置是 %d; 速度为 %d' % (self.loc, self.speed))
        self.loc += self.speed
        if self.loc <= n:
            road[self.loc] = 1
        # print('移动至 %d' % self.loc)


if __name__ == '__main__':
    cnt = 0
    init_car = np.random.randint(low=1, high=20, size=10, dtype='int')
    # init_car = [17, 4, 7, 8]
    cars = []
    # 初始化车辆
    for i in init_car:
        cars.append(Car(i))
        cars[-1].update()
    # 迭代
    print(road)
    while len(cars):
        for i in cars:
            i.speed_up()
            i.speed_down()
            i.break_down()
        del_index = []
        for i in range(len(cars)):
            cars[i].update()
            if cars[i].loc > n:
                del_index.append(cars[i])
        for i in del_index:
            cars.remove(i)
        print(road)
