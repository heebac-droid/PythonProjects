import pygame  

pygame.init()

#Defines game window length
width = 1000
height = 700
screen = pygame.display.set_mode((width,height))
# text function
def text():
    font = pygame.font.Font("game_text.txt",50)
    hello = font.render("hello",True,(0,0,0))
    screen.blit(hello,(500,100))
#Sets up name for game window
pygame.display.set_caption("pygame development mate")
FPS = pygame.time.Clock() # Frame rate counter
image = pygame.image.load("Kirby.jpeg") # Loads game sprite
x_pos = 200
y_pos = 100
# Used for moving around in game window
change_in_x = 0
change_in_y = 0
running = True
# start of game loop
while running == True:
    text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Used for identifing key being pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                change_in_x -= 10
            elif event.key == pygame.K_l:
                change_in_x += 10
            elif event.key == pygame.K_k:
                change_in_y -= 10
            elif event.key == pygame.K_j:
                change_in_y += 10
        # Used for identifing key not being pressed down
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                change_in_x = 0
            elif event.key == pygame.K_l:
                change_in_x = 0
            elif event.key == pygame.K_k:
                change_in_y = 0
            elif event.key == pygame.K_j:
                change_in_y = 0
    x_pos += change_in_x # Allows sprite to move in game 
    print(f"x: {x_pos}")
    y_pos += change_in_y # Allows sprite to move in game 
    print(f"y: {y_pos}")
    if x_pos > width:
        x_pos = 200 # Returns sprite to view of player
    elif x_pos < -400:
        x_pos = 200 # Returns sprite to view of player
    if y_pos > height:
        y_pos = 100 # Returns sprite to view of player
    elif y_pos < -320:
        y_pos = 100 # Returns sprite to view of player
    screen.fill("white")
    screen.blit(image,(x_pos,y_pos)) # Displays image on top of game window
    pygame.display.update() # updates current actions / inputs to game window
    FPS.tick(60)
