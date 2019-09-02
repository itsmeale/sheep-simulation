from random import choice

from sheep import Sheep
from grass import Grass
from colors import SHEEP_COLORS


# Parametros da simulacao
SIM_WIDTH = 800
SIM_HEIGHT = 800
FOOD_SIZE = 5  # precisa ser um multiplo comum de SIM_WIDTH e SIM_HEIGHT
N_AGENTS = 1

# Lista de agentes e recursos
sheeps = list()
foods = list()


def setup():
    size(SIM_WIDTH, SIM_HEIGHT)
    noStroke()

    # Instancia os recursos
    for x in range(0, width, FOOD_SIZE):
        for y in range(0, height, FOOD_SIZE):
            foods.append(Grass(x, y, FOOD_SIZE))

    # Instancia os agentes
    for i in range(N_AGENTS):
        sheeps.append(
            Sheep(
                random(width),
                random(height),
                choice(SHEEP_COLORS)
            )
        )


def draw():
    background(0)

    for food in foods:
        food.update()

    for sheep in sheeps:
        sheep.update(sheeps, foods)
