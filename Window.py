
import sys
import os
import libtcodpy as libtcod
import weakref



#TODO handle more colors, easier acces
class Palette:

	def __init__(self,data=None):

		if not data:
			data=[(0,0,0),(0,0,128),(0,128,0),(0,128,128),(128,0,0),(128,0,128),(128,128,0),(192,192,192),(128,128,128),(0,0,255),(0,255,0),(0,255,255),(255,0,0),(255,0,255),(255,255,0),(255,255,255)]
			print data[0]

		self.BLACK=libtcod.Color(*data[0])
		self.BLUE=libtcod.Color(*data[1])
		self.GREEN=libtcod.Color(*data[2])
		self.CYAN=libtcod.Color(*data[3])
		self.RED=libtcod.Color(*data[4])
		self.MAGENTA=libtcod.Color(*data[5])
		self.BROWN=libtcod.Color(*data[6])
		self.LGREY=libtcod.Color(*data[7])
		self.DGREY=libtcod.Color(*data[8])

		self.LBLUE=libtcod.Color(*data[9])

		self.LGREEN=libtcod.Color(*data[10])

		self.LCYAN=libtcod.Color(*data[11])

		self.LRED=libtcod.Color(*data[12])

		self.LMAGENTA=libtcod.Color(*data[13])

		self.YELLOW=libtcod.Color(*data[14])

		self.WHITE=libtcod.Color(*data[15])






class W_Window:

	def __init__(self,parent,width,height):

		self.parent = weakref.ref(parent)
		self.width=width
		self.height=height
		self.console=libtcod.console_new(width,height)

	def get_palette(self):

		pal=self.parent().get_palette()
		return pal


class Main_Window(W_Window):

	def __init__(self,parent,width,height,palette=False):

		W_Window.__init__(self,parent,width,height)

		#self.window=libtcod.console_new(width,height)
		self.sub_windows=list()

		if not palette:
			palette=Palette()

		self.color=palette

	def get_palette(self):

		return self.color

	def create_window(self,width,height,rx,ry,id):

		wind=Simple_Window(self,width,height,rx,ry,id)
		self.sub_windows.append(wind)
		return wind

	def build(self):

		for window in self.sub_windows:
			window.build()

	def render(self):

		for window in self.sub_windows:
			#window.render()
			libtcod.console_blit(window.console,0,0,window.width,window.height,self.console,window.rx,window.ry)

		libtcod.console_blit(self.console,0,0,self.width,self.height,0,0,0)
		libtcod.console_flush()


class Sub_Window(W_Window):

	def __init__(self,parent,width,height,rx,ry,id):

		W_Window.__init__(self,parent,width,height)

		self.rx=rx
		self.ry=ry
		self.id=id


class Simple_Window(Sub_Window):

	def __init__(self,parent,width,height,rx,ry,id):

		Sub_Window.__init__(self,parent,width,height,rx,ry,id)
		self.content=None

		self.bk_color=False
		self.color=False

	def set_content(self,elem):

		self.content=elem

	def add_elem(self,elem):

		self.set_content(elem)


	def set_bk_color(self,color):

		self.bk_color=color

	def set_color(self,color):

		self.color=color

	def get_bk_color(self):

		if self.bk_color:
			return self.bk_color
		else:
			return self.get_palette().DGREY

	def get_color(self):

		if self.color:
			return self.color
		else:
			return self.get_palette().BLUE


	def build(self):


		print 'built!'
		libtcod.console_set_default_foreground(self.console,self.get_color())
		libtcod.console_set_default_background(self.console,self.get_bk_color())
		libtcod.console_print_frame(self.console,0,0,self.width,self.height,True,libtcod.BKGND_SET,self.id)

		temp=libtcod.console_new(self.width-2,self.height-2)
		y=1
		if not self.content:
			print 'fenetre vide'
		else:
			#TODO: redo this, exeptions
			self.content.build(temp)
			libtcod.console_blit(temp,0,0,self.content.width,self.content.height,self.console,1,y)


class Folding_Window(Sub_Window):

	def __init__(self,parent,width,height,rx,ry,id):

		Sub_Window.__init__(self,parent,width,height,rx,ry,id)
		self.content=list()

		#self.mode=

	def add_elem(self,elem):

		self.content.append(elem)

	def build(self):


		print 'built!'
		libtcod.console_set_default_foreground(self.console,self.get_palette().LBLUE)
		libtcod.console_set_default_background(self.console,self.get_palette().DGREY)
		libtcod.console_print_frame(self.console,0,0,self.width,self.height,True,libtcod.BKGND_SET,'fenetre1')

		temp=libtcod.console_new(self.width-2,self.height-2)

		libtcod.console_set_default_foreground(temp,self.get_palette().LBLUE)
		libtcod.console_set_default_background(temp,self.get_palette().DGREY)
		y=1

		for elem in self.content:
			libtcod.console_clear(temp)
			height=elem.build(temp)

			libtcod.console_blit(temp,0,0,elem.width,elem.height,self.console,1,y)

			y+=height

	def render(self):

		pass
