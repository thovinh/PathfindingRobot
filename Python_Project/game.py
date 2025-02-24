import pygame
from constants import *
from menu import main_menu
from maze import create_maze
from pathfinding import bfs
from graphics import load_images, draw_grid

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pathfinding Robot")
        self.images = load_images()
        self.reset_game()

    def reset_game(self):
        self.grid, self.start, self.goal = create_maze()
        self.robot_pos = list(self.start)
        self.step_count = 0
        self.game_completed = False
        self.path = []

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                if event.type == pygame.KEYDOWN and not self.game_completed:
                    if event.key == pygame.K_b:
                        self.path = bfs(self.grid, tuple(self.robot_pos), self.goal)
                    else:
                        self.handle_movement(event.key)

            draw_grid(self.screen, self.grid, self.path, self.start, self.goal, 
                     self.robot_pos, self.images, self.step_count, self.game_completed)
            pygame.display.flip()

    def handle_movement(self, key):
        x, y = self.robot_pos
        moved = False

        if key == pygame.K_LEFT and x > 0 and self.grid[y][x-1] == 0:
            x -= 1
            moved = True
        elif key == pygame.K_RIGHT and x < COLS-1 and self.grid[y][x+1] == 0:
            x += 1
            moved = True
        elif key == pygame.K_UP and y > 0 and self.grid[y-1][x] == 0:
            y -= 1
            moved = True
        elif key == pygame.K_DOWN and y < ROWS-1 and self.grid[y+1][x] == 0:
            y += 1
            moved = True

        if moved:
            self.robot_pos = [x, y]
            self.step_count += 1
            if (x, y) == self.goal:
                self.game_completed = True
                font = pygame.font.Font(None, 36)
                victory_text = font.render(f"Chuc mung! Ban da hoan thanh voi {self.step_count} buoc!", True, RED)
                text_rect = victory_text.get_rect(center=(WIDTH//2, HEIGHT//2))
                self.screen.blit(victory_text, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)  # Dừng 2 giây để hiển thị thông báo

if __name__ == "__main__":
    game = Game()
    if main_menu(game.screen, WIDTH, HEIGHT):
        game.run()
    pygame.quit()
