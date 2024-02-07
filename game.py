"""
This is a simple rocket battle game that I have made, the game ends when one user's health is under 10.
The game will restart it's self after a 5 second delay, to quit the game press the exit button in the top right corner.
"""

import sys
import pygame
pygame.font.init()

WIDTH = 1000
HEIGHT = 800
CHARACTER_WIDTH, CHARACTER_HEIGHT = 55, 40
# different colors used through project
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
CANT_CROSS = pygame.Rect(500, 10, 10, 800)

# creating event to detect bullet hitting
PLAYER2_HIT = pygame.USEREVENT + 1
PLAYER1_HIT = pygame.USEREVENT + 2

HEALTH_FONT = pygame.font.SysFont("Times New Roman", 40)
END_FONT = pygame.font.SysFont("Times New Roman", 80)

FPS = 60
VELOCITY = 10
BULLET_SPEED = 6
NUM_BULLETS = 6
# Game window size
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# text at top
pygame.display.set_caption("Rocket Battle!")


YELLOW_SPACESHIP = pygame.image.load("spaceship_yellow.png")
YELLOW_SPACESHIP_SiZE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP, (55, 40)), 90)

RED_SPACESHIP = pygame.image.load("spaceship_red.png")
RED_SPACESHIP_SiZE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP, (55, 40)), 270)

SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load("space3.jpg"), (WIDTH, HEIGHT))
SPACE2_BACKGROUND = pygame.transform.scale(pygame.image.load("space2.jpeg"), (WIDTH, HEIGHT))
SPACE3_BACKGROUND = pygame.transform.scale(pygame.image.load("space4.png"), (WIDTH, HEIGHT))
BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load("black_screen.png"), (WIDTH, HEIGHT))

def get_player_names():
    player1_name = ""
    player2_name = ""
    font = pygame.font.SysFont("Times New Roman", 40)
    label1 = font.render("Player 1 Name: ", True, WHITE)
    label2 = font.render("Player 2 Name: ", True, WHITE)

    # width, height, box dimensions
    input_box1 = pygame.Rect(WIDTH // 2, HEIGHT // 2 - 50, 350, 60)
    input_box2 = pygame.Rect(WIDTH // 2, HEIGHT // 2 + 50, 350, 60)    
    color_inactive = pygame.Color(RED)
    color_active = pygame.Color(GREEN)
    color = color_inactive
    active = 0
    text1 = ''
    text2 = ''
    input_names = False  # Flag to determine when to exit the loop

    while not input_names:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active = 1
                elif input_box2.collidepoint(event.pos):
                    active = 2
                else:
                    active = 0
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active == 1:
                    if event.key == pygame.K_RETURN:
                        player1_name = text1
                        active = 0
                        input_names = True  # Set the flag to exit the loop
                    elif event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode
                elif active == 2:
                    if event.key == pygame.K_RETURN:
                        player2_name = text2
                        active = 0
                        input_names = True  # Set the flag to exit the loop
                    elif event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode

        WINDOW.fill((30, 30, 30))
        WINDOW.blit(label1, (WIDTH // 2 - label1.get_width() - 10, HEIGHT // 2 - 50))
        WINDOW.blit(label2, (WIDTH // 2 - label2.get_width() - 10, HEIGHT // 2 + 50))
        txt_surface1 = font.render(text1, True, color)
        width = max(200, txt_surface1.get_width()+10)
        input_box1.w = width
        WINDOW.blit(txt_surface1, (input_box1.x+5, input_box1.y+5))
        pygame.draw.rect(WINDOW, color, input_box1, 2)

        txt_surface2 = font.render(text2, True, color)
        width = max(200, txt_surface2.get_width()+10)
        input_box2.w = width
        WINDOW.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(WINDOW, color, input_box2, 2)

        pygame.display.flip()

    return player1_name, player2_name
    
# draws the game onto the window
def draw_game(player1, player2, player1_bullets, player2_bullets, player1_health, player2_health):
    # how to get background
    WINDOW.blit(SPACE_BACKGROUND, (0, 0))
    
    # border in middle
    pygame.draw.rect(WINDOW, BLACK, CANT_CROSS)
    red_health_text = HEALTH_FONT.render("Health:" + str(player1_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health:" + str(player2_health), True, WHITE)

    WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))
    WINDOW.blit(YELLOW_SPACESHIP_SiZE, (player2.x, player2.y))
    WINDOW.blit(RED_SPACESHIP_SiZE, (player1.x, player1.y))
    # used to project player1 bullet in game
    for bullet in player1_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    # used to project player2 bullet
    for bullet in player2_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    pygame.display.update()


def move_player2(keys_pressed, player2):
    if keys_pressed[pygame.K_a]:
        if player2.x - VELOCITY > 0:
            player2.x -= VELOCITY
    # right
    if keys_pressed[pygame.K_d]:
        if player2.x + VELOCITY + player2.width < CANT_CROSS.x:
            player2.x += VELOCITY
    # up
    if keys_pressed[pygame.K_w]:
        if player2.y - VELOCITY > 0:
            player2.y -= VELOCITY
    # down
    if keys_pressed[pygame.K_s]:
        if player2.y + VELOCITY + player2.height < HEIGHT - 15:
            player2.y += VELOCITY


def move_player1(keys_pressed, player1):
    if keys_pressed[pygame.K_LEFT]:
        if player1.x - VELOCITY > CANT_CROSS.x:
            player1.x -= VELOCITY
    # right
    if keys_pressed[pygame.K_RIGHT]:
        if player1.x + VELOCITY + player1.width < WIDTH:
            player1.x += VELOCITY
    # up
    if keys_pressed[pygame.K_UP]:
        if player1.y - VELOCITY > 0:
            player1.y -= VELOCITY
    # down
    if keys_pressed[pygame.K_DOWN]:
        if player1.y + VELOCITY + player1.height < HEIGHT - 15:
            player1.y += VELOCITY


def shoot_bullet(player2_bullets, player1_bullets, player2, player1):
    for bullet in player2_bullets:
        bullet.x += BULLET_SPEED
        # will detect if player2 bullet hits player1 hit box
        if player1.colliderect(bullet):
            # triggers the event
            pygame.event.post(pygame.event.Event(PLAYER1_HIT))
            # gets rid of the bullet
            player2_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            # if the bullet goes off the screen it will get rid of it
            player2_bullets.remove(bullet)

    for bullet in player1_bullets:
        bullet.x -= BULLET_SPEED
        if player2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER2_HIT))
            player1_bullets.remove(bullet)

        elif bullet.x < 0:
            player1_bullets.remove(bullet)

            
def winner_of_game(text):
    #set screen to black
    WINDOW.blit(BLACK_BACKGROUND, (0, 0))
    draw = END_FONT.render(text, True, WHITE)
    WINDOW.blit(draw, (WIDTH / 2 - draw.get_width() / 2, HEIGHT / 2 - draw.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2500)


def start_menu():
   
    menu_font = pygame.font.SysFont("Times New Roman", 25)
    menu_font2 = pygame.font.SysFont("Times New Roman", 70)
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if button_rect.collidepoint(event.pos):
                        return  # Exit the start menu if the button is clicked

        # Clear the screen
        WINDOW.blit(SPACE3_BACKGROUND, (0, 0))

        # Display "Rocket Battle!" at the top of the screen
        title_text = menu_font2.render("Welcome to Rocket Battle!", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
        WINDOW.blit(title_text, title_rect)

        # Draw the button
        pygame.draw.rect(WINDOW, WHITE, button_rect)
        menu_text = menu_font.render("Begin Game", True, BLACK)
        text_rect = menu_text.get_rect(center=button_rect.center)
        WINDOW.blit(menu_text, text_rect)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(FPS)


def run_game(player1_bullets, player2_bullets, player1_health, player2_health, game_status, clock, player1, player2, player1_name, player2_name):
    while game_status:
        # control for 60 fps
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(player2_bullets) < NUM_BULLETS:
                    bullet = pygame.Rect(player2.x + player2.width, player2.y + player2.height//2 - 2, 10, 5)
                    player2_bullets.append(bullet)

                if event.key == pygame.K_SPACE and len(player1_bullets) < NUM_BULLETS:
                    bullet = pygame.Rect(player1.x - player1.width, player1.y + player1.height // 2 - 2, 10, 5)
                    player1_bullets.append(bullet)

            if event.type == PLAYER1_HIT:
                player1_health -= 1

            if event.type == PLAYER2_HIT:
                player2_health -= 1
        winner = ""
        if player1_health <= 0:
            winner = f"{player2_name} wins!"

        if player2_health <= 0:
            winner = f"{player1_name} wins!"

        if winner != "":
            winner_of_game(winner)
            break

        keys_pressed = pygame.key.get_pressed()
        move_player2(keys_pressed, player2)
        move_player1(keys_pressed, player1)

        shoot_bullet(player2_bullets, player1_bullets, player2, player1)

        draw_game(player1, player2, player1_bullets, player2_bullets, player1_health, player2_health)
   
    main()



def main():
    start_menu()
    player1_name, player2_name = get_player_names()
    # creates the hit boxes for both player1 and player2
    player1 = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    player2 = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    # to get it to run at 60 fps
    clock = pygame.time.Clock()
    game_status = True

    player1_bullets = []
    player2_bullets = []
    # base health (adjusted to 1 for testing)
    player1_health = 1
    player2_health = 1


    run_game(player1_bullets, player2_bullets, player1_health, player2_health, game_status, clock, player1, player2, player1_name, player2_name)
    # reruns game after someone wins
    main()


if __name__ == "__main__":
    main()
