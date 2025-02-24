import random
from constants import ROWS, COLS

def create_maze():
    # Khởi tạo grid với tường
    grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]
    
    def _generate(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < COLS and 0 <= new_y < ROWS and grid[new_y][new_x] == 1:
                grid[y][x] = 0
                grid[y + dy//2][x + dx//2] = 0
                grid[new_y][new_x] = 0
                _generate(new_x, new_y)

    # Bắt đầu tạo mê cung từ (1,1)
    _generate(1, 1)
    
    # Đặt điểm bắt đầu và đích
    start = (1, 1)
    goal = (COLS-2, ROWS-2)
    grid[start[1]][start[0]] = 0
    grid[goal[1]][goal[0]] = 0
    
    # Đảm bảo có đường đi đến đích
    def ensure_path_to_goal():
        current_x, current_y = goal
        while (current_x, current_y) != start:
            if current_x > start[0]:
                current_x -= 1
            elif current_x < start[0]:
                current_x += 1
            if current_y > start[1]:
                current_y -= 1
            elif current_y < start[1]:
                current_y += 1
            grid[current_y][current_x] = 0

    ensure_path_to_goal()
    return grid, start, goal 