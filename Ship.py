class Ship:
    """A representation of single ship on "Sea battle" game field."""

    def __init__(self, ship_cords: list):
        """
        Constructor.
        :param ship_cords: a list of tuples which represents
            ship parts coordinates
        """
        self.ship_cords = ship_cords

    def is_ship_in_cell(self, cell_cords: tuple) -> bool:
        """
        Return `True` if ship part is in cell
            of "Sea battle" game field, else return `False`.
        :param cell_cords: coordinates of cell
            which we want to check
        :return: `bool` which means
            if part of (or whole) ship is in cell
        """
        return cell_cords in self.ship_cords

    def destroy_part_of_ship(self, part_cords: tuple) -> None:
        """
        Remove part of ship
        :param part_cords: coordinates of part of ship
            which we want to remove
        """
        if self.is_ship_in_cell(part_cords):
            self.ship_cords.remove(part_cords)

    def get_ship_health(self) -> int:
        """
        Return length of unbroken ship parts;
            if there is no unbroken parts, return 0.

        :return: `int` which is number of unbroken ship parts
        """
        return len(self.ship_cords)

    def get_ship_cords(self) -> list:
        """
        Return `ship coordinates`

        :return: `list` of ship coordinates
        """
        return self.ship_cords
