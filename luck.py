import pygame
import random
from sys import exit

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

clock = pygame.time.Clock()

title_font = pygame.font.SysFont(None, 50)
font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 50)

input_box = pygame.Rect(250, 180, 200, 50)
user_text = ""

secret_number = random.randint(1, 100)

message = "Guess a number between 1 and 100"
game_over = False
confirm_quit = False

running = True

while running:
    screen.fill(BG_COLOR)

    title = title_font.render("Number Guessing Game", True, WHITE)
    screen.blit(title, (150, 50))

    instruction = font.render(
        "Enter your guess and press ENTER",
        True,
        WHITE
    )
    screen.blit(instruction, (120, 120))

    pygame.draw.rect(screen, WHITE, input_box, 2)

    text_surface = font.render(user_text, True, WHITE)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    msg = font.render(message, True, WHITE)
    screen.blit(msg, (50, 300))

    if game_over and not confirm_quit:
        replay = font.render(
            "Press Y to play again or N to quit",
            True,
            WHITE
        )
        screen.blit(replay, (100, 380))

    if confirm_quit:
        quit_msg = font.render(
            "Are you sure you want to quit? Y = Yes, N = No",
            True,
            WHITE
        )
        screen.blit(quit_msg, (30, 420))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            if confirm_quit:

                if event.key == pygame.K_y:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_n:
                    confirm_quit = False

            elif game_over:

                if event.key == pygame.K_y:
                    secret_number = random.randint(1, 100)
                    user_text = ""
                    message = "Guess a number between 1 and 100"
                    game_over = False

                elif event.key == pygame.K_n:
                    confirm_quit = True

            else:

                if event.key == pygame.K_RETURN:

                    if user_text.isdigit():

                        guess = int(user_text)

                        if guess < secret_number:
                            message = f"Too Low! Correct number was {secret_number}"
                            game_over = True

                        elif guess > secret_number:
                            message = f"Too High! Correct number was {secret_number}"
                            game_over = True

                        else:
                            message = f"You WIN! Correct number was {secret_number}"
                            game_over = True

                        user_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                else:
                    if event.unicode.isdigit():
                        user_text += event.unicode

    pygame.display.update()
    clock.tick(60)