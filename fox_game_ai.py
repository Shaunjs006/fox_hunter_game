import pygame
import random
from agent import RlAgent



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
guess_count = 0
reward = 0

agent = RlAgent(HOLES, HOLES)

# Game loop
running = True
while running:
    current_state = fox_position - 1  # Adjust state to zero-index for RL agent

    # Agent makes a guess (zero-indexed)
    action = agent.choose_action(current_state)
    player_guess = action + 1  # Adjust back to game's indexing

    guess_count += 1

    # Check if the fox was caught
    reward = 10 if player_guess == fox_position else -1

    # Render the game state
    screen.fill((255, 255, 255))
    draw_holes_and_fox(fox_position)
    display_guesses(guess_count)
    pygame.display.flip()

    # Move the fox for the next round
    if fox_position not in [1, HOLES]:
        fox_position += random.choice([-1, 1])
    else:
        fox_position = 2 if fox_position == 1 else 4

    next_state = fox_position - 1  # Next state after the fox moves

    # Update the RL agent
    agent.learn(current_state, action, reward, next_state)

    # Check for game over condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif player_guess == fox_position:
            print("Fox caught! Game Over. Total Guesses:", guess_count)
            running = False

pygame.quit()