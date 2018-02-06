
import sys
import os
import libtcodpy as libtcod
import copy


class TilesetListener:

	def __init__(self,tileset):

		self.tempData=[0 for i in range(7)]
		self.tileset=tileset

	def new_struct(self,str,name):

		if libtcod.struct_get_name(str)=='tile':
			self.tempdata=[0 for i in range(7)]
			self.tempdata[1]=name
			return True
		else:
			return False


	def new_flag(self,name):

		return False

	def new_property(self,name,type,value):

		if name=='id':
			self.tempdata[0]=value
		elif name=='chara':
			self.tempdata[2]=value
		elif name=='path':
			self.tempdata[3]=value
		elif name=='view':
			self.tempdata[4]=value

		elif name=='ccolor':
			self.tempdata[5]=(value.r,value.g,value.b)

		elif name=='bcgcolor':
			self.tempdata[6]=(value.r,value.g,value.b)

		else:
			return False

		#print name, value

		return True


	def end_struct(self,struct,name):

		#print self.tempdata
		self.tileset.tile_data[self.tempdata[0]]=copy.deepcopy(self.tempdata)

		return True


	def error(self,msg):

		print msg
		return True



	def __del__(self):

		print 'listener destroyed'


class Tile:

	def __init__(self,passable,viewable,char,color,bkgnd_color):

		self.path=passable
		self.view=viewable
		self.char=char
		self.color=color
		self.background=bkgnd_color




class Tileset:

	def __init__(self,size):

		self.tile_data=[0 for i in range(size)]


	def load(self,file):

		parser=libtcod.parser_new()
		tile_struc=libtcod.parser_new_struct(parser,"tile")
		libtcod.struct_add_property(tile_struc,"id",libtcod.TYPE_INT,True)
		libtcod.struct_add_property(tile_struc,"chara",libtcod.TYPE_CHAR,True)

		libtcod.struct_add_property(tile_struc,"path",libtcod.TYPE_BOOL,True)
		libtcod.struct_add_property(tile_struc,"view",libtcod.TYPE_BOOL,True)

		libtcod.struct_add_property(tile_struc,"ccolor",libtcod.TYPE_COLOR,True)
		libtcod.struct_add_property(tile_struc,"bcgcolor",libtcod.TYPE_COLOR,True)


		libtcod.parser_run(parser,file,TilesetListener(self))

		print "ended"

		libtcod.parser_delete(parser)

	def create_tile(self,id):

		return Tile(self.tile_data[id][3],self.tile_data[id][4],self.tile_data[id][2],libtcod.Color(*self.tile_data[id][5]),libtcod.Color(*self.tile_data[id][6]))

class Map:

	def __init__(self,width,height):

		self.width=width
		self.height=height
		self.data=[[Tile(False,False,chr(219),libtcod.light_blue,libtcod.black) for X in range(width)] for Y in range(height)]

	def get_tile(self,x,y):
		return self.data[y][x]

	def set_tile(self,x,y,tile):
		self.data[y][x]=tile

	def __del__(self):

		print "Map deleted"
