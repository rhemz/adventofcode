class BingoBoardWon(Exception):

    def __init__(self, num, where, board):
        self.message = 'We have a winner, number {}!  Found on a {}.'.format(num, where)
        self.num = num
        self.sum = board.sum()
        self.board = board

        super().__init__(self.message)


class BingoBoard:

    def __init__(self, data):
        self._data = data
        self._board = []

    def parse(self):
        for row in self._data:
            self._board.append([[int(x), False] for x in row.split()])

    def check(self, num):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j][0] == num:
                    self._board[i][j][1] = True  # flip called flag to true

        # am I a wiener?
        self.is_winner(num)

    def is_winner(self, num):
        # check each row
        for row in self._board:
            if all([x[1] for x in row]):
                raise BingoBoardWon(num=num, where='row', board=self)

        # check each column
        for i in range(len(self._board[0])):
            if all([x[i][1] for x in self._board]):
                raise BingoBoardWon(num=num, where='column', board=self)

    def sum(self):
        total = 0
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if not self._board[i][j][1]:
                    total += self._board[i][j][0]

        return total
