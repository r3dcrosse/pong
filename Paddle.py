"""
 Paddle is a moving paddle in a graphics window
 
 (David Wayman 2012)
 
"""
#from time import sleep
#from random import randrange, random
from graphics import *
#from Ball import *

  	
class Paddle:

	def __init__(self, win):
		self.pad = Rectangle(Point(950,310), Point(970,190))
		self.pad.setFill("tan")
		self.getLen()
		self.getMiddle()
		self.getfTop()
		self.getfBottom()
		self.pad.draw(win)
    
	def getfTop(self):
		p1 = self.pad.getP2()
		return p1.getY()
		
	def getfBottom(self):
		p2 = self.pad.getP1()
		return p2.getY()
    
	def getLen(self):
		p1 = self.pad.getP1()
		p2 = self.pad.getP2()
		lengthPad = p1.getY() - p2.getY()
		#print "length", lengthPad
		return lengthPad
    
	def getMiddle(self):
		mid = self.pad.getCenter()
		#print "middle", mid.getY()
		return mid.getY()

	def move(self, win, dy):
	  	self.pad.move(0, (dy - self.getMiddle()))
	  		
	  	
	  	

""" Main Driver function to test Paddle class """ 		
def main():
  w = 500
  h = 500
  pWin = GraphWin("Pong", w, h )
  
  #create an instant of the Ball Class
  b = Ball(pWin)
  
  #create an instant of the Paddle Class
  p = Paddle(pWin)
  
  
  game = True
  cnt = 0
  #while pWin.checkMouse() == None:
  while game == True:
    clickPoint = pWin.checkMouse()
    if clickPoint != None:
      dy = clickPoint.getY()
      p.move(pWin,dy) 
    p.getFront()
    p.getMiddle()
    b.move(pWin)
    cnt = cnt+1
    sleep(0.01)
    if cnt % 1000 == 0:
      b.goFaster()

  
    
  
  
  
  
  """ Only runs main if asked to run Paddle.py"""
if __name__ == '__main__':
    main()