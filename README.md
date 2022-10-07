# Janggi-Game
2-player Korean Chess game developed in Python for CS162.
Rules: https://en.wikipedia.org/wiki/Janggi

Game uses object-oriented programming to simulate a Janggi board using a JanggiGame class. 
There are 2 players: blue and red, with blue as starting player. 

Locations on the board are specified with columns labeled a-i and rows labeled 1-10, with row 1 being the Red side and row 10 the Blue side. 

Relevant methods:
* A method called `get_game_state` that just returns one of these values, depending on the game state: 'UNFINISHED' or 'RED_WON' or 'BLUE_WON'.

* A method called `is_in_check` that takes as a parameter either 'red' or 'blue' and returns True if that player is in check, but returns False otherwise.

* A method called `make_move` that takes two parameters - strings that represent the square to move from and the square to move to.  For example, `make_move('b3', 'b10')`.  If the square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated move is not legal, or if the game has already been won, it should returns False.  Otherwise it makes the indicated move, removes any captured piece, updates the game state if necessary, updates whose turn it is, and returns True. If the `make_move` method is passed the same string for the square moved from and to, it is processed as the player passing their turn, and returns True.

* A method called `print_board` that prints the board at any given state.


Example:
game = JanggiGame()
game.print_board()
move_result = game.make_move('c1', 'e3') #should be False because it's not Red's turn
move_result = game.make_move('a7,'b7') #should return True
game.print_board()
blue_in_check = game.is_in_check('blue') #should return False
game.make_move('a4', 'a5') #should return True
game.print_board()
state = game.get_game_state() #should return UNFINISHED
game.make_move('b7','b6') #should return True
game.print_board()
game.make_move('b3','b6') #should return False because it's an invalid move
game.make_move('a1','a4') #should return True
game.make_move('c7','d7') #should return True
game.print_board()
game.make_move('a4','a4') #this will pass the Red's turn and return True

