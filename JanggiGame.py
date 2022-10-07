# Author: Samuel Suede
# Date: 3/11/2021
#: Description: Janggi: a Korean chess game. Pieces include general, guard, chariot, horse, elephant, and cannon.
#               Valid moves are detailed below. Blue goes first. Player can pass turn if not in check, so no
#               possibility of stalemate. A general is in check if it could be captured on the opposing player's
#               next move. Player cannot make a move that places themselves in check.  A player cannot make a move
#               that puts or leaves their general in check.The game ends when one player checkmates the other's general.

class Piece:
    """
    Parent class for a Janggi piece.
    """

    def __init__(self, color, position):
        """
        Initializes private data members color and position for a piece.
        """
        self._color = color
        self._position = position
        self._name = ""

    def __repr__(self):
        """'Dunder' method to represent objects with descriptors"""
        return self._color[0:1] + self._name[0:2] + self._position[0:1].upper()

    def get_name(self):
        """
        Returns name of piece.
        """
        return self._name

    def get_color(self):
        """
        Returns color of piece
        """
        return self._color

    def get_position(self):
        """
        Returns position of piece
        """
        return self._position

    def set_position(self, position):
        """
        Sets position of piece
        """
        self._position = position


class Soldier(Piece):
    """
     Represents a Soldier piece. Child class of Piece. Name's the piece and defines its move set.
     """

    def __init__(self, color, position):
        """
         Initializes private data members for Soldier piece.
         """
        super().__init__(color, position)
        self._name = "Soldier"

    def possible_moves(self):
        """
         Takes no parameters. Takes current position and maps out possible positions for piece to move. A soldier
         can move one position forward or sideways. In addition, it can move diagonally forward when in fortress.
         Soldier cannot move backwards.
         """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[self._position[0]]
        row = int(self._position[1:])

        if self._color == "blue":

            possible_move_list = [(column, row - 1), (column + 1, row), (column - 1, row)]

            if self._position == 'e2':
                possible_move_list += [(column - 1, row - 1), (column + 1, row - 1)]
            elif self._position == 'd3':
                possible_move_list.append((column + 1, row - 1))
            elif self._position == 'f3':
                possible_move_list.append((column - 1, row - 1))

        else:

            possible_move_list = [(column, row + 1), (column + 1, row), (column - 1, row)]

            if self._position == 'e9':
                possible_move_list += [(column - 1, row + 1), (column + 1, row + 1)]

            elif self._position == 'd8':
                possible_move_list.append((column + 1, row + 1))
            elif self._position == 'f8':
                possible_move_list.append((column - 1, row + 1))

        for (col, row) in possible_move_list:
            if col not in range(1, 10) or row not in range(1, 11):
                possible_move_list.remove((col, row))

        if len(possible_move_list) == 0:
            return []
        else:
            return possible_move_list


class General(Piece):
    """
    Represents a General piece. Child class of Piece. Name's the piece and defines its move set.
    """

    def __init__(self, color, position):
        """
        Initializes private data members for General piece.
        """
        super().__init__(color, position)
        self._name = "General"

    def possible_moves(self):
        """
        Takes no parameters. Takes current position and maps out possible positions for piece to move depending on move set.
        A general can move one position in any direction, but only within its fortress.
         """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[self._position[0]]
        row = int(self._position[1:])

        possible_move_list = [(column, row + 1), (column - 1, row), (column, row - 1), (column + 1, row)]
        diagonal_valid_square = ['d8', 'f8', 'e9', 'd10', 'f10', 'd1', 'f1', 'e2', 'd3', 'f3']

        if self._position in diagonal_valid_square:
            possible_move_list += [(column + 1, row + 1), (column - 1, row - 1), (column + 1, row - 1),
                                   (column - 1, row + 1)]

        final_possible_move_list = []

        if self._color == "blue":
            for (col, row) in possible_move_list:
                if col in range(4, 7) and row in range(8, 11):
                    final_possible_move_list += [(col, row)]
        else:
            for (col, row) in possible_move_list:
                if col in range(4, 7) and row in range(1, 4):
                    final_possible_move_list += [(col, row)]

        return final_possible_move_list


class Guard(Piece):
    """
    Represents an Guard piece. Child class of Piece. Name's the piece and defines its move set.
    A guard can move one position in any direction, but only within its fortress.
    """

    def __init__(self, color, position):
        """
        Initializes private data members for Guard piece.
        """
        super().__init__(color, position)
        self._name = "Guard"

    def possible_moves(self):
        """
        Takes no parameters. Takes current position and maps out possible positions for piece to move depending on move set.
        An elephant can move one position orthogonally and then one position diagonally, but cannot jump over pieces.
         """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[self._position[0]]
        row = int(self._position[1:])

        possible_move_list = [(column, row + 1), (column - 1, row), (column, row - 1), (column + 1, row)]
        diagonal_valid_square = ['d8', 'f8', 'e9', 'd10', 'f10', 'd1', 'f1', 'e2', 'd3', 'f3']

        if self._position in diagonal_valid_square:
            possible_move_list += [(column + 1, row + 1), (column - 1, row - 1), (column + 1, row - 1),
                                   (column - 1, row + 1)]

        final_possible_move_list = []

        if self._color == "blue":
            for (col, row) in possible_move_list:
                if col in range(4, 7) and row in range(8, 11):
                    final_possible_move_list += [(col, row)]
        else:
            for (col, row) in possible_move_list:
                if col in range(4, 7) and row in range(1, 4):
                    final_possible_move_list += [(col, row)]

        return final_possible_move_list


class Chariot(Piece):
    """
    Represents a Chariot piece. Child class of Piece. Name's the piece and defines its move set.
    """

    def __init__(self, color, position):
        """
        Initializes private data members for Chariot piece.
        """
        super().__init__(color, position)
        self._name = "Chariot"

    def possible_moves(self):
        """
        Takes no parameters. Takes current position and maps out possible positions for piece to move depending on move set.
        A chariot can move unlimited positions in one way orthogonally, but cannot jump over pieces. In addition, it can
        move unlimited positions in one way diagonally in fortress, but only in straight lines.
         """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[self._position[0]]
        row = int(self._position[1:])
        possible_move_list = []

        for num in range(1, 11):
            possible_move_list.append((column,num))

        for num in range(1,10):
            possible_move_list.append((num,row))

        possible_move_list.remove((column,row))
        possible_move_list.remove((column,row))

        if self._position in ['d8','e9','f10']:
            possible_move_list += [(4,8),(5,9),(6,10)]
            possible_move_list.remove((column, row))

        if self._position in ['f8','e9','d10']:
            possible_move_list += [(6,8),(5,9),(4,10)]
            possible_move_list.remove((column,row))

        if self._position in ['d1', 'e2', 'f3']:
                possible_move_list += [(4, 1), (5, 2), (6, 3)]
                possible_move_list.remove((column,row))

        if self._position in ['f1', 'e2', 'd3']:
                possible_move_list += [(6, 1), (5, 2), (4, 3)]
                possible_move_list.remove((column,row))


        return possible_move_list

class Horse(Piece):
    """
    Represents a Horse piece. Child class of Piece. Name's the piece and defines its move set. A horse can
    """

    def __init__(self, color, position):
        """
        Initializes private data members for a Horse piece.
        """
        super().__init__(color, position)
        self._name = "Horse"

    def possible_moves(self):
        """
        Takes no parameters. Takes current position and maps out possible positions for piece to move depending on move set.
        A horse can move one position orthogonally and then one position diagonally, but cannot jump over pieces.
         """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[self._position[0]]
        row = int(self._position[1:])
        possible_move_list = [(column - 1, row - 2), (column + 1, row - 2), (column + 2, row - 1),
                              (column + 2, row + 1), (column + 1, row + 2), (column - 1, row + 2),
                              (column - 2, row - 1), (column - 2, row + 1)]

        final_move_list = []

        for (col, row) in possible_move_list:
            if col in range(1, 10) and row in range(1, 11):
                final_move_list += [(col, row)]

        return final_move_list



class Elephant(Piece):
    """
    Represents an Elephant piece. Child class of Piece. Name's the piece and defines its move set.
    """

    def __init__(self, color, position):
        """
        Initializes private data members for an Elephant piece.
        """
        super().__init__(color, position)
        self._name = "Elephant"


    def possible_moves(self):
        """
        Takes no parameters. Takes current position and maps out possible positions for piece to move depending on move set.
        An elephant can move one position orthogonally and then two positions diagonally, but cannot jump over pieces.
        """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[self._position[0]]
        row = int(self._position[1:])
        possible_move_list = [(column - 2, row - 3), (column + 2, row - 3), (column + 3, row - 2),
                              (column + 3, row + 2), (column + 2, row + 3), (column - 2, row + 3),
                              (column - 3, row - 2), (column - 3, row + 2)]

        final_move_list = []

        for (col, row) in possible_move_list:
            if col in range(1, 10) and row in range(1, 11):
                final_move_list += [(col, row)]

        return final_move_list


class Cannon(Piece):
    """
    Represent a Cannon piece. Child class of Piece. Name's the piece and defines its move set.
    """

    def __init__(self, color, position):
        """
        Initializes private data members for Advisor piece.
        """
        super().__init__(color, position)
        self._name = "Cannon"

    def possible_moves(self):
        """
        Takes no parameters. Takes current position and maps out possible positions for piece to move depending on move set.
        A cannot can move unlimited positions in one way orthogonally, but only if there is exactly one piece between.
        A cannon cannot capture another cannon or jump over another cannon. A cannon can also capture diagonally within
        fortress if its in a corner.
         """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[self._position[0]]
        row = int(self._position[1:])
        possible_move_list = []

        for num in range(1, 11):
            possible_move_list.append((column,num))

        for num in range(1,10):
            possible_move_list.append((num,row))

        possible_move_list.remove((column,row))
        possible_move_list.remove((column,row))

        if self._position in ['d8','f10']:
            possible_move_list += [(4,8),(6,10)]
            possible_move_list.remove((column, row))

        if self._position in ['f8','d10']:
            possible_move_list += [(6,8),(4,10)]
            possible_move_list.remove((column,row))

        if self._position in ['d1', 'f3']:
                possible_move_list += [(4, 1), (6, 3)]
                possible_move_list.remove((column,row))

        if self._position in ['f1', 'd3']:
                possible_move_list += [(6, 1), (4, 3)]
                possible_move_list.remove((column,row))



        return possible_move_list


class JanggiGame:
    """Initializes Janggi game and gameboard. Interacts with Janggi object pieces using composition. Has methods that
     get game state, player's turn and who is in check. Has methods that validate moves and check for objects within rows, columns and diagonals.
     Has method make_move that checks for a valid move and changes board and game states. """

    def __init__(self):
        self._game_state = "UNFINISHED"
        self._players_turn = "tbd"
        self._is_in_check = ""
        self._captured_list_red = []
        self._captured_list_blue = []

        # initialize pieces
        self._red_soldier_1 = Soldier("red", "a4")
        self._red_soldier_2 = Soldier("red", "c4")
        self._red_soldier_3 = Soldier("red", "e4")
        self._red_soldier_4 = Soldier("red", "g4")
        self._red_soldier_5 = Soldier("red", "i4")
        self._red_general = General("red", "e2")
        self._red_guard_1 = Guard("red", "d1")
        self._red_guard_2 = Guard("red", "f1")
        self._red_chariot_1 = Chariot("red", "a1")
        self._red_chariot_2 = Chariot("red", "i1")
        self._red_horse_1 = Horse("red", "c1")
        self._red_horse_2 = Horse("red", "h1")
        self._red_elephant_1 = Elephant("red", "b1")
        self._red_elephant_2 = Elephant("red", "g1")
        self._red_cannon_1 = Cannon("red", "b3")
        self._red_cannon_2 = Cannon("red", "h3")

        self._blue_soldier_1 = Soldier("blue", "a7")
        self._blue_soldier_2 = Soldier("blue", "c7")
        self._blue_soldier_3 = Soldier("blue", "e7")
        self._blue_soldier_4 = Soldier("blue", "g7")
        self._blue_soldier_5 = Soldier("blue", "i7")
        self._blue_general = General("blue", "e9")
        self._blue_guard_1 = Guard("blue", "d10")
        self._blue_guard_2 = Guard("blue", "f10")
        self._blue_chariot_1 = Chariot("blue", "a10")
        self._blue_chariot_2 = Chariot("blue", "i10")
        self._blue_horse_1 = Horse("blue", "c10")
        self._blue_horse_2 = Horse("blue", "h10")
        self._blue_elephant_1 = Elephant("blue", "b10")
        self._blue_elephant_2 = Elephant("blue", "g10")
        self._blue_cannon_1 = Cannon("blue", "b8")
        self._blue_cannon_2 = Cannon("blue", "h8")

        # represents each player's chest
        self._red_pieces = [self._red_soldier_1,self._red_soldier_2,self._red_soldier_3,self._red_soldier_4,self._red_soldier_5,
                            self._red_general,self._red_guard_1,self._red_guard_2,self._red_chariot_1,self._red_chariot_2,
                            self._red_horse_1,self._red_horse_2,self._red_elephant_1,self._red_elephant_2,self._red_cannon_1,self._red_cannon_2]
        self._blue_pieces =[self._blue_soldier_1,self._blue_soldier_2,self._blue_soldier_3,self._blue_soldier_4,self._blue_soldier_5,
                            self._blue_general,self._blue_guard_1,self._blue_guard_2,self._blue_chariot_1,self._blue_chariot_2,
                            self._blue_horse_1,self._blue_horse_2,self._blue_elephant_1,self._blue_elephant_2,self._blue_cannon_1,self._blue_cannon_2]

        # places game pieces in their initial positions
        self._game_board = [[], [None, self._red_chariot_1, None, None, self._red_soldier_1, None, None,
                                 self._blue_soldier_1, None, None, self._blue_chariot_1],
                            [None, self._red_elephant_1, None, self._red_cannon_1, None, None, None, None,
                             self._blue_cannon_1, None, self._blue_elephant_1],
                            [None, self._red_horse_1, None, None, self._red_soldier_2, None, None, self._blue_soldier_2,
                             None, None, self._blue_horse_1],
                            [None, self._red_guard_1, None, None, None, None, None, None, None, None,
                             self._blue_guard_1],
                            [None, None, self._red_general, None, self._red_soldier_3, None, None, self._blue_soldier_3,
                             None, self._blue_general, None],
                            [None, self._red_guard_2, None, None, None, None, None, None, None, None,
                             self._blue_guard_2],
                            [None, self._red_elephant_2, None, None, self._red_soldier_4, None, None,
                             self._blue_soldier_4, None, None, self._blue_elephant_2],
                            [None, self._red_horse_2, None, self._red_cannon_2, None, None, None, None,
                             self._blue_cannon_2, None, self._blue_horse_2],
                            [None, self._red_chariot_2, None, None, self._red_soldier_5, None, None,
                             self._blue_soldier_5, None, None, self._blue_chariot_2]]

    def print_board(self):
        """
        Prints out game_board
        """

        print("  ----------------------------------------------------------------")
        print("1 |", self._game_board[1][1], "|", self._game_board[2][1], "|", self._game_board[3][1], "|",
              self._game_board[4][1], "|",
              self._game_board[5][1], "|", self._game_board[6][1], "|", self._game_board[7][1], "|",
              self._game_board[8][1], "|",
              self._game_board[9][1], "|",
              " Ca = Cannon, Ch = Chariot, El = Elephant, Ho = Horse, Gu = Guard, Ge = General")
        print("  ----------------------------------------------------------------")
        print("2 |", self._game_board[1][2], "|", self._game_board[2][2], "|", self._game_board[3][2], "|",
              self._game_board[4][2], "|",
              self._game_board[5][2], "|", self._game_board[6][2], "|", self._game_board[7][2], "|",
              self._game_board[8][2], "|",
              self._game_board[9][2], "|", " ColorPieceColumn i.e rChA = red Chariot in column A,",
              "bSoC = blue Soldier in column C")
        print("  ----------------------------------------------------------------")
        print("3 |", self._game_board[1][3], "|", self._game_board[2][3], "|", self._game_board[3][3], "|",
              self._game_board[4][3], "|",
              self._game_board[5][3], "|", self._game_board[6][3], "|", self._game_board[7][3], "|",
              self._game_board[8][3], "|",
              self._game_board[9][3], "|")
        print("  ----------------------------------------------------------------")
        print("4 |", self._game_board[1][4], "|", self._game_board[2][4], "|", self._game_board[3][4], "|",
              self._game_board[4][4], "|",
              self._game_board[5][4], "|", self._game_board[6][4], "|", self._game_board[7][4], "|",
              self._game_board[8][4], "|",
              self._game_board[9][4], "|")
        print("  ----------------------------------------------------------------")
        print("5 |", self._game_board[1][5], "|", self._game_board[2][5], "|", self._game_board[3][5], "|",
              self._game_board[4][5], "|",
              self._game_board[5][5], "|", self._game_board[6][5], "|", self._game_board[7][5], "|",
              self._game_board[8][5], "|",
              self._game_board[9][5], "|")
        print("  ----------------------------------------------------------------")
        print("6 |", self._game_board[1][6], "|", self._game_board[2][6], "|", self._game_board[3][6], "|",
              self._game_board[4][6], "|",
              self._game_board[5][6], "|", self._game_board[6][6], "|", self._game_board[7][6], "|",
              self._game_board[8][6], "|",
              self._game_board[9][6], "|")
        print("  ----------------------------------------------------------------")
        print("7 |", self._game_board[1][7], "|", self._game_board[2][7], "|", self._game_board[3][7], "|",
              self._game_board[4][7], "|",
              self._game_board[5][7], "|", self._game_board[6][7], "|", self._game_board[7][7], "|",
              self._game_board[8][7], "|",
              self._game_board[9][7], "|")
        print("  ----------------------------------------------------------------")
        print("8 |", self._game_board[1][8], "|", self._game_board[2][8], "|", self._game_board[3][8], "|",
              self._game_board[4][8], "|",
              self._game_board[5][8], "|", self._game_board[6][8], "|", self._game_board[7][8], "|",
              self._game_board[8][8], "|",
              self._game_board[9][8], "|")
        print("  ----------------------------------------------------------------")
        print("9 |", self._game_board[1][9], "|", self._game_board[2][9], "|", self._game_board[3][9], "|",
              self._game_board[4][9], "|",
              self._game_board[5][9], "|", self._game_board[6][9], "|", self._game_board[7][9], "|",
              self._game_board[8][9], "|",
              self._game_board[9][9], "|")
        print("  ________________________________________________________________")
        print("10|", self._game_board[1][10], "|", self._game_board[2][10], "|", self._game_board[3][10], "|",
              self._game_board[4][10], "|",
              self._game_board[5][10], "|", self._game_board[6][10], "|", self._game_board[7][10], "|",
              self._game_board[8][10], "|",
              self._game_board[9][10], "|")

    def get_game_state(self):
        """
        Returns the game's state
        """
        return self._game_state

    def get_players_turn(self):
        """
        Returns player of current turn
        """
        return self._players_turn

    def get_is_in_check(self):
        """
        Returns who is in check
        """
        if self._is_in_check == 'blue':
            return "blue"
        if self._is_in_check == 'red':
            return 'red'
        else:
             return 'no one in check'

    def is_in_check(self, color):
        """
        Takes in a parameter a color and returns True or False if that player is in check
        """

        if color == 'blue':
            return self._is_in_check == "blue"
        elif color == "red":
            return self._is_in_check == "red"
        else:
            return False


    def get_captured_list(self):
        """
        Takes no parameters and returns list of each player's captured pieces.
        """
        print("blue pieces: ", self._captured_list_blue,"red pieces: ",self._captured_list_red)

    def get_piece_from_position(self, position):
        """
        Takes a position column and row as parameters and returns the piece in that position
        """

        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

        column = key[position[0]]
        row = int(position[1:])

        return self._game_board[column][row]


    def get_objects_in_row(self, start_position,end_position):
        """Takes a start position and an end position as parameters and returns a list of pieces within a row inclusively.
        """

        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
        reverse_key = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
        end_column = key[end_position[0]]
        end_row = int(end_position[1:])
        start_column = key[start_position[0]]
        start_row = int(start_position[1:])

        if start_row !=end_row:

                    return False

        if start_column not in range(1,10) or end_column not in range(1,10) or start_row not in range(1,11) or end_row not in range(1,11):
            return False

        object_list = []
        row = start_row

        if end_column > start_column:

            for num in range(start_column, end_column + 1):
                a_position = reverse_key[num] + str(row)
                a_piece = self.get_piece_from_position(a_position)
                object_list.append(self.get_piece_from_position(a_position))


        elif start_column > end_column:
            for num in range(end_column, start_column + 1):
                a_position = reverse_key[num] + str(row)
                a_piece = self.get_piece_from_position(a_position)
                object_list.append(self.get_piece_from_position(a_position))

            object_list.reverse()

        else:
            object_list.append(self.get_piece_from_position(start_position))

        final_object_list = []

        for an_object in object_list:
            if an_object is not None:
                final_object_list.append(an_object)

        return final_object_list

    def get_objects_in_column(self, start_position,end_position):
        """Takes a start position and an end position as parameters and returns pieces within that column in a list inclusively.
        """

        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
        end_column = key[end_position[0]]
        end_row = int(end_position[1:])
        start_column = key[start_position[0]]
        start_row = int(start_position[1:])

        if start_column != end_column:
            return False

        if start_column not in range(1, 10) or end_column not in range(1, 10) or start_row not in range(1,11) or end_row not in range(1, 11):
            return False

        object_list = []

        if end_row > start_row:

            for num in range(start_row, end_row + 1):
                a_position = start_position[0] + str(num)
                a_piece = self.get_piece_from_position(a_position)
                object_list.append(self.get_piece_from_position(a_position))


        elif start_row > end_row:
            for num in range(end_row, start_row + 1):
                a_position = start_position[0] + str(num)
                a_piece = self.get_piece_from_position(a_position)
                object_list.append(self.get_piece_from_position(a_position))

            object_list.reverse()

        else:
            object_list.append(self.get_piece_from_position(start_position))

        final_object_list = []

        for an_object in object_list:
            if an_object is not None:
                final_object_list.append(an_object)

        return final_object_list

    def get_objects_in_diagonal(self, start_position,end_position):

        """Takes a start position and an end position as parameters and returns pieces in that diagonal inclusively.
        """

        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
        reverse_key = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i'}
        end_column = key[end_position[0]]
        end_row = int(end_position[1:])
        start_column = key[start_position[0]]
        start_row = int(start_position[1:])

        if abs(end_column-start_column) != abs(end_row-start_row):
            return False

        if start_column not in range(1, 10) or end_column not in range(1, 10) or start_row not in range(1,11) or end_row not in range(1, 11):
            return False

        object_list = []

        if end_column > start_column:

            row = start_row

            if end_row > start_row:

                for num in range(start_column, end_column + 1):
                    a_piece = reverse_key[num] + str(row)
                    object_list.append(self.get_piece_from_position(a_piece))
                    row += 1


            elif end_row < start_row:

                for num in range(start_column, end_column + 1):
                    a_piece = reverse_key[num] + str(row)
                    object_list.append(self.get_piece_from_position(a_piece))
                    row -= 1


        elif start_column > end_column:

            row = end_row

            if end_row > start_row:

                for num in range(end_column, start_column + 1):
                    a_piece = reverse_key[num] + str(row)
                    object_list.append(self.get_piece_from_position(a_piece))
                    row -= 1

                object_list.reverse()


            elif start_row > end_row:

                for num in range(end_column, start_column + 1):
                    a_piece = reverse_key[num] + str(row)
                    object_list.append(self.get_piece_from_position(a_piece))
                    row += 1

                object_list.reverse()

            else:
                object_list.append(start_position)


        final_object_list = []

        for an_object in object_list:
            if an_object is not None:
                final_object_list.append(an_object)

        return final_object_list

    def is_valid_move(self,current_position,new_position):
        """Takes as parameters a current position and new position and returns True or False depending on validity of move"""

        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
        reverse_key = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i'}
        new_column = key[new_position[0]]
        new_row = int(new_position[1:])
        current_column = key[current_position[0]]
        current_row = int(current_position[1:])

        if self.get_piece_from_position(current_position) is not None:
            piece = self.get_piece_from_position(current_position)
        else:
            return False

        if self.get_piece_from_position(new_position) is not None:
            if piece.get_color() == self.get_piece_from_position(new_position).get_color():
                return False

        if (new_column,new_row) not in piece.possible_moves():
            return False

        # Ensures that chariot does not jump over pieces
        if piece.get_name() == 'Chariot':
            row_objects = self.get_objects_in_row(current_position,new_position)
            column_objects = self.get_objects_in_column(current_position,new_position)
            diagonal_objects = self.get_objects_in_diagonal(current_position,new_position)

            if current_row == new_row and (len(row_objects) == 1 or (len(row_objects) == 2 and row_objects[1] == self.get_piece_from_position(new_position))):
                return True
            if current_column == new_column and (len(column_objects) == 1 or (len(column_objects) == 2 and column_objects[1] == self.get_piece_from_position(new_position))):
                return True
            if current_row != new_row and current_column != new_column and (len(diagonal_objects) == 1 or (len(diagonal_objects) == 2 and diagonal_objects[1] == self.get_piece_from_position(new_position))):
                return True

            return False

        # Ensures that cannon has exactly one piece to jump over, is not jumping over a cannon and is not capturing another cannon
        if piece.get_name() == 'Cannon':
            row_objects = self.get_objects_in_row(current_position, new_position)
            column_objects = self.get_objects_in_column(current_position, new_position)
            diagonal_objects = self.get_objects_in_diagonal(current_position, new_position)

            if current_row == new_row and len(row_objects) == 3:
                if row_objects[1].get_name() != 'Cannon' and row_objects[2].get_name() != 'Cannon':
                    return True
            if current_column == new_column and len(column_objects) == 3:
                if column_objects[1].get_name() != 'Cannon' and column_objects[2].get_name() != 'Cannon':
                    return True
            if current_row != new_row and current_column != new_column and diagonal_objects == 3:
                if diagonal_objects[1].get_name() != 'Cannon' and diagonal_objects[2].get_name() != 'Cannon':
                    return True


            if current_row == new_row and len(row_objects) == 2:
                if self.get_piece_from_position(new_position) is None and row_objects[1].get_name() != 'Cannon':
                    return True
            if current_column == new_column and len(column_objects) == 2:
                if self.get_piece_from_position(new_position) is None and column_objects[1].get_name() != 'Cannon':
                    return True
            if current_row != new_row and current_column != new_column and diagonal_objects == 2:
                if self.get_piece_from_position(new_position) is None and diagonal_objects[1].get_name() != 'Cannon':
                    return True

            return False

        # Ensures that horse is not jumping over pieces
        if piece.get_name() == "Horse":

            if current_row > new_row and abs(current_column-new_column) == 1:
                check_position = reverse_key[current_column]+str(current_row-1)
                if self.get_piece_from_position(check_position) is None:
                    return True
            if current_row < new_row and abs(current_column-new_column) == 1:
                check_position = reverse_key[current_column] + str(current_row + 1)
                if self.get_piece_from_position(check_position) is None:
                    return True
            if current_column > new_column and abs(current_row-new_row) == 1:
                check_position = reverse_key[current_column-1] + str(current_row)
                if self.get_piece_from_position(check_position) is None:
                    return True
            if current_column < new_column and abs(current_row-new_row) == 1:
                check_position = reverse_key[current_column+1] + str(current_row)
                if self.get_piece_from_position(check_position) is None:
                    return True

            return False

        #Ensures that elephant is not jumping over pieces
        if piece.get_name() == 'Elephant':
            if current_row > new_row and current_column > new_column:
                diagonal_position_1 = reverse_key[new_column+1]+str(new_row+1)
                diagonal_position_2 = reverse_key[new_column+2]+str(new_row+2)
                check_objects = self.get_objects_in_diagonal(diagonal_position_1,diagonal_position_2)
                if len(check_objects) == 0:
                    return True

            if current_row > new_row and current_column < new_column:
                diagonal_position_1 = reverse_key[new_column - 1] + str(new_row + 1)
                diagonal_position_2 = reverse_key[new_column - 2] + str(new_row + 2)
                check_objects = self.get_objects_in_diagonal(diagonal_position_1, diagonal_position_2)
                if len(check_objects) == 0:
                    return True

            if current_row < new_row and current_column > new_column:
                diagonal_position_1 = reverse_key[new_column + 1] + str(new_row - 1)
                diagonal_position_2 = reverse_key[new_column + 2] + str(new_row - 2)
                check_objects = self.get_objects_in_diagonal(diagonal_position_1, diagonal_position_2)
                if len(check_objects) == 0:
                    return True


            if current_row < new_row and current_column < new_column:
                diagonal_position_1 = reverse_key[new_column - 1] + str(new_row - 1)
                diagonal_position_2 = reverse_key[new_column - 2] + str(new_row - 2)
                check_objects = self.get_objects_in_diagonal(diagonal_position_1, diagonal_position_2)
                if len(check_objects) == 0:
                    return True

            return False

        # returns True for General or Soldier since no further restrictions of movement
        if piece.get_name() == "General" or piece.get_name() == "Soldier":
            return True


    def make_move(self, current_position, new_position):
        """Takes as parameters a current position and a new position, makes a move if valid, checks if a player is in check or checkmated,
        and updates player's turn and game state
        """
        key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
        reverse_key = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i'}
        new_column = key[new_position[0]]
        new_row = int(new_position[1:])
        current_column = key[current_position[0]]
        current_row = int(current_position[1:])

        # ends game if game has been won
        if self._game_state != "UNFINISHED":
            return False

        # allows a player to pass if player is not in check
        if current_position == new_position:

            if self._is_in_check == 'blue' and self._players_turn == 'blue':
                    return False
            elif self._is_in_check == 'red' and self._players_turn == 'red':
                    return False
            else:
                if self._players_turn == 'blue':
                    self._players_turn = 'red'
                elif self._players_turn == 'red':
                    self._players_turn = 'blue'
                return True

        # picks up a piece only if there is a piece present
        if self.get_piece_from_position(current_position) is not None:
            piece = self.get_piece_from_position(current_position)
        else:
            return False

        # ensures that blue is first player to go
        if self._players_turn == 'tbd' and piece.get_color() == 'red':
            return False
        elif self._players_turn == 'tbd' and piece.get_color() == 'blue':
            self._players_turn = 'blue'

        # ensures that it is correct player's turn to go
        if piece.get_color() != self._players_turn:
            if self._players_turn == "tbd":
                pass
            else:
                return False

        # ensures that position is within game board
        if new_row not in range(1, 11) or new_column not in range(1, 10):
            return False


        # ensures that move is ultimately valid
        if self.is_valid_move(current_position,new_position) is False:
            return False

        # save captured piece in case player places themselves in check and need to reverse the move
        saved_captured_piece = self.get_piece_from_position(new_position)
        # change piece's listed position
        piece.set_position(new_position)

        #  If a piece is captured, change its listed position to captured
        if self.get_piece_from_position(new_position) is not None:
           captured_piece = self.get_piece_from_position(new_position)
           captured_piece.set_position("captured")

           ### List of captured pieces
           if captured_piece.get_color() == "blue":
               self._captured_list_blue.append(captured_piece)
           elif  captured_piece.get_color() == "red":
               self._captured_list_red.append(captured_piece)

        # update board to reflect new positions
        self._game_board[new_column][new_row] = piece
        self._game_board[current_column][current_row] = None


        if self.get_players_turn() == 'blue':
            # reverse move if player places themselves in check and return False
            for a_red_piece in self._red_pieces:
                if a_red_piece.get_position() != 'captured':
                    if self.is_valid_move(a_red_piece.get_position(),self._blue_general.get_position()) is True:
                        if saved_captured_piece is not None:
                            saved_captured_piece.set_position(new_position)
                        piece.set_position(current_position)
                        self._game_board[new_column][new_row] = saved_captured_piece
                        self._game_board[current_column][current_row] = piece
                        return False
                    else:
                        continue

            # if player was in check, then take them out of check
            self._is_in_check = ""

            # if opposite player is in check after move, then update is_in_check
            for a_blue_piece in self._blue_pieces:
                if a_blue_piece.get_position() != "captured":
                    if self.is_valid_move(a_blue_piece.get_position(),self._red_general.get_position()) is True:
                        self._is_in_check = 'red'
                        break
                    else:
                        continue

            # if opposite player is in check, determine if they are in checkmate
            if self._is_in_check == 'red':

                red_can_capture_piece = False
                # if opposite player can capture piece that placed them in check, then opposite player can
                # get out of check in next move. Set red_can_capture_piece to True.
                for a_red_piece in self._red_pieces:
                    if a_red_piece.get_position() != "captured":
                        if self.is_valid_move(a_red_piece.get_position(),piece.get_position()) is True:
                            red_can_capture_piece = True
                            break

                general_column = key[self._red_general.get_position()[0]]
                general_row = int(self._red_general.get_position()[1:])
                piece_column = key[piece.get_position()[0]]
                piece_row = int(self._red_general.get_position()[1:])
                red_can_block_piece = False



                # Check to see if special pieces can be blocked to prevent a check
                if piece.get_name() == 'Horse':
                    if general_row > piece_row and abs(piece_column - general_column) == 1:
                        check_position = reverse_key[piece_column] + str(general_row - 1)
                    if general_row < piece_row and abs(piece_column - general_column) == 1:
                        check_position = reverse_key[piece_column] + str(piece_row + 1)
                    if piece_column > general_column and abs(piece_row - general_row) == 1:
                        check_position = reverse_key[piece_column - 1] + str(piece_row)
                    if piece_column < general_column and abs(piece_row - general_row) == 1:
                        check_position = reverse_key[piece_column + 1] + str(piece_row)

                    for a_red_piece in self._red_pieces:
                        if a_red_piece.get_position() != 'captured' and a_red_piece.get_name() != 'General':
                            if self.is_valid_move(a_red_piece.get_position(), check_position) is True:
                                red_can_block_piece = True
                                break
                            else:
                                continue

                if piece.get_name() == 'Elephant':
                    if piece_row > general_row and piece_column > general_column:
                        diagonal_position_1 = reverse_key[general_column + 1] + str(general_row + 1)
                        diagonal_position_2 = reverse_key[general_column + 2] + str(general_row + 2)
                        check_positions = [diagonal_position_1, diagonal_position_2]


                    if piece_row > general_row and piece_column < general_column:
                        diagonal_position_1 = reverse_key[general_column - 1] + str(general_row + 1)
                        diagonal_position_2 = reverse_key[general_column - 2] + str(general_row + 2)
                        check_positions = [diagonal_position_1, diagonal_position_2]

                    if piece_row < general_row and piece_column > general_column:
                        diagonal_position_1 = reverse_key[general_column + 1] + str(general_row - 1)
                        diagonal_position_2 = reverse_key[general_column + 2] + str(general_row - 2)
                        check_positions = [diagonal_position_1, diagonal_position_2]

                    if piece_row < general_row and piece_column < general_column:
                        diagonal_position_1 = reverse_key[general_column - 1] + str(general_row - 1)
                        diagonal_position_2 = reverse_key[general_column - 2] + str(general_row - 2)
                        check_positions = [diagonal_position_1, diagonal_position_2]


                    for a_position in check_positions:

                        for a_red_piece in self._red_pieces:
                            if a_red_piece.get_position() != 'captured' and a_red_piece.get_name() != 'General':
                                if self.is_valid_move(a_red_piece.get_position(),a_position) is True:
                                    red_can_block_piece = True
                                    break

                        if red_can_block_piece is True:
                            break


                a_red_fortress_position = ['d1','e1','f1','d2','e2','f2','d3','e3','f3']
                valid_moves = set()

                # Determine valid positions for general and place them in a set named valid_moves
                for a_position in a_red_fortress_position:
                    if self.is_valid_move(self._red_general.get_position(),a_position) is True:
                        valid_moves.add(a_position)

                valid_moves.add(self._red_general.get_position())
                saved_red_general_position = self._red_general.get_position()
                red_in_check_position = set()

                # For a general's valid moves, move the general to that position and see if opposite player's pieces
                # can capture the general. If they can, then place that position in a set named red_in_check_position.
                for a_position in valid_moves:

                    if saved_red_general_position != a_position:
                        self._red_general.set_position(a_position)
                        saved_piece = self.get_piece_from_position(a_position)
                        if saved_piece is not None:
                            saved_piece.set_position("captured")

                        self._game_board[key[a_position[0]]][int(a_position[1:])] = self._red_general
                        self._game_board[key[saved_red_general_position[0]]][int(saved_red_general_position[1:])] = None

                    for a_blue_piece in self._blue_pieces:
                        if a_blue_piece.get_position() != "captured":
                            if self.is_valid_move(a_blue_piece.get_position(),self._red_general.get_position()) is True:
                                red_in_check_position.add(self._red_general.get_position())

                    if saved_red_general_position != a_position:
                        self._red_general.set_position(saved_red_general_position)

                        if saved_piece is not None:
                            saved_piece.set_position(a_position)

                        self._game_board[key[saved_red_general_position[0]]][int(saved_red_general_position[1:])] = self._red_general
                        self._game_board[key[a_position[0]]][int(a_position[1:])] = saved_piece

                #If the set valid_moves is a subset of red_in_check_in_position, then
                # red will be in check for all of its valid moves, and red_general_cannot_move is True.
                red_general_cannot_move = valid_moves.issubset(red_in_check_position)
                # If below conditions are true, then blue player has won. Update game state.
                if red_general_cannot_move is True and red_can_capture_piece is False and red_can_block_piece is False:
                    self._game_state = "BLUE_WON"


        elif self.get_players_turn() == 'red':
            # reverse move if player places themselves in check and return False
            for a_blue_piece in self._blue_pieces:
                if a_blue_piece.get_position() != 'captured':
                    if self.is_valid_move(a_blue_piece.get_position(), self._red_general.get_position()) is True:

                        if saved_captured_piece is not None:
                            saved_captured_piece.set_position(new_position)
                        piece.set_position(current_position)
                        self._game_board[new_column][new_row] = saved_captured_piece
                        self._game_board[current_column][current_row] = piece
                        return False
                    else:
                        continue

            # if player was in check, take them out of check
            self._is_in_check = ""

            # if opposite player is in check after move, then update is_in_check
            for a_red_piece in self._red_pieces:
                if a_red_piece.get_position() != "captured":
                    if self.is_valid_move(a_red_piece.get_position(), self._blue_general.get_position()) is True:
                        self._is_in_check = 'blue'
                        break
                    else:
                        continue

            # if opposite player is in check, determine if they are in checkmate
            if self._is_in_check == 'blue':

                blue_can_capture_piece = False
                # if opposite player can capture piece that placed them in check, then opposite player can
                # get out of check in next move. Set blue_can_capture_piece to True.
                for a_blue_piece in self._red_pieces:
                    if a_blue_piece.get_position() != "captured":
                        if self.is_valid_move(a_blue_piece.get_position(), piece.get_position()) is True:
                            blue_can_capture_piece = True
                            break

                general_column = key[self._blue_general.get_position()[0]]
                general_row = int(self._blue_general.get_position()[1:])
                piece_column = key[piece.get_position()[0]]
                piece_row = int(self._blue_general.get_position()[1:])
                blue_can_block_piece = False


                # Check to see if special pieces can be blocked to prevent a check
                if piece.get_name() == 'Horse':
                    if general_row > piece_row and abs(piece_column - general_column) == 1:
                        check_position = reverse_key[piece_column] + str(general_row - 1)
                    if piece_row < general_row and abs(piece_column - general_column) == 1:
                        check_position = reverse_key[piece_column] + str(piece_row + 1)
                    if piece_column > general_column and abs(piece_row - general_row) == 1:
                        check_position = reverse_key[piece_column - 1] + str(piece_row)
                    if piece_column < general_column and abs(piece_row - general_row) == 1:
                        check_position = reverse_key[piece_column + 1] + str(piece_row)

                    for a_blue_piece in self._blue_pieces:
                        if a_blue_piece.get_position() != 'captured' and a_blue_piece.get_name() != 'General':
                            if self.is_valid_move(a_blue_piece.get_position(), check_position) is True:
                                blue_can_block_piece = True
                                break
                            else:
                                continue

                if piece.get_name() == 'Elephant':
                    if piece_row > general_row and piece_column > general_column:
                        diagonal_position_1 = reverse_key[general_column + 1] + str(general_row + 1)
                        diagonal_position_2 = reverse_key[general_column + 2] + str(general_row + 2)
                        check_positions = [diagonal_position_1, diagonal_position_2]


                    if piece_row > general_row and piece_column < general_column:
                        diagonal_position_1 = reverse_key[general_column - 1] + str(general_row + 1)
                        diagonal_position_2 = reverse_key[general_column - 2] + str(general_row + 2)
                        check_objects = [diagonal_position_1, diagonal_position_2]

                    if piece_row < general_row and piece_column > general_column:
                        diagonal_position_1 = reverse_key[general_column + 1] + str(general_row - 1)
                        diagonal_position_2 = reverse_key[general_column + 2] + str(general_row - 2)
                        check_positions = [diagonal_position_1, diagonal_position_2]

                    if piece_row < general_row and piece_column < general_column:
                        diagonal_position_1 = reverse_key[general_column - 1] + str(general_row - 1)
                        diagonal_position_2 = reverse_key[general_column - 2] + str(general_row - 2)
                        check_positions = [diagonal_position_1, diagonal_position_2]

                    for a_position in check_positions:

                        for a_blue_piece in self._blue_pieces:
                            if a_blue_piece.get_position() != 'captured' and a_blue_piece.get_name() != 'General':
                                if self.is_valid_move(a_blue_piece.get_position(),a_position) is True:
                                    blue_can_block_piece = True
                                    break

                        if blue_can_block_piece is True:
                            break

                a_blue_fortress_position = ['d8', 'e8', 'f8', 'd9', 'e9', 'f9', 'd10', 'e10', 'f10']
                valid_moves = set()

                # Determine valid positions for general and place them in a set named valid_moves
                for a_position in a_blue_fortress_position:
                    if self.is_valid_move(self._blue_general.get_position(), a_position) is True:
                        valid_moves.add(a_position)

                valid_moves.add(self._blue_general.get_position())
                saved_blue_general_position = self._blue_general.get_position()
                blue_in_check_position = set()

                # For a general's valid moves, move the general to that position and see if opposite player's pieces
                # can capture the general. If they can, then place that position in a set named blue_in_check_position.
                for a_position in valid_moves:

                    if saved_blue_general_position != a_position:

                        self._blue_general.set_position(a_position)
                        saved_piece = self.get_piece_from_position(a_position)
                        if saved_piece is not None:
                            saved_piece.set_position("captured")

                        self._game_board[key[a_position[0]]][int(a_position[1:])] = self._blue_general
                        self._game_board[key[saved_blue_general_position[0]]][int(saved_blue_general_position[1:])] = None

                    for a_red_piece in self._red_pieces:
                        if a_red_piece.get_position() != "captured":
                            if self.is_valid_move(a_red_piece.get_position(), self._blue_general.get_position()) is True:
                                blue_in_check_position.add(self._blue_general.get_position())

                    if saved_blue_general_position != a_position:

                        self._blue_general.set_position(saved_blue_general_position)

                        if saved_piece is not None:
                            saved_piece.set_position(a_position)

                        self._game_board[key[saved_blue_general_position[0]]][int(saved_blue_general_position[1:])] = self._blue_general
                        self._game_board[key[a_position[0]]][int(a_position[1:])] = saved_piece

                #If the set valid_moves is a subset of blue_in_check_in_position, then
                # blue will be in check for all of its valid moves. Set blue_general_cannot_move to True.
                blue_general_cannot_move = valid_moves.issubset(blue_in_check_position)
                # If below conditions are true, then blue player has won. Update game state.
                if blue_general_cannot_move is True and blue_can_capture_piece is False and blue_can_block_piece is False:
                    self._game_state = "RED_WON"


        # If game is unfinished, then update player's turn and return True
        if self._game_state == 'UNFINISHED':
            if self._players_turn == 'red':
                self._players_turn = 'blue'
            elif self._players_turn == 'blue':
                self._players_turn = 'red'

        return True

