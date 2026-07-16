## Flow Chart

CONNECT FOUR GAME
```
├── Initialisation
│
├── Button Class
│   ├── __init__()
│   │   └── Creates button
│   │
│   ├── draw()
│   │   └── Displays button
│   │
│   └── clicked()
│       └── Detects button press
│
├── Game Functions
│   │
│   ├── reset_game()
│   │   └── Resets board and variables
│   │
│   ├── get_next_row()
│   │   └── Finds empty position for piece
│   │
│   └── check_win()
│       └── Checks four connected pieces
│
├── Drawing Functions
│   │
│   ├── draw_ui()
│   │   └── Displays text and scores
│   │
│   ├── draw_board()
│   │   └── Draws Connect Four board
│   │
│   └── draw_hover_piece()
│       └── Shows preview piece
│
└── Main Game Loop
    ├── Receive Events
    ├── Update Game State
    └── Draw Screen
```
# How the code works
## Settings
- pygame.init() initializes all the Pygame modules so the program can use its features.
- WIDTH and HEIGHT set the window size to 900 × 700 pixels.
- FPS = 60 sets the game to update at 60 frames per second for smooth gameplay.
- ROWS = 6 and COLS = 7 define a game board with 6 rows and 7 columns.
- CELL_SIZE = 75 sets each board square to 75 × 75 pixels.
- BOARD_WIDTH and BOARD_HEIGHT calculate the total size of the board based on the number of rows, columns, and cell size.
- BOARD_X and BOARD_Y determine the board's position on the screen, centering it horizontally and placing it 150 pixels from the top of the window.

## Colours
- BG sets the dark background colour of the game window.
- PANEL is the colour of the top information panel that displays the title, turn indicator, and scores.
- BOARD_BLUE is used to draw the Connect Four board.
- RED is the colour of Player 1's counters and text.
- YELLOW is the colour of Player 2's counters and text.
- WHITE is used for most text and other light elements.
- BLACK is used for the empty spaces (holes) in the board.
- GREEN is the normal colour of the Reset Game button.
- GREEN_HOVER is the lighter green shown when the mouse is hovering over the button.

## Windows
- pygame.display.set_mode((WIDTH, HEIGHT)) creates the game window using the width and height defined earlier (900 × 700 pixels).
- The variable screen represents the window that everything is drawn onto.
- pygame.display.set_caption("Connect Four") sets the title shown in the window's title bar to "Connect Four".
- pygame.time.Clock() creates a clock object that controls the game's frame rate, helping it run smoothly at the specified 60 FPS.
- pygame.font.SysFont("arial", 42, bold=True) creates a large, bold Arial font for the game's title.
- ui_font creates a medium-sized font used for interface text, such as the current player's turn.
- small_font creates a smaller font used for information such as the move counter, score, and instructions.

## Game State
- board = [[0 for _ in range(COLS)] for _ in range(ROWS)] creates a 6 × 7 two-dimensional list representing the game board. Each position starts with the value 0, meaning it is empty.
0 = Empty space
1 = Red player's counter
2 = Yellow player's counter
- current_player = 1 sets the first turn to Player 1 (Red).
- winner = None stores the winner of the game. It remains None until a player connects four counters.
- game_over = False is a Boolean variable that indicates whether the game has finished. It changes to True when a player wins or the board is full.
- moves = 0 counts how many counters have been placed. This is used to detect when the board is full and the game ends in a draw.
- red_wins = 0 keeps track of how many games the Red player has won.
- yellow_wins = 0 keeps track of how many games the Yellow player has won.
- draws = 0 records the number of games that end without a winner.

## Button Class

The Button class creates a clickable button for the game. It stores the button’s position, size and text, draws the button on the screen, changes colour when the mouse hovers over it, and detects when the left mouse button is clicked inside the button area.

## __init__() Method

The __init__() method is the constructor for the Button class. It runs automatically whenever a new button object is created. Its purpose is to initialise the button's properties, including its position (x, y), size (w, h), and display text. It also creates a pygame.Rect object, which is used for drawing the button and detecting mouse interactions.

## draw() Method

The draw() method displays the button on the screen. First, it gets the current mouse position using pygame.mouse.get_pos(). It then checks whether the mouse is hovering over the button using self.rect.collidepoint(mouse). If the mouse is over the button, the button is coloured GREEN_HOVER; otherwise, it remains GREEN.

The method then draws the button as a rectangle with rounded corners using pygame.draw.rect(). Finally, it renders the button text, centres it within the button, and displays it on the screen using surface.blit().

## clicked() Method

The clicked() method checks whether the button has been clicked. It returns True only when three conditions are met:

- The event is a mouse button press (pygame.MOUSEBUTTONDOWN).
- The left mouse button is used (event.button == 1).
- The mouse click occurs inside the button's rectangular area (self.rect.collidepoint(event.pos)).

If any of these conditions are not met, the method returns False. This allows the program to detect when the user clicks the button and perform an action, such as resetting the game.

## Reset Button Creation

```python
reset_button = Button(WIDTH // 2 - 80, HEIGHT - 80, 160, 50, "Reset Game")
```
This line creates a Button object called reset_button. The button is positioned near the bottom centre of the game window, has a width of 160 pixels and a height of 50 pixels, and displays the text "Reset Game". The button is used to restart the game when clicked.

## Reset Game Function

The `reset_game()` function resets the current game state so a new game can begin.

```python
def reset_game():
    global board, current_player, winner, game_over, moves

    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    current_player = 1
    winner = None
    game_over = False
    moves = 0
```

- `global` allows the function to modify the existing game variables.
- The board is recreated with all spaces set to `0`, removing all pieces.
- `current_player` is reset to `1`, meaning Red starts again.
- `winner` is cleared and `game_over` is set to `False` so the game can continue.
- `moves` is reset to `0`.

This function restarts the game while keeping the win and draw counters unchanged.

## Get Next Row Function

The `get_next_row()` function finds the lowest available position in a selected column where a new piece can be placed.

```python
def get_next_row(col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            return row
    return None
```

- The function starts checking from the bottom of the column (`ROWS - 1`) because Connect Four pieces fall downwards.
- It moves upwards through the column until it finds an empty space (`0`).
- It returns the row number where the piece should be placed.
- If the column is full, it returns `None`, preventing another piece from being added.
  
## Check Win Function

The `check_win()` function checks whether a player has connected four pieces in a row. It checks all possible winning directions: horizontal, vertical, and both diagonal directions.

```python
def check_win(piece):
```

The function takes the player's piece (`1` for Red or `2` for Yellow) and searches the board for four matching pieces.

- **Horizontal check:** Searches each row for four connected pieces from left to right.
- **Vertical check:** Searches each column for four connected pieces from top to bottom.
- **Diagonal down-right check:** Checks diagonal lines going from top-left to bottom-right.
- **Diagonal up-right check:** Checks diagonal lines going from bottom-left to top-right.

If four matching pieces are found, the function returns `True`, meaning the player has won. If no winning combination is found, it returns `False`.

## Draw UI Function

The `draw_ui()` function is responsible for displaying all the information shown at the top of the game window. It updates the interface based on the current game state, such as whose turn it is, whether someone has won, or if the game has ended in a draw.

```python
def draw_ui():
```

### Background and Title

```python
screen.fill(BG)
pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, 120))
```

The screen is cleared with the background colour, and a top panel is drawn to hold the game information.

```python
title = title_font.render("Connect Four", True, WHITE)
screen.blit(title, (25, 20))
```

Creates and displays the game title at the top-left corner.

---

### Displaying Current Turn

```python
if not game_over:
```

Checks if the game is still running.

```python
turn_name = "Red" if current_player == 1 else "Yellow"
```

Determines which player's turn it is based on the `current_player` variable.

```python
turn_text = ui_font.render(
    f"Current Turn: {turn_name}",
    True,
    RED if current_player == 1 else YELLOW,
)
```

Creates a text message showing the current player and changes the text colour depending on whether it is Red or Yellow's turn.

---

### Displaying Game Results

When `game_over` becomes `True`, the function checks whether there is a winner.

```python
if winner:
```

If a player has won:

- Displays **"RED WINS!"** if `winner == 1`.
- Displays **"YELLOW WINS!"** if `winner == 2`.
- Shows a message telling the player to press reset.

If there is no winner:

```python
else:
    msg = ui_font.render("DRAW GAME!", True, WHITE)
```

The game is a draw because the board is completely filled without a winning combination. A message is displayed telling the player to reset the game.

---

### Drawing

```python
moves_text = small_font.render(
    f"Moves Played: {moves}",
    True,
    WHITE,
)
```

Displays the total number of moves made in the current game.

```python
f"Red Wins: {red_wins}"
f"Yellow Wins: {yellow_wins}"
f"Draws: {draws}"
```

Displays the overall game statistics:

- Number of Red wins.
- Number of Yellow wins.
- Number of draws.

These counters remain after pressing reset, allowing the player to track results across multiple games.

---

Overall, `draw_ui()` keeps the player informed by updating the interface every frame based on the current game state.

## Draw Board Function

The `draw_board()` function is responsible for displaying the Connect Four board and all player pieces on the screen. It draws the blue board background, creates the empty slots, and places Red or Yellow pieces depending on the current board state.

```python
def draw_board():
```

### Drawing the Board Background

```python
pygame.draw.rect(
    screen,
    BOARD_BLUE,
    (
        BOARD_X,
        BOARD_Y,
        BOARD_WIDTH,
        BOARD_HEIGHT,
    ),
    border_radius=10,
)
```

Creates the main blue rectangle that represents the Connect Four board. The `border_radius` parameter gives the board rounded corners.

---

### Looping Through Board Positions

```python
for row in range(ROWS):
    for col in range(COLS):
```

Uses nested loops to go through every position on the 6x7 grid.

- The outer loop moves through each row.
- The inner loop moves through each column.

This allows the program to check every slot on the board.

---

### Calculating Piece Positions

```python
x = BOARD_X + col * CELL_SIZE + CELL_SIZE // 2
y = BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2
```

Calculates the centre position of each circle on the board. This ensures that every piece is drawn in the middle of its grid slot.

---

### Drawing Empty Slots

```python
pygame.draw.circle(
    screen,
    BLACK,
    (x, y),
    CELL_SIZE // 2 - 6,
)
```

Draws black circles representing empty spaces where pieces can be placed.

---

### Drawing Player Pieces

```python
if board[row][col] == 1:
```

Checks if the position contains a Red piece.

```python
elif board[row][col] == 2:
```

Checks if the position contains a Yellow piece.

The function then draws the corresponding coloured circle in that position.

---

Overall, `draw_board()` converts the internal board array into a visual Connect Four grid by drawing empty slots and updating them with player pieces after each move.
