import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0, 100, 255)

direction=1
right=False
left=False

firing_timer=0
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def moveLR(self, direction):
        self.rect.x+=5*direction

    def moveDown(self):
        self.rect.y+=75
        
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
bullets_list = pygame.sprite.Group()
enemy_bullets_list = pygame.sprite.Group()

blockX=75
 
for i in range(5):
    # This represents a block
    block = Block(WHITE, 25, 25)
 
    # Set a random location for the block
    block.rect.x = blockX
    block.rect.y = 50
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    blockX+=125

blockX=137.5

for i in range(4):
    block = Block(WHITE, 25, 25)
    block.rect.x = blockX
    block.rect.y = 125
    block_list.add(block)
    all_sprites_list.add(block)
    blockX+=125

blockX=75

for i in range(5):
    block = Block(WHITE, 25, 25)
 
    block.rect.x = blockX
    block.rect.y = 200
 
    block_list.add(block)
    all_sprites_list.add(block)
    blockX+=125

blockX=85

for i in range(4):
    block = Block(GREEN, 60, 40)
 
    block.rect.x = blockX
    block.rect.y = 600
 
    
    all_sprites_list.add(block)
    blockX+=148.5
 
# Create a RED player block
player = Block(RED, 20, 20)
player.rect.x = 330
player.rect.y = 680
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right=True
            elif event.key == pygame.K_LEFT:
                left=True
            elif event.key == pygame.K_SPACE:
                bullet=Block(BLUE, 5, 20)
                bullet.rect.x = player.rect.x+7.5
                bullet.rect.y = 680
                all_sprites_list.add(bullet)
                bullets_list.add(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right=False
            if event.key == pygame.K_LEFT:
                left=False
 
    # Clear the screen
    screen.fill(BLACK)
   
    if direction==1:
        for block in block_list:
            block.rect.x+=1
            if block.rect.x>675:
                for block in block_list:
                    #block.rect.x-=75
                    for block in block_list:                  
                        block.rect.y+=25
                    direction=-1
                    break
                break
    else:
        for block in block_list:
            block.rect.x-=1
            if block.rect.x<0:
                for block in block_list:
                    #block.rect.x-=10
                    block.rect.y+=25
                    direction=1
                    
    for bullet in bullets_list:
        bullet.rect.y -= 5
        if bullet.rect.y<50:
            bullet.kill()

    for enemy_bullet in enemy_bullets_list:
        enemy_bullet.rect.y += 5
        if enemy_bullet.rect.y>400:
            enemy_bullet.kill()

    if firing_timer % 60 == 0:
        for block in block_list:
            enemy_bullet=Block(GREEN,5,5)
            enemy_bullet.rect.x = block.rect.x
            enemy_bullet.rect.y = block.rect.y
            all_sprites_list.add(enemy_bullet)
            enemy_bullets_list.add(enemy_bullet)
            
        
    
        
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
##    pos = pygame.mouse.get_pos()
## 
##    # Fetch the x and y out of the list,
##       # just like we'd fetch letters out of a string.
##    # Set the player object to the mouse location
##    player.rect.x = pos[0]
##    player.rect.y = pos[1]
## 
##    # See if the player block has collided with anything.
##    blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

    for bullet in bullets_list:
        for block in block_list:
            if block.rect.colliderect(bullet.rect):
                block.kill()
                bullet.kill()
 
    # Check the list of collisions.
##    for block in blocks_hit_list:
##        block.kill()

    if right and player.rect.x<680:
        player.rect.x+=5
    if left and player.rect.x>0:
        player.rect.x-=5

    firing_timer+=1

 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
