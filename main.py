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
    field = create_empty_field()

    length = 4  # initial length (we'll start from 4-unit ship)
    ship_count = 1  # initial quantity of ships of `length` (at start we want to build 1 4-unit ship)
    local_ship_count = ship_count  # used in `while` loop

    ships_to_generate = []

    while length > 0:
        x = random.randint(0, 9)  # get random x coordinate of head of ship
        y = random.randint(0, 9)  # get random y coordinate of head of ship
        direction = random.randint(1, 2)  # 1 - vertical, 2 - horizontal

        x_limit = get_x_limit(direction, length, x)
        y_limit = get_y_limit(direction, length, y)

        if (direction == 1 and x + length > 10) or (direction == 2 and y + length > 10):  # if ship will be out of range
            continue
        for i in range(x, x_limit):
            for j in range(y, y_limit):
                start_pos_x = get_start_position(i)
                start_pos_y = get_start_position(j)
                end_pos_x = get_end_position(i)
                end_pos_y = get_end_position(j)
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

            update_field(field, ship_cords, x, x_limit, y, y_limit)

            ships_to_generate.append(Ship(ship_cords))

            local_ship_count -= 1
            if local_ship_count == 0:
                ship_count += 1
                length -= 1
                local_ship_count = ship_count

    return ships_to_generate


def update_field(field, ship_cords, x, x_limit, y, y_limit):
    for i in range(x, x_limit):
        for j in range(y, y_limit):
            field[i][j] = 1
            ship_cords.append((i, j))


def get_y_limit(direction, length, y):
    y_limit = y + length if direction == 2 else y + 1
    return y_limit


def get_x_limit(direction, length, x):
    x_limit = x + length if direction == 1 else x + 1
    return x_limit


def get_end_position(index):
    end_pos = index + 1 if index < 9 else index
    return end_pos


def get_start_position(index):
    start_pos = index - 1 if index > 0 else index
    return start_pos


def create_empty_field():
    field = list()
    for i in range(10):
        field.append([])
        for j in range(10):
            field[i].append(0)  # init field with empty cells
    return field


if __name__ == "__main__":
    ships = generate_ships()
    local_ships = list(ships)
    killed_ship_parts = []

    for ship in ships:
        print(ship.ship_cords)  # TODO: remove after testing

    field = create_empty_field()

    gf = GameField(field)

    killed_ships = 0
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

            message = ""

            for ship in local_ships:
                if ship.is_ship_in_cell(chosen_cell_cords):

                    ship.destroy_part_of_ship(chosen_cell_cords)
                    if ship.get_ship_health() == 0:
                        message = "You killed the ship"
                        killed_ships += 1
                        local_ships.remove(ship)

                        for killed_ship in ships:
                            if killed_ship.is_ship_in_cell(chosen_cell_cords):
                                for x, y in killed_ship.get_ship_cords():
                                    start_pos_x = get_start_position(x)
                                    start_pos_y = get_start_position(y)
                                    end_pos_x = get_end_position(x)
                                    end_pos_y = get_end_position(y)
                                    for i in range(start_pos_x, end_pos_x + 1):
                                        for j in range(start_pos_y, end_pos_y + 1):
                                            cords = i, j
                                            gf.shoot_cell(cords)
                    else:
                        message = "You hit the ship"

                    killed_ship_parts.append(chosen_cell_cords)
                    break
            else:
                message = "You miss"

            print(message)
    else:
        print("You win!!!")
