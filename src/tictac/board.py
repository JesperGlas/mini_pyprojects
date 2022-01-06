from typing import List

NEW_BOARD: List[int] = [
    -1, -1, -1,
    -1, -1, -1,
    -1, -1, -1
]

class Board:
    def __init__(self, side: int = 3):
        self.side: int = side
        self.state: List[int] = [-1]*side**2

    def __str__(self) -> str:
        res: str = '.' + '_.'*self.side + '\n'

        for i, elem in enumerate(self.state):
            if i%self.side == 0:
                res += '|'
            if elem == -1:
                res += '_'
            elif elem == 0:
                res += 'o'
            elif elem == 1:
                res += 'x'
            res += '|'
            if i%self.side == self.side-1:
                res += '\n'

        return res

    def get(self) -> List[int]:
        return self.state

    def at_pos(self, pos: int) -> int:
        return self.state[pos]

    def get_size(self) -> int:
        return self.side

    def update(self, pos: int, player: int) -> bool:
        if self.state[pos] == -1:
            self.state[pos] = player
            return True
        
        return False

    def row(self, index: int) -> List[int]:
        start: int = index * self.side
        return self.state[start:start+self.side]

    def col(self, index: int) -> List[int]:
        indexes: List[int] = [i for i in range(index, len(self.state), self.side)]
        return [x for i, x in enumerate(self.state) if i in indexes]

    def diag(self, index: int) -> List[int]:
        indexes: List[int] = []
        if index == 0:
            indexes = [i for i in range(0, len(self.state), self.side+1)]
        else:
            indexes = [i for i in range(self.side-1, len(self.state)-1, self.side-1)]
        return [x for i, x in enumerate(self.state) if i in indexes]

    def finished(self) -> int:
        # Check rows
        rows = [self.row(i) for i in range(0, self.get_size())]
        for row in rows:
            if len(set(row)) == 1 and -1 not in row:
                return row[0]
        # Check cols
        cols = [self.col(i) for i in range(0, self.get_size())]
        for col in cols:
            if len(set(col)) == 1 and -1 not in col:
                return col[0]
        # Check diag
        diags = [self.diag(i) for i in range(0, 2)]
        for diag in diags:
            if len(set(diag)) == 1 and -1 not in diag:
                return diag[0]

        if -1 not in self.get():
            return 2

        return -1