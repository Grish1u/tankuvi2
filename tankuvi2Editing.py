import pygame
import math
# pygame.draw.circle(win, silver, (x_cen, y_cen), x_cen - 1, 2 )
pygame.init()
clock = pygame.time.Clock()
displayW = 500
displayH = 500
windowmode = (displayW, displayH)

myDisplay = pygame.display.set_mode(windowmode)
pygame.display.set_caption('Mein Tankuvi 2 - Edittor')


#colors
black = (0, 0, 0)
white = (255, 255, 255)
silverToWhite = (168, 168, 168)
silver = (112, 112, 112)
red = (255, 0, 0)
blue = (0, 0, 255)

# 
class Player(object):
	def __init__(self, pX, pY, color):
		self.pX = pX
		self.pY = pY
		self.color = color
		self.bodyRadius = 20
		self.vel = 5
		self.up = True # index 0
		self.down = False # index 1
		self.left = False # index 2
		self.right = False # index 3
		self.standing = True
		self.currDirs = [self.up, self.down, self.left, self.right] # Current direction - traces the direction the gun should be drawn 
	def drawMe(self, myDisplay):
		pygame.draw.circle(myDisplay, self.color, (self.pX, self.pY), self.bodyRadius, 0)
		if not(self.standing):
			if p1.currDirs[0] == True: # AIMER UP
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX, self.pY - 2*self.bodyRadius), 3)
			elif p1.currDirs[0] and p1.currDirs[2]: # AIMER UP + LEFT
				pass
			if p1.currDirs[0] and p1.currDirs[3]: # AIMER UP + RIGHT
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX + self.pX*((math.sqrt(2))/2), self.pY - self.pY*((math.sqrt(2))/2)))
			elif p1.currDirs[1] == True: # AIMER DOWN
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX, self.pY + 2*self.bodyRadius), 3) 
			elif p1.currDirs[1] and p1.currDirs[2]: # AIMER DOWN + LEFT
				pass 
			elif p1.currDirs[1] and p1.currDirs[3]:  #AIMER DOWN + RIGHT
				pass
			elif p1.currDirs[2] == True: # AIMER LEFT
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX - 2*self.bodyRadius, self.pY), 3) 
			elif p1.currDirs[3] == True: # AIMER RIGHT
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX + 2*self.bodyRadius, self.pY), 3) 
		else: # AIMER DEFAULT
			if p1.currDirs[0] == True: # AIMER UP
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX, self.pY - 2*self.bodyRadius), 3)
			elif p1.currDirs[0] and p1.currDirs[2]: # AIMER UP + LEFT
				pass
			elif p1.currDirs[0] and p1.currDirs[3]: # AIMER UP + RIGHT
				pygame.draw.line(myDisplay, self.color, (self.px, self.py), (self.px + 15, self.py - 15), 3)
			elif p1.currDirs[1] == True: # AIMER DOWN
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX, self.pY + 2*self.bodyRadius), 3) 
			elif p1.currDirs[1] and p1.currDirs[2]: # AIMER DOWN + LEFT
				pass 
			elif p1.currDirs[1] and p1.currDirs[3]:  #AIMER DOWN + RIGHT
				pass
			elif p1.currDirs[2] == True: # AIMER LEFT
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX - 2*self.bodyRadius, self.pY), 3) 
			elif p1.currDirs[3] == True: # AIMER RIGHT
				pygame.draw.line(myDisplay, self.color, (self.pX, self.pY), (self.pX + 2*self.bodyRadius, self.pY), 3) 
class Projectile(object):
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.radius = Player.bodyRadius / 5
		self.color = white
def redrawLoop():
	# myDisplay.blit(bg, (0,0)) # blit puts pic objects on top of stuff , not for now
	myDisplay.fill(black) # background needs to be written first, so evryth else is on top
	pOneInfo = font.render('Directions array: ' + str(p1.currDirs), 1, silverToWhite )
	pOneInfo2 = font.render('Standing: ' + str(p1.standing), 1, silverToWhite)
	myDisplay.blit(pOneInfo, (190, 10))
	myDisplay.blit(pOneInfo2, (190, 25))
	p1.drawMe(myDisplay)
	pygame.display.update()

#-----------------------------------------------------
font = pygame.font.SysFont('comicsans', 20, True)
p1 = Player(250, 250, silver)
#print('aimer length = ' + calcDistance(p1.pX, p1.pY, p1.pX, p1.pY - 2*p1.bodyRadius))
bullets = []
run = True
while run:
	clock.tick(47)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# bulleting
	#for bullet in bullets:
	#	if bullet.x
	# player movement
	keys = pygame.key.get_pressed()
	# after pressing a key it makes the opposite dir automatically false (to prevent future buggs :D)
	if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
		if keys[pygame.K_UP] and p1.pY >= p1.bodyRadius + p1.vel:
			p1.pY -= p1.vel
			# for the projectile we need to set the last direction
			p1.currDirs[0] = True
			p1.currDirs[1] = False
			p1.standing = False
			#p1.currDirs[2] = False
			#p1.currDirs[3] = False
		elif not keys[pygame.K_UP]:
			p1.currDirs[0] = False
		if keys[pygame.K_DOWN] and p1.pY <= displayH - p1.vel - p1.bodyRadius:
			p1.pY += p1.vel
			p1.currDirs[0] = False
			p1.currDirs[1] = True
			p1.standing = False
			#p1.currDirs[2] = False
			#p1.currDirs[3] = False
		elif not keys[pygame.K_UP]:
			p1.currDirs[1] = False
		if keys[pygame.K_LEFT] and p1.pX >= p1.bodyRadius + p1.vel:
			p1.pX -= p1.vel
			#p1.currDirs[0] = False
			#p1.currDirs[1] = False
			p1.currDirs[2] = True
			p1.currDirs[3] = False
			p1.standing = False
		elif not keys[pygame.K_UP]:
			p1.currDirs[2] = False
		if keys[pygame.K_RIGHT] and p1.pX <= displayW - p1.vel - p1.bodyRadius:
			p1.pX += p1.vel
			#p1.currDirs[0] = False
			#p1.currDirs[1] = False
			p1.currDirs[2] = False
			p1.currDirs[3] = True
			p1.standing = False
		elif not keys[pygame.K_UP]:
			p1.currDirs[3] = False
	else: # not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
		p1.standing = True
	if keys[pygame.K_SPACE]:
		pass


	redrawLoop()
pygame.quit()


# whats done, what Im working on and whats to do (bottom #s for each sector is the most recently added)
# Just Did 
	# - projectile class
	# - bullet list
	# - rendered the directions array info on the screen
	# - made it so if arrow key is released it goes back to False
	# - I actually fixed it by adding If or or or statement before ...
	# ... if each direction key is pressed statement. This meant that even If I didn't have...
	# ... the else: standing = true, the aimer was still going to aim at the last dir...
	# ... I guess this will help later in the development of the game
# Current Work:
	# adding 4 more diagonal directions to the aimer (to draw them)
	# im on the right path - need to change the elifs with ifs for each diagonal direction !!!
	# check google search : 'point around circumference', link: https://www.mathsisfun.com/geometry/unit-circle.html !!! need to polish this up ...
	# ... i have an attempt for UP and RIGHT but it is something different
# Need to do :
	# - for loop for bullets to pop them out if out of border
	# just spotted a problem, whenever i move the gun is aimed in the right direction, after moving stops it goes back Up, FIX THAT (needs to be pointed at the last dir)
	# just spotted that I have a default value - maybe thats how I can fix the last TODO - have some kind of a solution
	# draw the aimer in the rest 4 directions : on 45*, 135*, 225*, 315*...
# THANKS TO TECHWITHTIM FOR THE TUTORIALS : LINK >>> https://techwithtim.net/