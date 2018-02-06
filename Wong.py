
import sys
import os
import libtcodpy as libtcod
import weakref

from Map import *
from Window import *
from Ui import *


class Wong_Game:

	def __init__(self):

		self.window=Main_Window(self,80,50)
		self.ui=Ui(Palette())
		self.state=1
		self.key=libtcod.Key()
		self.mouse=libtcod.Mouse()


	def render(self):

		self.window.render()

	def input(self):

		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS|libtcod.EVENT_MOUSE,self.key,self.mouse)
		if self.key.vk == libtcod.KEY_ENTER and self.key.lalt:
	        #Alt+Enter: toggle fullscreen
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

		elif self.key.vk == libtcod.KEY_ESCAPE:
			self.state=0

		elif self.key.vk == libtcod.KEY_SPACE:
			print str(self.mouse.cx) + ' - '+ str(self.mouse.cy)




	def run(self):

		while self.state!=0:

			self.render()
			self.input()
