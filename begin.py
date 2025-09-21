import pygame  

pygame.init()

screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("pygame development mate")
FPS = pygame.time.Clock()
image = pygame.image.load("Kirby.jpeg")
x_pos = 200
y_pos = 100
change_in_x = 0
change_in_y = 0
kirby_speed = 0
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                change_in_x -= 10
            elif event.key == pygame.K_l:
                change_in_x += 10
            elif event.key == pygame.K_k:
                change_in_y -= 10
            elif event.key == pygame.K_j:
                change_in_y += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                change_in_x = 0
            elif event.key == pygame.K_l:
                change_in_x = 0
            elif event.key == pygame.K_k:
                change_in_y = 0
            elif event.key == pygame.K_j:
                change_in_y = 0
    x_pos += change_in_x
    y_pos += change_in_y
    screen.fill("white")
    screen.blit(image,(x_pos,y_pos))
    pygame.display.update()
    FPS.tick(60)
