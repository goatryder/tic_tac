class BoardView:
    def __init__(self, board):
        """
        should initialize inside Game object
        :param board: should be taken from Game object
        """
        self.__board = board

    def show_board(self):
        """
        print current board state
        """
        c0, c1, c2, c3, c4, c5, c6, c7, c8 = self.__board._get_states()

        def fabulous_cell(cell):
            if cell == 1:
                return "X"
            elif cell == 0:
                return "O"
            else:
                return " "

        print(
            "|%c|%c|%c|\n"
            "|%c|%c|%c|\n"
            "|%c|%c|%c|\n"
            % (fabulous_cell(c0), fabulous_cell(c1), fabulous_cell(c2),
               fabulous_cell(c3), fabulous_cell(c4), fabulous_cell(c5),
               fabulous_cell(c6), fabulous_cell(c7), fabulous_cell(c8)))
