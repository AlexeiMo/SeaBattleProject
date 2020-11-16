from Ship import Ship
from GameField import GameField
import random

literals = "ABCDEFGHIJ"


def print_game_field(game_field: GameField) -> None:
    """
    Print "Sea battle" game field to the `console`

    :param game_field: field we want to print
    """

    print("   ", end='')
    for letter in literals:
        print(letter, end=' ')
    print()

    for i in range(10):
        print("{:<2}".format(i + 1), end=' ')

        for j in range(10):
            cell_cords = i, j

            if game_field.get_cell_state(cell_cords):
                for cords in killed_ship_parts:
                    if cell_cords == cords:
                        print("x", end=' ')
                        break
                else:
                    print("1", end=' ')
            else:
                print("-", end=' ')
        print()


def generate_ships() -> list:
    """
    Return randomly generated list of `Ship` objects

    :return: list of `Ship` objects
    """
    field = list()
    for i in range(10):
        field.append([])
        for j in range(10):
            field[i].append(0)  # init field with empty cells

    length = 4  # initial length (we'll start from 4-unit ship)
    ship_count = 1  # initial quantity of ships of `length` (at start we want to build 1 4-unit ship)
    local_ship_count = ship_count  # used in `while` loop

    ships_to_generate = []

    while length > 0:
        x = random.randint(0, 9)  # get random x coordinate of head of ship
        y = random.randint(0, 9)  # get random y coordinate of head of ship
        direction = random.randint(1, 2)  # 1 - vertical, 2 - horizontal

        x_limit = x + length if direction == 1 else x + 1
        y_limit = y + length if direction == 2 else y + 1

        if (direction == 1 and x + length > 10) or (direction == 2 and y + length > 10):  # if ship will be out of range
            continue
        for i in range(x, x_limit):
            for j in range(y, y_limit):
                start_pos_x = i - 1 if i > 0 else i
                start_pos_y = j - 1 if j > 0 else j
                end_pos_x = i + 1 if i < 9 else i
                end_pos_y = j + 1 if j < 9 else j
                for k in range(start_pos_x, end_pos_x + 1):
                    for m in range(start_pos_y, end_pos_y + 1):
                        if field[k][m] == 1:
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            ship_cords = []

            for i in range(x, x_limit):
                for j in range(y, y_limit):
                    field[i][j] = 1
                    ship_cords.append((i, j))

            ships_to_generate.append(Ship(ship_cords))

            local_ship_count -= 1
            if local_ship_count == 0:
                ship_count += 1
                length -= 1
                local_ship_count = ship_count

    return ships_to_generate


if __name__ == "__main__":
    ships = generate_ships()
    local_ships = list(ships)
    killed_ships = 0
    killed_ship_parts = []

    for ship in ships:
        print(ship.ship_cords)

    field = []
    for i in range(10):
        field.append([])
        for j in range(10):
            field[i].append(False)

    gf = GameField(field)

    while killed_ships < 10:
        print_game_field(gf)

        print()

        input_string = input(
            "Please select cell you want to shoot or 0 to quit\n(please enter your choice in format \"A:1\"): ").upper()

        if input_string == "0":  # quit the game
            print("Goodbye")
            break
        elif len(input_string) < 3 or input_string[0] not in literals or input_string[1] != ':' or not input_string[
            2].isdigit() or int(
                input_string[2]) not in range(1, 11):
            print("{} is incorrect input. Please try again".format(input_string))
            continue
        else:
            input_string = input_string.split(sep=':')
            x = int(input_string[1]) - 1
            y = 0
            for index, char in enumerate(literals):
                if char == input_string[0]:
                    y = index
                    break

            chosen_cell_cords = (x, y)

            gf.shoot_cell(chosen_cell_cords)

            for ship in local_ships:
                if ship.is_ship_in_cell(chosen_cell_cords):
                    ship.destroy_part_of_ship(chosen_cell_cords)
                    if ship.get_ship_health() == 0:
                        print("You killed the ship")
                        killed_ships += 1
                        local_ships.remove(ship)
                    else:
                        print("You hit the ship")
                    killed_ship_parts.append(chosen_cell_cords)
                    break
            else:
                print("You loose")

            if len(ships) == 0:
                print("You win!!!")
                break
