class GameField:
    """
    Class which realizes "Sea battle" game field
    """

    def __init__(self, cell_states: list):
        """
        Constructor.

        Initialize a `cell_states` field which is `list`
            which values are also `list`s (which represents
            certain rows of field). In its turn, rows values are
            `bool`s ('True' or 'False') which represents state of
            certain cell (was it shot or not).

        :param cell_states: list of lists
            of cell states
        """
        self.cell_states = cell_states

    def get_cell_state(self, cords: tuple) -> bool:
        """
        Return `True` if cell was shot, else return `False`.

        :param cords: `tuple` which consists of x and y
            coordinates of certain cell
        :return: if cell was shot
        """
        x, y = cords    # x is number, y is letter
        return self.cell_states[x][y]

    def shoot_cell(self, cords: tuple) -> None:
        """
        Set the state of shot cell to `True` if it's `False`
        :param cords: coordinates of cell
        """
        x, y = cords    # x is number, y is letter
        if not self.get_cell_state(cords):
            self.cell_states[x][y] = True
