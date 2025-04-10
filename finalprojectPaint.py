#this is a painting application. THe user can use a avrety of tools to make whatever they want. The user can use pen, pencil, brush, spray
# and eraser tools to freehand draw an image of their color of choice. The user can save their work and load up images on their computer.
#the user can also choose the background they want to draw on, as well as stamps to put on their work.

from pygame import *
from random import *
from math import *      #all libraries used
from tkinter import *
from tkinter import filedialog

font.init()
root = Tk()     #initialize font and tkinter
root.withdraw()

screen = display.set_mode((1800,1000))
screen.fill((255, 255, 255))    #set background and window size
fieldColor = (255, 255, 255)

def drawTrue(colorChosen, colorUsed):
        colorChosen = True
        colorUsed.remove([0])
        colorUsed.append(colorChosen) #Dead Functions

def shapesTrue(shapeChosen, shapeInUse):
    shapeChosen = 1
    shapeInUse = 0

def drawColorBoxes(x, y, color):
    colorBoxes = Rect(x, y, 50, 50) #draws color boxes
    draw.rect(screen, color, colorBoxes)

def chooseColor(boundary, colorDrawing, selectedColor, colorActuallyUsed):
        colorActuallyUsed += 1
        if Rect(boundary).collidepoint(mx, my) and click:       #useless function
                colorDrawing = selectedColor

def drawStamps(x, y, imageList, rand):
    for i in range(len(imageList)):
	    screen.blit(imageList[0 + rand], (x, y)) #blits all stamps on the screen
	    rand += 1
	    x += 110
def selected(color, field):
    if field.collidepoint(mx, my) and click: #Chages field color if user clicks on a button
        color = (83, 83, 83)
def drawBack(button, listofBack, listElementNum, FieldToDraw):
        if button.collidepoint(mx, my) and click:               #changes image on field when button is pressed
            screen.blit(listofBack[listElementNum], FieldToDraw)
            if listElementNum == len(listofBack):
                    listElementNum = 0
            listElementNum += 1
        
shapes = False
stamps = False #all types of things user can use declared false util user presses on  button to make them true
tools = False
mouseOnCanvas = False
smallerFont = font.SysFont("Arial", 30)
TitleFont = font.SysFont("Arial", 60) #fonts
canvas = Rect(275, 150, 1300, 650) # canvas



redChosen = 0
orangeChosen = 0
yellowChosen = 0
greenChosen = 0
blueChosen = 0
indigoChosen = 0 #previous method of choosing colors
violetChosen = 0
blackChosen = 0
colorSpectrum = image.load("colorchart.jpg")
colorSpectrumBox = Rect(50, 100, 201, 801) 
colorDraw = (0, 0, 0)

#shapes

rectangleChosen = 0
circleChosen = 0
lineChosen = 0 #number will be 1 if shape can be used
fillRect = 0
fillCirc = 0
shapesList = [rectangleChosen, circleChosen, lineChosen]
shapeUsing = [rectangleChosen]

rectangleHover = Rect(1650, 130, 90, 40)
filledRectangleHover = Rect(1650, 130, 90, 40)
lineHover = Rect(1660, 200, 80, 80)
circleHover = Rect(1660, 310, 80, 80) #all field/boxes for shapes
fRectBox = Rect(1050, 875, 80, 80)
fCircBox = Rect(1150, 875, 80, 80)

#Tools

PenBox = Rect(1660, 400, 60, 60)
PencilBox = Rect(1660, 480, 60, 60)
BrushBox = Rect(1660, 560, 60, 60) #all field/boxes for tools
SprayBox = Rect(1660, 640, 60, 60)
EraserBox = Rect(1660, 720, 60, 60)

Pen = 0
Pencil = 0
Brush = 0
Spray = 0 #tools set to false
Eraser = 0

#Stamps
smiley = image.load("smileyfacePaint.png")
car = image.load("carPaintEdited.jpg")
phone = image.load("phonePaint.png") #stamps
house = image.load("housePaint.png")
plane = image.load("planePaint.png")
basketball = image.load("basketballPaint.png")

stampList = [smiley, phone, house, plane, basketball, car]

smileyBox = Rect(300, 875, 60, 60)
phoneBox = Rect(410, 875, 60, 60)
houseBox = Rect(520, 875, 60, 60)
planeBox = Rect(630, 875, 60, 60)
basketballBox = Rect(740, 875, 60, 60)
carBox = Rect(850, 875, 150, 60)

smileyTF = 0
phoneTF = 0
houseTF = 0
planeTF = 0
basketballTF = 0
carTF = 0

#buttons

clearButton = Rect(1635, 60, 100, 30)
saveButton = Rect(1625, 800, 100, 30)
loadButton = Rect(1625, 910, 80, 30)

#backgrounds

ocean = image.load("deepoceanpaint.jpg")
earth = image.load("earthpaint.jpg")
space = image.load("spacepaint.jpg")
field = image.load("fieldpaint.jpg")
ncity = image.load("nycpaint.jpg")

backgroundList = [space, earth, ocean, ncity, field]

backBox = Rect(1560, 60, 50, 50)

backgroundNum = 0 # will increase in the list to change background

running = True
while running:
    rbClick = False
    click = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN and evt.button == 1:
            click = True
            sx, sy = evt.pos
            back = screen.copy() #events for mouse actions
        if evt.type == MOUSEBUTTONDOWN and evt.button == 3:
            rbClick = True
        if evt.type == MOUSEMOTION:
            posBefore = evt.pos
        
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    draw.rect(screen, (0, 0, 0), canvas, 2)

    cBoxX = 85
    cBoxY = 110
    colorBoxList = [(255, 0, 0), (255, 106, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130),  (127, 0, 255), (0, 0, 0), (255, 255, 255)]
    shapeBoxList = [rectangleChosen, lineChosen, circleChosen]
    chooseColorBox = 0

    redBox = (cBoxX, 110, 50, 50)
    orangeBox = (cBoxX, 210, 50, 50)
    yellowBox = (cBoxX, 310, 50, 50)
    greenBox = (cBoxX, 410, 50, 50)
    blueBox = (cBoxX, 510, 50, 50)
    indigoBox = (cBoxX, 610, 50, 50)
    violetBox = (cBoxX, 710, 50, 50)
    blackBox = (cBoxX, 810, 50, 50)

    for i in range(8):
        drawColorBoxes(cBoxX, cBoxY, colorBoxList[chooseColorBox])
        cBoxY += 100
        chooseColorBox += 1

    if colorSpectrumBox.collidepoint(mx, my) and mb[0]: #to choose color on color spectrum
            colorDraw = screen.get_at((mx, my))

    chooseColor(redBox, colorDraw, (255, 0, 0), redChosen)

    if rectangleHover.collidepoint(mx, my):
        draw.rect(screen, (255, 255, 255), rectangleHover)
        if click:
            rectangleChosen += 1
            circleChosen = 0
            lineChosen = 0  #blocks of this code sets tool/shape/stamp to 1 and sets class of item to true
            fillRect = 0
            fillCirc = 0
            shapes = True
            stamps = False
            tools = False
            draw.rect(screen, (211, 211, 211), rectangleHover)
        if mb[0]:
            draw.rect(screen, (83, 83, 83), rectangleHover)          
    if lineHover.collidepoint(mx, my):
        if click:
            shapes = True
            stamps = False
            tools = False
            lineChosen += 1
            circleChosen = 0
            rectangleChosen = 0
            fillRect = 0
            fillCirc = 0
            draw.rect(screen, (211, 211, 211), lineHover)
        else:
            draw.rect(screen, (83, 83, 83), lineHover, 1)
    if circleHover.collidepoint(mx, my):
        if click:
            shapes = True
            stamps = False
            tools = False
            circleChosen += 1
            rectangleChosen = 0
            lineChosen = 0
            fillRect = 0
            fillCirc = 0
            draw.rect(screen, (211, 211, 211), circleHover)
        else:
            draw.rect(screen, (83, 83, 83), circleHover, 1)
    if fRectBox.collidepoint(mx, my):
        if click:
            shapes = True
            stamps = False
            tools = False
            circleChosen = 0
            rectangleChosen = 0
            lineChosen = 0
            fillRect = 1
            fillCirc = 0
            draw.rect(screen, (211, 211, 211), fRectBox)
        else:
            draw.rect(screen, (83, 83, 83), fRectBox, 1)
    if fCircBox.collidepoint(mx, my):
        if click:
            shapes = True
            stamps = False
            tools = False
            circleChosen = 0
            rectangleChosen = 0
            lineChosen = 0
            fillRect = 0
            fillCirc = 1
            draw.rect(screen, (211, 211, 211), fCircBox)
        else:
            draw.rect(screen, (83, 83, 83), fCircBox, 1)

    #Tools
  
    if PenBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = False
            tools = True
            Pen = 1
            Pencil = 0
            Brush = 0
            Spray = 0
            Eraser = 0
            draw.rect(screen, (211, 211, 211), PenBox)
        else:
            draw.rect(screen, (200, 200, 200), PenBox, 1)
    if PencilBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = False
            tools = True
            Pen = 0
            Pencil = 1
            Brush = 0
            Spray = 0
            Eraser = 0
            draw.rect(screen, (211, 211, 211), PencilBox)
        else:
            draw.rect(screen, (200, 200, 200), PencilBox, 1)
    if BrushBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = False
            tools = True
            Pen = 0
            Pencil = 0
            Brush = 1
            Spray = 0
            Eraser = 0
            draw.rect(screen, (211, 211, 211), BrushBox)
        else:
            draw.rect(screen, (200, 200, 200), BrushBox, 1)  
    if SprayBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = False
            tools = True
            Pen = 0
            Pencil = 0
            Brush = 0
            Spray = 1
            Eraser = 0
            draw.rect(screen, (211, 211, 211), SprayBox)
        else:
            draw.rect(screen, (200, 200, 200), SprayBox, 1)
    if EraserBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = False
            tools = True
            Pen = 0
            Pencil = 0
            Brush = 0
            Spray = 0
            Eraser = 1
            draw.rect(screen, (211, 211, 211), EraserBox)
        else:
            draw.rect(screen, (200, 200, 200), EraserBox, 1)

    #stamps

    if smileyBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = True
            tools = False
            smileyTF = 1
            phoneTF = 0
            houseTF = 0
            planeTF = 0
            basketballTF = 0
            carTF = 0
            draw.rect(screen, (211, 211, 211), smileyBox)
    if phoneBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = True
            tools = False
            smileyTF = 0
            phoneTF = 1
            houseTF = 0
            planeTF = 0
            basketballTF = 0
            carTF = 0
            draw.rect(screen, (211, 211, 211), phoneBox)
    if houseBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = True
            tools = False
            smileyTF = 0
            phoneTF = 0
            houseTF = 1
            planeTF = 0
            basketballTF = 0
            carTF = 0
            draw.rect(screen, (211, 211, 211), houseBox)
    if planeBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = True
            tools = False
            smileyTF = 0
            phoneTF = 0
            houseTF = 0
            planeTF = 1
            basketballTF = 0
            carTF = 0
            draw.rect(screen, (211, 211, 211), planeBox)
    if basketballBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = True
            tools = False
            smileyTF = 0
            phoneTF = 0
            houseTF = 0
            planeTF = 0
            basketballTF = 1
            carTF = 0
            draw.rect(screen, (211, 211, 211), basketballBox)
    if carBox.collidepoint(mx, my):
        if click:
            shapes = False
            stamps = True
            tools = False
            smileyTF = 0
            phoneTF = 0
            houseTF = 0
            planeTF = 0
            basketballTF = 0
            carTF = 1
            draw.rect(screen, (211, 211, 211), carBox)
    #buttons

    if clearButton.collidepoint(mx, my):
        if click:
            draw.rect(screen, (255, 255, 255), canvas)
            draw.rect(screen, (211, 211, 211), clearButton) #will clear canvas by drawing white rectangle over it
    if saveButton.collidepoint(mx, my):
        if click:
              imageSaved = screen.subsurface(canvas)
              imageName = filedialog.asksaveasfilename()#asks user for file name .jpg and saves it in user's preferred location
              image.save(imageSaved, imageName)
              draw.rect(screen, (211, 211, 211), saveButton)
    if loadButton.collidepoint(mx, my):
        if click:
              screen.set_clip(canvas)
              loaded = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")]) #opens files and blits htem onto the canvas
              screen.blit(loaded, (275, 150))
              draw.rect(screen, (211, 211, 211), loadButton)
        
    screen.blit(colorSpectrum, (50, 100)) #draws color spectrum selection image

    if rbClick:
        mbRbX, mbRbY = mouse.get_pos()
    
    if canvas.collidepoint(mx, my):
        if rectangleChosen == 1 and mb[0] == 1 and shapes == True:
            screen.set_clip(canvas)
            screen.blit(back, (0, 0))
            draw.line(screen, colorDraw, (sx, my), (mx, my), 1)
            draw.line(screen, colorDraw, (sx, sy), (sx, my), 1) #draws cutom size rectangle with 4 lines
            draw.line(screen, colorDraw, (mx, sy), (mx, my), 1)
            draw.line(screen, colorDraw, (sx, sy), (mx, sy), 1)
        if lineChosen == 1 and mb[0] == 1 and shapes == True:
            screen.set_clip(canvas)
            screen.blit(back, (0,0))
            draw.line(screen, colorDraw, (sx, sy), (mx, my), 1) #draws line
        if circleChosen == 1 and mb[0] and shapes == True:
            screen.set_clip(canvas)
            draw.circle (screen, colorDraw, (mx, my), 30, 1) #draws circle
        if fillCirc == 1 and mb[0] and shapes == True:
            screen.set_clip(canvas)     #filled cricle
            draw.circle(screen, colorDraw, (mx, my), 20)
        if fillRect == 1 and mb[0] and shapes == True:
            screen.set_clip(canvas)     #filled rectangle
            draw.rect(screen, colorDraw, (mx, my, 50, 30))
        if Pen == 1 and mb[0] and tools == True:
            screen.set_clip(canvas)
            draw.line(screen, colorDraw, (omx, omy), (mx, my), 2)
        if Pencil == 1 and mb[0] and tools == True:
            screen.set_clip(canvas)
            draw.line(screen, (0, 0, 0), (omx, omy), (mx, my), 1)
        if Brush == 1 and mb[0] and tools == True:
            screen.set_clip(canvas)
            draw.circle(screen, colorDraw, (mx, my), 4)
        if Spray == 1 and mb[0] and tools == True:
            randspray = randint(0, 16)
            screen.set_clip(canvas)
            for i in range(2):
                draw.circle(screen, colorDraw, (mx + randspray, my - randspray), 2)
                draw.circle(screen, colorDraw, (mx + randspray, my + randspray), 2)
                draw.circle(screen, colorDraw, (mx - randspray, my - randspray), 2)
                draw.circle(screen, colorDraw, (mx - randspray, my + randspray), 2)
                draw.circle(screen, colorDraw, (mx + randspray - 2 - randspray, my - randspray - randspray), 2)
                draw.circle(screen, colorDraw, (mx + randspray - 2, my + randspray - 2 + randspray), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 - randspray, my - randspray + 2), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 + randspray, my + randspray - 2 + randspray), 2)
                draw.circle(screen, colorDraw, (mx + randspray - 2 - randspray + randspray - 15, my - randspray - randspray), 2)
                draw.circle(screen, colorDraw, (mx + randspray - 2 + randspray, my + randspray - 2 + randspray), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 - randspray - randspray, my - randspray + 2), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 + randspray + randspray, my + randspray - 2 + randspray - 12), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 - randspray - randspray + 15, my + randspray + randspray), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 + randspray, my - randspray + 2 + randspray), 2)#spray draw many random circles
                draw.circle(screen, colorDraw, (mx + randspray - 2 - randspray + randspray, my + randspray - 2), 2)
                draw.circle(screen, colorDraw, (mx + randspray - 2 + randspray - randspray, my - randspray + 2 - randspray + 12), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 - randspray - randspray + 15, my + randspray + randspray), 2)
                draw.circle(screen, colorDraw, (mx - randspray + 2 + randspray, my - randspray + 2 + randspray), 2)
                draw.circle(screen, colorDraw, (mx + randspray - 2 - randspray - randspray * 2 + randspray, my + randspray - 2), 2)
                draw.circle(screen, colorDraw, (mx + randspray - 2 * randspray + randspray - randspray, my - randspray + randspray * 2 - randspray + 12), 2)
                draw.circle(screen, colorDraw, (mx - randspray, my - randspray + 4), 2)
                draw.circle(screen, colorDraw, (mx + randspray, my + randspray - 4 + randspray), 2)
                draw.circle(screen, colorDraw, (mx + 7 - randspray, my - randspray - randspray), 2)
                draw.circle(screen, colorDraw, (mx + randspray + 3, my + randspray), 2)
        if Eraser == 1 and mb[0] and tools == True:
            screen.set_clip(canvas)
            draw.circle(screen, (255, 255, 255), (mx, my), 20)
        if smileyTF == 1 and click and stamps == True:
            screen.set_clip(canvas)
            screen.blit(smiley, (mx - 30, my - 30))
        if phoneTF == 1 and click and stamps == True:
            screen.set_clip(canvas)
            screen.blit(phone, (mx - 30, my - 30))
        if planeTF == 1 and click and stamps == True:
            screen.set_clip(canvas)
            screen.blit(plane, (mx - 30, my - 30)) #draws stamps
        if houseTF == 1 and click and stamps == True:
            screen.set_clip(canvas)
            screen.blit(house, (mx - 30, my - 30))
        if basketballTF == 1 and click and stamps == True:
            screen.set_clip(canvas)
            screen.blit(basketball, (mx - 30, my - 30))
        if carTF == 1 and click and stamps == True:
            screen.set_clip(canvas)
            screen.blit(car, (mx - 30, my - 30))

    #shapes
    
    draw.rect(screen, (0, 0, 0), rectangleHover, 1)
    draw.rect(screen, (0, 0, 0), Rect(1660, 140, 70 , 20), 1)
    
    draw.rect(screen, (0, 0, 0), lineHover, 1)
    draw.line(screen, (0, 0, 0), (1670, 240), (1730, 240), 1) #draws all shape boxes and icons

    draw.rect(screen, (0, 0, 0), circleHover, 1)
    draw.circle (screen, (0, 0, 0), (1700, 350), 30, 1)

    draw.rect(screen, (0, 0, 0), fRectBox, 1)
    draw.rect(screen, (0, 0, 0), (1070, 895, 40, 30))

    draw.rect(screen, (0, 0, 0), fCircBox, 1)
    draw.circle(screen, (0, 0, 0), (1190, 905), 20)

    #Tools
    
    draw.rect(screen, (0, 0, 0), PenBox, 1)
    draw.line(screen, (0, 0, 0), (1665, 405), (1715, 455), 1)
    
    draw.rect(screen, (0, 0, 0), PencilBox, 1)
    draw.line(screen, (255, 255, 0), (1665, 485), (1715, 535), 5)
    draw.line(screen, (0, 0, 0), (1665, 485), (1715, 535), 1)
    
    draw.rect(screen, (0, 0, 0), BrushBox, 1)
    draw.line(screen, (0, 0, 0), (1680, 580), (1715, 615), 2)
    draw.polygon(screen, (0, 0, 0), ((1680, 580), (1660, 560), (1660, 570)))#draws all tool boxes and icons
    
    draw.rect(screen, (0, 0, 0), SprayBox, 1)
    draw.rect(screen, (0, 0, 0), (1680, 670, 20, 30))
    draw.rect(screen, (0, 0, 0), (1675, 663, 18, 4))
    draw.circle(screen, (0, 0, 0), (1690, 670), 10, 1) 
    
    draw.rect(screen, (0, 0, 0), EraserBox, 1)
    draw.rect(screen, (255, 192, 203), (1675, 740, 30, 15))

    #Buttons

    draw.rect(screen, (0, 0, 0), clearButton, 1)
    clearText = smallerFont.render("Clear", True, (0, 0, 0))
    screen.blit(clearText, (1654, 57))

    draw.rect(screen, (0, 0, 0), saveButton, 1)
    saveText = smallerFont.render("Save", True, (0, 0, 0))
    screen.blit(saveText, (1648, 795))

    draw.rect(screen, (0, 0, 0), loadButton, 1)
    loadText = smallerFont.render("Load", True, (0, 0, 0))#draws all buttons and words
    screen.blit(loadText, (loadButton))

    draw.rect(screen, (0, 0, 0), backBox, 1)
    if backBox.collidepoint(mx, my) and click:
            screen.blit(backgroundList[backgroundNum], canvas)
            if backgroundNum == 4:      #Changes background
                    backgroundNum = 0
            backgroundNum += 1
    drawBack(backBox, backgroundList, backgroundNum, canvas)
    draw.line(screen, (0, 0, 0), (1570, 70), (1600, 90), 1)
    draw.line(screen, (0, 0, 0), (1600, 90), (1570, 100), 1)

    #Titles

    earthPaint = TitleFont.render("             Anish.K_Paint                   Background:", True, (144, 238, 144)) #title
    screen.blit(earthPaint, (500, 50))

    #Stamps
    
    drawStamps(300, 875, stampList, 0) #draws stamps

    draw.rect(screen, (0, 0, 0), smileyBox, 1)
    draw.rect(screen, (0, 0, 0), phoneBox, 1)
    draw.rect(screen, (0, 0, 0), planeBox, 1) #draws stamp boxes
    draw.rect(screen, (0, 0, 0), houseBox, 1)
    draw.rect(screen, (0, 0, 0), basketballBox, 1)
    draw.rect(screen, (0, 0, 0), carBox, 1)

    omx, omy = mx, my      
    display.flip()

quit()
