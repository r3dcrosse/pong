"""
 Ball - represents a moving ball in a graphics window
 
 (@author Doug Turnbull 2012
 modified by David Wayman 2012)
 
"""
#from time import sleep
from random import randrange, random
from graphics import *

class Ball:

	def __init__(self, win):
	  
	  center = Point(100, 100)
	  self.circ = Circle(center, 10)
	  self.circ.setFill("red")
	  self.circ.draw(win)
	  
	  self.dx = randrange(2,5)
	  self.dy = randrange(2,5)
	  
		
	def getCenter(self):
		return self.circ.getCenter()
		
	def getRadius(self):
		return self.circ.getRadius()
	
	def goFaster(self):
		self.dx = self.dx * (1 + random())
		self.dy = self.dy * (1 + random())
	
	def reverseX(self):
		self.dx = self.dx * (-1)
		
	def reverseY(self):
		self.dy = self.dy * (-1)
				
	def move(self, win):
		winHeight = win.getHeight()
	  	winWidth = win.getWidth()
	
	  	topEdge = self.getCenter().getY() - self.getRadius()
	  	bottomEdge = self.getCenter().getY() + self.getRadius()
	  	leftEdge = self.getCenter().getX() - self.getRadius()
	  	rightEdge = self.getCenter().getX() + self.getRadius()

		if topEdge + self.dy < 0:
				self.reverseY()
		if bottomEdge + self.dy > winHeight:
	    		self.reverseY()
		if leftEdge + self.dx < 0:
	    		self.reverseX()
		#if rightEdge + self.dx > winWidth:
	    		#self.reverseX()
	  
	  	self.circ.move(self.dx, self.dy)
	
	
			
""" Main Driver function to test Ball class """ 		
def main():
	w = 300
	h = 300
	pWin = GraphWin("Pong", w, h )

	#create an instant of the Ball Class
	b = Ball(pWin)

	b2 = Ball(pWin)
  
	cnt = 0
	while pWin.checkMouse() == None:
		b.move(pWin)
		b2.move(pWin)
    	cnt = cnt+1
    	sleep(0.01)
	if cnt % 100 == 0:
		b.goFaster()
  
  
	pWin.getMouse()
	pWin.close()
  
  
""" Only runs main if asked to run Ball.py"""
if __name__ == '__main__':
    main()
    

    
    
    
