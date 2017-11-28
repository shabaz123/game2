####################################
# ball.py
# rev. 1
####################################

# definitions
import sys
import pygame
import spritesheet

# constants
screenwidth=320
screenheight=200
xdelstep=2
xmaxdel=25
numframes=1

# functions
def load_frame(fname):
  img=pygame.image.load(fname)
  return img

# the Ball class (inherits from Sprite class) and its member functions
class Ball(pygame.sprite.Sprite):
  def __init__(self): # this gets called when a Ball object is instantiated
    super(Ball, self).__init__()
    ss=spritesheet.spritesheet('assets/ball1-ss.png');
    # the frames for the sprite!
    self.frames=ss.load_strip((0,0,25,25), numframes, 0);

    self.idx=0 # create an idx member variable to reference the frame
    self.incr=0 # create a variable to pace the sprite animation
    self.frame_period=20 # set frames to update at this period
    self.image=self.frames[self.idx]
    self.rect=pygame.Rect(5, 100, 25, 25) # defines an area sixe 25x25 at pos (5,100)

    self.ballxincr=0
    self.ballyincr=0
    self.ballxdel=1
    self.ballydel=1
    self.ballxx=1
    self.ballyy=1
    self.moved=0

  def speed_up(self):
    self.ballxdel=self.ballxdel-xdelstep
    if self.ballxdel<1:
      self.ballxdel=1

  def speed_down(self):
    self.ballxdel=self.ballxdel+xdelstep
    if self.ballxdel>xmaxdel:
      self.ballxdel=xmaxdel

  def collision(self, other, mv):
    self.incr=self.frame_period
    self.ballxincr=self.ballxdel
    #if self.rect.centery<=other.top:
    if self.rect.bottom<=other.top+1:
      # it was a collision with top surface of bat
      if self.rect.centerx>=other.left and self.rect.centerx<=other.right:
        # it was a collision with central portion of the bat
        self.ballyy=-1
        if self.moved>0:
          if self.ballxx>0:
            self.speed_up()
          else:
            self.speed_down()
        elif self.moved<0:
          if self.ballxx<0:
            self.speed_up()
          else: 
            self.speed_down()
      elif self.rect.centerx>=other.left-12 and self.rect.centerx<=other.right+12:
        # it was a collision with the left or right edge of the bat
        self.ballyy=-1
        if self.rect.centerx<other.left:
          self.ballxx=-1
          if self.moved<0:
            self.speed_up()
          elif self.moved>0:
            self.speed_down()
        else:
          self.ballxx=1
          if self.moved>0:
            self.speed_up()
          elif self.moved<0:
            self.speed_down()
          
    else: 
      # the collision was lower
      if self.rect.centerx>=other.left-12 and self.rect.centerx<=other.right+12:
        # it was a collision with the left or right edge of the bat
        if self.rect.centerx<other.left:
          self.ballxx=-1
        else:
          self.ballxx=1

  def getrect(self):
    return self.rect

  def accel(self, mv):
    self.moved=mv

  def movepos(self, loc):
    self.rect.move_ip(loc[0], loc[1]);

  def update(self):
    self.incr=self.incr+1
    if (self.incr>=self.frame_period): # is it time for incrementing the frame?
      self.incr=0
      self.moved=self.moved*2
      if abs(self.moved)>=4:
        self.moved=0
      # update the ball position
      self.ballxincr=self.ballxincr+1
      if self.ballxincr>=self.ballxdel:
        self.ballxincr=0
        self.movepos([self.ballxx, 0])
        if self.rect.right>=screenwidth:
          self.rect.right=screenwidth
          self.ballxx=-self.ballxx
          self.movepos([self.ballxx, 0])
        elif self.rect.left<=0:
          self.rect.left=0
          self.ballxx=-self.ballxx
          self.movepos([self.ballxx, 0])
      self.ballyincr=self.ballyincr+1
      if self.ballyincr>=self.ballydel:
        self.ballyincr=0
        self.movepos([0, self.ballyy])
        if self.rect.top<=0:
          self.rect.top=0
          self.ballyy=-self.ballyy
          self.movepos([0, self.ballyy])
        if self.rect.bottom>=screenheight:
          self.rect.bottom=screenheight
          self.ballyy=-self.ballyy
          self.movepos([0, self.ballyy])

    self.image=self.frames[self.idx] 


