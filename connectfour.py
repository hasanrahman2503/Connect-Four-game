import pygame
import sys

# ----------------------------
# SETTINGS
# ----------------------------
pygame.init()

WIDTH, HEIGHT = 900, 700
FPS = 60

ROWS = 6
COLS = 7
CELL_SIZE = 75

BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

BOARD_X = (WIDTH - BOARD_WIDTH) // 2
BOARD_Y = 150

# Colours
BG = (25, 25, 35)
PANEL = (40, 40, 55)
BOARD_BLUE = (50, 90, 220)

RED = (220, 60, 60)
YELLOW = (240, 210, 50)

WHITE = (245, 245, 245)
BLACK = (15, 15, 15)

GREEN = (70, 180, 100)
GREEN_HOVER = (90, 210, 120)

# ----------------------------
# WINDOW
# ----------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

title_font = pygame.font.SysFont("arial", 42, bold=True)
ui_font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 22)

# ----------------------------
# GAME STATE
# ----------------------------
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

current_player = 1
winner = None
game_over = False
moves = 0

red_wins = 0
yellow_wins = 0
draws = 0


# ----------------------------
# BUTTON
# ----------------------------
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()

        color = GREEN_HOVER if self.rect.collidepoint(mouse) else GREEN

        pygame.draw.rect(surface, color, self.rect, border_radius=10)

        text = small_font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


reset_button = Button(WIDTH // 2 - 80, HEIGHT - 80, 160, 50, "Reset Game")


# ----------------------------
# GAME FUNCTIONS
# ----------------------------
def reset_game():
    global board, current_player, winner, game_over, moves

    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    current_player = 1
    winner = None
    game_over = False
    moves = 0


def get_next_row(col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            return row
    return None


def check_win(piece):
    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Diagonal down-right
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Diagonal up-right
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False


# ----------------------------
# DRAWING
# ----------------------------
def draw_ui():
    screen.fill(BG)
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, 120))
    title = title_font.render("Connect Four", True, WHITE)
    screen.blit(title, (25, 20))

    if not game_over:
        turn_name = "Red" if current_player == 1 else "Yellow"
        turn_text = ui_font.render(
            f"Current Turn: {turn_name}",
            True,
            RED if current_player == 1 else YELLOW,
        )
        screen.blit(turn_text, (25, 70))
    else:
        if winner:
            colour = RED if winner == 1 else YELLOW
            text = "RED WINS!" if winner == 1 else "YELLOW WINS!"
            msg = ui_font.render(text, True, colour)
            screen.blit(msg, (25, 70))
            hint = small_font.render(
                "Press Reset to play again",
                True,
                WHITE,
            )
            screen.blit(hint, (250, 75))
        else:
            msg = ui_font.render("DRAW GAME!", True, WHITE)
            screen.blit(msg, (25, 70))
            hint = small_font.render(
                "Board full - Press Reset to play again",
                True,
                WHITE,
            )
            screen.blit(hint, (250, 75))
    moves_text = small_font.render(
        f"Moves Played: {moves}",
        True,
        WHITE,
    )
    screen.blit(moves_text, (650, 80))

    red_text = small_font.render(
        f"Red Wins: {red_wins}",
        True,
        RED,
    )
    screen.blit(red_text, (500, 40))

    yellow_text = small_font.render(
        f"Yellow Wins: {yellow_wins}",
        True,
        YELLOW,
    )
    screen.blit(yellow_text, (500, 65))

    draw_text = small_font.render(
        f"Draws: {draws}",
        True,
        WHITE,
    )
    screen.blit(draw_text, (500, 90))


def draw_board():
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

    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL_SIZE + CELL_SIZE // 2
            y = BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2

            pygame.draw.circle(
                screen,
                BLACK,
                (x, y),
                CELL_SIZE // 2 - 6,
            )

            if board[row][col] == 1:
                pygame.draw.circle(
                    screen,
                    RED,
                    (x, y),
                    CELL_SIZE // 2 - 6,
                )

            elif board[row][col] == 2:
                pygame.draw.circle(
                    screen,
                    YELLOW,
                    (x, y),
                    CELL_SIZE // 2 - 6,
                )


def draw_hover_piece():
    if game_over:
        return

    mouse_x = pygame.mouse.get_pos()[0]

    if BOARD_X <= mouse_x <= BOARD_X + BOARD_WIDTH:
        color = RED if current_player == 1 else YELLOW
        pygame.draw.circle(
            screen,
            color,
            (mouse_x, BOARD_Y - 40),
            CELL_SIZE // 2 - 6,
        )


# ----------------------------
# MAIN LOOP
# ----------------------------
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if reset_button.clicked(event):
            reset_game()
        
        elif (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and not game_over
        ):
            mouse_x = event.pos[0]
            if BOARD_X <= mouse_x <= BOARD_X + BOARD_WIDTH:
                col = (mouse_x - BOARD_X) // CELL_SIZE
                row = get_next_row(col)
                if row is not None:
                    board[row][col] = current_player
                    moves += 1
                    # Check for win
                    if check_win(current_player):
                        winner = current_player
                        game_over = True
                        if current_player == 1:
                            red_wins += 1
                        else:
                            yellow_wins += 1
                    elif moves == ROWS * COLS:
                        # Draw
                        winner = None
                        game_over = True
                        draws += 1
                    else:
                        # Switch player
                        current_player = 2 if current_player == 1 else 1

    # Draw everything
    draw_ui()
    draw_board()
    draw_hover_piece()
    reset_button.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
