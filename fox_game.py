import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 830, 600
HOLES = 5

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Fox")

# Initialize Font
font = pygame.font.SysFont(None, 36)  # You can also use a specific font

def display_guesses(guess_count):
    text = font.render(f"Guesses: {guess_count}", True, (0, 0, 0))
    screen.blit(text, (WIDTH - 150, 10))  # Positioning the text in the top right corner


def draw_holes_and_fox(fox_position):
    for i in range(1, HOLES + 1):
        color = (255, 0, 0) if i == fox_position else (0, 0, 0)
        pygame.draw.circle(screen, color, (i * 150, HEIGHT // 2), 40)
def get_hole_number_from_click(pos):
    x, y = pos
    return ((x+40) // 150) if ((x+40) % 150 <= 80 and HEIGHT // 2 - 40 <= y <= HEIGHT // 2 + 40) else None

guess_count = 1

# Fox and Holes positions (for simplicity, using numbers)
fox_position = random.randint(1, HOLES)
player_guess = None

game_recap = []

# Game loop
running = True
while running:
    current_stat = ["day: " + str(guess_count)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle player input here (e.g., mouse clicks)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_guess = get_hole_number_from_click(pygame.mouse.get_pos())
            if player_guess:
                guess_count += 1

                current_stat = current_stat + [fox_position, player_guess]
                game_recap.append(current_stat)

                # Check if the player caught the fox
                if player_guess == fox_position:
                    print("Fox caught! Game Over")
                    print(game_recap)
                    running = False

                # Game logic for moving the fox
                if fox_position not in [1, HOLES]:
                    fox_position += random.choice([-1, 1])
                else:
                    fox_position = 2 if fox_position == 1 else 4

            

    # Render the game state
    screen.fill((255, 255, 255))
    # Render holes and fox here

    draw_holes_and_fox(fox_position)
    display_guesses(guess_count)
    
    pygame.display.flip()

pygame.quit()
