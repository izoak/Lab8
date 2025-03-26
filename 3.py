import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

radius = 15
mode = 'blue'
drawing_shape = 'line'  # 'line', 'circle', 'rectangle', 'eraser'
start_pos = None
objects = []  # Список для хранения нарисованных объектов

def draw_objects():
    screen.fill(BLACK)
    for obj in objects:
        if obj[0] == 'line':
            pygame.draw.line(screen, obj[1], obj[2], obj[3], obj[4])
        elif obj[0] == 'circle':
            pygame.draw.ellipse(screen, obj[1], obj[2], 2)
        elif obj[0] == 'rectangle':
            pygame.draw.rect(screen, obj[1], obj[2], 2)
        elif obj[0] == 'eraser':
            pygame.draw.circle(screen, BLACK, obj[1], obj[2])

def main():
    global drawing_shape, start_pos, radius, mode
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = (0, 0, 255)
                elif event.key == pygame.K_e:
                    drawing_shape = 'eraser'
                elif event.key == pygame.K_l:
                    drawing_shape = 'line'
                elif event.key == pygame.K_c:
                    drawing_shape = 'circle'
                elif event.key == pygame.K_t:
                    drawing_shape = 'rectangle'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
            elif event.type == pygame.MOUSEMOTION and start_pos:
                if drawing_shape == 'line':
                    objects.append(('line', mode, start_pos, event.pos, radius))
                    start_pos = event.pos
                elif drawing_shape == 'eraser':
                    objects.append(('eraser', event.pos, radius * 2))
            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing_shape in ['circle', 'rectangle'] and start_pos:
                    end_pos = event.pos
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    objects.append((drawing_shape, mode, rect))
                start_pos = None
        draw_objects()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()