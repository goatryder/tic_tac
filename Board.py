class Board:
    def __init__(self):
        self.__cells_state = []
        self.reset()

    def set_state(self, cell, state):
        self.__cells_state[cell] = state

    def get_state(self, cell):
        return self.__cells_state[cell]

    def reset(self):
        self.__cells_state = [-1 for i in range(9)]

    def _get_states(self):
        return self.__cells_state
