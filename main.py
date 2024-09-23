import pygame
import sprites
import sys
import random

pygame.init()
clock = pygame.time.Clock()

score = 0
lives = 5

screen_width = 480
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("background.jpg")
collision_sound = pygame.mixer.Sound("ding.mp3")
death_sound = pygame.mixer.Sound("error.mp3")

text_colour = (255, 255, 255)
text_font = pygame.font.Font("arial.ttf", 18)
score_text = text_font.render("Your score is: " + str(score), True, text_colour, None)
lives_text = text_font.render("Your lives left: " + str(lives), True, text_colour, None)

pad = sprites.pad(240, 600)
pad_group = pygame.sprite.Group()
pad_group.add(pad)

ball = sprites.ball(240, 587)
ball_group = pygame.sprite.Group()
ball_group.add(ball)

pad_speed = 6
ball_dx = 3
ball_dy = -3
brick_images = ("red_brick.jpg", "orange_brick.jpg", "gold_brick.jpg", "yellow_brick.jpg", \
                "lime_brick.jpg", "green_brick.jpg", "aqua_brick.jpg", "blue_brick.jpg", \
                "sapphire_brick.jpg", "purple_brick.jpg")

def draw_all_bricks(brick_images):
    group = pygame.sprite.Group()
    y = 40
    for n in range(0, 10):
        x = 35
        for i in range(0, 11):
            group.add(sprites.brick(x, y, brick_images[n]))
            x += 40
        y += 20
    return(group)
all_bricks = draw_all_bricks(brick_images)

def brick_collision(ball_dx, ball_dy):
    ball_dy *= -1
    collision_sound.play()
    brick.kill()
    if random.randint(0, 1) == 0:
        ball_dx *= -1
    return ball_dx, ball_dy

while True:
    score_text = text_font.render("Your score is: " + str(score), True, text_colour, None)
    lives_text = text_font.render("Your lives left: " + str(lives), True, text_colour, None)
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if key[pygame.K_a] and pad.x > 40:
        pad.x -= pad_speed
    elif key[pygame.K_d] and pad.x < 440:
        pad.x += pad_speed
    
    ball.x += ball_dx
    ball.y += ball_dy

    if ball.x > 470 or ball.x < 10:
        ball_dx *= -1
        collision_sound.play()
    
    if ball.y < 7:
        ball_dy *= -1
        collision_sound.play()
    elif ball.y > 713 and lives > 0:
        ball_dy *= -1
        lives -= 1
        death_sound.play()
        pad.x = 240
        pad.y = 600
        ball.x = 240
        ball.y = 587
    elif ball.y > 713 and lives == 0:
        break
    
    if pad.rect.colliderect(ball) == True and ball_dy > 0:
        collision_sound.play()
        ball_dy *= -1
        if random.randint(0, 1) == 0:
            ball_dx *= -1
    
    for brick in all_bricks:
        if brick.rect.colliderect(ball) == True:
            score += 10
            ball_dx, ball_dy = brick_collision(ball_dx, ball_dy)

    pygame.display.flip()
    screen.blit(background, (0, 0))
    screen.blit(score_text, (20, 650))
    screen.blit(lives_text, (20, 670))

    pad_group.draw(screen)
    pad_group.update()

    ball_group.draw(screen)
    ball_group.update()

    all_bricks.draw(screen)

    clock.tick(60)
    pygame.display.update()