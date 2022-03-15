from selectors import SelectSelector
from tkinter.tix import WINDOW
import pygame,sys,time,os
from pygame.locals import * # Importing all the modules from pygame
from PIL import Image
import glob

global cards, card_vals
pygame.init()
WINDOW_SIZE = ((600,800))
screen = pygame.display.set_mode(WINDOW_SIZE)
title = pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
alagard_font = "data/fonts/alagard/alagard.ttf"
paths = []
cards = []
card_vals = []

for folder in ['Diamonds','Clubs','Hearts','Spades']:
    for filename in glob.glob(f'.\\data\\Cards\\{folder}\\*.jpg'):
        paths.append(filename)
def sort(arr):
    tpath = '.\\data\\Cards\\'
    start = len(tpath)
    card_num = ''
    card_suit = ''
    offset = 0
    card_val = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
    temp = ['','','','','','','','','','','','','', '','','','','','','','','','','','','', '','','','','','','','','','','','','', '','','','','','','','','','','','','']
    tempValues = []
    for ele in temp:
        tempValues.append(0)

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
        tempValues[section + offset] = (card_num)
    return temp, tempValues

temp = []
paths,temp = sort(paths)

for path in paths:
    img = pygame.image.load(path)
    cards.append(img)
for val in temp:
    if val in ['11','12','13']:
        card_vals.append(10)
    else:
        card_vals.append(int(val))
#Store Cards, Randomize cards, acess cards, card values
class Deck:
    def __init__(self, cards, cardValues):
        self.cards = cards
        self.vals = cardValues
        self.usedCard = []
        self.usedVal = []
        
    def randomize(self, seed):
        for num in seed:
            cardh1 = []
            cardh2 = []
            cardh3 = []
            cardh4 = []
            val1 = []
            val2 = []
            val3 = []
            val4 = []
            allcard = []
            allval = []
            #cut half deck
            if num == '0':
                cardh1 = self.cards[:len(self.cards)//2]
                cardh2 = self.cards[len(self.cards)//2:]
                val1 = self.vals[:len(self.cards)//2]
                val2 = self.vals[len(self.cards)//2:]
                allval = val2 + val1
                allcard = cardh2 + cardh1
            #two halves merge every other riffle shuffle
            if num == '1':
                cardh1 = self.cards[:len(self.cards)//2]
                cardh2 = self.cards[len(self.cards)//2:]
                val1 = self.vals[:len(self.cards)//2]
                val2 = self.vals[len(self.cards)//2:]
                for index in range(len(self.cards)//2):
                    allval.append(val1[index])
                    allval.append(val2[index])
                    allcard.append(cardh1[index])
                    allcard.append(cardh2[index])
            #Middle cut
            if num == '2':
                cardh1 = self.cards[0:13]
                cardh2 = self.cards[13:26]
                cardh3 = self.cards[26:39]
                cardh4 = self.cards[39:]
                val1 = self.vals[0:13]
                val2 = self.vals[13:26]
                val3 = self.vals[26:39]
                val4 = self.vals[39:]
                allval = val2+val3+val1+val4
                allcard = cardh2+cardh3+cardh1+cardh4

            #top cut- 1/3 off top to bottom
            if num == '3':
                cardh1 = self.cards[0:18]
                cardh2 = self.cards[18:34]
                cardh3 = self.cards[34:]
                val1 = self.vals[0:18]
                val2 = self.vals[18:34]
                val3 = self.vals[34:]
                allval = val1+val2+val3
                allcard = cardh2+cardh3+cardh1
            #bottom cut- 1/3 off bottom to top
            if num == '4':
                cardh1 = self.cards[0:18]
                cardh2 = self.cards[18:34]
                cardh3 = self.cards[34:]
                val1 = self.vals[0:18]
                val2 = self.vals[18:34]
                val3 = self.vals[34:]
                allval = val3+val1+val2
                allcard = cardh3+cardh1+cardh2
            self.cards = allcard
            self.vals = allval

    def get_top(self):
        top = self.cards[0]
        top_val = self.vals[0]
        self.usedCard.append(top)
        self.usedVal.append(top_val)
        del self.cards[0]
        del self.vals[0]

        return [top,top_val]

#deck = Deck(cards, cards_vals)
#playerhand = Deal(screen, deck)
#playerhand.drawCard() --> history.append(self.deck.get_top) for i range(len(history)): screen.blit(history[i][0], (0,0))

#Display cards in hand
class Deal:
    def __init__(self, screen, deck, start):
        self.screen = screen
        self.deck = deck
        self.start = start
        self.history = []
        self.first = True
        self.ace_Vals = [False,False,False,False]
    
    def hand(self, x , y):
        cards = []

    def busted(self, new_vals):
        for i in range(len(new_vals)):
            if new_vals[i] == True:
                self.deck.vals[i] == 11 
        sum = 0
        for card in self.history:
            sum += card[1]

        if sum > 21:
            return True
        else:
            return False
    
    def deal_card(self):
        self.history.append(self.deck.get_top())
        if self.first and len(self.history) == 1 and self.history[0][1] == 1:
            self.history[0][1] = 11
            self.first = False
    
    def draw_hand(self):
        offset = 0
        for card in self.history:
            screen.blit(card[0], (0+offset,self.start))
            offset += 100
        

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
                

def game():
    offset = 100
    title = Text('BlackJack', [0,0,0], 80, screen, WINDOW_SIZE[0], WINDOW_SIZE[1], 0, 0, alagard_font)
    game_btn = [pygame.Rect(title.textrect.x-(200 - title.textrect.width)//2, title.textrect.y-(60 - title.textrect.height)//2- offset, 200,60),pygame.Rect(title.textrect.x-(200 - title.textrect.width)//2,title.textrect.y-(60 - title.textrect.height)//2 + offset, 200,60)]
    game_txt = [Text('Hit',[200,254, 22], 50, screen, game_btn[0].width, game_btn[0].height, game_btn[0].x, game_btn[0].y, alagard_font), Text('Stand', [200,254, 22],  10, screen, game_btn[1].w, game_btn[1].h, game_btn[1].x, game_btn[1].y, alagard_font)]
    selector_rect = game_btn[0]
    selectPos = [game_btn[1].y, game_btn[0].y]
    deck = Deck(cards, card_vals)
    deck.randomize('0132102110')
    playerhand = Deal(screen,deck,WINDOW_SIZE[1]-deck.cards[-1].get_height())
    dealerhand = Deal(screen,deck, 0)
    aceValues = [False,False,False,False]
    pos_index = 1
    click  = False
    drag = False
    size = 30
    cnt = 0
    while True:
        if(playerhand.busted(aceValues)):
            title.text = 'You Lose!'
        mx,my = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        # #Card Postion
        # if cnt >= len(cards):
        #     cnt = 0
        # elif cnt < 0:
        #     cnt = len(cards)-1
        # #Drawing Cards
        # screen.blit(cards[cnt], (0,0))
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

        #Draw hands
        playerhand.draw_hand()
        dealerhand.draw_hand()

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
                if event.key == pygame.K_t:
                    print(busted)
                    playerhand.deal_card()
                if event.key == pygame.K_y:
                    print(playerhand.history)
                if event.key == pygame.K_RETURN and selector_rect.colliderect(game_txt[0].textrect) == True:
                    print(selector_rect.colliderect(game_txt[0].textrect) == True)
                    playerhand.deal_card()
                elif event.key == pygame.K_RETURN and selector_rect.colliderect(game_txt[1].textrect) == True:
                    dealerhand.deal_card()
                if event.key == pygame.K_w:
                    pos_index += 1
                if event.key == pygame.K_s:
                    pos_index -= 1
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
