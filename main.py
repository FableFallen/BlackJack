from selectors import SelectSelector
from tkinter.tix import WINDOW
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
    def __init__(self, text, color, size, surf, w ,h, x, y,font = 'arial'):
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.pyfont = pygame.font.Font(self.font, self.size)
        self.textobj = self.pyfont.render(self.text, True, self.color)
        self.textrect = self.textobj.get_rect(center=(w/2,h/2))
        self.x =x
        self.y = y
        self.w, self.h = w,h
        self.surf = surf
        self.font = font
        self.ani = animation(self.color)
        
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

    def draw(self, center, size=None):
        self.textobj = self.pyfont.render(self.text, True, self.color)
        if size != None:
            self.pyfont = pygame.font.Font(self.font, size)
            self.textobj = self.pyfont.render(self.text, True, self.color)
            self.textrect = self.textobj.get_rect()

        if center:  
            self.textrect.x = self.x+(self.w/2-self.textrect.width/2)
            self.textrect.y = self.y+(self.h/2-self.textrect.height/2)

        self.surf.blit(self.textobj, self.textrect)

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

class player:
    def __init__(self):
        pass

def sort(arr):
    tpath = '.\\data\\Cards\\'
    start = len(tpath)
    card_num = ''
    card_suit = ''
    offset = 0
    card_val = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
    temp = ['','','','','','','','','','','','','', '','','','','','','','','','','','','', '','','','','','','','','','','','','', '','','','','','','','','','','','','']
    
    for path in arr:
        section = 0
        #Removes file extension
        card = path[len(tpath):-1].replace('.jp','')
        #removes folder infront example: folder/img.jpg  -> img.jpg
        for folder in ['Diamonds\\','Clubs\\','Hearts\\','Spades\\']:
             if (folder) in card:
                 card = card.replace(folder, '')
        
        card_suit = card
        i = 0
        while i < (len(card_suit)):
            if card_suit[i] in ['0','1','2','3','4','5','6','7','8','9']:
                card_suit = card_suit.replace(card_suit[i], '')
                i -=1
            i+=1

        start = len(path[:len(tpath)+len(card_suit)])+1
        #Getting the card value from the file
        if card_suit == 'clubs':
            offset = 0
            card_num = path[start+len(card_suit): (start + len(card_suit)) + len(card) - len(card_suit)]
        elif card_suit == 'diamonds':
            offset = 1
            card_num = path[start+len(card_suit): (start + len(card_suit)) + len(card) - len(card_suit)]
        elif card_suit == 'hearts':
            offset = 2
            card_num = path[start+len(card_suit): (start + len(card_suit)) + len(card) - len(card_suit)]
        elif card_suit == 'spades':
            offset = 3
            card_num = path[start+len(card_suit): (start + len(card_suit)) + len(card) - len(card_suit)]  
        index = 0
        while index < len(card_val):
            if card_num == card_val[index]:
                break
            index += 1
            section += 4

        temp[section +offset] = path

    return temp

paths = []
cards = []
for folder in ['Diamonds','Clubs','Hearts','Spades']:
    for filename in glob.glob(f'.\\data\\Cards\\{folder}\\*.jpg'):
        paths.append(filename)

paths = (sort(paths))

for path in paths:
    img = pygame.image.load(path)
    cards.append(img)

def game():
    offset = 100
    title = Text('BlackJack', [0,0,0], 80, screen, WINDOW_SIZE[0], WINDOW_SIZE[1], 0, 0, alagard_font)
    game_btn = [pygame.Rect(title.textrect.x-(200 - title.textrect.width)//2, title.textrect.y-(60 - title.textrect.height)//2- offset, 200,60),pygame.Rect(title.textrect.x-(200 - title.textrect.width)//2,title.textrect.y-(60 - title.textrect.height)//2 + offset, 200,60)]
    game_txt = [Text('Hit',[200,254, 22], 50, screen, game_btn[0].width, game_btn[0].height, game_btn[0].x, game_btn[0].y, alagard_font), Text('Stand', [200,254, 22],  10, screen, game_btn[1].w, game_btn[1].h, game_btn[1].x, game_btn[1].y, alagard_font)]
    selector_rect = game_btn[0]
    selectPos = [game_btn[1].y, game_btn[0].y]
    pos_index = 1
    click  = False
    drag = False
    size = 30
    cnt = 0
    while True:
        mx,my = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        #Card Postion
        if cnt >= len(cards):
            cnt = 0
        elif cnt < 0:
            cnt = len(cards)-1
        #Drawing Cards
        screen.blit(cards[cnt], (0,0))
        #Clicking/Dragging Button Actions
        if game_btn[0].collidepoint(mx,my) and drag:
            game_btn[0].x, game_btn[0].y = mx-100, my-50
        elif game_btn[0].collidepoint(mx,my) and click:
            pass
        elif game_btn[1].collidepoint(mx,my) and drag:
            game_btn[1].x, game_btn[1].y = mx-100, my-50

        #Pos Counter
        if pos_index < 0:
            pos_index = 0
        if pos_index > 1:
            pos_index = 1
        
        selector_rect.y = selectPos[pos_index]
        #Selector Rect
        pygame.draw.rect(screen, (145,223,232), selector_rect)

        #Drawing Buttons and Text on buttons
        for i in range(len(game_btn)):
            # pygame.draw.rect(screen, (20,234,200), game_btn[i])
            game_txt[i].draw(True, size)
            game_txt[i].set_animation(10, False,False, True)

        title.draw(True)
        title.set_animation(1, True, False, False)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    drag = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    print(mx-100, ' ' , my-50)
                    click = False
                    drag = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    pos_index += 1
                if event.key == pygame.K_DOWN:
                    pos_index -= 1
                if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_ALT and pygame.KMOD_LCTRL:
                    pygame.quit
                    sys.exit()
                if event.key == pygame.K_MINUS:
                    size -= 10
                    print(size)
                if event.key == pygame.K_EQUALS:
                    size += 10
                    print(size)
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
