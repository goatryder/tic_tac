class Game:
    def __init__(self, board, player_x, player_o, class_view):
        self.__board = board
        self.__player_x = player_x
        self.__player_o = player_o
        self.__view = class_view(self.__board)

    def __proper_winner_find(self):
        """
        Proper brute force winner finder
        Board cells represented as simple array for sake of simplicity
        but this method taste better with cells represented in 2D array
        so let's write some powerful loops :\

        :return: 2 if all cells used and no winner, 1 if player_x win,
                 0 if player_o win, -1 if no winner yet
        """
        cur_state = self.__board._get_states()
        board_size = int(pow(len(cur_state), 0.5))

        def check_cells_set(cell0, cell1, cell2):
            """
            inner func to check if there winner in cell set
            :param cell0:
            :param cell1:
            :param cell2:
            :return: 1 if X win, 0 if O win, -1 if no winner
            """

            if cell0 != -1 and cell0 == cell1 and cell0 == cell2:
                return cell0  # return winner
            return -1  # no winner yet

        # Checking rows
        for i in range(board_size):
            cells_set = []
            for j in range(board_size):
                cells_set.append(cur_state[i * board_size + j])
            rc = check_cells_set(*cells_set)  # unpacking list as args
            if rc != -1:
                return rc

        # Checking columns
        for i in range(board_size):
            cells_set = []
            for j in range(board_size):
                cells_set.append(cur_state[i + board_size * j])  # swapping + and * from prev to do so
            rc = check_cells_set(*cells_set)
            if rc != -1:
                return rc

        # Checking upper left to down right diagonal
        cells_set = []
        for i in range(board_size):
            cells_set.append(cur_state[
                                 i * (board_size + 1)
                                 ])
        rc = check_cells_set(*cells_set)
        if rc != -1:
            return rc

        # Checking upper right to down left diagonal
        cells_set = []
        for i in range(board_size):
            cells_set.append(cur_state[
                                 (board_size - 1) * (i + 1)
                                 ])
        rc = check_cells_set(*cells_set)
        if rc != -1:
            return rc

        # if no winner yet and board is full, return code 2
        # else mean board is not full and no winner, return corresponding code
        if -1 not in cur_state:
            return 2
        else:
            return -1

    # disable this masterpiece
    #    win_sets = [
    #        [0, 1, 2],
    #        [3, 4, 5],
    #        [6, 7, 8],
    #
    #        [0, 3, 6],
    #        [1, 4, 7],
    #        [2, 5, 8],
    #
    #        [0, 4, 8],
    #        [2, 4, 6]
    #    ]
    #
    #    def __find_winner(self):
    #        """
    #        kinda fast, simple, but work only with board 3x3
    #        :return: 2 if all cells used and no winner, 1 if player_x win,
    #                 0 if player_o win, -1 if no winner yet
    #        """
    #        cur_state = self.__board._get_states()
    #
    #        for w_set in self.win_sets:  # loop through win sets
    #            cell_id_0, cell_id_1, cell_id_2 = w_set
    #
    #            # initialize cells
    #            cell_0 = cur_state(cell_id_0)
    #            cell_1 = cur_state.get_state(cell_id_1)
    #            cell_2 = cur_state.get_state(cell_id_2)
    #
    #            # check if we have winner
    #            if cell_0 != -1 and cell_0 == cell_1 and cell_0 == cell_2:
    #                return cell_0  # return winner
    #            elif -1 not in cur_state:  # if !winner and all cells used return 2
    #                return 2
    #        return -1  # if !winner and !all cells used return -1

    def swap_players(self):
        """
        Method which allow to swap player sides after game finished

        :return: none
        """
        temp = self.__player_x
        self.__player_x = self.__player_o
        self.__player_o = temp

    def play(self):
        winner = -1  # -1: no winner yet, 0: player_o win, 1: player_x win, 2: no winner game over
        turn_switcher = True  # True : player_x turn, False : player_o turn

        def turn_handle():
            """
            helpful inner function for turn handling
            :return:
            """
            nonlocal turn_switcher  # also determine value of cell, (X)True: 1 (O)False: 0

            if turn_switcher:  # player_x move
                print(f"Waiting for {self.__player_x.name} (X) to move:")
            else:  # player_o move
                print(f"Waiting for {self.__player_o.name} (O) to move:")

            player_cell = input()
            if player_cell.isdecimal():
                player_cell = int(player_cell)
                if 0 <= player_cell <= 8:
                    if self.__board.get_state(player_cell) == -1:
                        self.__board.set_state(player_cell, turn_switcher)
                        turn_switcher = not turn_switcher
                    else:
                        print("Cell already used, pick another one")
                else:
                    print("Pick correct cell from 0 to 8!")
            else:
                print("Print correct cell number!")

        def game_result_handle():
            """
            inner function for winner congratulation and
            alter player_x, player_o stats

            :return:
            """
            nonlocal winner

            if winner == 2:
                print("Friendship wins")
            elif winner == 1:
                print(f"SHOUT-OUT FOR WINNER!!! {self.__player_x.name}"
                      f" smashed {self.__player_o.name} into dust")
                self.__player_x.wins += 1
                self.__player_o.loses += 1
            elif winner == 0:
                print(f"SHOUT-OUT FOR WINNER!!! {self.__player_o.name}"
                      f" smashed {self.__player_x.name} into dust")
                self.__player_o.wins += 1
                self.__player_x.loses += 1

            print(str(self.__player_o))
            print(str(self.__player_x))

        print("This is tic tac toe game.\n"
              "To move select cell number [0-8]")

        self.__view.show_board()
        while winner == -1:
            turn_handle()
            self.__view.show_board()
            # winner = self.__find_winner()
            winner = self.__proper_winner_find()

        game_result_handle()
        self.__board.reset()
        self.swap_players()
