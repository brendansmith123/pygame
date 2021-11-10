# Example 2

# Import and initialize pygame
import pygame
from random import randint
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height)) REMOVE!
    # self.surf.fill((255, 0, 255)) REMOVE!
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
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
        self.x = randint(50, 400)
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
    self.x = randint(50, 400)
    self.y = -64  

# Make an instance of GameObject
# box = GameObject(120, 300, 50, 50) REMOVE!
apple1 = GameObject(0, 0, 'apple.png') # ADD!
apple2 = GameObject(500, 30, 'apple.png') 
apple3 = GameObject(480, 480, 'apple.png')
apple4 = GameObject(0, 500, 'apple.png') 
apple5 = GameObject(250, 250, 'apple.png') 
strawberry1 = GameObject(15, 250, 'strawberry.png') # ADD!
strawberry2 = GameObject(250, 15, 'strawberry.png')
strawberry3 = GameObject(500, 250, 'strawberry.png')
strawberry4 = GameObject(250, 500, 'strawberry.png')

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # Clear screen
  screen.fill((255, 255, 255))
  # Draw apple
  strawberry1.render(screen)
  strawberry2.render(screen)
  strawberry3.render(screen)
  strawberry4.render(screen)
  apple1.render(screen)
  apple2.render(screen)
  apple3.render(screen)
  apple4.render(screen)
  apple5.render(screen)
  # Update the window
  pygame.display.flip()

