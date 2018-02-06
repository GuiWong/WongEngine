
import sys
import os
import libtcodpy as libtcod

class Tile:

	def __init__(self,passable,viewable,char,color,bkgnd_color):

		self.path=passable
		self.view=viewable
		self.char=char
		self.color=color
		self.background=bkgnd_color

	def __del__(self):

		print "Tile deleted"



class Map:

	def __init__(self,width,height):

		self.width=height
		self.height=height
		self.data=[[Tile(false,false,chr(219),libtcod.light_blue,libtcod.black) for Y in range(height)] for X in range(width)]


	def __del__(self):

		print "Map deleted"
