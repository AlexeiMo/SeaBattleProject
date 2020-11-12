# from Ship import Ship
from GameField import GameField
import random

literals = "ABCDEFGHIJ"
directions = {
    1: "horizontal",
    2: "vertical"
}


def is_ship_fits(game_field: GameField, ship_length: int, ship_direction: str, ship_cords: tuple) -> bool:
    """Checks if field has enough space for the ship"""
    for i in range(1, 11):
        for j in literals:
            if ship_direction == 1:
                # add checking for ship to be placed
                pass
    return True


field = {}
for i in range(1, 11):
    field[i] = {}
    for j in literals:
        field[i][j] = False

gf = GameField(field)
ships = []

for i in range(1, 5):
    ship_len = 5 - i
    while i != 0:
        x = random.randint(1, 10)
        y = literals[random.randint(0, 9)]
        ship_cords = (x, y)
        print(ship_cords)
        for ship in ships:
            if not ship.is_ship_in_cell(ship_cords):
                pass    # stub for ship placing code
