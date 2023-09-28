"""
Plays a game in which the user controls a piper that is trying to collect as many clams as possible before either time runs out
or they get hit by the wave. The number of clams collected is displayed as the player's score when the game ends.

CSCI150 Lab 10

Name: Kunal Handa
Section: B

Creativity:
Game can be run from the command line with any inputted time.
We also changed the function that changes the x position of the wave rectangle so that it progressively takes up more and more
of the screen. It also doesn't go back all the way after a certain number of waves and we did this so that the game gets harder
and harder as you go on.
"""
import pygame
from random import *
from math import *
import sys

# Constants to determine the size of the screen
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 500

# Number of clams to draw at the beginning of the game (or when regenerating)
NUM_CLAMS = 10

# Amount the player should move with each key press
STEP = 50

# Frames-per-second for the game
FPS = 60

class Entity():
    """Base class for all game entities

    You should not ever explicitly create an Entity object, only its child classes should be instantiated.

    Attributes:
        rect: A pygame.Rect that describes the location and size of the entity
    """
    def __init__(self, x, y, width, height):
        """Initialize an Entity

        Args:
            x, y: Initial x,y position for entity
            width: Width of entity's rectangle
            height: Height of entity's rectangle
        """
        self.rect = pygame.Rect(x, y, width, height)
    
    def get_x(self):
        """Return the current x-coordinate"""
        return self.rect.x
    
    def set_x(self, value):
        """Set the x-coordinate to value"""
        self.rect.x = value
    
    def shift_x(self, shift):
        """Shift the x-coordinate by shift (positively or negatively)"""
        self.rect.x += shift
    
    def get_y(self):
        """Return the current y-coordinate"""
        return self.rect.y
    
    def set_y(self, value):
        """Set the y-coordinate to value"""
        self.rect.y = value
    
    def shift_y(self, shift):
        """Shift the y-coordinate by shift (positively or negatively)"""
        self.rect.y += shift
        
    def collide(self, other):
        """
        Returns "true" if the two objects collide, "false" if not
        """
        return self.rect.colliderect(other.rect)
    
class Player(Entity):
    def __init__(self):
        """
        Initiliazes player
        
        """
        super().__init__(0, 0, 50, 50)
        self.image = pygame.transform.scale(pygame.image.load('piper.png'), (50,50))
        
    def render(self, screen):
        """
        draws the rectangle with piper
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def shift_x(self, shift):
        """Shift the x-coordinate by shift (positively or negatively)"""
        self.rect.x += shift
    
    def shift_y(self, shift):
        """Shift the y-coordinate by shift (positively or negatively)"""
        self.rect.y += shift
        
class Clam(Entity):
    def __init__(self):
        """
        initiliazes the clam
        """
        super().__init__(randint(0.5*SCREEN_WIDTH, SCREEN_WIDTH-30),
                         randint(0, SCREEN_HEIGHT-30),
                         30, 30)
        self.image = pygame.transform.scale(pygame.image.load('clam.png'), (50,50))
        
        self.visible = True
        
    def render(self, screen):
        """
        draws the clam if it has not been taken by piper
        """
        if self.visible == True:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        
class Wave(Entity):
    def __init__(self):
        """
        initiliazes wave
        """
        super().__init__(.75*SCREEN_WIDTH,0, SCREEN_WIDTH, SCREEN_HEIGHT)
        
    def render(self, screen):
        """
        draws the wave
        """
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
    

def play_game(max_time):
    """Main game function for Piper's adventure

    Args:
        max_time: Number of seconds to play for
    """
    
    # Initialize the pygame engine
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial',14)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Piper's adventures")

    # Initialize Player, Wave and Clams
    player = Player()
    
    clams = []
    for _ in range(NUM_CLAMS):
        clams.append(Clam())
        
    wave = Wave()


    time  = 0
    score = 0

    # Main game loop
    while time < max_time:

        # Obtain any user inputs
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
          break

        # Screen origin (0, 0) is the upper-left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.shift_x(STEP)
            elif event.key == pygame.K_LEFT:
                player.shift_x(-STEP)
            elif event.key == pygame.K_UP:
                player.shift_y(-STEP)
            elif event.key == pygame.K_DOWN:
                player.shift_y(STEP)
        
        # Determine if Piper gathered more clams
        
                
        # Update the position of the wave
        wave.rect.x = (.8 - time/100)*SCREEN_WIDTH - .25*SCREEN_WIDTH*sin(time) 
        
       
        # When the wave has reached its peak create new clams
        if wave.rect.x < 0.51*SCREEN_WIDTH:
            clams = []
            for _ in range(NUM_CLAMS):
                clams.append(Clam())
            

        # If the piper touched the wave the game is over...
        if wave.collide(player):
            break

        # Draw all of the game elements
        screen.fill([255,255,255])
        for clam in clams:
            clam.render(screen)
            if clam.collide(player):
                if clam.visible == True:
                    score += 1
                    clam.visible = False
                
    
        player.render(screen)
        
        wave.render(screen)
       
        # Render the current time and score
        text = font.render('Time = ' + str(round(max_time-time, 1)), True, (0, 0, 0))
        screen.blit(text, (10, 0.95*SCREEN_HEIGHT))
    
        text = font.render('Score = ' + str(score), True, (0, 0, 0))
        screen.blit(text, (10, 0.90*SCREEN_HEIGHT))

        # Render next frame
        pygame.display.update()
        clock.tick(FPS)

        # Update game time by advancing time for each frame
        time += 1.0/FPS

    print('Game over!')
    print('Score =', score)

    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        play_game(int(sys.argv[1]))
    else:
        play_game(30)

