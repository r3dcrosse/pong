"""
 This is one player Pong, played by clicking the mouse where
 ever you want the mouse to move.

 (David Wayman 2012)

"""

from time import sleep
from random import randrange, random
from graphics import *
from Ball import *
from Paddle import *

class Pong:

	def __init__(self):
		self.pic = Image(Point(500,250),"background.gif")
		width = self.pic.getWidth()
		height = self.pic.getHeight()

		self.pongWin = GraphWin("Pong", width, height)
		self.pic.draw(self.pongWin)

		#create an instance of the Ball Class
		self.ball = Ball(self.pongWin)

		#create an instance of the Paddle Class
		self.paddle = Paddle(self.pongWin)


	def checkContact(self, ball, paddle):
		FrontTop = paddle.getfTop()
		FrontBottom = paddle.getfBottom()
		ballEdge = ball.getCenter()
		#print "paddleFront", paddle.getfTop(), paddle.getfBottom()
		#print "ballEdge", ballEdge.getX(), ballEdge.getY()

		#checks if the ball makes contact with the paddle
		if (ballEdge.getX() >= 940 and ballEdge.getX() <= 950) and ((ballEdge.getY() >= FrontTop) and (ballEdge.getY() <= FrontBottom)):
			ball.reverseX()
			ball.reverseY()
			return True

	def gameOver(self):
		if self.ball.getCenter().getX() > 990:
			return False
		else:
			return True

	def play(self):
		message = Text(Point(500,250), "")
  		message.setSize(30)
  		message.setTextColor("white")
  		message.setText("Welcome to 1 player Pong! Click anywhere to play!")
  		message.draw(self.pongWin)
  		self.pongWin.getMouse()
  		message.undraw()
  		Level = Text(Point(500, 110), "Level: 0")
		Level.setSize(20)
		Level.setTextColor("light blue")
		Level.draw(self.pongWin)
		scoreTxt = Text(Point(553,58), "0")
		scoreTxt.setSize(30)
		scoreTxt.setTextColor("red")
		scoreTxt.draw(self.pongWin)
		numHits = 0
		lvl = 1
		while self.gameOver() == True:
			clickPoint = self.pongWin.checkMouse()
			if clickPoint != None:
				dy = clickPoint.getY()
				self.paddle.move(self.pongWin, dy)
			self.ball.move(self.pongWin)
			if self.checkContact(self.ball, self.paddle) == True:
				numHits = numHits + 1
				#update the scoreboard
				scoreTxt.undraw()
				scoreTxt.setText(numHits)
				scoreTxt.setSize(30)
				scoreTxt.setTextColor("red")
				scoreTxt.draw(self.pongWin)
				if lvl == 1 and numHits == 1:
					Level.undraw()
					Level.setText("Level:")
					Level.draw(self.pongWin)
					lvlTxt = Text(Point(533, 110), lvl)
					lvlTxt.setSize(20)
					lvlTxt.setTextColor("light blue")
					lvlTxt.draw(self.pongWin)
				if numHits % 5 == 0:
					lvl = lvl + 1
					Level.undraw()
					lvlTxt.undraw()
					Level.setText("Level:")
					Level.draw(self.pongWin)
					lvlTxt = Text(Point(533, 110), lvl)
					lvlTxt.setSize(20)
					lvlTxt.setTextColor("light blue")
					lvlTxt.draw(self.pongWin)
					self.ball.goFaster()
			sleep(0.01)
		#state that the game is over
  		message.setText("You LOST!!!! Your score is:")
  		message.setTextColor("red")
  		EndScore = Text(Point(700, 250), numHits)
  		EndScore.setTextColor("red")
  		EndScore.setSize(30)
  		EndScore.draw(self.pongWin)
  		message.draw(self.pongWin)
  		self.pongWin.getMouse()


def main():

	pongGame = Pong()
	pongGame.play()

main()
