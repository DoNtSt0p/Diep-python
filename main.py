from pygame import *
from math import *

window = display.set_mode()
size = Vector2( window.get_size() )
center = size / 2
clock = time.Clock()

class Set:
	def __init__(self):
		self.hlth = 1 # Health
		self.regn = 1 # Regeneration
		self.armr = 1 # Armor
		self.shld = 0 # Shield

		self.damg = 1 # Bullet damage
		self.powr = 1 # Bullet power
		self.bspd = 1 # Bullet speed
		self.reld = 1 # Gun reload

		self.visn = 1 # Vision distance
		self.sped = 1 # Tank speed
		self.mass = 1 # Body mass
		self.ramd = 1 # Body ram damage

class Tank:
	def __init__(self, pos, name, team = None):
		self.pos = Vector2(pos)
		self.vec = Vector2(0, 0)
		self.name = name
		self.team = team
		self.move = Vector2(0, 0)
		self.color = (191, 191, 191)
		self.set = Set()
	
	def update(self):
		self.pos += self.vec
		self.vec *= 0.9
		if self.move.x != 0 or self.move.y != 0:
			l = 

	def draw(self):
		draw.circle(window, self.color, self.pos + center, 10)

player = Tank(Vector2(0, 0), "You")

pressed_keys = key.get_pressed()

loop = True
while loop:
	window.fill((0, 0, 0))
	
	player.update()
	player.draw()

	display.update()

	clock.tick(60)
	
	pressed_keys = key.get_pressed()

	if pressed_keys[K_w] and not pressed_keys[K_s]:
		player.move.y = -1
	elif pressed_keys[K_s] and not pressed_keys[K_w]:
		player.move.y = 1
	else:
		player.move.y = 0
	if pressed_keys[K_a] and not pressed_keys[K_d]:
		player.move.x = -1
	elif pressed_keys[K_d] and not pressed_keys[K_a]:
		player.move.x = 1
	else:
		player.move.x = 0

	for e in event.get():
		if e.type == WINDOWCLOSE:
			loop = False
		elif e.type == KEYDOWN:
			if e.key == K_DELETE:
				loop = False