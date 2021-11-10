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



# Make an instance of GameObject
# box = GameObject(120, 300, 50, 50) REMOVE!
apple = GameObject(120, 300, 'apple.png') # ADD!
strawberry = GameObject(160, 350, 'strawberry.png')
# Clear screen
screen.fill((255, 255, 255))
# Draw box
strawberry.render(screen)
apple.render(screen) # ADD!
# Update the window
pygame.display.flip()

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
  apple.render(screen)
  # Update the window
  pygame.display.flip()

