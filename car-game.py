import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("....................CAR GAME....................")
background_color = (34,139,34)

line_height=80
line_width=20
gap=40
clock=pygame.time.Clock()

lines=[]

for i in range(0,screen_height,line_height + gap):
    lines.append(i)
print(lines)

car=pygame.image.load('car3.png')
car=pygame.transform.scale(car,(120,120))

car1=pygame.image.load('car7-removebg-preview.png')
car1=pygame.transform.scale(car1,(120,120))

car2=pygame.image.load('car7-removebg-preview.png')
car2=pygame.transform.scale(car2,(120,120))

car3=pygame.image.load('car7-removebg-preview.png')
car3=pygame.transform.scale(car3,(120,120))

car4=pygame.image.load('car7-removebg-preview.png')
car4=pygame.transform.scale(car4,(120,120))

car5=pygame.image.load('car7-removebg-preview.png')
car5=pygame.transform.scale(car5,(120,120))

car_x=100
car_y=270

car1_x=250
car1_y=100

car2_x=350
car2_y=189

car3_x=250
car3_y=500

car4_x=399
car4_y=500

car5_x=399
car5_y=500

left_bound=screen_width//3
right_bound=2*screen_width//3 - car.get_width()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_x + 20 > 34:
        car_x -= 30

    if keys[pygame.K_RIGHT] and car_x + 100 < 762:
        car_x += 30

    if keys[pygame.K_UP]:
        car_y -= 10

    if keys[pygame.K_DOWN]:
        car_y += 1.75



    screen.fill(background_color)

    pygame.draw.rect(screen,(50, 50, 50), (50, 0, 700, screen_height))

    car1_y += 5
    if car1_y > screen_height:
        car1_y =- 10

    car2_y += 5.5
    if car2_y > screen_height:
        car2_y = -10

    car3_y += 5.55
    if car3_y > screen_height:
        car3_y = -10

    car4_y += 5.67
    if car4_y > screen_height:
        car4_y = -10

    car4_y += 5.67
    if car4_y > screen_height:
        car4_y = -10


    for i in range(len(lines)):
        lines[i] += 5
        if lines[i] > screen_height:
            lines[i] =- line_height

        pygame.draw.rect(screen,'white',(screen_width//2 - line_width//2, lines[i], line_width,line_height))

    screen.blit(car,(car_x,car_y))
    screen.blit(car1, (car1_x, car1_y))
    screen.blit(car2, (car2_x, car2_y))
    screen.blit(car3, (car3_x, car3_y))
    screen.blit(car4, (car4_x, car4_y))
    screen.blit(car5, (car5_x, car5_y))

    player_rect = pygame.Rect(car_x + 40, car_y + 10, car.get_width() - 75, car.get_height() - 10)
    # pygame.draw.rect(screen,'red',player_rect,1)

    hittingthings1_rect = pygame.Rect(car1_x +40, car1_y +10, car1.get_width() -75, car1.get_height() -10)


    hittingthings2_rect = pygame.Rect(car2_x + 40, car2_y + 10, car2.get_width() - 75, car2.get_height() - 10)


    hittingthings3_rect = pygame.Rect(car3_x + 40, car3_y + 10, car3.get_width() - 75, car3.get_height() - 10)


    hittingthings4_rect = pygame.Rect(car4_x + 40, car4_y + 10, car4.get_width() - 75, car4.get_height() - 10)


    hittingthings5_rect = pygame.Rect(car5_x + 40, car5_y + 10, car5.get_width() - 75, car5.get_height() - 10)


    hittingthings2_rect = pygame.Rect(car2_x, car2_y, car2.get_width(), car2.get_height())
    hittingthings3_rect = pygame.Rect(car3_x, car3_y, car3.get_width(), car3.get_height())
    hittingthings4_rect = pygame.Rect(car4_x, car4_y, car4.get_width(), car4.get_height())
    hittingthings5_rect = pygame.Rect(car5_x, car5_y, car5.get_width(), car5.get_height())

    if player_rect.colliderect(hittingthings1_rect):
        font = pygame.font.Font(None, 72)
        text = font.render('GAME OVER!', True, "red")
        screen.blit(text, (200 ,200))
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(hittingthings2_rect):
        font = pygame.font.Font(None, 72)
        text = font.render('GAME OVER!', True, "red")
        screen.blit(text, (200 ,200))
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(hittingthings3_rect):
        font = pygame.font.Font(None, 72)
        text = font.render('GAME OVER!', True, "red")
        screen.blit(text, (200 ,200))
        pygame.display.update()
        pygame.time.wait(50000)
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(hittingthings4_rect):
        font = pygame.font.Font(None, 72)
        text = font.render('GAME OVER!', True, "red")
        screen.blit(text, (200 ,200))
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(hittingthings5_rect):
        font = pygame.font.Font(None, 72)
        text = font.render('GAME OVER!.', True, "red")
        screen.blit(text, (50 ,200))
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    clock.tick(40)
