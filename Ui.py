
import sys
import os
import libtcodpy as libtcod
import weakref

class Wui_elem:

	def __init__(self,parent,width,height,pos=False):

		self.parent = weakref.ref(parent)
		self.width=width
		self.height=height
		self.pos=pos

	def __del__(self):

		print "Wui object deleted"


		#TODO wrapping,colors, etc...
class W_Text(Wui_elem):

	def __init__(self,parent,width,height,text,pos=False):

		Wui_elem.__init__(self,parent,width,height,pos)

		self.text=text

	def build(self,con):

		print 'and build here too'
		#libtcod.console_set_default_foreground(con,libtcod.blue)
		#libtcod.console_set_default_background(con,libtcod.red)
		libtcod.console_print_ex(con,0,0,libtcod.BKGND_NONE,libtcod.LEFT,self.text)
		self.width=len(self.text)
		self.height=1

		return 1







class Ui_holder(Wui_elem):

	def __init__(self):

		self.content=list()

	def add_elem(self,elem):

		self.content.append(elem)



	def __del__(self):

		print "ui holder object deleted"






class Simple_Menu(Ui_holder,Wui_elem):

	def __init__(self,parent,width,height,name,id,pos=False):

		Ui_holder.__init__(self)
		Wui_elem.__init__(self,parent,width,height,pos)

		self.name=name
		self.id=id

	def build(self,con):

		#build the menu itself

		libtcod.console_print_ex(con,self.width/2,0,libtcod.BKGND_NONE,libtcod.CENTER,self.name)




		i=1

		temp=libtcod.console_new(self.width,self.height)


		for elem in self.content:

			print elem
			print "built"
			dh=elem.build(temp)
			libtcod.console_blit(temp,0,0,elem.width,dh,con,1,i)

			libtcod.console_clear(temp)
			libtcod.console_put_char_ex(con,0,i,chr(26),libtcod.white,libtcod.black)
		#	libtcod.console_set_char_background(con, 0, i, libtcod.blue)
			i+=dh

		self.height=i+1


class Line_Menu(Simple_Menu):

	def __init__(self,parent,width,height,name,id,pos=False):

		Simple_Menu.__init__(self,parent,width,height,name,id,pos)

	def build(self,con):

		i=0

		temp=libtcod.console_new(self.width,self.height)

		for elem in self.content:
			elem.build(temp)

			libtcod.console_blit(temp,0,0,elem.width,elem.height,con,i,0)
			i+= elem.width

			libtcod.console_put_char_ex(con,i,0,chr(186),libtcod.white,libtcod.black)
			i+=1
			libtcod.console_clear(temp)



#Main Class, used for all ui manipulations, and constant keeping
class Ui:
	"""
	Main class of the Ui module
	used as interface to Create ui component

	"""

	def __init__(self,palette):
		"""
		
		"""

		self.color=palette

	def create_menu(self,type,window,width,height,name,pos=False):



		if type=='simple':			#TODO: change and automate this
			menu=Simple_Menu(window,width,height,name,42,pos)

		elif type=='line':
			menu = Line_Menu(window,width,height,name,42,pos)

		window.add_elem(menu)
		return menu

	def create_text(self,menu,text,pos=False):

		tex=W_Text(menu,1,1,text,pos)
		menu.add_elem(tex)
		return tex
