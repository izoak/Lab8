import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def reset_game():
    global snake, direction, food, score, level, speed, game_over
    snake = [(100, 100)]
    direction = (GRID_SIZE, 0)
    food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
    score = 0
    level = 1
    speed = 10
    game_over = False

def check_collision(pos):
    return pos in snake or pos[0] < 0 or pos[1] < 0 or pos[0] >= WIDTH or pos[1] >= HEIGHT

def random_food():
    while True:
        pos = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
        if pos not in snake:
            return pos

def update_snake():
    global food, score, level, speed, game_over
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if check_collision(new_head):
        game_over = True
        return
    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
        food = random_food()
    else:
        snake.pop()

def draw():
    screen.fill(BLACK)
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("You Died! Press R to Restart", True, RED)
        screen.blit(text, (WIDTH // 4, HEIGHT // 2))
    else:
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
        font = pygame.font.Font(None, 24)
        text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(text, (10, 10))
    pygame.display.flip()

reset_game()
running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction[1] == 0:
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction[1] == 0:
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction[0] == 0:
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction[0] == 0:
                direction = (GRID_SIZE, 0)
            elif event.key == pygame.K_r and game_over:
                reset_game()
    
    if not game_over:
        update_snake()
    
    draw()

pygame.quit()