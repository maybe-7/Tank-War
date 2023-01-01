# coding: utf-8
# 场景类(墙、河流、树、冰)
import pygame
import random


# 石头墙
class Brick(pygame.sprite.Sprite):  # 图片大小为24 * 24
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.brick = pygame.image.load('./images/scene/brick.png')
		self.rect = self.brick.get_rect()
		self.being = False


# 钢墙
class Iron(pygame.sprite.Sprite):   #  图片大小为24 * 24
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.iron = pygame.image.load('./images/scene/iron.png')
		self.rect = self.iron.get_rect()
		self.being = False


# 冰
class Ice(pygame.sprite.Sprite):  #  图片大小为12 * 12
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ice = pygame.image.load('./images/scene/ice.png')
		self.rect = self.ice.get_rect()
		self.being = False


# 河流
class River(pygame.sprite.Sprite):  #  图片大小为12 * 12
	def __init__(self, kind=None):
		pygame.sprite.Sprite.__init__(self)
		if kind is None:
			self.kind = random.randint(0, 1)
		self.rivers = ['./images/scene/river1.png', './images/scene/river2.png']
		self.river = pygame.image.load(self.rivers[self.kind])
		self.rect = self.river.get_rect()
		self.being = False


# 树
class Tree(pygame.sprite.Sprite):    # 12 * 12
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.tree = pygame.image.load('./images/scene/tree.png')
		self.rect = self.tree.get_rect()
		self.being = False


# 地图
class Map():
	def __init__(self, stage):
		self.brickGroup = pygame.sprite.Group()
		self.ironGroup = pygame.sprite.Group()
		self.iceGroup = pygame.sprite.Group()
		self.riverGroup = pygame.sprite.Group()
		self.treeGroup = pygame.sprite.Group()
		# commented
		# if stage == 1:
		# 	self.stage1()
		# elif stage == 2:
		# 	self.stage2()
		self.set_stage(stage)
	#
	def set_stage(self, stage=1):
		self.stage1()
	# 关卡一
#this is Brick

	def stage1(self):  # 630 * 630;    630 = 24 * 26 + 6 = 24 * 26 + 3 * 2
		for x in [8,9,10,11,12,13,14,15,16]:
			for y in [6,9,16]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)


	def stage1(self):  # 630 * 630;    630 = 24 * 26 + 6 = 24 * 26 + 3 * 2
		for x in [8,9,10,11,12,13,14,15,16]:
			for y in [6,9,16]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

		for x in [8,12,16]:
			for y in [6,7,8,9,10,11,12]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [10,14]:
			for y in [7,11,19]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [6]:
			for y in [6,7,8,11,12]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [5]:
			for y in [5,12,13,14,15,16]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [4]:
			for y in [17,18]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [9,15]:
			for y in [20]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [11,13]:
			for y in [18]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [11]:
			for y in [4]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [4]:
			for y in [9, 10, 14]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [12]:
			for y in [15,17]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

				for x in [41,42,43,44,45,46,47,48]:
					for y in [6, 9, 16]:
						tree= Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
						tree.being = True
						self.treeGroup.add(tree)
				for x in [41, 45,49 ]:
					for y in [6, 7, 8, 9, 10, 11, 12]:
						tree= Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
						tree.being = True
						self.treeGroup.add(tree)
		for x in [43,47]:
			for y in [7,11,19]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [39]:
			for y in [6,7,8,11,12]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [38]:
			for y in [5,12,13,14,15,16]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [37]:
			for y in [17,18]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [37,46]:
			for y in [19]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [43,45]:
			for y in [18]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [44]:
			for y in [4]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [44]:
			for y in [9, 10, 14]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)
		for x in [47]:
			for y in [20]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)

	def stage2(self):  # 630 * 630;    630 = 24 * 26 + 6 = 24 * 26 + 3 * 2
		for x in [2, 3,4,5 ,6, 7, 8, 9, 10]:
			for y in [3]:
				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)


		for x in [1,2, 3,4,5 ,6, 7, 8, 9, 10,11]:
			for y in [8]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [6]:
			for y in [9,10,11,12,13]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [9]:
			for y in [4]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)

				#this is tree
				for x in [38]:
					for y in [3]:
						tree= Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
						tree.being = True
						self.treeGroup.add(tree)
						for x in [37]:
							for y in [4,5,6]:
								tree = Tree()
								tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
								tree.being = True
								self.treeGroup.add(tree)
						for x in [36, 37, 38]:
							for y in [2]:
								tree = Tree()
								tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
							tree.being = True
							self.treeGroup.add(tree)
				for x in [34, 35, 36, 37, 38,39]:
					for y in [4]:
						tree = Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
					tree.being = True
					self.treeGroup.add(tree)
				for x in [36]:
					for y in [2,3,5,6]:
						tree = Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
					tree.being = True
					self.treeGroup.add(tree)
		for x in [8]:
			for y in [5]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

				for x in [7]:
					for y in [6]:
						brick = Brick()
						brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
						brick.being = True
						self.brickGroup.add(brick)
		for x in [6]:
			for y in [7]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [5]:
			for y in [8]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
				for x in [4]:
					for y in [12]:
						brick = Brick()
						brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
						brick.being = True
						self.brickGroup.add(brick)
						for x in [5]:
							for y in [13]:
								brick = Brick()
								brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
								brick.being = True
								self.brickGroup.add(brick)
	#	for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
#			brick = Brick()
	#		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
#			brick.being = True
#			self.brickGroup.add(brick)
#
		# 作弊模式: 司令部总是被钢板保护
		self.protect_home()

		for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
			iron = Iron()
			iron.rect.left, iron.rect.top = 3 + x * 24, 3 + y * 24
			iron.being = True
			self.ironGroup.add(iron)
	# 关卡二
	def stage3(self):
		self.stage1()
		# for x in [2, 3, 6, 7, 18, 19, 22, 23]:
		# 	for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [10, 11, 14, 15]:
		# 	for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [4, 5, 6, 7, 18, 19, 20, 21]:
		# 	for y in [13, 14]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [12, 13]:
		# 	for y in [16, 17]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
		# 	brick = Brick()
		# 	brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 	brick.being = True
		# 	self.brickGroup.add(brick)
		# for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
		# 	iron = Iron()
		# 	iron.rect.left, iron.rect.top = 3 + x * 24, 3 + y * 24
		# 	iron.being = True
		# 	self.ironGroup.add(iron)
	def stage5(self):
		for x in [2, 3,4,5 ,6, 7, 8, 9, 10]:
			for y in [3]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)


		for x in [1,2, 3,4,5 ,6, 7, 8, 9, 10,11]:
			for y in [8]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [6]:
			for y in [9,10,11,12,13]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
	def stage6(self):
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			iron = Iron()
			iron.rect.left, iron.rect.top = 3 + x * 24, 3 + y * 24
			iron.being = True
			self.ironGroup.add(iron)
		for x in [6]:
			for y in [9,10,11,12,13]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in [9]:
			for y in [4]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

				tree = Tree()
				tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
				tree.being = True
				self.treeGroup.add(tree)

				#this is tree
				for x in [38]:
					for y in [3]:
						tree= Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
						tree.being = True
						self.treeGroup.add(tree)
						for x in [37]:
							for y in [4,5,6]:
								tree = Tree()
								tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
								tree.being = True
								self.treeGroup.add(tree)
						for x in [36, 37, 38]:
							for y in [2]:
								tree = Tree()
								tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
							tree.being = True
							self.treeGroup.add(tree)
				for x in [34, 35, 36, 37, 38,39]:
					for y in [4]:
						tree = Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
					tree.being = True
					self.treeGroup.add(tree)
				for x in [36]:
					for y in [2,3,5,6]:
						tree = Tree()
						tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
					tree.being = True
					self.treeGroup.add(tree)