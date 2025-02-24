import queue

def bfs(grid, start, goal):
    q = queue.Queue()
    q.put((start, []))
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while not q.empty():
        (x, y), path = q.get()
        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == 0:
                    q.put(((nx, ny), path + [(x, y)]))
    return [] 