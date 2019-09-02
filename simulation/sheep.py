from colors import WHITE, YELLOW
from random import randint


class Sheep:
    
    def __init__(self, x, y, sheep_color = WHITE):
        self.x = x
        self.y = y
        self.size = 8
        self.speed = 4
        self.energy = 20
        self.color = sheep_color
        self.reproduction_energy = 40
        self.energy_comsumption = {
            'move': 1,
            'reproduction': self.reproduction_energy*.8
        }
        
        # E se adicionarmos uma mutacao?
        if random(0, 100) < 1:
            self.mutation()
            
    def mutation(self):
        self.color = color(randint(1, 255), randint(1, 255), randint(1, 255))
        self.speed *= random(0, 2)
        self.reproduction_energy *= random(0.5, 2)
        self.energy_comsumption = {
            'move': 1*random(0,2),
            'reproduction': self.reproduction_energy*random(0,2)
        }

    def move(self):
        """ Faz a ovelha se movimentar
        de acordo com sua velocidade em
        uma direcao aleatoria.
        
        Se a ovelha ultrapassar os limites
        da tela, ela sera renderizada do
        lado oposto ao qual ela ultrapassou
        os limites.
        """
        self.x += random(-self.speed, self.speed)
        self.y += random(-self.speed, self.speed)
        self.fix_position()
        fill(self.color)
        ellipse(self.x, self.y, self.size, self.size)
        self.energy -= self.energy_comsumption['move']
    
    def fix_position(self):
        """ Mantem a ovelha dentro
        do campo de visao, a operacao
        de modulo na posicao da ovelha
        faz ela se manter dentro das posicoes
        posiveis do janela.
        """
        if self.x > width:
            self.x %= width
        
        if self.x < 0:
            self.x  += width
        
        if self.y > height:
            self.y %= height
        
        if self.y < 0:
            self.y += height
    
    def die(self, sheeps):
        """ Se a energia da ovelha
        chegar a zero ela morre. Ou seja,
        sai da lista de ovelhas vivas.
        """
        if self.energy <= 0:
            sheeps.remove(self)
    
    def reproduce(self, sheeps):
        """ A ovelha se reproduz se
        chegar no limiar de energia necessario
        para reproducao.
        """
        if self.energy >= self.reproduction_energy:
            self.energy -= self.energy_comsumption['reproduction']
            sheeps.append(Sheep(self.x, self.y, self.color))
    
    def try_eat(self, foods):
        """ A ovelha tenta se alimentar, se a posicao em
        que ela estiver for a posicao de uma comida disponivel,
        ela come.
        """
        food_rows = int(height/foods[0].size)
        x_scale = int(self.x/foods[0].size)
        y_scale = int(self.y/foods[0].size)
        food = foods[x_scale * food_rows + y_scale]
        if not food.eaten:
            self.energy += food.energy
            food.eated()
    
    def update(self, sheeps, foods):
        self.move()
        self.try_eat(foods)
        self.reproduce(sheeps)
        self.die(sheeps)
