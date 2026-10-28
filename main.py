
import pygame

pygame.init()

# Step 1: Create game window
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

Blue = (0, 255, 255)
Red = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

bg = pygame.Rect(0, 0, 500, 500)

# Step 2: Create Classes

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 80)
        self.speed = 5

    def move(self, up_key, down_key, walls):
        keys = pygame.key.get_pressed()
        old_pos = self.rect.copy()

        if keys[up_key]:
            self.rect.y -= self.speed

        if keys[down_key]:
            self.rect.y += self.speed

        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect = old_pos
                break

    def draw(self, surface):
        pygame.draw.rect(surface, Blue, self.rect)


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed_x = 4
        self.speed_y = 4

    def update(self, paddles, walls):
        # Move the ball
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Collision with top and bottom walls
        for wall in walls:
            if self.rect.colliderect(wall):
                self.speed_y = -self.speed_y
                break

        # Collision with paddles
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.speed_x = -self.speed_x

                if self.speed_x > 0:
                    self.rect.left = paddle.rect.right
                else:
                    self.rect.right = paddle.rect.left

                break

    def draw(self, surface):
        pygame.draw.rect(surface, Red, self.rect)

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.speed_x = -self.speed_x


# Step 3: Create Objects
player1 = Paddle(50, 500 // 2 - 40)
player2 = Paddle(500 - 60, 500 // 2 - 40)

ball = Ball(500 // 2, 500 // 2)

walls = [
    pygame.Rect(0, 0, 500, 10),
    pygame.Rect(0, 490, 500, 10)
]

score1 = 0
score2 = 0

font = pygame.font.SysFont(None, 36)

# Step 4: Game Loop
run = True

while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Paddle movement
    player1.move(pygame.K_w, pygame.K_s, walls)
    player2.move(pygame.K_UP, pygame.K_DOWN, walls)

    # Ball movement
    ball.update([player1, player2], walls)

    # Scoring
    if ball.rect.left <= 0:
        score2 += 1
        ball.reset(500 // 2, 500 // 2)

    if ball.rect.right >= 500:
        score1 += 1
        ball.reset(500 // 2, 500 // 2)

    # Draw background
    window.fill(BLACK)

    # Draw paddles and ball
    player1.draw(window)
    player2.draw(window)
    ball.draw(window)

    # Draw score
    score_text = font.render(
        f"{score1} : {score2}",
        True,
        WHITE
    )

    window.blit(
        score_text,
        (500 // 2 - score_text.get_width() // 2, 20)
    )

    pygame.display.update()
    clock.tick(60)

pygame.quit()
