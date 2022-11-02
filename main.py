from selectors import SelectSelector
from tkinter.tix import WINDOW
import pygame,sys, random,time
from pygame.locals import * # Importing all the modules from pygame
from PIL import Image
import glob

global cards, card_vals
pygame.init()
WINDOW_SIZE = ((600,700))
screen = pygame.display.set_mode(WINDOW_SIZE)
title = pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
alagard_font = "data/fonts/alagard/alagard.ttf"
backCard = 'data/Cards/Back_0.jpg'
backCard_img = pygame.image.load(backCard)
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

def load_animation(loc, type):
    frames = []
    for filename in glob.glob(f'.\\data\\{loc}\\*.{type}'):
        frames.append(filename)
    print(frames)

load_animation("ace","png")
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
            elif num == '1':
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
            elif num == '2':
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
            elif num == '3':
                cardh1 = self.cards[0:18]
                cardh2 = self.cards[18:34]
                cardh3 = self.cards[34:]
                val1 = self.vals[0:18]
                val2 = self.vals[18:34]
                val3 = self.vals[34:]
                allval = val2+val3+val1
                allcard = cardh2+cardh3+cardh1
            #bottom cut- 1/3 off bottom to top
            elif num == '4':
                cardh1 = self.cards[0:18]
                cardh2 = self.cards[18:34]
                cardh3 = self.cards[34:]
                val1 = self.vals[0:18]
                val2 = self.vals[18:34]
                val3 = self.vals[34:]
                allval = val3+val1+val2
                allcard = cardh3+cardh1+cardh2 
            #Cut Middle of Middle and half cut
            elif num == '5':
                tempcards = None
                tempvals = None
                cardh1 = self.cards[0:13]
                cardh2 = self.cards[13:26]
                cardh3 = self.cards[26:39]
                cardh4 = self.cards[39:]
                val1 = self.vals[0:13]
                val2 = self.vals[13:26]
                val3 = self.vals[26:39]
                val4 = self.vals[39:]
                tempcards = cardh2+cardh3+cardh1+cardh4
                tempvals = val2+val3+val1+val4
                cardh1 = tempcards[:13-6]
                cardh2 = tempcards[13-6:13+6]
                cardh3 = tempcards[19:]
                val1 = tempvals[:13-6]
                val2 = tempvals[13-6:13+6]
                val3 = tempvals[19:]
                tempcards = cardh1 + cardh2 + cardh3
                tempvals = val1 + val2 + val3
                cardh1 = tempcards[:26]
                cardh2 = tempcards[26:]
                val1 = tempvals[:26]
                val2 = tempvals[26:]
                allcard = cardh1 + cardh2
                allval = val1 + val2
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

#Display cards in hand
class Deal:
    def __init__(self, screen, deck, start, dealer = False):
        self.screen = screen
        self.deck = deck
        self.start = start
        self.history = []
        self.first = True
        self.aceValues = [False,False,False,False]
        self.backCard_img = backCard_img
        self.dealer = dealer
        self.holdCard = None
        if self.dealer: self.holdCard = [self.deck.cards[1], self.deck.vals[1]]

    def get_Sum(self):
        sum = 0
        for card in self.history:
            sum += card[1]
        return sum

    def busted(self, aceValues):
        self.aceValues = aceValues
        for i in range(len(self.aceValues)):
            if self.aceValues[i] == True:
                self.deck.vals[i] == 11 

        if self.get_Sum() > 21:
            return True
        else:
            return False
    
    def winState(self, other, dealer = False):
        if self.get_Sum() >= 16 or dealer == False:
            if self.get_Sum() > other.get_Sum() or (dealer and self.get_Sum() == other.get_Sum()):
                return True
            else:
                return False

    def deal_card(self):
        top = self.deck.get_top()
        self.history.append(top)
        if top[1] == 1 and len(self.history) == 1:
            for index in range(len(self.aceValues)):
                if self.aceValues[index] == False:
                    self.aceValues[index] = True
                    break
            
        elif self.dealer and len(self.history) == 2:
            self.history[1] = [self.backCard_img,top[1]]
            self.screen.blit(top[0], (300,200))
        elif self.dealer and len(self.history)>2:
            self.history[1] = self.holdCard
        elif self.first and len(self.history) == 1 and self.history[0][1] == 1:
            self.history[0][1] = 11
            self.first = False
    
    def dealer_draw(self):
        self.history[1] = self.holdCard
        while not(self.busted(self.aceValues)) and self.get_Sum() < 16:
            self.deal_card()
        return self.busted(self.aceValues)

    def draw_hand(self):
        offset = 0
        for card in self.history:
            screen.blit(card[0], (0+offset,self.start))
            offset += 100
        

class Text:
    def __init__(self, color, size, surf, w, h, x, y, text = '', font = 'arial'):
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.pyfont = pygame.font.Font(self.font, self.size)
        self.textobj = self.pyfont.render(self.text, True, self.color)
        self.textrect = self.textobj.get_rect(center=(w/2, h/2))
        self.x = x
        self.y = y
        self.w, self.h = w, h
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

    def set_loc(self,w,h,x,y):
        self.w,self.h,self.x,self.y = w,h,x,y

    def draw(self, center, w=0, h=0, x=0, y=0, text = '', size=None, color = []):
        if len(text) > 0:
            self.text = text
        if len(color) > 0:
            self.color = color
        if(x != 0 and y!= 0) or (w != 0 and h!= 0):
            self.w = w
            self.h = h
            self.x = x
            self.y = y
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
                
def aceOptionWindow(hand):
    xoffset = 60
    yoffset = -80
    width, height = 100,60
    mainText = Text([255,0,255], 80, screen, WINDOW_SIZE[0], WINDOW_SIZE[1], 0, 0, 'Ace\'s Option', alagard_font)
    buttons = [pygame.Rect(mainText.textrect.x-(width - mainText.textrect.width)//2-xoffset, mainText.textrect.y-(height-mainText.textrect.height)//2-yoffset, width, height), pygame.Rect(mainText.textrect.x-(width - mainText.textrect.width)//2+xoffset, mainText.textrect.y-(height-mainText.textrect.height)//2-yoffset, width, height)]
    selector = pygame.Rect(mainText.textrect.x-(width - mainText.textrect.width)//2-xoffset, mainText.textrect.y-(height-mainText.textrect.height)//2-yoffset, width, height)
    optionText = Text([0,255,255], 50, screen, buttons[0].w, buttons[0].h, buttons[0].x,buttons[0].y, '1', alagard_font)
    pos_index = 0
    while 1:
        screen.fill((255,255,255))
        if pos_index > 1:
            pos_index = 1
        elif pos_index < 0:
            pos_index = 0
        selector.x,selector.y = buttons[pos_index].x, buttons[pos_index].y
        pygame.draw.rect(screen, [0,0,0], selector)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if pos_index == 0:
                        return 1
                    else:
                        return 11
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pos_index -= 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pos_index += 1
        mainText.draw(True)
        
        if (pos_index <= 0):
            optionText.draw(True,buttons[0].w, buttons[0].h, buttons[0].x,buttons[0].y, '1', 50, [0,255,255])
        if (pos_index<=0):
            optionText.draw(True,buttons[1].w, buttons[1].h, buttons[1].x,buttons[1].y, '11', 20, [255,34,90])
        if (pos_index >= 1):
            optionText.draw(True,buttons[1].w, buttons[1].h, buttons[1].x,buttons[1].y, '11', 50, [0,255,255])
        if (pos_index>=1):
            optionText.draw(True,buttons[0].w, buttons[0].h, buttons[0].x,buttons[0].y, '1', 20, [255,34,90])
            
        pygame.display.update()
        clock.tick(60)

def resultMenu(result):
    xoffset = 60
    yoffset = -80
    width, height = 100,60
    mainText = Text([255,0,255], 80, screen, WINDOW_SIZE[0], WINDOW_SIZE[1], 0, 0, f'You {result}', alagard_font)
    buttons = [pygame.Rect(mainText.textrect.x-(width - mainText.textrect.width)//2-xoffset, mainText.textrect.y-(height-mainText.textrect.height)//2-yoffset, width, height), pygame.Rect(mainText.textrect.x-(width - mainText.textrect.width)//2+xoffset, mainText.textrect.y-(height-mainText.textrect.height)//2-yoffset, width, height)]
    selector = pygame.Rect(mainText.textrect.x-(width - mainText.textrect.width)//2-xoffset, mainText.textrect.y-(height-mainText.textrect.height)//2-yoffset, width, height)
    optionText = Text([0,255,255], 50, screen, buttons[0].w, buttons[0].h, buttons[0].x,buttons[0].y, '1', alagard_font)
    pos_index = 0
    while 1:
        screen.fill((255,255,255))
        if pos_index > 1:
            pos_index = 1
        elif pos_index < 0:
            pos_index = 0
        selector.x,selector.y = buttons[pos_index].x, buttons[pos_index].y
        pygame.draw.rect(screen, [0,0,0], selector)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if pos_index == 0:
                        game()
                    else:
                        sys.exit()
                        pygame.exit()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pos_index -= 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pos_index += 1
        mainText.draw(True)
        
        if (pos_index <= 0):
            optionText.draw(True,buttons[0].w, buttons[0].h, buttons[0].x,buttons[0].y, 'Retry', 35, [0,255,255])
        if (pos_index>=1):
            optionText.draw(True,buttons[0].w, buttons[0].h, buttons[0].x,buttons[0].y, 'Retry', 20, [255,34,90])
        if (pos_index >= 1):
            optionText.draw(True,buttons[1].w, buttons[1].h, buttons[1].x,buttons[1].y, 'QUIT', 35, [0,255,255])
        if (pos_index<=0):
            optionText.draw(True,buttons[1].w, buttons[1].h, buttons[1].x,buttons[1].y, 'QUIT', 20, [255,34,90])
            
        pygame.display.update()
        clock.tick(60)

def run_once(f):
    def wrapper(*args,**kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args,**kwargs)
    wrapper.has_run = False
    return wrapper

def game():
    seed = ''
    for i in range(20):
        seed += (str(random.randint(0,5)))

    offset = 100
    title = Text([0,0,0], 80, screen, WINDOW_SIZE[0], WINDOW_SIZE[1], 0, 0, 'BlackJack', alagard_font)
    game_btn = [pygame.Rect(title.textrect.x-(200 - title.textrect.width)//2, title.textrect.y-(60 - title.textrect.height)//2- offset, 200,60),pygame.Rect(title.textrect.x-(200 - title.textrect.width)//2,title.textrect.y-(60 - title.textrect.height)//2 + offset, 200,60)]
    game_txt = [Text([200,254, 22], 50, screen, game_btn[0].width, game_btn[0].height, game_btn[0].x, game_btn[0].y, 'Hit', alagard_font), Text([200,254, 22],  50, screen, game_btn[1].w, game_btn[1].h, game_btn[1].x, game_btn[1].y, 'Stand', alagard_font)]
    selector_rect = game_btn[0]
    selectPos = [game_btn[1].y, game_btn[0].y]
    deck = Deck(cards, card_vals)
    print(seed)
    deck.randomize(seed)
    playerhand = Deal(screen,deck,WINDOW_SIZE[1]-deck.cards[-1].get_height())
    dealerhand = Deal(screen,deck, 0, True)
    aceValues = [False,False,False,False]
    pos_index = 1
    click  = False
    drag = False
    size = 30
    for i in range(2):
        dealerhand.deal_card()
    dealerhand.draw_hand()
    selected = False
    locked = False
    standed = False
    surf = pygame.display.get_surface().get_rect()
    veil = pygame.Surface(surf.size)
    veil.fill([255,255,255])
    alpha = 0
    TICK = USEREVENT + 1 # event type
    pygame.time.set_timer(TICK, 1000)
    time = 0
    duration_reach = False
    duration_limit = 3
    duration = 0
    run_once = False
    while True:
        mx,my = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        
        if game_btn[0].collidepoint(mx,my) and drag:
            game_btn[0].x, game_btn[0].y = mx-100, my-50
        elif game_btn[0].collidepoint(mx,my) and click:
            pass
        elif game_btn[1].collidepoint(mx,my) and drag:
            game_btn[1].x, game_btn[1].y = mx-100, my-50

        #Button Pos Counter
        if pos_index < 0:
            pos_index = 0
        if pos_index > 1:
            pos_index = 1
        
        selector_rect.y = selectPos[pos_index]
        #Selector Rect
        pygame.draw.rect(screen, (145,223,232), selector_rect)
         
        #Drawing Buttons and Text on buttons
        for i in range(len(game_btn)):
            game_txt[i].draw(True, size)
            game_txt[i].set_animation(10, False,False, True)
            
        #Draw hands
        playerhand.draw_hand()
        dealerhand.draw_hand()

        #Drawing Text
        title.draw(True)
        title.set_animation(1, True, False, False)
        
        #Checking Winning States
        if(playerhand.busted(aceValues) or (standed and dealerhand.winState(playerhand, True))):
            if run_once == False:
                duration = time
                print(f'Duration: {duration}\nCurrent Time: {time}')
                run_once = True
            if duration_reach:
                resultMenu('Lose!')
        if(dealerhand.busted(aceValues) or (standed and playerhand.winState(dealerhand))):
            if run_once == False:
                duration = time
                print(f'Duration: {duration}\nCurrent Time: {time}')
                run_once = True
            if duration_reach:
                resultMenu('Won!')

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
                if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_ALT and pygame.KMOD_LCTRL:
                    pygame.quit
                    sys.exit()
                if locked == False and event.key == pygame.K_RETURN and selector_rect.colliderect(game_txt[0].textrect):
                    print('Hit')
                    playerhand.deal_card()
                    print(playerhand.get_Sum())
                    if playerhand.history[-1][1] == 1:
                        selected = True
                if locked == False and event.key == pygame.K_RETURN and selector_rect.colliderect(game_txt[1].textrect):
                    print('Stand')
                    standed = True
                    dealerhand.dealer_draw()
                    print(dealerhand.get_Sum())
                if locked == False and event.key == pygame.K_w or event.key == pygame.K_UP:
                    pos_index += 1
                if locked == False and event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pos_index -= 1
                if event.key == pygame.K_MINUS:
                    size -= 10
                    print(size)
                if event.key == pygame.K_EQUALS:
                    size += 10
                    print(size)
                if event.key == pygame.K_r:
                    game()
                if event.key == pygame.K_a:
                    print(playerhand.busted(aceValues))
                if event.key == pygame.K_e:
                    print(time)
            if event.type == TICK:
                time += 1
                      
        #Ace Selector
        if(len(playerhand.history) > 0) and (playerhand.history[-1][1] == 1) and (selected):
            playerhand.history[-1][1] = aceOptionWindow(playerhand)
            print(playerhand.get_Sum())
            selected = False
        
        if duration != 0 and ((time - duration) < duration_limit):
            alpha += 2
        elif duration != 0 and time - duration == duration_limit:
            duration_reach = True
        veil.set_alpha(alpha)
        screen.blit(veil, (0,0))

        pygame.display.update()   
        clock.tick(60)

game()