####################################
# bat.py
# rev. 1
####################################

# definitions
import sys
import pygame
import spritesheet

# constants
numframes=10

# functions
def load_frame(fname):
  img=pygame.image.load(fname)
  return img

# the Bat class (inherits from Sprite class) and its member functions
class Bat(pygame.sprite.Sprite):
  def __init__(self): # this gets called when a Bat object is instantiated
    super(Bat, self).__init__()
    ss=spritesheet.spritesheet('assets/bat-ss.png');
    # the frames for the sprite!
    self.frames=ss.load_strip((0,0,75,13), numframes, 0);

    self.idx=0 # create an idx member variable to reference the frame
    self.incr=0 # create a variable to pace the sprite animation
    self.frame_period=200 # set frames to update at this period
    self.image=self.frames[self.idx]
    self.rect=pygame.Rect(100, 175, 75, 13) # defines an area sixe 75x13 at pos (100,175)

  def getrect(self):
    return self.rect

  def movepos(self, loc):
    self.rect.move_ip(loc[0], loc[1]);

  def update(self):
    self.incr=self.incr+1
    if (self.incr>self.frame_period): # is it time for incrementing the frame?
      self.incr=0
      self.idx=self.idx+1 # increment the frame reference (idx)
      if (self.idx >= len(self.frames)): # loop animation so that it restarts
        self.idx=0

    self.image=self.frames[self.idx] 


