import pygame
from pygame.rect import Rect
import math
import random

pygame.init()

SIZE = width, height = (800, 600)
screen = pygame.display.set_mode(SIZE)
titleFont = pygame.font.SysFont("Times New Roman", 30) # times size 30
LinguleFont = pygame.font.SysFont("Times New Roman", 60, True) # times size 30

# sets color values

# normal colors
RED = (255, 0, 0)
WHT = (255, 255, 255)
RED = (255, 0, 0) 
GRN = (0, 255, 0)
BLU = (0, 0, 255)
WHT = (255, 255, 255)
BLK = (0, 0, 0)
GRY = (75, 75, 75)
BRW = (92, 54, 10)
YLW = (255, 255, 0)
ORA = (255, 165, 0)
PUR = (227, 185, 255)

# house-paint like colors
HBEI = (244, 232, 210)
HRED = (255, 119, 107)
HDRED = (214, 100, 90)
HBRW = (176, 165, 144)

# dark colors
DBLU = (4, 115, 130)
DBRW = (200, 137, 101)
DGRN = (46, 112, 45)
VDGRN = (37, 89, 42)

# light colors
LGRY = (160, 160, 160)
LBLU = (227, 251, 255)
LBRW = (201, 180, 155)
LYLW = (255, 255, 171)
LPNK = (252, 177, 172)
LPUR = (235, 223, 247)
LGRN = (237, 255, 245)

# special colors
SBLU = (166, 200, 255)
SGRN = (82, 219, 79)
PGRN = (193, 225, 193)
JGRN = (0, 163, 108)
WBLU = (133, 231, 255)
NBLU = (2, 9, 33)

# initializes images
backgroundJPEG = pygame.image.load("output-onlinepngtools.png")

running = True
myClock = pygame.time.Clock()
mx = my = 0
backgroundX = 0

#files
frWords = []
frEnWords = []
spWords = []
spEnWords = []
frFile = open("French.txt", "r")
frEnFile = open("French English.txt", "r")
spFile = open("Spanish.txt", "r")
spEnFile = open("Spanish English.txt", "r")

for line in frFile:
  line = line.strip()
  frWords.append(line)

for line in frEnFile:
  line = line.strip()
  frWords.append(line)

for line in spFile:
  line = line.strip()
  frWords.append(line)

for line in spEnFile:
  line = line.strip()
  frWords.append(line)

frFile.close()
frEnFile.close()
spFile.close()
spEnFile.close()

choice = "fr"

# prompts user if they are sure of their descion
def areYouSure(screen, button, mx, my, states, prompt, futureState):

    # draws rectangles 
    # draws background rectangle
    pygame.draw.rect(screen, PGRN, (200, 100, 400, 400))
    pygame.draw.rect(screen, BLK, (200, 100, 400, 400), 20)
    pygame.draw.rect(screen, WHT, (200, 100, 400, 400), 12)
    pygame.draw.rect(screen, BLK, (200, 100, 400, 400), 4)

    # draws yes button
    pygame.draw.rect(screen, WHT, (325, 300, 150, 45))
    pygame.draw.rect(screen, BLK, (325, 300, 150, 45), 2)

    # draws no button
    pygame.draw.rect(screen, WHT, (325, 390, 150, 45))
    pygame.draw.rect(screen, BLK, (325, 390, 150, 45), 2)      

    string = "" # creates an empty string
    height = 0 # assignts the height as zero
    for word in prompt: # for each word in the prompt (given)
        string += word # adds it to the string

        textWidth, textHeight = titleFont.size(string) # finds height and width of the string

         # checks if the string can fits inside the rectangle to its maximum capacity (with grammar)
        if textWidth >= 230 and string[-1] == " " or word == "?":

            inX = (800 - textWidth)//2 # finds the x's position
            areYou = titleFont.render(string, 1, BLK)	 #string, 1, colour - keep as 1
            screen.blit(areYou, (inX, 165+(50*height), textWidth, textHeight)) # blits the prompt
            height += 1 # increases the height
            string = "" # resets the string   

    # finds middle spot for formatting yes
    textWidth, textHeight = titleFont.size("YES")
    yesInX = (325 - textWidth)//2 # finds x middle
    yesInY = (45 - textHeight)//2 # finds y middle
    yes = titleFont.render("YES", 1, BLK)	 #string, 1, colour - keep as 1
    screen.blit(yes, (yesInX+235, yesInY+300, textWidth, textHeight)) # blits yes       

    # finds middle spot for formatting no
    textWidth, textHeight = titleFont.size("NO")
    noInX = (325 - textWidth)//2 # finds x middle
    noInY = (45 - textHeight)//2 # finds y middle
    no = titleFont.render("NO", 1, BLK)	 #string, 1, colour - keep as 1
    screen.blit(no, (noInX+235, noInY+390, textWidth, textHeight)) # blits no

    # defines the sizing for each button, and determines rect
    yesRect = Rect(325, 300, 150, 45)
    noRect = Rect(325, 390, 150, 45)

    # checks if yes is being hovered (with mouse)
    if yesRect.collidepoint(mx, my) == True:
        # draws button with color change (becomes darker green)
        pygame.draw.rect(screen, JGRN, yesRect) 
        pygame.draw.rect(screen, BLK, yesRect, 10) 
        pygame.draw.rect(screen, WHT, yesRect, 5)
        pygame.draw.rect(screen, BLK, yesRect, 2)
        screen.blit(yes, (yesInX+235, yesInY+298, textWidth, textHeight)) # blits yes in slightly different position
        if button == 1: #check for button down
            states = futureState # changes state

    # checks if no button is being hovered (with mouse)
    elif noRect.collidepoint(mx, my) == True:
        # draws button with color change (becomes red)
        pygame.draw.rect(screen, HRED, noRect)
        pygame.draw.rect(screen, BLK, noRect, 10) 
        pygame.draw.rect(screen, WHT, noRect, 5)
        pygame.draw.rect(screen, BLK, noRect, 2)
        screen.blit(no, (noInX+235, noInY+388, textWidth, textHeight)) # blits no in slightly different position
        if button == 1: #check for button down
            states = STATE_HOME # returns to menu

    else: # blits the text normally over the previously drawn buttons       
        screen.blit(no, (noInX+235, noInY+390, textWidth, textHeight)) 

        screen.blit(yes, (yesInX+235, yesInY+300, textWidth, textHeight))

    return states # returns the state

# checks if the state for the buttons at the menu should change
def answerPrompt(isItTrue, stateOri, statesy, fr):
    global choice
    states = stateOri # state becomes equal to the original/previous state

    if isItTrue == True: # checks if there is a state change from button click of function "drawButtons"
        states = statesy # changes state to new state
        if fr == 1:
          choice = "sp"
        elif fr == 2:
          choice == "fr"

    return states

# draws the title
def drawTitle():
    # creates the title text
    textWidth, textHeight = LinguleFont.size("LINGULE")  # takes height and width of text 

    tW = int(textWidth / 2)
    tH = int(textHeight / 2)

    pygame.draw.rect(screen, WHT, (400-15-tW, 150-10-tH, textWidth+30, textHeight+20), 0, 15)
    pygame.draw.rect(screen, BLK, (400-15-tW, 150-10-tH, textWidth+30, textHeight+20), 2, 15)
    titleTop = LinguleFont.render("LINGULE", 1, DGRN)

    screen.blit(titleTop, (400-tW, 150-tH, 200, 100))  #(240, 25, 215, 50)

def drawBackgroundJPEGMenu(screen, xMenuBack):
    # takes image and blits positions accordingly to create a scrolling motion
    screen.blit(backgroundJPEG, pygame.Rect(xMenuBack, 0, width, height)) 
    screen.blit(backgroundJPEG, pygame.Rect(xMenuBack + width, 0, width, height))

# draws buttons for menu screen
def drawButtons(screen, button, mx, my, prompt, xButton, yButton, states): 
    prompt = str(prompt) # what the button will say
    stateChange = False # if the button is clicked and causes a state change

    r = Rect(xButton, yButton, 300, 75) # button dimensions

    # finds the formatting to fit text in the middle
    textWidth, textHeight = titleFont.size(prompt)  # takes height and width of text 
    inX = ((300 - textWidth))//2 + xButton # finds middle x from size
    inY = ((75 - textHeight)//2) + yButton # finds middle y from size
    text = titleFont.render(prompt, 1, BLK)	 #string, 1, colour - keep as 1

    # changes colors if mouse is over button
    if r.collidepoint(mx, my) == True:
        # draws button
        pygame.draw.rect(screen, PGRN, r) 
        pygame.draw.rect(screen, BLK, r, 10) 
        pygame.draw.rect(screen, WHT, r, 5)
        pygame.draw.rect(screen, BLK, r, 2)
        screen.blit(text, (inX, inY-2, textWidth, textHeight))	#rectangle represents where the text will be
        if button == 1: #check for button down
            stateChange = True
          
    else:
        # draws button (normally, no mouse over)
        pygame.draw.rect(screen, WHT, r)
        pygame.draw.rect(screen, BLK, r, 2)
        screen.blit(text, (inX, inY, textWidth, textHeight))	#rectangle represents where the text will be
    
    return stateChange # returns True if state should change and False if not

# draws home button at top right of screen to bring user to menu
def drawHomeButton(states, stateOri, button):
    states = stateOri # states becomes equal to the original/previous state
  
    # defines rect and sizing
    rect = Rect(600, 0, 200, 50)

    # grabs text to make it centred
    textWidth, textHeight = titleFont.size("H O M E")  #BARFONT!!!!!!   
    inX = ((200 - textWidth))//2 + 600
    inY = ((50 - textHeight)//2) 
    text = titleFont.render("H O M E", 1, BLK)	 #string, 1, colour - keep as 1

    # checks for if mouse over button
    if rect.collidepoint(mx, my) == True: # changes button color
        pygame.draw.rect(screen, PGRN, rect)
        pygame.draw.rect(screen, BLK, rect, 10) 
        pygame.draw.rect(screen, WHT, rect, 5)
        pygame.draw.rect(screen, BLK, rect, 2)
        screen.blit(text, (inX, inY-2, textWidth, textHeight))	# rectangle represents where the text will be
        if button == 1: #check for button down
            states = STATE_HOME # changes state to return to menu

    else: 
        # draws button (normal, no mouse over)
        pygame.draw.rect(screen, WHT, (600, 0, 200, 50))
        pygame.draw.rect(screen, BLK, (600, 0, 200, 50), 3)
        pygame.draw.rect(screen, WHT, (600, 0, 200, 50), 2)
        pygame.draw.rect(screen, BLK, (600, 0, 200, 50), 1)        
        screen.blit(text, (inX, inY, textWidth, textHeight))	#rectangle represents where the text will be

    
    return states # returns state, especially if button has been clicked to change into menu

# functions

def drawSquare():
  
  for i in range(6):
 	  for j in range(5):
 		  pygame.draw.rect(screen, WHT,(0,0,50,50),2)


def drawHome(mx, my, button):
  global state
  state = STATE_HOME
  drawBackgroundJPEGMenu(screen, backgroundX)
  drawTitle()

  langQues = drawButtons(screen, button, mx, my, "Language", 50, 300, STATE_LANG) # language button
  gameQues = drawButtons(screen, button, mx, my, "Play Game", 450, 300, STATE_LANG) # language button
  endQues = drawButtons(screen, button, mx, my, "Quit", 250, 450, STATE_LANG) # language button

  state = answerPrompt(langQues, state, STATE_LANG, 3) # checks if state should change
  state = answerPrompt(gameQues, state, STATE_GAME, 3) # checks if state should change
  state = answerPrompt(endQues, state, STATE_SURE, 3) # checks if state should change
  return state

def drawLang(button):
  global state, my, mx
  state = STATE_LANG
  screen.fill(DBLU)
  frenchQues = drawButtons(screen, button, mx, my, "French", 50, 200, STATE_GAME) # french language button
  spanishQues = drawButtons(screen, button, mx, my, "Spanish", 400, 200, STATE_GAME) # spanish language button
  
  state = answerPrompt(frenchQues, state, STATE_GAME, 2) # checks if state should change
  state = answerPrompt(spanishQues, state, STATE_GAME, 1) # checks if state should change

  state = drawHomeButton(state, STATE_LANG, button)
  return state

def drawGame(button):
  global state
  screen.fill(DBLU)

  drawSquare()

  state = drawHomeButton(state, STATE_GAME, button)
  return state



STATE_HOME = 0
STATE_LANG = 1
STATE_GAME = 2
STATE_SURE = 3
STATE_END = 4

state = STATE_HOME

while running:
  button = 0 # resets the button
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_TAB:
        state = STATE_HOME

    if event.type == pygame.MOUSEBUTTONDOWN:
      mx, my = pygame.mouse.get_pos()
      button = event.button

    if event.type == pygame.MOUSEMOTION: # checks mouse movement
      mx, my = event.pos # grabs mouse movement

  if state == STATE_HOME:
    drawHome(mx, my, button)
    backgroundX -= 1  #scrolling background
    if backgroundX < -1*800:
      backgroundX = 0   

  elif state == STATE_LANG:
    state = drawLang(button)

  elif state == STATE_GAME:
    state = drawGame(button)

  elif state == STATE_SURE:
    state = areYouSure(screen, button, mx, my, state, "Are you sure you want to quit?", STATE_END)
  
  elif state == STATE_END:
    running = False

  pygame.display.flip()
  myClock.tick(60)

pygame.quit()