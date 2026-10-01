"""A simple Snake game built with Pygame.

Controls:
    Arrow keys / WASD  - move the snake
    R                  - restart after game over
    ESC or window close - quit
"""

import random
import sys

import pygame

# --- Game settings -----------------------------------------------------------
CELL = 24                      # pixel size of one grid cell
GRID_W, GRID_H = 24, 18        # board size in cells
FPS = 8                        # snake speed (cells per second)

WIDTH = CELL * GRID_W
HEIGHT = CELL * GRID_H
TITLE = "Snake"

# --- Colors (R, G, B) --------------------------------------------------------
BG_COLOR = (24, 26, 32)
GRID_COLOR = (32, 35, 42)
SNAKE_HEAD = (120, 220, 120)
SNAKE_BODY = (80, 180, 90)
FOOD_COLOR = (230, 80, 80)
TEXT_COLOR = (235, 235, 235)
OVERLAY_COLOR = (10, 10, 14)

# Movement vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Map of key -> direction
KEY_DIRS = {
    pygame.K_UP: UP,
    pygame.K_w: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_s: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_a: LEFT,
    pygame.K_RIGHT: RIGHT,
    pygame.K_d: RIGHT,
}


def random_food(snake):
    """Pick a random empty cell that is not occupied by the snake."""
    occupied = set(snake)
    free = [(x, y) for x in range(GRID_W) for y in range(GRID_H) if (x, y) not in occupied]
    return random.choice(free)


class SnakeGame:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.reset()

    def reset(self):
        mid = (GRID_W // 2, GRID_H // 2)
        # Snake starts as 3 segments moving to the right
        self.snake = [mid, (mid[0] - 1, mid[1]), (mid[0] - 2, mid[1])]
        self.direction = RIGHT
        self.pending_direction = RIGHT  # direction queued for the next tick
        self.food = random_food(self.snake)
        self.score = 0
        self.game_over = False

    # --- Logic ---------------------------------------------------------------
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_r and self.game_over:
                    self.reset()
                if event.key in KEY_DIRS:
                    new_dir = KEY_DIRS[event.key]
                    # Ignore 180-degree reversals
                    if (new_dir[0] + self.direction[0], new_dir[1] + self.direction[1]) != (0, 0):
                        self.pending_direction = new_dir
        return True

    def tick(self):
        """Advance the game by one step (call at the snake's speed)."""
        if self.game_over:
            return
        self.direction = self.pending_direction
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Wall collision
        if not (0 <= new_head[0] < GRID_W and 0 <= new_head[1] < GRID_H):
            self.game_over = True
            return

        # Self collision (tail cell is about to move away unless we eat)
        eating = new_head == self.food
        body = self.snake if not eating else self.snake[:-1]
        if new_head in body:
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if eating:
            self.score += 1
            self.food = random_food(self.snake)
        else:
            self.snake.pop()

    # --- Drawing -------------------------------------------------------------
    def cell_rect(self, pos):
        return pygame.Rect(pos[0] * CELL, pos[1] * CELL, CELL, CELL)

    def draw(self):
        self.screen.fill(BG_COLOR)

        # Subtle grid lines
        for x in range(0, WIDTH, CELL):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y))

        # Food
        food_rect = self.cell_rect(self.food).inflate(-6, -6)
        pygame.draw.rect(self.screen, FOOD_COLOR, food_rect, border_radius=8)

        # Snake
        for i, segment in enumerate(self.snake):
            color = SNAKE_HEAD if i == 0 else SNAKE_BODY
            rect = self.cell_rect(segment).inflate(-2, -2)
            pygame.draw.rect(self.screen, color, rect, border_radius=6)

        # Score
        score_surf = self.font.render(f"Score: {self.score}", True, TEXT_COLOR)
        self.screen.blit(score_surf, (8, 4))

        # Game over overlay
        if self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((*OVERLAY_COLOR, 200))
            self.screen.blit(overlay, (0, 0))

            over_surf = self.font.render("Game Over!", True, FOOD_COLOR)
            score_text = self.font.render(f"Final score: {self.score}", True, TEXT_COLOR)
            hint_surf = self.font.render("Press R to restart, ESC to quit", True, TEXT_COLOR)

            for surf, dy in ((over_surf, HEIGHT // 2 - 60),
                             (score_text, HEIGHT // 2 - 12),
                             (hint_surf, HEIGHT // 2 + 36)):
                self.screen.blit(surf, surf.get_rect(center=(WIDTH // 2, dy)))

        pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas,menlo,monospace", 24)

    game = SnakeGame(screen, font)

    # Use a millisecond interval so we don't need the time module per tick
    tick_interval = int(1000 / FPS)
    next_tick = pygame.time.get_ticks()

    running = True
    while running:
        running = game.handle_input()

        now = pygame.time.get_ticks()
        if now >= next_tick:
            game.tick()
            next_tick = now + tick_interval

        game.draw()
        clock.tick(60)  # cap frame rate for smooth rendering

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
