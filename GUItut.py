import button
import pygame
# setup display
WIDTH,HEIGHT= 700,700
pygame.init()
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cow and Bull")
icon = pygame.image.load("cow.png")
pygame.display.set_icon(icon)
# Load images
grass = pygame.image.load("graassland.png")
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
mybutton1 = button.Button(grass,(WIDTH/2),((HEIGHT-200)/3),100,40,CORAL,TOMATO,"BUTTON",WHITE,  FONTS)
mybutton2 = button.Button(grass,(WIDTH/2),((HEIGHT-200)/3*2),100,40,CORAL,TOMATO,"BUTTON",WHITE,  FONTS)
mybutton3 = button.Button(grass,(WIDTH/2),((HEIGHT-200)),100,40,CORAL,TOMATO,"BUTTON",WHITE,  FONTS)
while run:
    clock.tick(FPS)
    WIN.blit(grass,(0,0))
    x,y = pygame.mouse.get_pos()
    mybutton1.draw(x,y)
    mybutton2.draw(x,y)
    mybutton3.draw(x,y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x,click_y = pygame.mouse.get_pos()
            
            if mybutton1.action(click_x,click_y):
                import Connect4
            if mybutton2.action(click_x,click_y):
                import COW
    pygame.display.update()


pygame.quit()
 