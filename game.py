
# Import and initialize pygame
import pygame
from random import randint
pygame.init()
import random

screen = pygame.display.set_mode([500, 500])

lanes = [93, 218, 343]


# Game Object
class GameObject(pygame.sprite.Sprite):
	def __init__(self, x, y, image):
		super(GameObject, self).__init__()
		self.surf = pygame.image.load(image)
		self.x = x
		self.y = y
		self.rect = self.surf.get_rect() # add 

	def render(self, screen):
		self.rect.x = self.x # add
		self.rect.y = self.y # add
		screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 500:
      self.reset()

  def reset(self):
    self.x = random.choice(lanes)
    self.y = -64

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500:
      self.reset()

  def reset(self):
    self.x = -64
    self.y = random.choice(lanes)


class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'bomb.png')
    self.dx = 0
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
      self.reset()

  def reset(self):
    direction = randint(1, 4)
    if direction == 1:
      self.x = -64
      self.y = random.choice(lanes)
      self.dx = (randint(0, 200) / 100) + 1
      self.dy = 0
    elif direction == 2:
      self.x = 500
      self.y = random.choice(lanes)
      self.dx = ((randint(0, 200) / 100) + 1) * -1
      self.dy = 0
    elif direction == 3:
      self.x = random.choice(lanes)
      self.y = -64
      self.dx = 0
      self.dy = (randint(0, 200) / 100) + 1
    else:
      self.x = random.choice(lanes)
      self.y = 500
      self.dx = 0
      self.dy = ((randint(0, 200) / 100) + 1) * -1  

# -------------------------------------------
# Player


class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
    self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
    self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
    self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
    self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y
  
  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]  

all_sprites = pygame.sprite.Group() 
fruit_sprites = pygame.sprite.Group()                 

apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

clock = pygame.time.Clock()

# Creat the game loop
running = True
while running:
 # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()  
  # Clear screen
  screen.fill((255, 255, 255))
  # Draw apple
  apple.move()
  apple.render(screen)
  strawberry.move()
  strawberry.render(screen)
  player.move()
  player.render(screen)
  bomb.move()
  bomb.render(screen)

  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
	  fruit.reset()

  if pygame.sprite.collide_rect(player, bomb):
	  running = False
  # Update the window
  pygame.display.flip()
  # tick the clock!
  clock.tick(20)


