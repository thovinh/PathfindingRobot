import pygame
import os
from constants import *

def load_images():
    try:
        robot_img = pygame.image.load(os.path.join('images', 'robot.png'))
        wall_img = pygame.image.load(os.path.join('images', 'wall.png'))
        goal_img = pygame.image.load(os.path.join('images', 'goal.png'))
        background_img = pygame.image.load(os.path.join('images', 'background.png'))

        # Scale cac hinh anh
        robot_img = pygame.transform.scale(robot_img, (GRID_SIZE, GRID_SIZE))
        wall_img = pygame.transform.scale(wall_img, (GRID_SIZE, GRID_SIZE))
        goal_img = pygame.transform.scale(goal_img, (GRID_SIZE, GRID_SIZE))
        background_img = pygame.transform.scale(background_img, (GRID_SIZE, GRID_SIZE))

        return robot_img, wall_img, goal_img, background_img
    except pygame.error as e:
        print(f"Khong the load hinh anh: {e}")
        return None, None, None, None

def draw_grid(screen, grid, path, start, goal, robot_pos, images, step_count, game_completed):
    robot_img, wall_img, goal_img, background_img = images
    screen.fill(WHITE)
    
    # Vẽ grid
    for y in range(ROWS):
        for x in range(COLS):
            pos = (x * GRID_SIZE, y * GRID_SIZE)
            if grid[y][x] == 1:
                if wall_img:
                    screen.blit(wall_img, pos)
                else:
                    pygame.draw.rect(screen, BLACK, (*pos, GRID_SIZE, GRID_SIZE))
            else:
                if background_img:
                    screen.blit(background_img, pos)
                else:
                    pygame.draw.rect(screen, WHITE, (*pos, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, GRAY, (*pos, GRID_SIZE, GRID_SIZE), 1)

    # Vẽ đường đi
    for (px, py) in path:
        if (px, py) != goal:
            pygame.draw.rect(screen, YELLOW, (px * GRID_SIZE, py * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Vẽ robot
    if robot_img:
        screen.blit(robot_img, (robot_pos[0] * GRID_SIZE, robot_pos[1] * GRID_SIZE))
    else:
        pygame.draw.rect(screen, BLUE, (robot_pos[0] * GRID_SIZE, robot_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Vẽ đích
    goal_pos = (goal[0] * GRID_SIZE, goal[1] * GRID_SIZE)
    if goal_img:
        screen.blit(goal_img, goal_pos)
    else:
        pygame.draw.rect(screen, RED, (*goal_pos, GRID_SIZE, GRID_SIZE))

    # Hiển thị số bước
    if not game_completed:
        font = pygame.font.Font(None, 36)
        step_text = font.render(f"So buoc: {step_count}", True, RED)
        screen.blit(step_text, (10, 10)) 