import numpy as np
from collections import deque

class A_star():
    def __init__(self, grid, x_start, y_start, x_end, y_end):
        self.grid = grid
        self.x_start = x_start
        self.y_start = y_start
        self.x = self.x_start
        self.y = self.y_start
        self.x_end = x_end
        self.y_end = y_end
        self.neighbors = list()
        self.neighbor()

    def neighbor(self):
        if self.x == self.x_end and self.y == self.y_end:
            return 'path found'

        self.grid[self.x][self.y] = 1
        if self.x > 0 and self.grid[self.x-1][self.y] == 0:
            self.neighbors.append([self.x - 1, self.y])

        if self.x < self.grid.shape[0] - 1 and self.grid[self.x+1][self.y] == 0:
            self.neighbors.append([self.x+1,self.y])

        if self.y > 0 and self.grid[self.x][self.y - 1] == 0:
            self.neighbors.append([self.x, self.y - 1])

        if self.y < self.grid.shape[1] - 1 and self.grid[self.x][self.y + 1] == 0:
            self.neighbors.append([self.x, self.y + 1])

        self.f_value()

    def f_value(self):
        h = deque()
        g = deque()

        for i in self.neighbors:
            x_distance = abs(i[0] - self.x_end)
            y_distance = abs(i[1] - self.y_end)
            h_value = (x_distance + y_distance)
            h.append(h_value)

        for i in self.neighbors:
            x_distance = abs(i[0] - self.x_start)
            y_distance = abs(i[1] - self.y_start)
            g_value = (x_distance + y_distance)
            g.append(g_value)

        self.f_values = [h + g for h, g in zip(h, g)]

        self.path()

    def path(self):
        for coordinate, i in enumerate(self.f_values):
            if i <= min(self.f_values):
                value = i
                index = coordinate

        self.x = self.neighbors[index][0]
        self.y = self.neighbors[index][1]

        print('f:', self.f_values)
        print('neighbors:', self.neighbors)

        self.neighbors.pop(index)
        self.f_values.pop(index)

        self.neighbor()
         
#test
#>>> grid = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#[1,1,1,1,1,1,0,1,1,1,1,1,0,1],
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#[1,0,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#[1,1,1,1,1,1,0,1,1,1,1,1,0,1],
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#[1,0,1,1,1,1,1,1,1,0,1,1,1,1],
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#[1,1,1,1,1,1,1,1,1,1,1,1,0,1],
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
#>>> A_star(grid, 1, 1, 8, 5)
