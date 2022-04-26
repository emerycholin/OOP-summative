import pygame
pygame.init()

window = pygame.display.set_mode((750, 500))
pygame.display.set_caption('OOP Summative')

white = (255, 255, 255)
black = (0, 0, 0)

class paddle_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()

class paddle_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1

paddle_1 = paddle_1()
paddle_1.rect.x = 25
paddle_1.rect.y = 225
paddle_2 = paddle_2()
paddle_2.rect.x = 715
paddle_2.rect.y = 225
paddle_speed = 10
pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle_1, paddle_2, pong)

def draw():
    window.fill(black)
    font = pygame.font.SysFont('Standard', 30)
    text = font.render('PONG', False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    window.blit(text, textRect)
    all_sprites.draw(window)
    pygame.display.update()
    
run = True
while run:
    pygame.time.delay(75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle_1.rect.y += -paddle_speed
    if key[pygame.K_s]:
        paddle_1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle_2.rect.y += -paddle_speed
    if key[pygame.K_DOWN]:
        paddle_2.rect.y += paddle_speed

    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    if pong.rect.y > 490:
        pong.dy = -1
    if pong.rect.y < 1:
        pong.dy = 1

    if paddle_1.rect.colliderect(pong.rect):
        pong.dx = 1
    if paddle_2.rect.colliderect(pong.rect):
        pong.dx = -1
    draw()

pygame.quit()