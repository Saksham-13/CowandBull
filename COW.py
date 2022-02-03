from operator import indexOf, pos
from turtle import done
import pygame as pg
#from Connect4 import Connect4

pg.init()
FONTS = pg.font.SysFont('comicsans',20)
import random
BLACK = (0,0,0)

screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)
chance = 7
l = []

def repCheck(n):
    a = list(str(n))
    b = True
    for i in a:
        if(a.count(i)>1):
            b = False
    return b
def digitcheck(n):


    
    
    s = str(n)
    if(len(s)==4):
        return True
    else :
        return False
def drawcow(n):
    global l
    n=1
    for i in l:
        if type(i) != str:
            c = i[0] 
            b = i[1]
            chn = i[2]
            choice = i[3]
            
            str1= str(choice)+"   Cows    "+str(c)+"    Bulls   "+str(b) + "    Chances left    "+ str(chn)
            
        else :
            str1 = str(i)
        text1 = FONTS.render(str1,1, BLACK)
        screen.blit(text1,(111,100+(n*30)))
        n=n+1

def cowbull(choice,ans,chn):
    ans1 = str(ans)
    choice1 = choice
    if chn >= 0 :
        if(not digitcheck(choice)):
            print("Enter a four digit number only")
            l.append("Invalid Choice; only four digit number allowed")
            return
        if(not repCheck(choice)):
            print("Invalid Choice; no repetetion of digits allowed")
            l.append("Invalid Choice; no repetetion of digits allowed")
            return
            
        cow=0
        bull = 0
        ans = list(str(ans))
        choice = list(str(choice))
        for i in range(0,len(ans)):
            if(ans[i]==choice[i]):
                bull += 1
                choice[i]=''
        for i in choice:
            cow += ans.count(i)
        
        b = (cow,bull,chn,choice1)
        l.append(b)
        
        if chn == 0:
            l.append("            FINAL ANSWER IS "+ str(ans1))
            return False
        elif bull == 4:
            l.append(str(ans1)+"IS CORRECT ANSWER")
            return False
            
        
        print("Cows ",b[0],"    Bulls   ",b[1] , "\n", "Chances left", chn)
        
       
        
       # if(b[2]==0):
       #     l.append("")
    else : 
        print("answer is ",ans)
        

    

answer = random.randint(1000,9999)
while(not repCheck(answer)):
    answer = random.randint(1000,9999)



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    cho = int(self.text)
                    global chance
                    chance = chance-1
                    b = cowbull(cho,answer,chance)
                    print(l)

                    
                    
                    
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)



def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(220, 50, 140, 32)
    
    input_boxes = [input_box1]
    done = False
    
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:

                done = True
            
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                print(pos)
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((112, 214, 255))#112, 214, 255
        for box in input_boxes:
            box.draw(screen)
        if chance < 7:
            
            drawcow(chance)
            if ( type(l[-1]) == str and not l[-1].startswith("Invalid")):
                pg.time.delay(1000)
                done = True 


            
            


        pg.display.flip()
        clock.tick(30)



main()
