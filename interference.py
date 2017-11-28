#!/usr/bin/python3
#############################################
# Interference - a game - interference.py
# rev 1
#############################################

#import modules
import sys
import pygame
from pygame.locals import *
from background import Background
from ball import Ball
from bat import Bat

#some definitions
screenwidth=320
screenheight=200
btn_left=K_o
btn_right=K_p

###########  main function  ##################
def main():
  pygame.init()
  pygame.display.set_caption('Interference');
  pygame.key.set_repeat(10,10) # keypresses to auto-repeat every 10msec
  rects=[] # create a list

  screen=pygame.display.set_mode((screenwidth, screenheight))
  background=Background("assets/level1-stage.gif", [0,0])
  bgsurface=pygame.Surface(screen.get_size())
  bgsurface=bgsurface.convert() # speeds up blitting
  bgsurface.fill([0,0,255]) # set background to blue
  # if we only use a portion of the background image, change the first two values here:
  bgsurface.blit(background.image.subsurface(0,0,screenwidth,screenheight), (0,0))
  screen.blit(bgsurface, (0,0)) # get the bgsurface onto the screen surface
  pygame.display.update() # update the entire display

  # instantiate the sprites
  ball_sprite=Ball()
  bat_sprite=Bat()

  # store all sprite rects we create into this list
  rects.append(ball_sprite.getrect())
  rects.append(bat_sprite.getrect())

  balls_group=pygame.sprite.Group(ball_sprite)
  characters_group=pygame.sprite.Group(bat_sprite)

  while True: # this is a forever loop
    ev=pygame.event.poll()
    if ev.type==pygame.QUIT:
        pygame.quit()
        sys.exit(0)

    batmoved=0
    if ev.type==KEYDOWN: # button pressed?
      if (ev.key==btn_left):
        batloc=[-1,0]
        bat_sprite.movepos(batloc)
        ball_sprite.accel(-1) # influence ball speed if needed
        batmoved=-1
      elif (ev.key==btn_right):
        batloc=[1,0]
        bat_sprite.movepos(batloc)
        ball_sprite.accel(1) # influence ball speed if needed
        batmoved=1

    # check for collisions
    collide=pygame.sprite.collide_rect(bat_sprite, ball_sprite)
    if collide:
       ball_sprite.collision(bat_sprite.getrect(), batmoved)

    # clear the sprite(s) and then update and redraw them
    characters_group.clear(screen, bgsurface)
    balls_group.clear(screen, bgsurface)
    characters_group.update()
    balls_group.update()
    characters_group.draw(screen)
    balls_group.draw(screen)

    pygame.display.update(rects)

###########  end of main function  ###########

if __name__=="__main__":
  main()


