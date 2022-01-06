from chess_func import allowed_moves


def show(chessboard):
    """Shows the chessboard in the console.
    DOES NOT WORK UNTIL ALL CLASES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!
    """
    WHITE = {
        Pawn: chr(9817),
        Knight: chr(9816),
        Queen: chr(9813),
        King: chr(9812),
        Rook: chr(9814),
        Bishop: chr(9815),
    }

    BLACK = {
        Pawn: chr(9823),
        Knight: chr(9822),
        Queen: chr(9819),
        King: chr(9818),
        Rook: chr(9820),
        Bishop: chr(9821),
    }
    for y in range(7, -1, -1):
        print(y, end='\t')

        for x in range(8):
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color == 'white':
                    print(WHITE[type(chessboard.board[x][y])], end='\t')


                else:
                    print(BLACK[type(chessboard.board[x][y])], end='\t')


            else:
                print('', end='\t')


        print('\n','-'*34)
    print('\t', end='')
    for x in range(8):
        print(x, end='\t')
    print()



class Chessboard:
    TURN = 0
    def __init__(self):
        self.color = ["white", "black"]
        self.board = [[None for i in range(8)] for a in range(8)]   #(i,7-a), change None if like to see postion on the chess_table

    def setup(self, start_setup):

        for el in range(8):
            for i in start_setup:
                self.board[i[el].x][i[el].y] = i[el]


    def list_allowed_moves(self,x,y):
        return self.board[x][y].list_allowed_movement()

    def move(self, from_x, from_y, to_x, to_y):
        # for el in self.board:
        #     if el != None:
        #         if el[0].x >= self.board[from_x][from_y].x +1:
        #             for i in self.board[from_x][from_y].list_allowed_movement():
        #                 del self.
        #             return "Nie mozna wykonac takiego ruchu"

        #
        # if Chessboard.TURN %2 ==0:
        #     self.board[from_x][from_y].color == "white"
        if self.board[to_x][to_y] == None:
            if (to_x, to_y) in self.board[from_x][from_y].list_allowed_movement():
                self.board[from_x][from_y].move(to_x, to_y)
                for el in range(8):
                    for i in self.board: #1
                        if i[el] is None:
                            pass
                        else:
                            self.board[i[el].x][i[el].y] = i[el] #2
                self.board[from_x][from_y] = None #3
        elif self.board[to_x][to_y].color == self.board[from_x][from_y].color:
            return "Nie można postawić figury na innej swojej figurze"

        Chessboard.TURN += 1

            #1 Podwójna pętle iterująca po tabeli szachow,
            #2 ma za zadanie przestawić figure na wybrane miejsce,
            #3 oraz usunac ja z poprzedniej pozycji





class Figure:
    def __init__(self, color, x, y):

        self.color = color
        self.x = x
        self.y =y

    def move(self, x, y):
            self.x = x
            self.y = y

    def __del__(self):
        pass
        # poczytac jak działa destruktor

class Pawn(Figure):
    def list_allowed_movement(self):
        self.list_moves_white = [(self.x, self.y+1),
                                 (self.x, self.y+2)]
        self.list_moves_black = [(self.x, self.y-1),
                                 (self.x, self.y-2)]
        if self.y >= 8 or self.y <= 0:
            return []
        if self.color == "white":
            return self.list_moves_white
        else:
            return self.list_moves_black

    def move(self, x, y):
        self.x = x
        self.y = y
        if len(self.list_moves_white) == 2:
            del self.list_moves_white[-1]
        if len(self.list_moves_black) == 2:
            del self.list_moves_black[-1]
        for el in m.board:
            if el != None:
                if el[0].x >= self.board[from_x][from_y].x +1:
                    for i in self.board[from_x][from_y].list_allowed_movement():

                        return "Nie mozna wykonac takiego ruchu"


class Knight(Figure):
    def list_allowed_movement(self):
        self.posible_moves = [(self.x + 1, self.y + 2),
                              (self.x - 1, self.y + 2),
                              (self.x - 2, self.y + 1),
                              (self.x + 2, self.y + 1),
                              (self.x - 2, self.y - 1),
                              (self.x + 2, self.y - 1),
                              (self.x + 1, self.y - 2),
                              (self.x - 1, self.y - 2),
                           ]

        return allowed_moves(self.posible_moves)


class Queen(Figure):
    def list_allowed_movement(self):
        self.posible_moves = []
        for el in range(1, 8):
            self.posible_moves.append((self.x + el, self.y))
            self.posible_moves.append((self.x, self.y + el))
            self.posible_moves.append((self.x - el, self.y))
            self.posible_moves.append((self.x, self.y - el))
            self.posible_moves.append((self.x + el, self.y + el))
            self.posible_moves.append((self.x - el, self.y - el))
            self.posible_moves.append((self.x + el, self.y - el))
            self.posible_moves.append((self.x - el, self.y + el))


        return allowed_moves(self.posible_moves)


class King(Figure):
    def list_allowed_movement(self):
        self.posible_moves = []

        for el in range(1, 2):
            self.posible_moves.append((self.x + el, self.y))
            self.posible_moves.append((self.x, self.y + el))
            self.posible_moves.append((self.x - el, self.y))
            self.posible_moves.append((self.x, self.y - el))
            self.posible_moves.append((self.x + el, self.y + el))
            self.posible_moves.append((self.x - el, self.y - el))
            self.posible_moves.append((self.x + el, self.y - el))
            self.posible_moves.append((self.x - el, self.y + el))

        return allowed_moves(self.posible_moves)


class Rook(Figure):
    def list_allowed_movement(self):

        self.posible_moves = []

        for el in range(1,8):
            self.posible_moves.append((self.x+el, self.y))
            self.posible_moves.append((self.x, self.y+el))
            self.posible_moves.append((self.x-el, self.y))
            self.posible_moves.append((self.x, self.y-el))

        return allowed_moves(self.posible_moves)

class Bishop(Figure):
    def list_allowed_movement(self):

        self.posible_moves = []

        for el in range(1,8):
            self.posible_moves.append((self.x+el, self.y+el))
            self.posible_moves.append((self.x-el, self.y-el))
            self.posible_moves.append((self.x+el, self.y-el))
            self.posible_moves.append((self.x-el, self.y+el))

        return allowed_moves(self.posible_moves)

def Begining_setup():
    white_pawn_list = []
    black_pawn_list = []
    # White figure

    W1knight = Knight("white", 1, 0)
    W2knigh = Knight("white", 6, 0)
    for i in range(8):
        WPawn = Pawn("white", i, 1)
        white_pawn_list.append(WPawn)
    W1Rook = Rook("white", 0, 0)
    W2Rook = Rook("white", 7, 0)
    W1Bishop = Bishop("white", 2, 0)
    W2Bishop = Bishop("white", 5, 0)
    WQueen = Queen("white", 3, 0)
    WKing = King("white", 4, 0)


    # Black figure

    B1knight = Knight("black", 1, 7)
    B2knigh = Knight("black", 6, 7)
    for i in range(8):
        BPawn = Pawn("black", i, 6)
        black_pawn_list.append(BPawn)
    B1Rook = Rook("black", 0, 7)
    B2Rook = Rook("black", 7, 7)
    B1Bishop = Bishop("black", 2, 7)
    B2Bishop = Bishop("black", 5, 7)
    BQueen = Queen("black", 3, 7)
    BKing = King("black", 4, 7)

    white_list = [W1Rook, W1knight, W1Bishop, WQueen, WKing, W2Bishop, W2knigh, W2Rook]
    black_list = [B1Rook, B1knight, B1Bishop, BQueen, BKing, B2Bishop, B2knigh, B2Rook]
    setup_list = [white_list, white_pawn_list, black_pawn_list, black_list]
    return setup_list


m = Chessboard()
m.setup(Begining_setup())
show(m)
m.move(3,0,6,3)
show(m)






