from colors import GREEN, BROWN


class Grass:
    
    def __init__(self, x, y, grass_size):
        self.x = x
        self.y = y
        self.size = grass_size
        self.energy = 10
        self.eaten = False
        self.color = GREEN
        self.time = 0
        self.time_to_growth = 80
    
    def eated(self):
        self.eaten = True
        self.color = BROWN
    
    def growth(self):
        if random(100) < 3 and self.time >= self.time_to_growth:
            self.time = 0
            self.eaten = False
            self.color = GREEN
    
    def update(self):
        fill(self.color)
        rect(self.x, self.y, self.size, self.size)
        self.time += 1
        self.growth()
