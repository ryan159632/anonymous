#!c:/Python27/python.exe
import pygame, sys

screen_width = 1024
old_width = screen_width
new_width = screen_width
screen_height = 768
old_height = screen_height
new_height = screen_width

pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  
    if event.type == pygame.VIDEORESIZE:
      new_width = event.w
      new_height = event.h
 
  if old_width != new_width or old_height != new_height:
    print '({0}, {1})'.format(new_width, new_height)
    old_width = new_width
    old_height = new_height
