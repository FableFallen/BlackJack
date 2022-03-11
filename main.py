import pygame,sys,time,os
from pygame.locals import * # Importing all the modules from pygame
from PIL import Image
import glob

pygame.init()
WINDOW_SIZE = ((600,800))
screen = pygame.display.set_mode(WINDOW_SIZE)
title = pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
alagard_font = "data/fonts/alagard/alagard.ttf"

class Text:
    def __init__(self, text, size, font = None):
        self.text = text
        self.font = font
        self.size = size
        self.color = [0,0,0]
        self.pyfont = None
        self.textobj = None
        self.textrect = None
        self.x, self.y = 0,0
        self.surf = pygame.display.get_surface()
        self.ani = animation(self.color)
            
    def set_surface(self):
        self.surf = pygame.display.get_surface()
        
    def set_text(self,text):
        self.text = text
        
    def set_color(self,col):
        self.color = col
        
    def set_animation(self, spd = 1, fadein = False, fadeout = False, blink = False):
        if fadein:
            self.color = self.ani.fade(spd)
        elif fadeout:
            self.color = self.ani.fade(spd, True)
        elif blink:
            self.color = self.ani.blink(spd)
            
    def set_surfDim(self):
        self.x,self.y = pygame.display.get_surface().get_size()
        self.x /=2
        self.y /=2
    
    def draw(self, surface, center):
        self.set_surfDim()
        self.pyfont = pygame.font.Font(self.font, self.size)
        self.textobj = self.pyfont.render(self.text, True, self.color)
        self.textrect = self.textobj.get_rect()
        if center:
            self.textrect.center = (self.x, self.y)
        surface.blit(self.textobj, self.textrect)


class animation:
    def __init__(self, color):
        self.col = color
        self.dir = [1,1,1]

    def fade(self,col_spd, rev = False):
        max,min = 255,0
        if rev:
            self.dir = [-1,-1,-1]
            max = 255
            min = 0
        for i in range(3):
            self.col[i] += col_spd * self.dir[i]
            if self.col[i] >= 255:
                self.col[i] = max
            elif self.col[i] <= 0:
                self.col[i] = min
                
        return self.col
    
    def blink(self, col_spd):
        for i in range(3):
            self.col[i] += col_spd * self.dir[i]
            if self.col[i] >= 255:
                self.col[i] = 0
            elif self.col[i] <= 0:
                self.col[i] = 255
                
        return self.col
                
    

paths = []
diamonds = []
def sort(arr):
    temp = []
    tempstr = 'C:\\Users\\bestm\\OneDrive\\Desktop\\Game\\Black Jack\\data\\Cards\\Diamonds\\'
    cnt = 0
    numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','12','13']

    while len(temp) < len(arr):
        for i, num in enumerate(numbers):
            pass
            
        #cnt+=1
    return temp
for filename in glob.glob('C:\\Users\\bestm\\OneDrive\\Desktop\\Game\\Black Jack\\data\\Cards\\Diamonds\\*.jpg'):
    paths.append(filename)

#print(sort(paths))
#print(paths)
for path in paths:
    img = pygame.image.load(path)
    diamonds.append(img)

def game():
    title = Text('Whatever', 40, alagard_font)
    cnt = 0
    while True:
        screen.fill((0,0,0))
        title.draw(screen, True)
        title.set_animation(1, True, False, False)
        if cnt >= len(diamonds):
            cnt = 0
        elif cnt < 0:
            cnt = len(diamonds)-1
        screen.blit(diamonds[cnt], (0,0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_a:
                    cnt -= 1
                if event.key == pygame.K_d:
                    cnt += 1
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()   
        clock.tick(60)
        
game()
