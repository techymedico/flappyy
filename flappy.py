
# This is a simple flappy bird game
# Import pygame module
import pygame

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Set the title and icon
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('bird.png')
pygame.display.set_icon(icon)

# Create a bird
bird = pygame.image.load('bird.png')
bird_x = 100
bird_y = 300
bird_dy = 0

# Create a pipe
pipe = pygame.image.load('pipe.png')
pipe_x = 800
pipe_y = 0
pipe_dx = -5

# Create a score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Define a function to display the score
def show_score():
    global score
    score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Define a function to check collision
def is_collision(bird_x, bird_y, pipe_x, pipe_y):
    if bird_x + 64 > pipe_x and bird_x < pipe_x + 64:
        if bird_y < pipe_y + 300 or bird_y + 64 > pipe_y + 400:
            return True
    return False

# Define a function to reset the game
def reset_game():
    global bird_x, bird_y, bird_dy, pipe_x, pipe_y, pipe_dx, score
    bird_x = 100
    bird_y = 300
    bird_dy = 0
    pipe_x = 800
    pipe_y = 0
    pipe_dx = -5
    score = 0

# Create a game loop
running = True
while running:

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Check for events
    for event in pygame.event.get():

        # If the user clicks the close button, exit the game loop
        if event.type == pygame.QUIT:
            running = False

        # If the user presses the space key, make the bird jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_dy = -10

        # If the user releases the space key, make the bird fall
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_dy = 5

    # Update the bird position and velocity
    bird_y += bird_dy

    # Check the boundaries of the bird position
    if bird_y < 0:
        bird_y = 0
    if bird_y > 536:
        bird_y = 536

    # Draw the bird on the screen
    screen.blit(bird, (bird_x, bird_y))

    # Update the pipe position and velocity
    pipe_x += pipe_dx

    # Check the boundaries of the pipe position and reset it if it goes out of the screen
    if pipe_x < -64:
        pipe_x = 800
        pipe_y = random.randint(-200, 0)
        score += 1

    # Draw the pipe on the screen
    screen.blit(pipe, (pipe_x, pipe_y))
    screen.blit(pipe, (pipe_x, pipe_y + 500))

    # Check for collision and reset the game if it happens
    if is_collision(bird_x, bird_y, pipe_x, pipe_y):
        reset_game()

    # Display the score on the screen
    show_score()

    # Update the display
    pygame.display.update()
