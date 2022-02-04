import button
import pygame
pygame.init()
# Load images
grass = pygame.image.load("graassland.png")
icon = pygame.image.load("cow.png")
# setup display
WIDTH,HEIGHT= 700,700

WIN=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("ARCADE GAMES")

pygame.display.set_icon(icon)

#colors
CORAL = (255,127,80)
TOMATO = (255,99,71)
WHITE = (255,255,255)
#fonts
FONTS = pygame.font.SysFont('comicsans',20)
pygame.transform.smoothscale(grass,(WIDTH,HEIGHT))
# Setup GameLoop
clock = pygame.time.Clock()
run = True
FPS=60
#create button object
mybutton1 = button.Button(grass,(WIDTH/2),((HEIGHT-200)/4),200,40,CORAL,TOMATO,"CONNECT 4",WHITE,  FONTS)
mybutton2 = button.Button(grass,(WIDTH/2),((HEIGHT-200)/4*2),200,40,CORAL,TOMATO,"COWS AND BULLS",WHITE,  FONTS)
mybutton3 = button.Button(grass,(WIDTH/2),((HEIGHT-200)/4*3),200,40,CORAL,TOMATO,"HANGMAN",WHITE,  FONTS)
mybutton4 = button.Button(grass,(WIDTH/2),((HEIGHT-200)),200,40,CORAL,TOMATO,"FLOOD IT",WHITE,  FONTS)
while run:
    clock.tick(FPS)
    WIN.blit(grass,(0,0))
    x,y = pygame.mouse.get_pos()
    mybutton1.draw(x,y)
    mybutton2.draw(x,y)
    mybutton3.draw(x,y)
    mybutton4.draw(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x,click_y = pygame.mouse.get_pos()
            
            if mybutton1.action(click_x,click_y):
                import Connect4
                WIN=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
                pygame.display.set_caption("ARCADE GAMES")
                pygame.display.set_icon(icon)

            if mybutton2.action(click_x,click_y):
                import COW
                WIN=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
                pygame.display.set_caption("ARCADE GAMES")
                pygame.display.set_icon(icon)
            if mybutton3.action(click_x,click_y):
                from Hangman import hangman
                WIN=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
                pygame.display.set_caption("ARCADE GAMES")
                pygame.display.set_icon(icon)
            if mybutton4.action(click_x,click_y):
                from FloodIT  import Flood_It
                WIN=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
                pygame.display.set_caption("ARCADE GAMES")
                pygame.display.set_icon(icon)
    pygame.display.update()


pygame.quit()
 