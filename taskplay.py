import pygame
import random

# Initializing pygame modules.

pygame.init()

# Creating the game screen and adding height and width values to it.

screen_width = 1900
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))

# Loading images for each of my objects in the game.

player = pygame.image.load("Hero.png")
user_win = pygame.image.load("Prize.png")
enemy1 = pygame.image.load("Monster1.png")
enemy2 = pygame.image.load("Monster2.png")
enemy3 = pygame.image.load("Monster3.png")

# Getting the height and width for all my images to set boundaries.

hero_height = player.get_height()
hero_width = player.get_width()
prize_height = user_win.get_height()
prize_width = user_win.get_width()
monster1_height = enemy1.get_height()
monster1_width = enemy1.get_width()
monster2_height = enemy2.get_height()
monster2_width = enemy2.get_width()
monster3_height = enemy3.get_height()
monster3_width = enemy3.get_width()

# Printing the height and width of the player image as an example.

print(f"This is the height of the player image: {hero_height}")
print(f"This is the width of the player image: {hero_width}")

# Setting the player and enemy starting positions.

playerXPosition = 100
playerYPosition = 50

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - monster1_height)
enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - monster2_height)
enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - monster3_height)
user_winXPosition = screen_width
user_winYPosition = random.randint(0, screen_height - prize_height)

# Setting arrow keys to False so they start as not pressed.

keyUp = False
keyDown = False
keyRight = False
keyLeft = False

# Using a while loop to loop the basic gameplay.

while 1:

    # Adding all images to the game.

    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(user_win, (user_winXPosition, user_winYPosition))

    # Updates the screen.

    pygame.display.flip()

    # Using a for loop to loop through events in the game.

    for event in pygame.event.get():

        # With this if statement I tell the program to quit when the user exits the game.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # The following two if statements on this indent checks if the keys are pressed in or not.

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # The following if statements determines what happens if the keys are pressed down.

    if keyUp:
        if playerYPosition > 0:
            playerYPosition -= 1

    if keyDown:
        if playerYPosition < screen_height - hero_height:
            playerYPosition += 1

    if keyLeft:
        if playerXPosition > 0:
            playerXPosition -= 1

    if keyRight:
        if playerXPosition < screen_width - hero_width:
            playerXPosition += 1

    # Here I create boundary boxes for the player and enemies.

    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition

    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition

    enemyBox3 = pygame.Rect(enemy3.get_rect())
    enemyBox3.top = enemy3YPosition
    enemyBox3.left = enemy3XPosition

    user_winBox = pygame.Rect(user_win.get_rect())
    user_winBox.top = user_winYPosition
    user_winBox.left = user_winXPosition

    # Using the boundary boxes I set conditions of what should happen in case these boxes colide.

    if playerBox.colliderect(enemyBox1):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBox2):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBox3):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(user_winBox):
        print("You win!")
        pygame.quit()
        exit(0)

    if user_winXPosition < 0:
        print("You lose!")
        pygame.quit()
        exit(0)

    # Setting movement for enemy and prize objects.

    enemy1XPosition -= 0.50
    enemy2XPosition -= 0.40
    enemy3XPosition -= 0.60
    user_winXPosition -= 0.70
