class Board:

    def __init__(self) -> None:
        self.rows = 5
        self.columns = 5
        self.board = [ [ 0 ] * self.columns for _ in range(self.rows) ]

    def drawBoard(self):
        print('  ', end='')
        for i in range(self.columns):
            print(f'   {i}', end='')
        print('')

        print('  ', end='')   
        for i in range(self.columns):
            print('----', end='')
        print('')

        for i in range(self.rows):
            asciiBaseCode = 97 + i
            print(f'{chr(asciiBaseCode)}|', end='')
            for j in range(self.columns):
                print(f'   {self.board[i][j]}', end='')
            print('')
        
        

b = Board()
b.drawBoard()