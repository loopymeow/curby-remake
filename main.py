#imports
import pygame
from pygame import mixer
import os
import time

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#window design
WIDTH, HEIGHT = 900, 675	#4:3 aspect ratio like a ds!
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("curby super star ultra!")
tile_size = 25

#load sounds
pygame.mixer.music.load("music/main_music.wav")
damage_sound = pygame.mixer.Sound("music/damage.wav")
damage_sound.set_volume(0.5)
gain_sound = pygame.mixer.Sound("music/gain.wav")
gain_sound.set_volume(0.5)
jump_sound = pygame.mixer.Sound("music/jump.wav")
jump_sound.set_volume(0.5)

class images():
	def __init__(self):
		#title
		title_original = pygame.image.load(
			os.path.join("images/original/title_original.png"))
		self.title_original = pygame.transform.scale(title_original, (900, 675))
		#
		title_slay = pygame.image.load(os.path.join("images/slay/title_slay.png"))
		self.title_slay = pygame.transform.scale(title_slay, (900, 675))
		#
		title_space = pygame.image.load(
			os.path.join("images/space/title_space.png"))
		self.title_space = pygame.transform.scale(title_space, (900, 675))
		#settings
		settings_original = pygame.image.load(
			os.path.join("images/original/settings_original.png"))
		self.settings_original = pygame.transform.scale(settings_original,(900, 675))
		settings_slay = pygame.image.load(
			os.path.join("images/slay/settings_slay.png"))
		self.settings_slay = pygame.transform.scale(settings_slay, (900, 675))
		#
		settings_space = pygame.image.load(
			os.path.join("images/space/settings_space.png"))
		self.settings_space = pygame.transform.scale(settings_space, (900, 675))
		#loadnew
		loadnew_original = pygame.image.load(
			os.path.join("images/original/loadnew_original.png"))
		self.loadnew_original = pygame.transform.scale(loadnew_original,(900, 675))
		#
		loadnew_slay = pygame.image.load(
			os.path.join("images/slay/loadnew_slay.png"))
		self.loadnew_slay = pygame.transform.scale(loadnew_slay, (900, 675))
		#
		loadnew_space = pygame.image.load(
			os.path.join("images/space/loadnew_space.png"))
		self.loadnew_space = pygame.transform.scale(loadnew_space, (900, 675))
		#load
		load_original = pygame.image.load(
			os.path.join("images/original/load_original.png"))
		self.load_original = pygame.transform.scale(load_original, (900, 675))
		#
		load_slay = pygame.image.load(os.path.join("images/slay/load_slay.png"))
		self.load_slay = pygame.transform.scale(load_slay, (900, 675))
		#
		load_space = pygame.image.load(os.path.join("images/space/load_space.png"))
		self.load_space = pygame.transform.scale(load_space, (900, 675))
		#new
		new_original = pygame.image.load(
			os.path.join("images/original/new_original.png"))
		self.new_original = pygame.transform.scale(new_original, (900, 675))
		#
		new_slay = pygame.image.load(os.path.join("images/slay/new_slay.png"))
		self.new_slay = pygame.transform.scale(new_slay, (900, 675))
		#
		new_space = pygame.image.load(os.path.join("images/space/new_space.png"))
		self.new_space = pygame.transform.scale(new_space, (900, 675))
		#error
		error_original = pygame.image.load(
			os.path.join("images/original/error_original.png"))
		self.error_original = pygame.transform.scale(error_original, (900, 675))
		#
		error_slay = pygame.image.load(os.path.join("images/slay/error_slay.png"))
		self.error_slay = pygame.transform.scale(error_slay, (900, 675))
		#
		error_space = pygame.image.load(
			os.path.join("images/space/error_space.png"))
		self.error_space = pygame.transform.scale(error_space, (900, 675))
		#
		#selector
		selector_original = pygame.image.load(
			os.path.join("images/original/selector_original.png"))
		self.selector_original = pygame.transform.scale(selector_original,(900, 675))
		#
		selector_slay = pygame.image.load(
			os.path.join("images/slay/selector_slay.png"))
		self.selector_slay = pygame.transform.scale(selector_slay, (900, 675))
		#
		selector_space = pygame.image.load(
			os.path.join("images/space/selector_space.png"))
		self.selector_space = pygame.transform.scale(selector_space, (900, 675))
		#
		#numbers
		self.zero = pygame.image.load(os.path.join("images/numbers/0.png"))
		#
		self.one = pygame.image.load(os.path.join("images/numbers/1.png"))
		#
		self.two = pygame.image.load(os.path.join("images/numbers/2.png"))
		#
		self.three = pygame.image.load(os.path.join("images/numbers/3.png"))
		#
		self.four = pygame.image.load(os.path.join("images/numbers/4.png"))
		#
		self.five = pygame.image.load(os.path.join("images/numbers/5.png"))
		#
		self.six = pygame.image.load(os.path.join("images/numbers/6.png"))
		#
		self.seven = pygame.image.load(os.path.join("images/numbers/7.png"))
		#
		self.eight = pygame.image.load(os.path.join("images/numbers/8.png"))
		#
		self.nine = pygame.image.load(os.path.join("images/numbers/9.png"))
		#
		#lock
		self.lock = pygame.image.load(os.path.join("images/lock.png"))
		#
		#moving background
		self.scrollbg = pygame.image.load(os.path.join("images/tiling/scrollbg.png"))
		#gameplay
		self.back = pygame.image.load(os.path.join("images/gameplay/back.png"))
		self.back = pygame.transform.scale(self.back, (581*0.3, 217*0.3))
		#
		self.control_D = pygame.image.load(os.path.join("images/gameplay/control_D.png"))
		self.control_D = pygame.transform.scale(self.control_D, (1162*0.3, 150*0.3))
		self.control = "d"
		self.control_U = pygame.image.load(os.path.join("images/gameplay/control_U.png"))
		self.control_U = pygame.transform.scale(self.control_U, (1163*0.5, 330*0.5))
		#
		self.scoreboard = pygame.image.load(os.path.join("images/gameplay/scoreboard.png"))
		self.scoreboard = pygame.transform.scale(self.scoreboard, (1743*0.3, 110*0.3))
		#
		#death message
		self.death_message = pygame.image.load(os.path.join("images/died.png"))
		self.death_message = pygame.transform.scale(self.death_message, (2086*0.3, 830*0.3))
	def titlePics(self, theme):
		if theme == "original":
			WIN.blit(self.title_original, (0, 0))
		if theme == "slay":
			WIN.blit(self.title_slay, (0, 0))
		if theme == "space":
			WIN.blit(self.title_space, (0, 0))
	def settingsPics(self, theme):
		if theme == "original":
			WIN.blit(self.settings_original, (0, 0))
		if theme == "slay":
			WIN.blit(self.settings_slay, (0, 0))
		if theme == "space":
			WIN.blit(self.settings_space, (0, 0))
		#
		fps = getFileValue("files/settings.txt", 0)
		#drawNumbers(file, line, char, x, y, xsize, ysize)
		if len(fps) == 2:
			images.drawNumber("files/settings.txt", 0, 0, 365, 255, 41, 60)
			images.drawNumber("files/settings.txt", 0, 1, 415, 255, 41, 60)
		if len(fps) == 3:
			images.drawNumber("files/settings.txt", 0, 0, 355, 255, 34.2, 50)
			images.drawNumber("files/settings.txt", 0, 1, 390, 255, 34.2, 50)
			images.drawNumber("files/settings.txt", 0, 2, 425, 255, 34.2, 50)
	def loadnew(self, theme):
		if theme == "original":
			WIN.blit(self.loadnew_original, (0, 0))
		if theme == "slay":
			WIN.blit(self.loadnew_slay, (0, 0))
		if theme == "space":
			WIN.blit(self.loadnew_space, (0, 0))

	def load(self, theme):
		if theme == "original":
			WIN.blit(self.load_original, (0, 0))
		if theme == "slay":
			WIN.blit(self.load_slay, (0, 0))
		if theme == "space":
			WIN.blit(self.load_space, (0, 0))

	def new(self, theme):
		if theme == "original":
			WIN.blit(self.new_original, (0, 0))
		if theme == "slay":
			WIN.blit(self.new_slay, (0, 0))
		if theme == "space":
			WIN.blit(self.new_space, (0, 0))

	def error(self, theme):
		if theme == "original":
			WIN.blit(self.error_original, (0, 0))
		if theme == "slay":
			WIN.blit(self.error_slay, (0, 0))
		if theme == "space":
			WIN.blit(self.error_space, (0, 0))
	def selector(self, theme):
		if theme == "original":
			WIN.blit(self.selector_original, (0, 0))
		if theme == "slay":
			WIN.blit(self.selector_slay, (0, 0))
		if theme == "space":
			WIN.blit(self.selector_space, (0, 0))
#drawing window and all sprites on screen
	def drawNumber(self, file, line, char, x, y, xsize, ysize):
		scene=images.scene
		if scene == "level1" or scene == "level2" or scene == "level3":
			data = str(player.score)
		else:
			data = getFileValue(file, line)
		if data[char] == "0":
			current = pygame.transform.scale(self.zero, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "1":
			current = pygame.transform.scale(self.one, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "2":
			current = pygame.transform.scale(self.two, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "3":
			current = pygame.transform.scale(self.three, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "4":
			current = pygame.transform.scale(self.four, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "5":
			current = pygame.transform.scale(self.five, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "6":
			current = pygame.transform.scale(self.six, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "7":
			current = pygame.transform.scale(self.seven, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "8":
			current = pygame.transform.scale(self.eight, (xsize, ysize))
			WIN.blit(current, (x, y))
		if data[char] == "9":
			current = pygame.transform.scale(self.nine, (xsize, ysize))
			WIN.blit(current, (x, y))
	def drawLock(self, file):
		if getFileValue(file, 1) == "False":
			WIN.blit(self.lock, (340, 300))
		if getFileValue(file, 3) == "False":
			WIN.blit(self.lock, (635, 300))
	def drawScrollBg(self):
		WIN.blit(self.scrollbg, (player.disp*0.1, 0))
	def gameplay(self):
		WIN.blit(self.back, (0,0))
		WIN.blit(self.scoreboard, (233, 0)) #<perfect middle
		if self.control == "d":
			WIN.blit(self.control_D, (552,630))
		if self.control == "u":
			WIN.blit(self.control_U, (319,510))
	def death(self):
		WIN.blit(self.death_message, (137, 213))
class Player():
	def __init__(self):
		self.finish_game = False
		self.died = False

		#hurt curby pictures
    #normal curby
		self.curby_fX = pygame.image.load("images/curby/hurt/curby_fX.png")
		self.curby_lX = pygame.image.load("images/curby/hurt/curby_lX.png")
		self.curby_rX = pygame.transform.flip(self.curby_lX, True, False)
		self.curby_l_inX = pygame.image.load("images/curby/hurt/curby_l_inX.png")
		self.curby_r_inX= pygame.transform.flip(self.curby_l_inX, True, False)
    #fire curby
		self.rcurby_fX = pygame.image.load("images/curby/hurt/rcurby_fX.png")
		self.rcurby_lX = pygame.image.load("images/curby/hurt/rcurby_lX.png")
		self.rcurby_rX = pygame.transform.flip(self.rcurby_lX, True, False)
		self.rcurby_l_inX = pygame.image.load("images/curby/hurt/rcurby_l_inX.png")
		self.rcurby_r_inX= pygame.transform.flip(self.rcurby_l_inX, True, False)
    #snow curby
		self.bcurby_fX = pygame.image.load("images/curby/hurt/bcurby_fX.png")
		self.bcurby_lX = pygame.image.load("images/curby/hurt/bcurby_lX.png")
		self.bcurby_rX = pygame.transform.flip(self.bcurby_lX, True, False)
		self.bcurby_l_inX = pygame.image.load("images/curby/hurt/bcurby_l_inX.png")
		self.bcurby_r_inX= pygame.transform.flip(self.bcurby_l_inX, True, False)

	def load_player(self,x,y,type):
		self.finish_game = False
		self.died = False
		self.heart_img = pygame.image.load("images/heart.png")
		self.type = type
		if type == "fire":
			type = "rcurby"
		if type == "snow":
			type = "bcurby"
		self.img_right = pygame.image.load("images/curby/"+type+"_r.png")
		self.img_left = pygame.image.load("images/curby/"+type+"_l.png")
		self.img_front = pygame.image.load("images/curby/"+type+"_f.png")     #normal curby pictures
		self.img_woah = pygame.image.load("images/curby/"+type+"_w.png")
		self.img_right_in = pygame.image.load("images/curby/"+type+"_r_in.png")
		self.img_left_in = pygame.image.load("images/curby/"+type+"_l_in.png")
    
		self.image = self.img_right
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.counter = 0

		self.health = 3
		self.enemy1_killed = False
		self.enemy2_killed = False
		self.enemy3_killed = False
		self.collide1 = 0
		self.collide2 = 0
		self.collide3 = 0

		self.hitbox_rect = self.image.get_rect()
		self.hitbox_rect.x = x
		self.hitbox_rect.y = y
		self.snow_breath = pygame.image.load("images/curby/snow_breath.png")
		self.fire_breath = pygame.image.load("images/curby/fire_breath.png")
		self.snow_breath_left = pygame.transform.flip(self.snow_breath, True, False)
		self.fire_breath_left = pygame.transform.flip(self.fire_breath, True, False)

    
		self.disp = 0
		self.finish_game = False
	def change_type(self, type):
		self.type = type
		if type == "fire":
			type = "rcurby"
			gain_sound.play()
		if type == "snow":
			type = "bcurby"
			gain_sound.play()
		self.img_right = pygame.image.load("images/curby/"+type+"_r.png")
		self.img_left = pygame.image.load("images/curby/"+type+"_l.png")
		self.img_front = pygame.image.load("images/curby/"+type+"_f.png")
		self.img_woah = pygame.image.load("images/curby/"+type+"_w.png")
		self.img_right_in = pygame.image.load("images/curby/"+type+"_r_in.png")
		self.img_left_in = pygame.image.load("images/curby/"+type+"_l_in.png")
	def update(self):
		if player.died == False:
			dx = 0
			dy = 0
			walk_cooldown = 5
	
			#get keypresses
			key = pygame.key.get_pressed()
			if key[pygame.K_w] and self.jumped == False:
				self.vel_y = -15
				self.jumped = True
				jump_sound.play()
			if key[pygame.K_w] == False:
				self.jumped = False
			if key[pygame.K_a]:
				self.disp += 5
				self.counter += 1
				self.direction = -1
			if key[pygame.K_d]:
				self.disp -= 5
				self.counter += 1
				self.direction = 1
			if key[pygame.K_s]:
				self.image = self.img_front
				self.direction = 0
			if key[pygame.K_LEFT]: #relinquish element
				player.change_type("curby")
			if key[pygame.K_a] == False and key[pygame.K_d] == False:
				self.counter = 0
				if self.direction == 1:
					self.image = self.img_right
				if self.direction == -1:
					self.image = self.img_left
			if key[pygame.K_RIGHT] :	# eating
				if self.direction == 1:
						self.image = self.img_right_in
						if self.type == "fire":
							WIN.blit(self.fire_breath_left, self.hitbox_rect)
						elif self.type == "snow":
							WIN.blit(self.snow_breath_left, self.hitbox_rect)
				if self.direction == -1:
						self.image = self.img_left_in
						if self.type == "fire":
							WIN.blit(self.fire_breath, self.hitbox_rect)
						elif self.type == "snow":
							WIN.blit(self.snow_breath, self.hitbox_rect)
				if self.hitbox_rect.colliderect(enemy1.rect):
					if player.type == "fire" and enemy1.type == "snow":
						print("fire!")
						enemy1.dead = True
						print("score = ",self.score)
						self.enemy1_killed = True
						enemy1.rect.x = -200
						
					elif player.type == "snow" and enemy1.type == "fire":
						print("snow!")
						enemy1.dead = True
						print("score = ",self.score)
						self.enemy1_killed = True
						enemy1.rect.x = -200
	
					elif player.type == "curby":
						enemy1.dead = True
						print("score = ",self.score)
						self.enemy1_killed = True
						enemy1.rect.x = -200
						player.change_type(enemy1.type)
						###
				if self.hitbox_rect.colliderect(enemy2.rect):
					if player.type == "fire" and enemy2.type == "snow":
						print("fire!")
						enemy2.dead = True
						print("score = ",self.score)
						self.enemy2_killed = True
						enemy2.rect.x = -200
	
					elif player.type == "snow" and enemy2.type == "fire":
						print("snow!")
						enemy2.dead = True
						print("score = ",self.score)
						self.enemy2_killed = True
						enemy2.rect.x = -200
	
					elif player.type == "curby":
						enemy2.dead = True
						print("score = ",self.score)
						self.enemy2_killed = True
						enemy2.rect.x = -200
						player.change_type(enemy2.type)
						###
				if self.hitbox_rect.colliderect(enemy3.rect):
					if player.type == "fire" and enemy3.type == "snow":
						print("fire!")
						enemy3.dead = True
						print("score = ",self.score)
						self.enemy3_killed = True
						enemy3.rect.x = -200
	
					elif player.type == "snow" and enemy3.type == "fire":
						print("snow!")
						enemy3.dead = True
						print("score = ",self.score)
						self.enemy3_killed = True
						enemy3.rect.x = -200
	
					elif player.type == "curby":
						enemy3.dead = True
						print("score = ",self.score)
						self.enemy3_killed = True
						enemy3.rect.x = -200
						player.change_type(enemy3.type)
	
	
			#player icon change
			if self.counter > walk_cooldown:
				self.counter = 0
				if self.direction == 1:
					self.image = self.img_right
				if self.direction == -1:
					self.image = self.img_left
	
			#gravity
			self.vel_y += 0.5
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y
	
			#collision checker
			for tile in level.new_tile_list:
				#x collision
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				#y collision
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					#check if y < ground
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					#check if y > ground
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
			#door collisions
			for tile in level.new_door_list:
				if tile[1].colliderect(self.rect.x , self.rect.y, self.width, self.height):
					player.finish_game = True
			#enemy collisions
			if self.rect.colliderect(enemy1.rect):	#checking enemy 1 collisions
				self.collide1 = 1
				player.hurt()
			elif self.collide1 == 1:
					self.collide1 = 0
					self.health -= 1
					print("health = ", self.health)
					damage_sound.play()
			if self.rect.colliderect(enemy2.rect):	#checking enemy 2 collisions
				self.collide2 = 1
				player.hurt()
			elif self.collide2 == 1:
					self.collide2 = 0
					self.health -= 1
					print("health = ", self.health)
					damage_sound.play()
			if self.rect.colliderect(enemy3.rect):	#checking enemy 3 collisions
				self.collide3 = 1
				player.hurt()
			elif self.collide3 == 1:
					self.collide3 = 0
					self.health -= 1
					print("health = ", self.health)
					damage_sound.play()
	
	
			#update player coordinates
			self.rect.x += dx
			self.rect.y += dy
	
			if self.rect.bottom > HEIGHT:
				self.rect.bottom = HEIGHT
				dy = 0
	
			#draw player onto screen
			WIN.blit(self.image, self.rect)
			#pygame.draw.rect(WIN, (255, 255, 255), self.rect, 2)#draw rect
	
	
			#modify score
			self.score = self.health*2000
			if self.enemy1_killed == True:
				self.score += 3000
			if self.enemy2_killed == True:
				self.score += 3000
			if self.enemy3_killed == True:
				self.score += 3000
	
			if self.health < 1 :
				self.died = True
				
	def draw_health(self):
		for i in range(0,self.health):
			WIN.blit(self.heart_img, (25+100*i,575))
	def hitbox(self):
		if self.direction == 0:
			self.hitbox_rect.x = self.rect.x
				
		if self.direction == -1:
			self.hitbox_rect.x = self.rect.x - 50
		if self.direction == 1:
			self.hitbox_rect.x = self.rect.x + 50

		self.hitbox_rect.y = self.rect.y
		#pygame.draw.rect(WIN, (159, 43, 104), self.hitbox_rect, 2)
		


	def hurt(self):
		if self.type == "curby" and self.image == self.img_front:
			self.image = self.curby_fX
		if self.type == "curby" and self.image == self.img_right:
			self.image = self.curby_rX
		if self.type == "curby" and self.image == self.img_left:
			self.image = self.curby_lX
		if self.type == "curby" and self.image == self.img_right_in:
			self.image = self.curby_r_inX
		if self.type == "curby" and self.image == self.img_left_in:
			self.image = self.curby_l_inX
				#fire
		if self.type == "fire" and self.image == self.img_front:
			self.image = self.rcurby_fX
		if self.type == "fire" and self.image == self.img_right:
			self.image = self.rcurby_rX
		if self.type == "fire" and self.image == self.img_left:
			self.image = self.rcurby_lX
		if self.type == "fire" and self.image == self.img_right_in:
			self.image = self.rcurby_r_inX
		if self.type == "fire" and self.image == self.img_left_in:
			self.image = self.rcurby_l_inX
			#snow
		if self.type == "snow" and self.image == self.img_front:
			self.image = self.bcurby_fX
		if self.type == "snow" and self.image == self.img_right:
			self.image = self.bcurby_rX
		if self.type == "snow" and self.image == self.img_left:
			self.image = self.bcurby_lX
		if self.type == "snow" and self.image == self.img_right_in:
			self.image = self.bcurby_r_inX
		if self.type == "snow" and self.image == self.img_left_in:
			self.image = self.bcurby_l_inX
class World():
	def __init__(self):
		#load images
		self.dirt_img = pygame.image.load('images/tiling/dirt.png')
		self.grass_img = pygame.image.load('images/tiling/grass_block.png')
		self.green_img = pygame.image.load('images/tiling/green.png')
		self.sandy_img = pygame.image.load('images/tiling/sandy.png')
		self.door_bottom = pygame.image.load('images/tiling/door_bottom.png')
		self.door_top = pygame.image.load('images/tiling/door_top.png')
		#load lists
		self.tile_list = []
		self.new_tile_list = []
		self.level1 = get_grid("files/level1.txt")
		self.level2 = get_grid("files/level2.txt")
		self.level3 = get_grid("files/level3.txt")
		self.current_level = ""
	def load_level(self, data):
		#load lists
		self.tile_list = []
		self.new_tile_list = []
		self.sandy_list = []
		self.new_sandy_list = []
		self.door_list = []
		self.new_door_list = []
		#load level
		if data == 1:
			self.current_level = self.level1
		elif data == 2:
			self.current_level = self.level2
		elif data == 3:
			self.current_level = self.level3
		row_count = 0
		for row in self.current_level:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = self.dirt_img
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = self.grass_img
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = self.green_img
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					img = self.sandy_img
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.sandy_list.append(tile)
				if tile == 5:
					img = self.door_bottom
					img_rect = img.get_rect()
					img_rect.x = col_count * 25
					img_rect.y = row_count * 25
					tile = (img, img_rect)
					self.door_list.append(tile)
				if tile == 6:
					img = self.door_top
					img_rect = img.get_rect()
					img_rect.x = col_count * 25
					img_rect.y = row_count * 25
					tile = (img, img_rect)
					self.door_list.append(tile)
				col_count += 1
			row_count += 1

	def modify_rect(self):
		disp = player.disp
		self.new_tile_list = []
		for tile in self.tile_list:
			pic = tile[0]
			rect = tile[1]
			xval = rect[0]
			yval = rect[1]
			pic_rect = pic.get_rect()
			pic_rect.x = xval + disp
			pic_rect.y = yval
			tile = (pic, pic_rect)
			self.new_tile_list.append(tile)
		self.new_sandy_list = []
		for tile in self.sandy_list:
			pic = tile[0]
			rect = tile[1]
			xval = rect[0]
			yval = rect[1]
			pic_rect = pic.get_rect()
			pic_rect.x = xval + disp
			pic_rect.y = yval
			tile = (pic, pic_rect)
			self.new_sandy_list.append(tile)
		self.new_door_list = []
		for tile in self.door_list:
			pic = tile[0]
			rect = tile[1]
			xval = rect[0]
			yval = rect[1]
			pic_rect = pic.get_rect()
			pic_rect.x = xval + disp
			pic_rect.y = yval
			tile = (pic, pic_rect)
			self.new_door_list.append(tile)

	def draw(self):
		for tile in self.new_tile_list:
			WIN.blit(tile[0], tile[1])
		for tile in self.new_sandy_list:
			WIN.blit(tile[0], tile[1])
		for tile in self.new_door_list:
			WIN.blit(tile[0], tile[1])
class Enemy():
	def load(self, type, xpos, ypos, distance):
		self.image_r = pygame.image.load("images/enemies/"+type+"_r.png")
		self.image_l = pygame.image.load("images/enemies/"+type+"_l.png")
		self.image = self.image_r
		self.rect = self.image.get_rect()

		self.type = type
		
		self.rect.x = xpos
		self.rect.y = ypos
		self.disp = 0

		self.rectOG = self.image.get_rect()
		self.rectOG.x = xpos
		self.rectOG.y = ypos
		
		self.direction = 1
		self.distance = distance
		self.counter = 0
		self.walk = 0

		self.dead = False

	def update(self):
		if self.dead == False:
			self.disp = player.disp
			if self.direction == 1:
				self.walk += 1
			elif self.direction == -1:
				self.walk -= 1
				###############^advance in the direction
			if self.counter > self.distance and self.direction == 1:
				self.counter = 0
				self.direction = -1
				self.image = self.image_l
			elif self.counter > self.distance and self.direction == -1:
				self.counter = 0
				self.direction = 1
				self.image = self.image_r
				#######################^check if walked far enough to reverse the walk
			self.counter += 1	#iterate the counter
	def draw(self):
		if self.dead == False:
			self.rect.x = self.rectOG.x + self.disp +self.walk
			WIN.blit(self.image, self.rect)
			#pygame.draw.rect(WIN, (255, 255, 255), self.rect, 2)#draw rect
def draw_window(scene, theme, currentSave):
	WIN.fill((222, 235, 247))	#219, 246, 249
	if scene == "title":
		images.titlePics(theme)
	if scene == "settings":
		images.settingsPics(theme)
	if scene == "loadnew":
		images.loadnew(theme)
	if scene == "load":
		images.load(theme)
		displayScores("newloaderror", currentSave)
	if scene == "new":
		images.new(theme)
		displayScores("newloaderror", currentSave)
	if scene == "error":
		images.error(theme)
		displayScores("newloaderror", currentSave)
	if scene == "selector":
		images.selector(theme)
		displayScores("selector", currentSave)
		images.drawLock(currentSave)
	if scene == "level1":
		images.drawScrollBg()
		level.modify_rect()
		level.draw()
		images.gameplay()
		if player.died == False:
			player.update()
			player.draw_health()
			player.hitbox()
			enemy1.draw()
			enemy1.update()
			enemy2.draw()
			enemy2.update()
			enemy3.draw()
			enemy3.update()
		else:
			images.death()
		displayScores(scene, 1)
	if scene == "level2":
		images.drawScrollBg()
		level.modify_rect()
		level.draw()
		images.gameplay()
		if player.died == False:
			player.update()
			player.draw_health()
			player.hitbox()
			enemy1.draw()
			enemy1.update()
			enemy2.draw()
			enemy2.update()
			enemy3.draw()
			enemy3.update()
		else:
			images.death()
		displayScores(scene, 1)
	if scene == "level3":
		images.drawScrollBg()
		level.modify_rect()
		level.draw()
		images.gameplay()
		if player.died == False:
			player.update()
			player.draw_health()
			player.hitbox()
			enemy1.draw()
			enemy1.update()
			enemy2.draw()
			enemy2.update()
			enemy3.draw()
			enemy3.update()
		else:
			images.death()
		displayScores(scene, 1)
	pygame.display.update()
def changeFileValue(file, line, new):
	oldf = open(file, "r")
	all = oldf.readlines()
	all[line] = str(new) + "\n"
	oldf.close()
	newf = open(file, "w")
	newf.writelines(all)
	newf.close()
def getFileValue(file, line):
	f = open(file, "r")
	all = f.readlines()
	all = all[line]
	all = all[0:(len(all) - 1)]
	f.close()
	return all
def displayScores(scene, currentSave):
	if scene == "newloaderror":
		#save1
		for x in range(0, 5, 2):
			length = len(getFileValue("files/save1.txt", x))
			for i in range(0, length):
				images.drawNumber("files/save1.txt", x, i, 150 + (20 * i), 540 + (18 * x), 20.5,30)
		#save2
		for x in range(0, 5, 2):
			length = len(getFileValue("files/save2.txt", x))
			for i in range(0, length):
				images.drawNumber("files/save2.txt", x, i, 445 + (20 * i), 540 + (18 * x), 20.5,30)
		#save2
		for x in range(0, 5, 2):
			length = len(getFileValue("files/save3.txt", x))
			for i in range(0, length):
				images.drawNumber("files/save3.txt", x, i, 745 + (20 * i), 540 + (18 * x), 20.5,30)
	if scene == "selector":
		for x in range(0, 5, 2):
			length = len(getFileValue(currentSave, x))
			for i in range(0, length):
				images.drawNumber(currentSave, x, i, 107 + (20 * i) + (145 * x), 540, 20.5,30)
	if scene == "level1" or scene == "level2" or scene == "level3":
		score = str(player.score)
		length = len(score)
		for i in range(0, length):
			images.drawNumber(score, 1, i, 560 + (20 * i), 0, 20.5,30)


	#
def get_grid(file):
		list = []
		for i in range (1, 28):
			data = getFileValue(file, i)
			tuple = []
			for char in data:
				if char == "0":
					tuple.append(0)
				if char == "1":
					tuple.append(1)
				if char == "2":
					tuple.append(2)
				if char == "3":
					tuple.append(3)
				if char == "4":
					tuple.append(4)
				if char == "5":
					tuple.append(5)
				if char == "6":
					tuple.append(6)
			list.append(tuple)
		return list
def fpsChanger():
	currentFps = ""
	count = 0
	loop = True
	while loop == True:
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if keys[pygame.K_0]:
				if count < 3:
					currentFps = currentFps + "0"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/0.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_1]:
				if count < 3:
					currentFps = currentFps + "1"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/1.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_2]:
				if count < 3:
					currentFps = currentFps + "2"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/2.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_3]:
				if count < 3:
					currentFps = currentFps + "3"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/3.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_4]:
				if count < 3:
					currentFps = currentFps + "4"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/4.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_5]:
				if count < 3:
					currentFps = currentFps + "5"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/5.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_6]:
				if count < 3:
					currentFps = currentFps + "6"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/6.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_7]:
				if count < 3:
					currentFps = currentFps + "7"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/7.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_8]:
				if count < 3:
					currentFps = currentFps + "8"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/8.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_9]:
				if count < 3:
					currentFps = currentFps + "9"
					count = count + 1
					number = pygame.image.load(os.path.join("images/numbers/9.png"))
					number = pygame.transform.scale(number, (34.2, 50))
					if count == 1:
						WIN.blit(number, (355, 255))
					if count == 2:
						WIN.blit(number, (390, 255))
					if count == 3:
						WIN.blit(number, (425, 255))
					pygame.display.update()
			if keys[pygame.K_SPACE]:
				if int(currentFps) <= 150 and int(currentFps) >= 25:
					changeFileValue("files/settings.txt", 0, currentFps)
					loop = False
				else:
					loop = False
			if keys[pygame.K_ESCAPE] or keys[pygame.K_w]:
				loop = False


def checkNew(save):
	new = False
	if getFileValue(save, 0) == "00000":
		if getFileValue(save, 1) == "False":
			if getFileValue(save, 2) == "00000":
				if getFileValue(save, 3) == "False":
					if getFileValue(save, 4) == "00000":
						new = True
	return new
def deleteSave(save):
	changeFileValue(save, 0, "00000")
	changeFileValue(save, 1, "False")
	changeFileValue(save, 2, "00000")
	changeFileValue(save, 3, "False")
	changeFileValue(save, 4, "00000")
def get_input(scene, currentSave, newORload):
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			print("quit")
		if scene == "title":###################################
			if keys[pygame.K_UP]:
				scene = "settings"
				return scene, currentSave, newORload
			if keys[pygame.K_DOWN]:
				scene = "loadnew"
				return scene, currentSave, newORload
			else:
				return scene, currentSave, newORload
		if scene == "settings":##################################
			if keys[pygame.K_UP]:
				scene = "title"
				return scene, currentSave, newORload
			if keys[pygame.K_LEFT]:
				changeFileValue("files/settings.txt", 2, "slay")
				return scene, currentSave, newORload
			if keys[pygame.K_DOWN]:
				changeFileValue("files/settings.txt", 2, "original")
				return scene, currentSave, newORload
			if keys[pygame.K_RIGHT]:
				changeFileValue("files/settings.txt", 2, "space")
			if keys[pygame.K_w]:
				fpsbox= pygame.image.load(os.path.join("images/fpsbox.png"))
				fpsbox= pygame.transform.scale(fpsbox, (130, 98))
				WIN.blit(fpsbox, (347, 237))
				pygame.display.update()
				fpsChanger()
				return scene, currentSave, newORload
			if keys[pygame.K_a]:
				pygame.mixer.music.play(-1,	0.0,	5000)
				changeFileValue("files/settings.txt", 1, "True")
				return scene, currentSave, newORload
			if keys[pygame.K_d]:
				pygame. mixer. music. stop()
				changeFileValue("files/settings.txt", 1, "False")
				return scene, currentSave, newORload
		if scene == "loadnew":
			if keys[pygame.K_UP]:
				scene = "title"
				return scene, currentSave, newORload
			if keys[pygame.K_RIGHT]:
				scene = "new"
				return scene, currentSave, newORload
			if keys[pygame.K_LEFT]:
				scene = "load"
				return scene, currentSave, newORload
			return scene, currentSave, newORload
		if scene == "load": ####################################################LOAD
			newORload = "load"
			if keys[pygame.K_UP]:
				scene = "loadnew"
				return scene, currentSave, newORload
			if keys[pygame.K_LEFT]:
				scene = "selector"
				currentSave = "files/save1.txt"
				return scene, currentSave, newORload
			if keys[pygame.K_DOWN]:
				scene = "selector"
				currentSave = "files/save2.txt"
				return scene, currentSave, newORload
			if keys[pygame.K_RIGHT]:
				scene = "selector"
				currentSave = "files/save3.txt"
				return scene, currentSave, newORload
			return scene, currentSave, newORload
		if scene == "new": #################################################NEW
			newORload = "new"
			if keys[pygame.K_UP]:
				scene = "loadnew"
				return scene, currentSave, newORload
			if keys[pygame.K_LEFT]:
				if checkNew("files/save1.txt") == True:
					scene = "selector"
					currentSave = "files/save1.txt"
					return scene, currentSave, newORload
				else:
					scene = "error"
					currentSave = "files/save1.txt"
					return scene, currentSave, newORload
			if keys[pygame.K_DOWN]:
				currentSave = "files/save2.txt"
				if checkNew("files/save2.txt") == True:
					scene = "selector"
					return scene, currentSave, newORload
				else:
					scene = "error"
					return scene, currentSave, newORload
			if keys[pygame.K_RIGHT]:
				currentSave = "files/save3.txt"
				if checkNew("files/save3.txt") == True:
					scene = "selector"
					return scene, currentSave, newORload
				else:
					scene = "error"
					return scene, currentSave, newORload
		if scene == "error":
			if keys[pygame.K_LEFT]:
				deleteSave(currentSave)
				scene = "selector"
				return scene, currentSave, newORload
			if keys[pygame.K_RIGHT]:
				scene = "new"
				currentSave = 0
				return scene, currentSave, newORload
			else:
				return scene, currentSave, newORload
		if scene == "selector": ######################################SELECTOR
			if keys[pygame.K_UP]:
				if newORload == "load":
					print("load")
					currentSave = 0
					scene = "load"
				if newORload == "new":
					currentSave = 0
					scene = "new"
				return scene, currentSave, newORload
			if keys[pygame.K_LEFT]:
				scene = "level1"
				level.load_level(1)
				player.load_player(450,425,"curby")
				images.control = "d"
				player.disp = -400
				enemy1.load("fire", 550, 200, 100)
				enemy2.load("snow", 1350, 175, 150)
				enemy3.load("fire", 1750, 250, 225)
				return scene, currentSave, newORload
			if keys[pygame.K_DOWN]:
				if getFileValue(currentSave, 1) == "True" or newORload == "load":
					scene = "level2"
					level.load_level(2)
					player.load_player(450,425,"curby")
					images.control = "d"
					player.disp = -400
					enemy1.load("snow", 775, 125, 200)
					enemy2.load("snow", 1050, 275, 200)
					enemy3.load("fire", 1725, 200, 175)
				return scene, currentSave, newORload
			if keys[pygame.K_RIGHT]:
				if getFileValue(currentSave, 3) == "True" or newORload == "load":
					scene = "level3"
					level.load_level(3)
					player.load_player(450,425,"curby")
					images.control = "d"
					player.disp = -400
					enemy1.load("fire", 750, 200, 75)
					enemy2.load("fire", 1150, 425, 100)
					enemy3.load("snow", 1775, 150, 300)
				return scene, currentSave, newORload
		if scene == "level1": #######################################################
			if player.finish_game == True:
				scene = "selector"
				print(getFileValue(currentSave, 0))
				if int(getFileValue(currentSave, 0)) < player.score:
					changeFileValue(currentSave, 0, player.score)
				changeFileValue(currentSave, 1, True)
				player.finish_game = False
				return scene, currentSave, newORload
			level.draw()
			player.update()
			if keys[pygame.K_UP]:
				scene = "selector"
				return scene, currentSave, newORload
			if keys[pygame.K_SPACE]:
				if images.control == "u":
					images.control = "d"
				else:
					images.control = "u"
				return scene, currentSave, newORload
			return scene, currentSave, newORload
		if scene == "level2":#######################################################
			if player.finish_game == True:
				scene = "selector"
				if int(getFileValue(currentSave, 2)) < player.score:
					changeFileValue(currentSave, 2, player.score)
				changeFileValue(currentSave, 3, True)
				player.finish_game = False
				return scene, currentSave, newORload
			level.draw()
			player.update()
			if keys[pygame.K_UP]:
				scene = "selector"
				return scene, currentSave, newORload
			if keys[pygame.K_SPACE]:
				if images.control == "u":
					images.control = "d"
				else:
					images.control = "u"
				return scene, currentSave, newORload
			return scene, currentSave, newORload
		if scene == "level3":#########################################################
			if player.finish_game == True:
				scene = "selector"
				if int(getFileValue(currentSave, 4)) < player.score:
					changeFileValue(currentSave, 4, player.score)
				player.finish_game = False
				return scene, currentSave, newORload
			level.draw()
			player.update()
			if keys[pygame.K_UP]:
				scene = "selector"
				return scene, currentSave, newORload
			if keys[pygame.K_SPACE]:
				if images.control == "u":
					images.control = "d"
				else:
					images.control = "u"
				return scene, currentSave, newORload
			return scene, currentSave, newORload
		return scene, currentSave, newORload
	return scene, currentSave, newORload


	
#the main
def main(scene, run):
	run = True
	currentSave = 0
	newORload = 0
	scene = scene
	while run == True:
		temp = get_input(scene, currentSave, newORload)
		scene = temp[0]
		currentSave = temp[1]
		newORload = temp[2]
		theme = getFileValue("files/settings.txt", 2)
		fps = getFileValue("files/settings.txt", 0)
		images.scene = scene
		draw_window(scene, theme, currentSave) 
		clock.tick(int(fps))	#60fps game!

#slay


#establishing classes
images = images()
level = World()
player = Player()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

#check	for	music
if	getFileValue("files/settings.txt",	1)	==	"True":
		pygame.mixer.music.play(-1,	0.0,	5000)

clock = pygame.time.Clock()
scene = "title" 
run = True
main(scene, run)