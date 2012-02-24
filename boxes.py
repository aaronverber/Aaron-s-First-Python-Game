import pygame

class Box(pygame.sprite.Sprite):
	def __init__(self, color, initial_position):
		self.image = pygame.Surface([15, 15])
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
		self.rect.topleft = initial_position
		
class UpDownBox(pygame.sprite.Sprite):
	def __init__(self, color, initial_position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([15, 15])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.topleft = initial_position
		self.going_down = True
		self.next_update_time = 0
		
	def update(self, current_time, bottom):
		if self.next_update_time < current_time:
			if self.rect.bottom == bottom - 1: self.going_down = False
			elif self.rect.top == 0: self.going_down = True
		
		if self.going_down: self.rect.top += 1
		else: self.rect.top -= 1
		
		self.next_update_time = current_time + 10