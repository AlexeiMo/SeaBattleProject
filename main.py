from Ship import Ship
from GameField import GameField

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

    for i in range(1, 11):
        print("{:<2}".format(i), end=' ')

        for j in literals:
            cell_cords = i, j

            if game_field.get_cell_state(cell_cords):
                for ship in killed_ships:
                    if ship.is_ship_in_cell(cell_cords):
                        print("x", end=' ')
                        break
                else:
                    print("0", end=' ')
            else:
                for ship in killed_ships:
                    if ship.is_ship_in_cell(cell_cords):
                        print("1", end=' ')
                        break
                else:
                    print("-", end=' ')
        print()


if __name__ == "__main__":
    ships = [
        Ship([(1, "A")]),
        Ship([(1, "C"), (1, "D")]),
        Ship([(3, "A"), (3, "B"), (3, "C")]),
        Ship([(2, "F"), (3, "F"), (4, "F"), (5, "F")]),
    ]

    killed_ships = []

    field = {}
    for i in range(1, 11):
        field[i] = {}
        for j in literals:
            field[i][j] = False

    gf = GameField(field)

    while True:
        print_game_field(gf)

        print()

        input_string = input(
            "Please select cell you want to shoot or 0 to quit\n(please enter your choice in format \"A:1\"): ").upper()

        if input_string == "0":  # quit the game
            print("Goodbye")
            break
        elif input_string[0] not in literals or input_string[1] != ':' or not input_string[2].isdigit() or int(
                input_string[2]) not in range(1, 11):
            print("{} is incorrect input. Please try again".format(input_string))
            continue
        else:
            input_string = input_string.split(sep=':')
            chosen_cell_cords = (int(input_string[1]), input_string[0])

            gf.shoot_cell(chosen_cell_cords)

            for ship in ships:
                if ship.is_ship_in_cell(chosen_cell_cords):
                    ship.destroy_part_of_ship(chosen_cell_cords)
                    if ship.get_ship_health() == 0:
                        print("You killed the ship")
                        ships.remove(ship)
                    else:
                        print("You hit the ship")
                    break
            else:
                print("You loose")

            if len(ships) == 0:
                print("You win!!!")
                break
