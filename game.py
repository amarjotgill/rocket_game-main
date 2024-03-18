"""
Authors:
- Yusuf Sattar
- Amarjot Gill
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

try:
    YELLOW_SPACESHIP = pygame.image.load("spaceship_yellow.png")
except pygame.error as e:
    print("Error Loading YELLOW_SPACESHIP")
YELLOW_SPACESHIP_SiZE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP, (55, 40)), 90)
try:
    RED_SPACESHIP = pygame.image.load("spaceship_red.png")
except pygame.error as e:
    print("Error Loading RED_SPACESHIP")
RED_SPACESHIP_SiZE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP, (55, 40)), 270)

try:
    SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load("space3.jpg"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading SPACE_BACKGROUND")
try:
    SPACE2_BACKGROUND = pygame.transform.scale(pygame.image.load("space2.jpeg"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading SPACE2_BACKGROUND")
try:
    SPACE3_BACKGROUND = pygame.transform.scale(pygame.image.load("space4.png"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading SPACE3_BACKGROUND")
try:
    SPACE4_BACKGROUND = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading SPACE4_BACKGROUND", e)
try:
    SPACE5_BACKGROUND = pygame.transform.scale(pygame.image.load("space5.png"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading SPACE5_BACKGROUND", e)
try:
    SPACE6_BACKGROUND = pygame.transform.scale(pygame.image.load("space6.png"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading SPACE6_BACKGROUND", e)
try:
    SPACE7_BACKGROUND = pygame.transform.scale(pygame.image.load("space7.png"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading SPACE7_BACKGROUND", e)
try:
    BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load("black_screen.png"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading BLACK_BACKGROUND", e)
try:
    BACKGROUND = pygame.transform.scale(pygame.image.load("background.jpeg"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading BACKGROUND")
try:
    BLACK_HOLE = pygame.transform.scale(pygame.image.load("black_hole.jpeg"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading BLACK_HOLE")

try:
    BACKGROUND_SELECTION = pygame.transform.scale(pygame.image.load("background_selection.png"), (WIDTH, HEIGHT))
except pygame.error as e:
    print("Error Loading BACKGROUND_SELECTION")

class Game:
    player1 = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    player2 = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    player1_name = ""
    player2_name = ""
    game_status = True
    player1_bullets = []
    player2_bullets = []
    player1_health = 1
    player2_health = 1
    current_background = SPACE2_BACKGROUND
    clock = pygame.time.Clock()

    def __init__(self):
        return
      
    def restart_game(self):
        self.game_status = True
        self.player1_bullets = []
        self.player2_bullets = []
        self.clock = pygame.time.Clock()
        # base health (adjusted to 1 for testing)
        self.player1_health = 10
        self.player2_health = 10
        self.select_background(self)

    @staticmethod
    def draw_button(x, label):
        button_rect = pygame.Rect(x, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, GRAY, button_rect)
        text = font.render(label, True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

    @staticmethod
    def set_player1_health(self):
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 50
        BUTTON_SPACING = 20
        return 7
        
    def get_player_names(self):
        player1_name = ""
        player2_name = ""
        font = pygame.font.SysFont("Times New Roman", 40)
        label1 = font.render("Player 1 Name: ", True, WHITE)
        label2 = font.render("Player 2 Name: ", True, WHITE)

        #background image for name input screen
        WINDOW.blit(SPACE4_BACKGROUND, (0, 0))

        # width, height, box dimensions
        input_box1 = pygame.Rect(WIDTH // 2, HEIGHT // 2 - 50, 350, 60)
        input_box2 = pygame.Rect(WIDTH // 2, HEIGHT // 2 + 50, 350, 60)    
        color_inactive = pygame.Color(RED)
        color_active = pygame.Color(GREEN)
        color = color_inactive
        active = 0
        text1 = ''
        text2 = ''
        input_names = False  # flag to stop lop

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
                            input_names = True  # Adjusting flag val
                        elif event.key == pygame.K_BACKSPACE:
                            text1 = text1[:-1]
                        else:
                            text1 += event.unicode
                    elif active == 2:
                        if event.key == pygame.K_RETURN:
                            player2_name = text2
                            active = 0
                            input_names = True  # Adjusting flag val
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode

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

        self.player1_name = player1_name
        self.player2_name = player2_name
        
        self.player1_health = self.set_player1_health(self)
        self.player2_health = self.set_player1_health(self)
        self.select_background(self)
        return
        
    # draws the game onto the window
    def draw_game(self):
        # how to get background
        WINDOW.blit(self.current_background, (0, 0))
        
        # border in middle
        pygame.draw.rect(WINDOW, BLACK, CANT_CROSS)
        red_health_text = HEALTH_FONT.render("Health:" + str(self.player1_health), True, WHITE)
        yellow_health_text = HEALTH_FONT.render("Health:" + str(self.player2_health), True, WHITE)

        WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        WINDOW.blit(yellow_health_text, (10, 10))
        WINDOW.blit(YELLOW_SPACESHIP_SiZE, (self.player2.x, self.player2.y))
        WINDOW.blit(RED_SPACESHIP_SiZE, (self.player1.x, self.player1.y))
        # used to project player1 bullet in game
        for bullet in self.player1_bullets:
            pygame.draw.rect(WINDOW, RED, bullet)
        # used to project player2 bullet
        for bullet in self.player2_bullets:
            pygame.draw.rect(WINDOW, YELLOW, bullet)

        pygame.display.update()

    def move_player2(self,keys_pressed):
        # left
        if keys_pressed[pygame.K_a]:
            if self.player2.x - VELOCITY > 0:
                self.player2.x -= VELOCITY
        # right
        if keys_pressed[pygame.K_d]:
            if self.player2.x + VELOCITY + self.player2.width < CANT_CROSS.x:
                self.player2.x += VELOCITY
        # up
        if keys_pressed[pygame.K_w]:
            if self.player2.y - VELOCITY > 0:
                self.player2.y -= VELOCITY
        # down
        if keys_pressed[pygame.K_s]:
            if self.player2.y + VELOCITY + self.player2.height < HEIGHT - 15:
                self.player2.y += VELOCITY

    def move_player1(self,keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            if self.player1.x - VELOCITY > CANT_CROSS.x:
                self.player1.x -= VELOCITY
        if keys_pressed[pygame.K_RIGHT]:
            if self.player1.x + VELOCITY + self.player1.width < WIDTH:
                self.player1.x += VELOCITY
        if keys_pressed[pygame.K_UP]:
            if self.player1.y - VELOCITY > 0:
                self.player1.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN]:
            if self.player1.y + VELOCITY + self.player1.height < HEIGHT - 15:
                self.player1.y += VELOCITY

    def shoot_bullet(self):
        for bullet in self.player2_bullets:
            bullet.x += BULLET_SPEED
            # will detect if player2 bullet hits player1 hit box
            if self.player1.colliderect(bullet):
                # triggers the event
                pygame.event.post(pygame.event.Event(PLAYER1_HIT))
                # gets rid of the bullet
                self.player2_bullets.remove(bullet)

            elif bullet.x > WIDTH:
                # if the bullet goes off the screen it will get rid of it
                self.player2_bullets.remove(bullet)

        for bullet in self.player1_bullets:
            bullet.x -= BULLET_SPEED
            if self.player2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(PLAYER2_HIT))
                self.player1_bullets.remove(bullet)

            elif bullet.x < 0:
                self.player1_bullets.remove(bullet)
         
    def winner_of_game(self,text):
        # Set screen to black
        WINDOW.blit(BLACK_BACKGROUND, (0, 0))
        draw = END_FONT.render(text, True, WHITE)
        WINDOW.blit(draw, (WIDTH / 2 - draw.get_width() / 2, HEIGHT / 2 - draw.get_height() / 2))

        # Draw restart button
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 100)
        pygame.draw.rect(WINDOW, WHITE, restart_button)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_text = menu_font.render("Play Again?", True, BLACK)
        text_rect = menu_text.get_rect(center=restart_button.center)
        WINDOW.blit(menu_text, text_rect)
        pygame.display.update()

        quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 250, 200, 100)
        pygame.draw.rect(WINDOW, WHITE, quit_button)
        quit_menu_font = pygame.font.SysFont("Times New Roman", 25)
        quit_menu_text = quit_menu_font.render("Quit Game", True, BLACK)
        quit_text_rect = quit_menu_text.get_rect(center=quit_button.center)
        WINDOW.blit(quit_menu_text, quit_text_rect)
        pygame.display.update()

        restart = False
        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        if restart_button.collidepoint(event.pos):
                            # Restart the game if the restart button is clicked
                            restart = True
                            self.restart_game(self)
                        elif quit_button.collidepoint(event.pos):
                            # Quit the game if the quit button is clicked
                            pygame.quit()
                            sys.exit()
                            
    def start_menu(self):
        try:
            START_BUTTON = pygame.transform.scale(pygame.image.load("start2_button.jpeg"), (WIDTH, HEIGHT))
        except pygame.error as e:
            print("Error Loading START2_BUTTON", e)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_font2 = pygame.font.SysFont("Times New Roman", 70)
        button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)

        # adjusting size of img to fit rect
        START_BUTTON = pygame.transform.scale(START_BUTTON, (button_rect.width, button_rect.height))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if button_rect.collidepoint(event.pos):
                            self.get_player_names(self)
                            return  # Exit the start menu if the button is clicked
            # Clear the screen
            WINDOW.blit(BLACK_HOLE, (0, 0))

            # Display "Rocket Battle!" at the top of the screen
            title_text = menu_font2.render("Welcome to Rocket Battle!", True, WHITE)
            title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
            WINDOW.blit(title_text, title_rect)

            # Draw the button
            WINDOW.blit(START_BUTTON, button_rect)

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            pygame.time.Clock().tick(FPS)

    def select_background(self):
        WINDOW.blit(BACKGROUND_SELECTION, (0, 0))
         # background selection buttons
        button_1 = pygame.Rect(WIDTH // 2 - 350, HEIGHT // 2 - 130, 150, 50)
        pygame.draw.rect(WINDOW, WHITE, button_1)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_text = menu_font.render("Background 1", True, BLACK)
        text_rect = menu_text.get_rect(center=button_1.center)
        WINDOW.blit(menu_text, text_rect)
        pygame.display.update()

        button_2 = pygame.Rect(WIDTH // 2 + 150, HEIGHT // 2 - 130, 150, 50)
        pygame.draw.rect(WINDOW, WHITE, button_2)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_text = menu_font.render("Background 2", True, BLACK)
        text_rect = menu_text.get_rect(center=button_2.center)
        WINDOW.blit(menu_text, text_rect)
        pygame.display.update()

        button_3 = pygame.Rect(WIDTH // 2 - 350, HEIGHT // 2 + 90, 150, 50)
        pygame.draw.rect(WINDOW, WHITE, button_3)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_text = menu_font.render("Background 3", True, BLACK)
        text_rect = menu_text.get_rect(center=button_3.center)
        WINDOW.blit(menu_text, text_rect)
        pygame.display.update()

        button_4 = pygame.Rect(WIDTH // 2 + 150, HEIGHT // 2 + 90, 150, 50)
        pygame.draw.rect(WINDOW, WHITE, button_4)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_text = menu_font.render("Background 4", True, BLACK)
        text_rect = menu_text.get_rect(center=button_4.center)
        WINDOW.blit(menu_text, text_rect)
        pygame.display.update()

        button_5 = pygame.Rect(WIDTH // 2 - 350, HEIGHT // 2 + 310, 150, 50)
        pygame.draw.rect(WINDOW, WHITE, button_5)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_text = menu_font.render("Background 5", True, BLACK)
        text_rect = menu_text.get_rect(center=button_5.center)
        WINDOW.blit(menu_text, text_rect)
        pygame.display.update()

        button_6 = pygame.Rect(WIDTH // 2 + 150, HEIGHT // 2 + 310, 150, 50)
        pygame.draw.rect(WINDOW, WHITE, button_6)
        menu_font = pygame.font.SysFont("Times New Roman", 25)
        menu_text = menu_font.render("Background 6", True, BLACK)
        text_rect = menu_text.get_rect(center=button_6.center)
        WINDOW.blit(menu_text, text_rect)
        pygame.display.update()

        selected = False
        while not selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        if button_1.collidepoint(event.pos):
                            self.current_background = SPACE_BACKGROUND
                            self.run_game(self)
                        elif button_2.collidepoint(event.pos):
                            self.current_background = SPACE4_BACKGROUND
                            self.run_game(self)
                        elif button_3.collidepoint(event.pos):
                            self.current_background = SPACE2_BACKGROUND
                            self.run_game(self)
                        elif button_4.collidepoint(event.pos):
                            self.current_background = SPACE5_BACKGROUND
                            self.run_game(self)
                        elif button_5.collidepoint(event.pos):
                            self.current_background = SPACE6_BACKGROUND
                            self.run_game(self)
                        elif button_6.collidepoint(event.pos):
                            self.current_background = SPACE7_BACKGROUND
                            self.run_game(self)

    def run_game(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT and len(self.player2_bullets) < NUM_BULLETS:
                        bullet = pygame.Rect(self.player2.x + self.player2.width, self.player2.y + self.player2.height//2 - 2, 10, 5)
                        self.player2_bullets.append(bullet)

                    if event.key == pygame.K_SPACE and len(self.player1_bullets) < NUM_BULLETS:
                        bullet = pygame.Rect(self.player1.x - self.player1.width, self.player1.y + self.player1.height // 2 - 2, 10, 5)
                        self.player1_bullets.append(bullet)

                if event.type == PLAYER1_HIT:
                    self.player1_health -= 1

                if event.type == PLAYER2_HIT:
                    self.player2_health -= 1

            winner = ""
            if self.player1_health <= 0:
                winner = f"{self.player2_name} wins!"

            if self.player2_health <= 0:
                winner = f"{self.player1_name} wins!"

            if winner != "":
                self.winner_of_game(self,winner)
                break

            keys_pressed = pygame.key.get_pressed()
            self.move_player2(self,keys_pressed)
            self.move_player1(self,keys_pressed)
            self.shoot_bullet(self)
            self.draw_game(self)

def main():
    game = Game
    game.start_menu(game)

if __name__ == "__main__":
    main()
