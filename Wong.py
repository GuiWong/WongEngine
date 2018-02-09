
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



		self.active_entities=list()
		self.current_map=Map(10,10)
		self.map_pos=[0,0]

		self.game_screen=False

	def set_state(self,state):
		'''
		set the game state
		0: init 1:playing 2: menu
		:param state: a int corresponding to new game state
		'''

	def set_game_window(self,window):

		self.game_screen=Game_Shower(window,window.width-2,
										window.height-2,self)
		window.add_elem(self.game_screen)

	def add_entity(self,entity):	#temporary

		self.active_entities.append(entity)

	def game_move_map(self,dx,dy):

		self.map_pos[0]=self.map_pos[0]+dx
		if self.map_pos[0] < 0:
			self.map_pos[0]=0
		elif self.map_pos[0] >=self.current_map.width:
			self.map_pos[0]=self.current_map.width

		self.map_pos[1]= self.map_pos[1] + dy

		if self.map_pos[1] < 0:
			self.map_pos[1]=0
		elif self.map_pos[1] >=self.current_map.height:
			self.map_pos[1]=self.current_map.height


		self.game_screen.update()



	def render(self):

		self.window.render()

		if self.game_screen:
			self.game_screen.update()

	def input(self):

		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS|libtcod.EVENT_MOUSE,self.key,self.mouse)
		if self.key.vk == libtcod.KEY_ENTER and self.key.lalt:
	        #Alt+Enter: toggle fullscreen
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

		elif self.key.vk == libtcod.KEY_ESCAPE:
			self.state=0

		elif self.key.vk == libtcod.KEY_SPACE:
			print str(self.mouse.cx) + ' - '+ str(self.mouse.cy)

	#Debug Purpose------------------------
		if self.mouse.mbutton_pressed:

			print self.window.get_elem_by_mouse()




	def run(self):

		while self.state!=0:

			self.render()
			self.input()


class TBS_Game(Wong_Game):

	def __init__(self):

		Wong_Game.__init__(self)

		self.turn=False



	def move_entity(self,entity,pos):

		entity.move()

	def initiate(self):
		'''
		all the thing your game need to initialize
		cfg loading, screen initializing etc
		'''

		pass

	def launch_game(self):
		'''
		create the map, the entities etc...
		can load all sorts of things
		'''

		pass

	def new_game(self):
		'''
		start a new game from the beggining
		all character creation/ etc...
		'''

		pass

	def input(self):

		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS|libtcod.EVENT_MOUSE,self.key,self.mouse)
		if self.key.vk == libtcod.KEY_ENTER and self.key.lalt:
	        #Alt+Enter: toggle fullscreen
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

		elif self.key.vk == libtcod.KEY_ESCAPE:
			self.state=0

		elif self.key.vk == libtcod.KEY_SPACE:
			print str(self.mouse.cx) + ' - '+ str(self.mouse.cy)

		elif self.key.vk == libtcod.KEY_UP:
			self.game_move_map(0,-1)
		elif self.key.vk == libtcod.KEY_DOWN:
			self.game_move_map(0,1)
		elif self.key.vk == libtcod.KEY_LEFT:
			self.game_move_map(-1,0)
		elif self.key.vk == libtcod.KEY_RIGHT:
			self.game_move_map(1,0)


	#Debug Purpose------------------------
		if self.mouse.mbutton_pressed:

			print self.window.get_elem_by_mouse()
