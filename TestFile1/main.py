import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong Game")

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.dx = 3
        self.dy = 3

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

# Create paddles and ball
paddle1 = Paddle(50, 250)
paddle2 = Paddle(740, 250)
ball = Ball(395, 295)

# Scores
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.rect.y -= 5
    if keys[pygame.K_s]:
        paddle1.rect.y += 5
    if keys[pygame.K_UP]:
        paddle2.rect.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.rect.y += 5

    ball.move()

    if ball.rect.top <= 0 or ball.rect.bottom >= 600:
        ball.dy *= -1
    if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
        ball.dx *= -1

    if ball.rect.left <= 0:
        score2 += 1
        ball.rect.x, ball.rect.y = 395, 295
    if ball.rect.right >= 800:
        score1 += 1
        ball.rect.x, ball.rect.y = 395, 295

    screen.fill((0, 0, 0))
    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)

    text = font.render(f"{score1} - {score2}", True, (255, 255, 255))
    screen.blit(text, (340, 10))
    pygame.display.flip()

pygame.quit()