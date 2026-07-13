import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
ROW_COUNT = 6
COL_COUNT = 7
SQUARESIZE = 80  # Smaller grid
RADIUS = SQUARESIZE // 2 - 5

# Calculate total size with padding
PADDING_X = 50
PADDING_Y = 50
WIDTH = COL_COUNT * SQUARESIZE + 2 * PADDING_X
HEIGHT = ROW_COUNT * SQUARESIZE + PADDING_Y + 60  # Extra space for messages

SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect Four")

# Colors
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Fonts
FONT = pygame.font.SysFont("Arial", 40)
LARGE_FONT = pygame.font.SysFont("Arial", 60)

def create_board():
    return np.zeros((ROW_COUNT, COL_COUNT))

def draw_board(board):
    # Fill background with grey
    SCREEN.fill(GREY)
    # Draw the grid
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            x = PADDING_X + c * SQUARESIZE
            y = PADDING_Y + r * SQUARESIZE
            pygame.draw.rect(SCREEN, BLUE, (x, y, SQUARESIZE, SQUARESIZE))
            if board[r][c] == 0:
                pygame.draw.circle(SCREEN, BLACK, (x + SQUARESIZE // 2, y + SQUARESIZE // 2), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(SCREEN, RED, (x + SQUARESIZE // 2, y + SQUARESIZE // 2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(YELLOW, (x + SQUARESIZE // 2, y + SQUARESIZE // 2), RADIUS)
    pygame.display.update()

def get_next_open_row(board, col):
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == 0:
            return r
    return None

def check_win(board, piece):
    # Check horizontal
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if all([board[r][c + i] == piece for i in range(4)]):
                return True
    # Check vertical
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if all([board[r + i][c] == piece for i in range(4)]):
                return True
    # Check positive diagonal
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all([board[r + i][c + i] == piece for i in range(4)]):
                return True
    # Check negative diagonal
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all([board[r - i][c + i] == piece for i in range(4)]):
                return True
    return False

def display_message(text):
    # Draw message background
    rect = pygame.Rect(0, HEIGHT - 60, WIDTH, 60)
    pygame.draw.rect(SCREEN, GREY, rect)
    # Render message
    label = FONT.render(text, True, WHITE)
    rect_text = label.get_rect(center=(WIDTH // 2, HEIGHT - 30))
    SCREEN.blit(label, rect_text)
    pygame.display.update()

def main():
    board = create_board()
    game_over = False
    turn = 0  # Player 1: 0, Player 2: 1

    draw_board(board)
    display_message("Player 1's turn (Red)")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if not game_over:
                if event.type == pygame.MOUSEMOTION:
                    # Show the current disc following the mouse
                    pygame.draw.rect(SCREEN, GREY, (0, 0, WIDTH, PADDING_Y))
                    posx = event.pos[0]
                    if turn % 2 == 0:
                        pygame.draw.circle(SCREEN, RED, (posx, PADDING_Y // 2), RADIUS)
                    else:
                        pygame.draw.circle(SCREEN, YELLOW, (posx, PADDING_Y // 2), RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Drop the disc
                    pygame.draw.rect(SCREEN, GREY, (0, 0, WIDTH, PADDING_Y))
                    posx = event.pos[0]
                    col = int((posx - PADDING_X) // SQUARESIZE)
                    if 0 <= col < COL_COUNT:
                        row = get_next_open_row(board, col)
                        if row is not None:
                            piece = 1 if turn % 2 == 0 else 2
                            board[row][col] = piece
                            draw_board(board)

                            if check_win(board, piece):
                                winner = "Player 1 (Red)" if piece == 1 else "Player 2 (Yellow)"
                                display_message(f"{winner} wins! Press Q to Quit")
                                game_over = True
                            else:
                                if np.count_nonzero(board) == ROW_COUNT * COL_COUNT:
                                    display_message("It's a Draw! Press Q to Quit")
                                    game_over = True
                                else:
                                    turn += 1
                                    next_player = "Player 1's turn (Red)" if turn % 2 == 0 else "Player 2's turn (Yellow)"
                                    display_message(next_player)

        if game_over:
            # Wait for user to press Q to quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

if __name__ == "__main__":
    main()
