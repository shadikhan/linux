'''
Prompt: Build the object-oriented design for a two-player Connect Four game. Players take turns dropping discs into a
7-column, 6-row board. The first to align four of their own discs vertically, horizontally, or diagonally wins.

Notes:
- two-player
- discs
- board: 7-column, 6-row
- The first to align four of their own discs vertically, horizontally, or diagonally wins.

Requirements:
- Game is two-player
- Players take turns until one wins (condition above).
- Players can't take turns out of order.
- Players don't select their place on the board => they drop discs into an available column. Validate column is available.
- Once a player drops a disc in the column, we (who?) should check the board to make sure that the game is over.
- Forgot to talk about colors! And the draw path (noon-happy path)

Entities:
- Game
- Board
- Player

Relationships and Responsibilities:
- Game
    - Has a board
    - Has a player (x2)
    - Tracks winner, current player
- Board
    - Is of dimension 7-column, 6-row
    - Should allow placements (.place) and disallow invalid ones.

---
Class Design:

class Game:
    - board: Board
    - player1 : Player
    - player2 : Player
    - currentPlayer : Player
    - state: GameState
    - winner: Player | None
    
    # interacts with the board based on current player, sets winner
    + makeMove(col): -> bool

class Board:
    - _board: List[List[Color | None]]

    # places the disk on the col (validly)
    + place(col, color) -> (row, col) | None

    # checks if a 4-valid on the board
    + four_in_a_row(row, col) -> bool
    + is_full() -> bool

class Player:
    - color : Color

enum Color: RED | YELLOW
enum GameState: IN_PROGRESS | WIN | DRAW

Shad's Critiques:
What I liked:
    - SRP, Game manages state of the game, and just make moves with the board. Doesn't manage underlying board state.
    - Game tracking GameState and winner.
    - Seperate place from is_full

What I can improve on:
    - My initial four_in_a_row was a check against the entire board. Would've still been constant time, but better to
    check from curr + up/down, left/right topleft/bottom/right, topright,bottomleft. Go in those directions until OOB
    or color doesn't match curr.

'''

from enum import Enum

class GameState(Enum):
    IN_PROGRESS = 1
    WIN = 2
    DRAW = 3

class Color(Enum):
    RED = 1
    YELLOW = 2

class Game:
    def __init__(self):
        self.winner = None
        self.state = GameState.IN_PROGRESS
        pass

    def makeMove(self, col: int) -> bool:
        if self.state != GameState.IN_PROGRESS:
            return False
        
        result = self.board.place(col, self.currentPlayer.color)
        
        if result is None:
            return False
        
        row, col = result
        
        if self.board.four_in_a_row(row, col):
            self.state = GameState.WIN
            self.winner = self.currentPlayer
        elif self.board.is_full():
            self.state = GameState.DRAW

        if self.state == GameState.IN_PROGRESS:
            self.currentPlayer = self.player1 if self.currentPlayer == self.player1 else self.player2
        
        return True
    
class Board:
    def __init__(self):
        self.num_cols = 7
        self.num_rows = 6
        self.board = [[None for _ in range(self.num_cols)] for _ in range(self.num_rows)]
    
    def place(self, col: int, color: Color) -> tuple[int, int] | None:
        if not(0 <= col < self.num_cols):
            return None
        
        for i in range(self.num_rows - 1, -1, -1):
            if self.board[i][col] == None:
                self.board[i][col] = color
                return (i, col)
        
        return None
    
    def four_in_a_row(self, row: int, col: int) -> bool:
        # Validate row and col are in bounds.
        # Check four in a row and return
        pass
    
    def is_full(self) -> bool:
        pass
