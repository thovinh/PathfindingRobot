import pygame

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (70, 130, 180)  # Steel Blue
BUTTON_HOVER_COLOR = (100, 149, 237)  # Cornflower Blue
BUTTON_TEXT_COLOR = WHITE

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.is_hovered = False
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        color = BUTTON_HOVER_COLOR if self.is_hovered else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        text_surface = self.font.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False

def show_instructions(screen, WIDTH, HEIGHT):
    font = pygame.font.Font(None, 36)
    instruction_text = [
        "Hướng dẫn chơi:",
        "- Sử dụng các phím mũi tên để di chuyển robot",
        "- Nhấn phím B để AI tìm đường đi",
        "- Di chuyển robot đến đích (ô màu đỏ)",
        "",
        "Nhấn SPACE để trở về menu"
    ]
    
    running = True
    while running:
        screen.fill(WHITE)
        y = HEIGHT // 4
        
        for line in instruction_text:
            text_surface = font.render(line, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH//2, y))
            screen.blit(text_surface, text_rect)
            y += 50
            
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
    return True

def main_menu(screen, WIDTH, HEIGHT):
    font = pygame.font.Font(None, 36)
    start_button = Button(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 50, "Bat dau")
    instruction_button = Button(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50, "Huong dan")
    
    running = True
    while running:
        screen.fill(WHITE)
        
        # Ve tieu de
        title_text = font.render("PATHFINDING ROBOT", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH//2, HEIGHT//4))
        screen.blit(title_text, title_rect)
        
        # Vẽ các nút
        start_button.draw(screen)
        instruction_button.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if start_button.handle_event(event):
                return True
                
            if instruction_button.handle_event(event):
                if not show_instructions(screen, WIDTH, HEIGHT):
                    return False
    return False
