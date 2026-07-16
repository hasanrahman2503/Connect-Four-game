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
