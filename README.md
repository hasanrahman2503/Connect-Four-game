## Connect Four Program Structure

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

pygame.init() initializes all the Pygame modules so the program can use its features.
WIDTH and HEIGHT set the window size to 900 × 700 pixels.
FPS = 60 sets the game to update at 60 frames per second for smooth gameplay.
ROWS = 6 and COLS = 7 define a game board with 6 rows and 7 columns.
CELL_SIZE = 75 sets each board square to 75 × 75 pixels.
BOARD_WIDTH and BOARD_HEIGHT calculate the total size of the board based on the number of rows, columns, and cell size.
BOARD_X and BOARD_Y determine the board's position on the screen, centering it horizontally and placing it 150 pixels from the top of the window.

