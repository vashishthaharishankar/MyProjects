import pygame

# Initialisation of PyGame
pygame.init()

def reset1(p):
    if p == True :

        # Orange BG
        myRectangle61 = pygame.Rect(0, 0, 400, 210)
        pygame.draw.rect(window, [255, 165, 0], myRectangle61)
        # White BG
        myRectangle61 = pygame.Rect(0, 210, 400, 210)
        pygame.draw.rect(window, [255, 255, 255], myRectangle61)
        # Green BG
        myRectangle61 = pygame.Rect(0, 420, 400, 210)
        pygame.draw.rect(window, [0, 255, 0], myRectangle61)

        # Reset Button flower Design
        pygame.draw.circle(window, (255, 255, 255), (175, 465), 25)
        pygame.draw.circle(window, (255, 255, 255), (200, 465), 25)
        pygame.draw.circle(window, (255, 255, 255), (225, 465), 25)
        # reset button Flower dESIGN
        pygame.draw.circle(window, (255, 255, 255), (175, 465), 25)
        pygame.draw.circle(window, (255, 255, 255), (200, 465), 25)
        pygame.draw.circle(window, (255, 255, 255), (225, 465), 25)

        # Text 1("Tic-Tac-Toe")
        font1 = pygame.font.Font(pygame.font.get_default_font(), 30)
        text1 = font1.render("Tic-Tac-Toe", True, [165, 42, 42])
        window.blit(text1, dest=(120, 15))
        # Text 1("Reset Button Text")
        font1 = pygame.font.Font(pygame.font.get_default_font(), 30)
        text1 = font1.render("Reset", True, [0, 0, 255])
        window.blit(text1, dest=(160, 451))

        # Lower White Box
        myRectangle6 = pygame.Rect(45, 495, 310, 80)
        pygame.draw.rect(window, [255,255,255], myRectangle6)
        # Lower Black Box
        myRectangle6 = pygame.Rect(50, 500, 300, 70)
        pygame.draw.rect(window, [0, 0, 0], myRectangle6)

        # Lower Ready Text
        font1 = pygame.font.Font(pygame.font.get_default_font(), 32)
        text1 = font1.render("Ready...", True, [255, 255, 255])
        window.blit(text1, dest=(137, 520))

        # Black Main square
        # Square 1
        myRectangle1 = pygame.Rect(10, 50, 380, 380)
        pygame.draw.rect(window, [0, 0, 0], myRectangle1)
        # White Perpendicular lines
        # Line 1
        myRectangle2 = pygame.Rect(130, 50, 10, 380)
        pygame.draw.rect(window, [255, 255, 255], myRectangle2)
        # Blue Left Side
        myRectangle2 = pygame.Rect(127, 50, 3, 380)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Blue Right Side
        myRectangle2 = pygame.Rect(140, 50, 3, 380)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Line 2
        myRectangle3 = pygame.Rect(260, 50, 10, 380)
        pygame.draw.rect(window, [255, 255, 255], myRectangle3)
        # Blue Left Side
        myRectangle2 = pygame.Rect(257, 50, 3, 380)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Blue Right Side
        myRectangle2 = pygame.Rect(270, 50, 3, 380)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # White Horizontal lines
        # Line 1
        myRectangle2 = pygame.Rect(10, 170, 380, 10)
        pygame.draw.rect(window, [255, 255, 255], myRectangle2)
        # Blue Upside
        myRectangle2 = pygame.Rect(10, 167, 380, 3)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Blue Downside
        myRectangle2 = pygame.Rect(10, 180, 380, 3)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Line 2
        myRectangle3 = pygame.Rect(10, 300, 380, 10)
        pygame.draw.rect(window, [255, 255, 255], myRectangle3)
        # Blue Upside
        myRectangle2 = pygame.Rect(10, 297, 380, 3)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Blue Downside
        myRectangle2 = pygame.Rect(10, 310, 380, 3)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Blue Boundary
        # Horizontal Boundary
        # line 1
        myRectangle2 = pygame.Rect(10, 50, 380, 3)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Line 2
        myRectangle2 = pygame.Rect(10, 427, 380, 3)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Perpendicular Boundary
        # Line 1
        myRectangle2 = pygame.Rect(10, 50, 3, 380)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        # Line 2
        myRectangle2 = pygame.Rect(387, 50, 3, 380)
        pygame.draw.rect(window, [0, 0, 255], myRectangle2)
        pygame.display.flip()
        gameRunning = True

# Defining Useful Variables
        i  =  0            # For Temp. Variable
        b1 = -1            # Block Is Clicked or Not (Green Or Red)
        b2 = -1            # Block Is Clicked or Not (Green Or Red)
        b3 = -1            # Block Is Clicked or Not (Green Or Red)
        b4 = -1            # Block Is Clicked or Not (Green Or Red)
        b5 = -1            # Block Is Clicked or Not (Green Or Red)
        b6 = -1            # Block Is Clicked or Not (Green Or Red)
        b7 = -1            # Block Is Clicked or Not (Green Or Red)
        b8 = -1            # Block Is Clicked or Not (Green Or Red)
        b9 = -1            # Block Is Clicked or Not (Green Or Red)
        result = 0         # To Check Result is declared or not
        cond = False;      #  Mouse Clicked Inside Black Box
        while gameRunning:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    x = position[0]
                    y = position[1]
                    # If Reset Button Clicked
                    if (x > 155 and x < 248) and (y > 444 and y < 488):
                        reset1(True)     # If Reset Button Clicked
                if result != 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Co-ordinates of Mouse Pointer
                        position = pygame.mouse.get_pos()
                        x = position[0]
                        y = position[1]
                        # Logic to Identify Block Number with Mouse Click
                        if (x > 10 and x < 390) and (y > 50 and y < 390):
                            cond = True
                            # Temp. Variable for Alternate Chance
                            z = i + 1
                            i = z

                            if (x > 10 and x < 130) and (y > 50 and y < 170):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 1 Clicked")
                                    myRectangle2 = pygame.Rect(65, 60, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(20, 105, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    pygame.display.flip()
                                    b1 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 1 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (70, 110), 50, 10)
                                    b1 = 1  # 1 for Red Block
                            elif (x > 140 and x < 260) and (y > 50 and y < 170):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 2 Clicked")
                                    myRectangle2 = pygame.Rect(195, 60, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(150, 105, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b2 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 2 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (200, 110), 50, 10)
                                    b2 = 1  # 1 for Red Block
                            elif (x > 270 and x < 390) and (y > 50 and y < 170):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 3 Clicked")
                                    myRectangle2 = pygame.Rect(325, 60, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(280, 105, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b3 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 3 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (330, 110), 50, 10)
                                    b3 = 1  # 1 for Red Block
                            elif (x > 10 and x < 130) and (y > 180 and y < 300):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 4 Clicked")
                                    myRectangle2 = pygame.Rect(65, 190, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(20, 235, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b4 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 4 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (70, 240), 50, 10)
                                    b4 = 1  # 1 for Red Block
                            elif (x > 140 and x < 260) and (y > 180 and y < 300):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 5 Clicked")
                                    myRectangle2 = pygame.Rect(195, 190, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(150, 235, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b5 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 5 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (200, 240), 50, 10)
                                    b5 = 1  # 1 for Red Block
                            elif (x > 270 and x < 390) and (y > 180 and y < 300):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 6 Clicked")
                                    myRectangle2 = pygame.Rect(325, 190, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(280, 235, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b6 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 6 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (330, 240), 50, 10)
                                    b6 = 1  # 1 for Red Block
                            elif (x > 10 and x < 130) and (y > 310 and y < 430):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 7 Clicked")
                                    myRectangle2 = pygame.Rect(65, 320, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(20, 365, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b7 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 7 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (70, 370), 50, 10)
                                    b7 = 1  # 1 for Red Block
                            elif (x > 140 and x < 260) and (y > 310 and y < 430):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 8 Clicked")
                                    myRectangle2 = pygame.Rect(195, 320, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(150, 365, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b8 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 8 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (200, 370), 50, 10)
                                    b8 = 1  # 1 for Red Block
                            elif (x > 270 and x < 390) and (y > 310 and y < 430):
                                if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                                    print("Block 9 Clicked")
                                    myRectangle2 = pygame.Rect(325, 320, 10, 100)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    myRectangle2 = pygame.Rect(280, 365, 100, 10)
                                    pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                                    b9 = 0  # 0 for Green Block
                                elif z == 2 or z == 4 or z == 6 or z == 8:
                                    print("Block 9 Clicked")
                                    pygame.draw.circle(window, (255, 0, 0), (330, 370), 50, 10)
                                    b9 = 1  # 1 for Red Block

                        # Resetting waiting . . .  text Rectangle Box
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        # Result waiting text
                        font1 = pygame.font.Font(pygame.font.get_default_font(), 27)
                        text1 = font1.render("Waiting for Result ...", True, [255, 255, 255])
                        window.blit(text1, dest=(60, 522))
                        # Last Font
                        font2 = pygame.font.Font(pygame.font.get_default_font(), 15)
                        text2 = font2.render("~ Harishankar Vashishtha", True, [0, 0, 255])
                        window.blit(text2, dest=(200, 610))

                        # Logic To declare Winner
                        if cond == True and result == 0:
                            if (b1 == 0 and b2 == 0 and b3 == 0) or (b4 == 0 and b5 == 0 and b6 == 0) or (
                                    b7 == 0 and b8 == 0 and b9 == 0):
                                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                                print("\nGreen is Winner")
                                font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                                text3 = font3.render("Green is Winner", True, [0, 255, 0])
                                window.blit(text3, dest=(73, 520))
                                result = 1
                            elif (b1 == 0 and b4 == 0 and b7 == 0) or (b2 == 0 and b5 == 0 and b8 == 0) or (
                                    b3 == 0 and b6 == 0 and b9 == 0):
                                print("\nGreen is Winner")
                                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                                font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                                text3 = font3.render("Green is Winner", True, [0, 255, 0])
                                window.blit(text3, dest=(73, 520))
                                result = 1
                            elif (b1 == 0 and b5 == 0 and b9 == 0) or (b3 == 0 and b5 == 0 and b7 == 0):
                                print("\nGreen is Winner")
                                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                                font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                                text3 = font3.render("Green is Winner", True, [0, 255, 0])
                                window.blit(text3, dest=(73, 520))
                                result = 1
                            elif (b1 == 1 and b2 == 1 and b3 == 1) or (b4 == 1 and b5 == 1 and b6 == 1) or (
                                    b7 == 1 and b8 == 1 and b9 == 1):
                                print("\nRed is Winner")
                                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                                font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                                text3 = font3.render("Red is Winner", True, [255, 0, 0])
                                window.blit(text3, dest=(88, 520))
                                result = 1
                            elif (b1 == 1 and b4 == 1 and b7 == 1) or (b2 == 1 and b5 == 1 and b8 == 1) or (
                                    b3 == 1 and b6 == 1 and b9 == 1):
                                print("\nRed is Winner")
                                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                                font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                                text3 = font3.render("Red is Winner", True, [255, 0, 0])
                                window.blit(text3, dest=(88, 520))
                                result = 1
                            elif (b1 == 1 and b5 == 1 and b9 == 1) or (b3 == 1 and b5 == 1 and b7 == 1):
                                print("\nRed is Winner")
                                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                                font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                                text3 = font3.render("Red is Winner", True, [255, 0, 0])
                                window.blit(text3, dest=(88, 520))
                                result = 1
                            # For Match Tied Purpose
                            elif result != -1 and z == 9:    # z=9 because Result can be declared after 9 clicks
                                print("\nMatch Tied")
                                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                                font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                                text3 = font3.render("Match Tied", True, [255, 255, 255])
                                window.blit(text3, dest=(110, 520))

                pygame.display.flip()

                #Exiting Loop
                if event.type == pygame.QUIT:
                    print("\nGame Closed Succesfully!")
                    gameRunning = False
                    pygame.quit()
                    exit()
                    break
###########################################################################################
# Main Programme

#Title Name
pygame.display.set_caption('Harishankar Vashishtha')
# Window Size & Display
window = pygame.display.set_mode([400, 630])
window.fill([200, 200, 200])  # Grey in RGB

#Orange BG
myRectangle61 = pygame.Rect(0, 0, 400, 210)
pygame.draw.rect(window, [255,165,0], myRectangle61)
#White BG
myRectangle61 = pygame.Rect(0, 210, 400, 210)
pygame.draw.rect(window, [255,255,255], myRectangle61)
#Green BG
myRectangle61 = pygame.Rect(0, 420, 400, 210)
pygame.draw.rect(window, [0,255,0], myRectangle61)

#Reset Button flower Design
pygame.draw.circle(window, (255, 255, 255), (175, 465), 25)
pygame.draw.circle(window, (255, 255, 255), (200, 465), 25)
pygame.draw.circle(window, (255, 255, 255), (225, 465), 25)
#reset button Flower dESIGN
pygame.draw.circle(window, (255, 255, 255), (175, 465), 25)
pygame.draw.circle(window, (255, 255, 255), (200, 465), 25)
pygame.draw.circle(window, (255, 255, 255), (225, 465), 25)

# Text 1("Tic-Tac-Toe")
font1 = pygame.font.Font(pygame.font.get_default_font(), 30)
text1 = font1.render("Tic-Tac-Toe", True, [165, 42, 42])
window.blit(text1, dest=(120, 15))

#Reset Button Rectangle Coordinates
# myRectangle6 = pygame.Rect(155, 444, 93, 44)
# pygame.draw.rect(window, [0, 0, 0], myRectangle6)
#Reset button Text
font1 = pygame.font.Font(pygame.font.get_default_font(), 30)
text1 = font1.render("Reset", True, [0,0,255])
window.blit(text1, dest=(160, 451))

#Lower Black Box

myRectangle6 = pygame.Rect(45, 495, 310, 80)
pygame.draw.rect(window, [255,255,255], myRectangle6)

myRectangle6 = pygame.Rect(50, 500, 300, 70)
pygame.draw.rect(window, [0, 0, 0], myRectangle6)

#Lower Ready Text
font1 = pygame.font.Font(pygame.font.get_default_font(), 32)
text1 = font1.render("Ready...", True, [255, 255, 255])
window.blit(text1, dest=(137, 520))

# Black Main square

# Square 1
myRectangle1 = pygame.Rect(10, 50, 380, 380)
pygame.draw.rect(window, [0, 0, 0], myRectangle1)

# White Perpendicular lines
# Line 1
myRectangle2 = pygame.Rect(130, 50, 10, 380)
pygame.draw.rect(window, [255, 255, 255], myRectangle2)
    # Blue Left Side
myRectangle2 = pygame.Rect(127, 50, 3, 380)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
    # Blue Right Side
myRectangle2 = pygame.Rect(140, 50, 3, 380)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
# Line 2
myRectangle3 = pygame.Rect(260, 50, 10, 380)
pygame.draw.rect(window, [255, 255, 255], myRectangle3)
    # Blue Left Side
myRectangle2 = pygame.Rect(257, 50, 3, 380)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
    # Blue Right Side
myRectangle2 = pygame.Rect(270, 50, 3, 380)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)

# White Horizontal lines
# Line 1
myRectangle2 = pygame.Rect(10, 170, 380, 10)
pygame.draw.rect(window, [255, 255, 255], myRectangle2)
    # Blue Upside
myRectangle2 = pygame.Rect(10, 167, 380, 3)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
    # Blue Downside
myRectangle2 = pygame.Rect(10, 180, 380, 3)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
# Line 2
myRectangle3 = pygame.Rect(10, 300, 380, 10)
pygame.draw.rect(window, [255, 255, 255], myRectangle3)
    # Blue Upside
myRectangle2 = pygame.Rect(10, 297, 380, 3)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
    # Blue Downside
myRectangle2 = pygame.Rect(10, 310, 380, 3)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)

# Blue Boundary
# Horizontal Boundary
# line 1
myRectangle2 = pygame.Rect(10, 50, 380, 3)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
# Line 2
myRectangle2 = pygame.Rect(10, 427, 380, 3)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
# Perpendicular Boundary
# Line 1
myRectangle2 = pygame.Rect(10, 50, 3, 380)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)
# Line 2
myRectangle2 = pygame.Rect(387, 50, 3, 380)
pygame.draw.rect(window, [0, 0, 255], myRectangle2)

pygame.display.flip()
gameRunning = True

#Defining Useful Variables
i  =  0            # For Temp. Variable
b1 = -1            # Block Is Clicked or Not (Green Or Red)
b2 = -1            # Block Is Clicked or Not (Green Or Red)
b3 = -1            # Block Is Clicked or Not (Green Or Red)
b4 = -1            # Block Is Clicked or Not (Green Or Red)
b5 = -1            # Block Is Clicked or Not (Green Or Red)
b6 = -1            # Block Is Clicked or Not (Green Or Red)
b7 = -1            # Block Is Clicked or Not (Green Or Red)
b8 = -1            # Block Is Clicked or Not (Green Or Red)
b9 = -1            # Block Is Clicked or Not (Green Or Red)
result = 0         # To Check Result is declared or not
cond = False;      #  Mouse Clicked Inside Black Box
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            x = position[0]
            y = position[1]
            if (x > 155 and x < 248) and (y > 444 and y < 488):
                reset1(True)
        if result!=1 :
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Co-ordinates of Mouse Pointer
                position = pygame.mouse.get_pos()
                x = position[0]
                y = position[1]

                # Logic to Identify Block Number with Mouse Click
                if (x > 10 and x < 390) and (y > 50 and y < 390):
                    cond = True
                    # Temp. Variable for Alternate chance
                    z = i + 1
                    i = z

                    if (x > 10 and x < 130) and (y > 50 and y < 170):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 1 Clicked")
                            myRectangle2 = pygame.Rect(65, 60, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(20, 105, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            pygame.display.flip()
                            b1 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 1 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (70, 110), 50, 10)
                            b1 = 1  # 1 for Red Block
                    elif (x > 140 and x < 260) and (y > 50 and y < 170):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 2 Clicked")
                            myRectangle2 = pygame.Rect(195, 60, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(150, 105, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b2 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 2 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (200, 110), 50, 10)
                            b2 = 1  # 1 for Red Block
                    elif (x > 270 and x < 390) and (y > 50 and y < 170):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 3 Clicked")
                            myRectangle2 = pygame.Rect(325, 60, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(280, 105, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b3 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 3 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (330, 110), 50, 10)
                            b3 = 1  # 1 for Red Block
                            d3 = True  # For Double Click Check on Same Box
                    elif (x > 10 and x < 130) and (y > 180 and y < 300):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 4 Clicked")
                            myRectangle2 = pygame.Rect(65, 190, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(20, 235, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b4 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 4 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (70, 240), 50, 10)
                            b4 = 1  # 1 for Red Block
                    elif (x > 140 and x < 260) and (y > 180 and y < 300):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 5 Clicked")
                            myRectangle2 = pygame.Rect(195, 190, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(150, 235, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b5 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 5 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (200, 240), 50, 10)
                            b5 = 1  # 1 for Red Block
                    elif (x > 270 and x < 390) and (y > 180 and y < 300):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 6 Clicked")
                            myRectangle2 = pygame.Rect(325, 190, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(280, 235, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b6 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 6 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (330, 240), 50, 10)
                            b6 = 1  # 1 for Red Block
                    elif (x > 10 and x < 130) and (y > 310 and y < 430):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 7 Clicked")
                            myRectangle2 = pygame.Rect(65, 320, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(20, 365, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b7 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 7 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (70, 370), 50, 10)
                            b7 = 1  # 1 for Red Block
                    elif (x > 140 and x < 260) and (y > 310 and y < 430):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 8 Clicked")
                            myRectangle2 = pygame.Rect(195, 320, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(150, 365, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b8 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 8 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (200, 370), 50, 10)
                            b8 = 1  # 1 for Red Block
                            d8 = True  # For Double Click Check on Same Box
                    elif (x > 270 and x < 390) and (y > 310 and y < 430):
                        if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9):
                            print("Block 9 Clicked")
                            myRectangle2 = pygame.Rect(325, 320, 10, 100)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            myRectangle2 = pygame.Rect(280, 365, 100, 10)
                            pygame.draw.rect(window, [0, 255, 0], myRectangle2)
                            b9 = 0  # 0 for Green Block
                        elif z == 2 or z == 4 or z == 6 or z == 8:
                            print("Block 9 Clicked")
                            pygame.draw.circle(window, (255, 0, 0), (330, 370), 50, 10)
                            b9 = 1  # 1 for Red Block

                # Resetting waiting . . .  text Rectangle Box
                myRectangle6 = pygame.Rect(50, 500, 300, 70)
                pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                # Result waiting text
                font1 = pygame.font.Font(pygame.font.get_default_font(), 27)
                text1 = font1.render("Waiting for Result ...", True, [255, 255, 255])
                window.blit(text1, dest=(60, 522))
                # Last Font
                font2 = pygame.font.Font(pygame.font.get_default_font(), 15)
                text2 = font2.render("~ Harishankar Vashishtha", True, [0, 0, 255])
                window.blit(text2, dest=(200, 610))

                # Logic To declare Winner
                if cond == True and result == 0:
                    if (b1 == 0 and b2 == 0 and b3 == 0) or (b4 == 0 and b5 == 0 and b6 == 0) or (
                            b7 == 0 and b8 == 0 and b9 == 0):
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        print("\nGreen is Winner")
                        font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                        text3 = font3.render("Green is Winner", True, [0, 255, 0])
                        window.blit(text3, dest=(73, 520))
                        result = 1
                    elif (b1 == 0 and b4 == 0 and b7 == 0) or (b2 == 0 and b5 == 0 and b8 == 0) or (
                            b3 == 0 and b6 == 0 and b9 == 0):
                        print("\nGreen is Winner")
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                        text3 = font3.render("Green is Winner", True, [0, 255, 0])
                        window.blit(text3, dest=(73, 520))
                        result = 1
                    elif (b1 == 0 and b5 == 0 and b9 == 0) or (b3 == 0 and b5 == 0 and b7 == 0):
                        print("\nGreen is Winner")
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                        text3 = font3.render("Green is Winner", True, [0, 255, 0])
                        window.blit(text3, dest=(73, 520))
                        result = 1
                    elif (b1 == 1 and b2 == 1 and b3 == 1) or (b4 == 1 and b5 == 1 and b6 == 1) or (
                            b7 == 1 and b8 == 1 and b9 == 1):
                        print("\nRed is Winner")
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                        text3 = font3.render("Red is Winner", True, [255, 0, 0])
                        window.blit(text3, dest=(88, 520))
                        result = 1
                    elif (b1 == 1 and b4 == 1 and b7 == 1) or (b2 == 1 and b5 == 1 and b8 == 1) or (
                            b3 == 1 and b6 == 1 and b9 == 1):
                        print("\nRed is Winner")
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                        text3 = font3.render("Red is Winner", True, [255, 0, 0])
                        window.blit(text3, dest=(88, 520))
                        result = 1
                    elif (b1 == 1 and b5 == 1 and b9 == 1) or (b3 == 1 and b5 == 1 and b7 == 1):
                        print("\nRed is Winner")
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                        text3 = font3.render("Red is Winner", True, [255, 0, 0])
                        window.blit(text3, dest=(88, 520))
                        result = 1
                    # For Match Tied Purpose
                    elif result != -1 and z == 9:
                        print("\nMatch Tied")
                        myRectangle6 = pygame.Rect(50, 500, 300, 70)
                        pygame.draw.rect(window, [0, 0, 0], myRectangle6)
                        font3 = pygame.font.Font(pygame.font.get_default_font(), 32)
                        text3 = font3.render("Match Tied", True, [255, 255, 255])
                        window.blit(text3, dest=(110, 520))
        pygame.display.flip()

        # Exiting Loop
        if event.type == pygame.QUIT:
            print("\nGame Closed Succesfully!")
            gameRunning = False
            break

pygame.quit()
exit()

