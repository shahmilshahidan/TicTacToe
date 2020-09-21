"""
    This is an implementation of Tic Tac Toe game using pygame engine.
    It is a standard 3 x 3 game where player that uses X will make a 
    move first followed by player uses O.

    Returns:
        [type]: [description]
"""


import pygame, sys, math
from pygame.locals import *

# Game screen
pygame.init()
WIDTH = 700
ROWS = 3
win = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Tic Tac Toe")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100 , 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# X and O
X_IMAGE = pygame.transform.scale(pygame.image.load('x_player.png'), (80, 80))
O_IMAGE = pygame.transform.scale(pygame.image.load('o_player.png'), (80, 80))

# Fonts
END_FONT = pygame.font.SysFont('courier', 40)


def draw_grid():
    """
    Create the 3*3 grid on the board.
    """
    gap = WIDTH // ROWS

    # Starting points
    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap

        pygame.draw.line(win, GRAY, (x,0), (x, WIDTH), 3)
        pygame.draw.line(win, GRAY, (0,x), (WIDTH, x), 3)

# Create grid
def prep_grid():
    """
    Set up game components. Initialize an array of n*n to keep track the of the gameplay.

    Returns:
        [array]: [Tic tac toe grid]
    """
    centre = WIDTH // ROWS // 2

    game_array = [[None, None, None], [None, None, None], [None, None, None]]
    
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = centre * (2 * j + 1)
            y = centre * (2 * i + 1)
            game_array[i][j] = (x, y, "", True)
    
    return game_array


def click(game_array):
    """
    Playing the game. A player needs to click at one of the empty square to make a move.

    Args:
        game_array ([array]): [grid that tracks the gameplay]
    """
    global x_turn, o_turn, images

    # Mouse options
    m_x, m_y = pygame.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, playable = game_array[i][j]
            
            # Distance between mouse and the centre of the square
            dist = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

            # If pointer inside the square
            if dist < WIDTH // ROWS // 2 and playable:
                if x_turn:
                    images.append((x, y, X_IMAGE))
                    x_turn = False
                    o_turn = True
                    game_array[i][j] = (x, y, 'x', False)
                
                elif o_turn:
                    images.append((x, y, O_IMAGE))
                    x_turn = True
                    o_turn = False
                    game_array[i][j] = (x, y, 'o', False)


def winner(game_array):
    """
    Check if there are any winners. For every turn, check the rows, columns and diagonal.
    Any rows, columns or diagonal that are occupied with all X or O will stop the game and 
    announce the winner.

    Args:
        game_array ([array]): [Grid to track gameplay]

    Returns:
        [array]: [Current status of the game]
    """
    # Check rows
    for row in range(len(game_array)):
        if (game_array[0][2] == game_array[1][2] == game_array[2][2]) and game_array[0][2] != "":
            display_message(game_array[0][2].upper() + " has won!")
            return True

    # Check columns
    for col in range(len(game_array)):
        if (game_array[0][2] == game_array[1][2] == game_array[2][2]) and game_array[0][2] != "":
            display_message(game_array[0][2].upper() + " has won!")
            return True

    # Check main diagonal
    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " has won!")
        return True

    # Check reverse diagonal
    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " has won!")
        return True
    
    return False
    

def drawn(game_array):
    """
    When all squares are filled and no rows, columns and diagonal are filled with all X or 
    O.

    Args:
        game_array ([array]): [Grid to track gameplay]

    Returns:
        [array]: [Current gameplay]
    """
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    display_message("It's a draw!")
    return True


def display_message(content):
    """
    Function to display message on the background.

    Args:
        content ([string]): [Winning, losing or draw message]
    """
    pygame.time.delay(500)
    win.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def render():
    """
    Update the game background
    """
    win.fill(WHITE)
    draw_grid()

    # Draw X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))
    
    pygame.display.update()


def run_game():
    """
    Main function to run the game
    """
    global x_turn, o_turn, images, draw

    images = []
    draw = False

    run = True

    x_turn = True
    o_turn = False

    game_array = prep_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)
        render()

        if winner(game_array) or drawn(game_array):
            run = False


if __name__ == "__main__":
    run_game()