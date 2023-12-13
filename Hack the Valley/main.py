import random
import math
from pygame import *
from os import listdir
from os.path import isfile, join

init()
SIZE = WIDTH, HEIGHT = 1000, 700
screen = display.set_mode(SIZE)
display.set_caption("Polyculture")

#the colours
PINK = (194, 157, 164)
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BROWN = (4, 24, 56)
BEIGE = (240, 245, 208)
YELLOW = (250, 226, 72)
BROWN = (214, 126, 24)
RED = (255, 0, 0)
ORANGE = (255, 145, 0)
LIGHTBROWN = (224, 143, 49)
BLUE = (125, 174, 199)

font30 = font.SysFont('Times New Roman', 30)
romanFont = font.Font("Roman SD.ttf", 30)
romanFontSmall = font.Font("Roman SD.ttf", 15)
norseFont = font.Font("Norse.otf", 30)
norseBoldFont = font.Font("Norsebold.otf", 200)

#the images
polyBackground = image.load("polyBackground.jpeg")
polyBackground = transform.scale(polyBackground, (WIDTH, HEIGHT))

polyScollingBG = image.load("polyScrollingBG.png")
polyScollingBG = transform.scale(polyScollingBG, (WIDTH, HEIGHT))

fox1 = image.load("fox (1).png")
fox1 = transform.scale(fox1, (fox1.get_width()*4,fox1.get_height()*4))

fox2 = image.load("fox (2).png")
fox2 = transform.scale(fox2, (fox2.get_width()*4,fox2.get_height()*4))

fox3 = image.load("fox (3).png")
fox3 = transform.scale(fox3, (fox3.get_width()*4,fox3.get_height()*4))


bubbles = image.load("bubbles.png")
bubbles = transform.scale(bubbles, (50,50))

turtle = image.load("turtle(+).png")
turtle = transform.scale(turtle, (50,50))

art = image.load("Art(+).png")
art = transform.scale(art, (50,50))

water = image.load("Water(+).png")
water = transform.scale(water, (50,50))

dirtyWater = image.load("dirtyWater(-).png")
dirtyWater = transform.scale(dirtyWater, (dirtyWater.get_width()//8, dirtyWater.get_height()//8))

question = image.load("question mark.png")
question = transform.scale(question, (50,50))


myClock = time.Clock()
FPS = 60
scollingX = 0

class Character:

  def __init__(self, yCord, width, height):
    self.xCord = 100
    self.yCord = yCord
    self.width = width
    self.height = height
    self.rect = Rect(self.xCord, self.yCord, width, height)
    # self.rect = Rect(self.xCord, self.yCord, 50, 50)

  def drawCharacter(self):
    global foxCount
    #draw.rect(screen, WHITE, (self.xCord, self.yCord, 50, 50))
    screen.blit(foxList[foxCount//8], (self.xCord, self.yCord))
    foxCount += 1
    if foxCount//8 >= len(foxList):
      foxCount = 0


  def setYCord(self, yCord):
    self.yCord = yCord

  def setImage(self, image):
    self.image = image

  def getYCord(self):
    return self.yCord

  def getRect(self):
    return self.rect



#defs

#circle radius = 25
# x, y - centre of circles
def checkCollision(x,y):
  for i in range(character.height):  #length 
    xCor = character.xCord+i  #cor of charact 
    for j in range(character.width):  #length of trash
      yCor = character.yCord+j   #trash top left y-coordinate plus width
      if ((x-xCor)**2 + (y-yCor)**2)**0.5 <= 25:  
        return True


def drawMenu():
  global state, run, mx, my
  state = MENU_STATE

  screen.blit(polyBackground,(0,0))
  #title
  title = norseBoldFont.render("Polyculture", True, WHITE)
  screen.blit(title, (WIDTH / 2 - title.get_width() / 2, 50))

  #draw button to start game
  rectStart = Rect(WIDTH / 2, HEIGHT / 8 * 3, WIDTH / 4, HEIGHT / 8)
  drawButton(rectStart, "START", BROWN, BEIGE, romanFont)

  if rectStart.collidepoint(mx,my) == True:  #check collision with start button
    draw.rect(screen, RED, rectStart, 2)
    if button == 1:  #if user click; start game
      state = GAME_STATE

  #draw button for the library
  rectQuit = Rect(WIDTH / 2, HEIGHT / 8 * 5, WIDTH / 4, HEIGHT / 8)
  drawButton(rectQuit, "QUIT", BROWN, BEIGE, romanFont)

  if rectQuit.collidepoint(mx, my) == True:  #check collision
    draw.rect(screen, RED, rectQuit, 2)
    if button == 1:  #if user left click, go to library page
      run = False
  else:
    drawButton(rectQuit, "QUIT", BROWN, BEIGE, romanFont)


def drawGame():
  global scollingX, points
  screen.blit(polyScollingBG, (scollingX, 0))
  screen.blit(polyScollingBG, (scollingX + polyScollingBG.get_width(), 0))
  scollingX -= 1
  if scollingX < -WIDTH:
    scollingX = 0
  
  character.drawCharacter()
  
  pointText = norseFont.render("Points: "+str(points), True, BROWN)
  textWidth, textHeight = norseFont.size("Points: "+str(points))
  screen.blit(pointText, (WIDTH - textWidth-50, HEIGHT - textHeight-50))


def drawGameOver():
  if button == 1:
    draw.rect(screen, GREEN, (mx, my, 5, 5))

def drawWin():
  if button == 1:
    draw.rect(screen, YELLOW, (mx, my, 5, 5))

questionList = []
def drawCollide(): 
  global state, questionNum, points
  draw.rect(screen, BROWN, (25, 25, 650, 125)) 

  question = questionList[questionNum][0]
  answer = questionList[questionNum][1]
  correction = questionList[questionNum][2]
  
  questionText = norseFont.render(question, True, WHITE)
  screen.blit(questionText,(50, 50))

  rectTrue = Rect(100, 100, 50, 25)
  drawButton(rectTrue, "TRUE", BROWN, BEIGE, romanFontSmall)

  if rectTrue.collidepoint(mx,my) == True:  #check collision with  button
    draw.rect(screen, RED, rectTrue, 2)
    if button == 1:  
      if answer == "T":
        points += 1
      else: 
        points -= 1
      state = GAME_STATE
      questionNum = random.randint(0,61) 
     
  
  rectFalse = Rect(500, 100, 50, 25)
  drawButton(rectFalse, "FALSE", BROWN, BEIGE, romanFontSmall)

  if rectFalse.collidepoint(mx,my) == True:  #check collision with  button
    draw.rect(screen, RED, rectFalse, 2)
    if button == 1:  
      if answer == "F":
        points += 1
      else:
        points -=1
      state = GAME_STATE
      questionNum = random.randint(0,61) 
  

def drawButton(
    rect, word, colourBase, colourWord,
    romanFont):  #a function used to draw all the buttons in the game

  draw.rect(screen, colourBase, rect)  #draw the rectangle of the button

  textWidth, textHeight = romanFont.size(word)  #centre the texts
  start = romanFont.render(word, 1, colourWord)
  inX = (rect[2] - textWidth) // 2
  inY = (rect[3] - textHeight) // 2

  screen.blit(start, (rect[0] + inX, rect[1] + inY))  #display
  draw.rect(screen, WHITE, rect, 2)  #draw the border


def plus(x, y):
  # + choice
  choice = random.choice("turtle, art, water")
  if choice == "turtle":
    screen.blit(turtle, (x,y))
  elif choice == "art":
    screen.blit(art, (x,y))
  else:
    screen.blit(water, (x,y))
  screen.blit(bubbles, (x,y))

def minus(x, y):
  screen.blit(dirtyWater, (x-dirtyWater.get_width()//2,y-dirtyWater.get_height()//2))
  screen.blit(bubbles, (x-bubbles.get_width()//2,y-bubbles.get_height()//2))

def question(x, y):
  screen.blit(question, (x,y))
  screen.blit(bubbles, (x,y))


run = True
button = 0

#states
MENU_STATE = 0
GAME_STATE = 1
GAME_OVER_STATE = 2
WIN_STATE = 3
COLLIDE_STATE = 4

state = MENU_STATE
mx = my = 0

#Lists
plusList = [] + [[1000, random.randint(100, HEIGHT - 100)]]
minusList = [] + [[1000, random.randint(100, HEIGHT - 100)]]
points = 0
obstacleSpeed=1


# characterRect = 

JUMPING = False
PRESS_DOWN = False
keyDown1 = False
GROUND = HEIGHT-fox1.get_height()-50
shotTimer = time.get_ticks()
shotTimer1 = time.get_ticks()

foxList = [fox1, fox2, fox3]
foxCount = 0

# sound
"""fireSound = mixer.Sound("fire.wav")
fireSound.play()"""

point = 0

questions = open("questions.txt","r")

while True:

  line = questions.readline()
  line = line.rstrip("\n")

  if line == "":
    break

  parts = line.split("/")
  questionList += [parts]
 
  
questions.close()
questionNum = random.randint(0,61) 

while run:

  objMove = 5 #initialize the speed for how fast the obj moves
  frequency = 400
  

  for e in event.get():
    if e.type == QUIT:
      run = False
    if e.type == MOUSEBUTTONDOWN:
      mx, my = e.pos
      button = e.button
      PRESS_DOWN = True
    elif e.type == MOUSEMOTION:
      mx, my = e.pos
    elif e.type == MOUSEBUTTONUP:
      button = 0


    if e.type == KEYDOWN: #detect the keys, check keys

      keys = e.unicode  #keys detection
      keyCode = e.key
  
      keyDown1 = True
  

      if e.key == K_UP:  #press up
        PRESS_UP = True
        if JUMPING == False:  #if the character was not jumping
          JUMPING = True
          speed = 60
          acceleration = -6  #acceleration for jumping in land
  
      if e.key == K_DOWN:  #press down
        PRESS_DOWN = True

    if e.type == KEYUP:  #if key up, boolean variables become false
      keyDown1 = False

      if e.key == K_UP:
        PRESS_UP = False
      if e.key == K_DOWN:
        PRESS_DOWN = False 
  
  if state == MENU_STATE:
    drawMenu()
    character = Character(600, fox1.get_width(),fox1.get_height())

    time0 = time.get_ticks()

    point = 0
  #Read the data before everything starts. 
    questions = open("questions.txt","r")
    while True:

      line = questions.readline()
      line = line.rstrip("\n")

      if line == "":
        break
        state = MENU_STATE

      parts = line.split("/")
      questionList += [parts]

    # questionText = parts[0]
    # answerText = parts[1]
    # displayText = parts[2]

    questions.close()
    
  elif state == GAME_STATE:
    drawGame()

    gameTimer = time.get_ticks()  #game timer or current time

    if JUMPING == True:  #if jumping is true

      if PRESS_DOWN == True:  #if press down

        character.setYCord(character.getYCord() - speed)      #character acceleration increase  
        speed += acceleration

        if character.getYCord() >= GROUND:  #if y-coordinate greater than ground
          character.setYCord(GROUND)
          PRESS_DOWN = False  #jumping and press-down is false
          JUMPING = False

      else:
        character.setYCord(character.getYCord() - speed) 
        speed -= 1

        if character.getYCord() >= GROUND:  #if character greater or equal to GROUND
          character.setYCord(GROUND) #reset variables
          JUMPING = False      

    elif character.getYCord() >= GROUND:  #if characterY greater than GROUND, set it on ground
      character.setYCord(GROUND) 
    
    for i in range(len(minusList)-1,-1,-1):
      minus(minusList[i][0], int(minusList[i][1]))
      # if len(minusList) < 5:
      minusY = minusList[i][1]  #y-coordinates of trash
      minusX = minusList[i][0]   #x-coordinates of trash
      if checkCollision(minusX,minusY):
      # if character.rect.colliderect(Rect(minusList[i][0],minusList[i][1],50, 50)):
        points -= 1
        del minusList[i]
        state = COLLIDE_STATE
        break

      if (gameTimer - time0) > 40000:  
        objMove = 10
        frequency = 530            
      elif gameTimer - time0 >= 35000:
        objMove = 9
        frequency = 570      
      elif gameTimer - time0 >= 25000:
        objMove = 8
        frequency = 620
      elif gameTimer - time0 >= 20000:
        objMove = 7
        frequency = 650      
      elif gameTimer - time0 >= 10000:
        objMove = 6
        frequency = 500


      minusList[i][0] -= objMove # move obj
        
      if minusList[i][0] < -50: # if off screen
        del minusList[i] # delete current 

      if time.get_ticks() - shotTimer >= frequency:
        xCord1 = 1000
        yCord1 = random.randint(100, HEIGHT - 100)
        minusList += [[xCord1, yCord1]]

        shotTimer = time.get_ticks() # reset timer   
        

    for i in range(len(plusList)-1,-1,-1):
      plus(int(plusList[i][0]), int(plusList[i][1]))
      # if len(minusList) < 5:
      plusY = plusList[i][1]  #y-coordinates of trash
      plusX = plusList[i][0]   #x-coordinates of trash
      if checkCollision(plusX,plusY):
      # if character.rect.colliderect(Rect(plusList[i][0],plusList[i][1],50, 50)):
        points += 1
        del plusList[i]
        state = COLLIDE_STATE
        break
      
    if (gameTimer - time0) > 40000:  
      if (gameTimer - time0) > 40000:  
        objMove = 10
        frequency1 = 530            
      elif gameTimer - time0 >= 35000:
        objMove = 9
        frequency1 = 570      
      elif gameTimer - time0 >= 25000:
        objMove = 8
        frequency1 = 620
      elif gameTimer - time0 >= 20000:
        objMove = 7
        frequency1 = 650      
      elif gameTimer - time0 >= 10000:
        objMove = 6
        frequency1 = 500

      plusList[i][0] -= objMove # move obj

      if plusList[i][0] < -50: # if off screen
        del plusList[i] # delete current 

      if time.get_ticks() - shotTimer1 >= frequency1:
        xCord1 = 1000
        yCord1 = random.randint(100, HEIGHT - 100)
        plusList += [[xCord1, yCord1]]

        shotTimer1 = time.get_ticks() # reset timer   
        
    
  elif state == GAME_OVER_STATE:
    drawGameOver()

  elif state == WIN_STATE:
    drawWin()

  elif state == COLLIDE_STATE:
    drawCollide()

  display.flip()
  myClock.tick(FPS)  

quit()
