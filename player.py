import pygame
import logic

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Monospace',20)

infoObject = pygame.display.Info()
screen_height = infoObject.current_h
screen_width = infoObject.current_w
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((255,255,255))
pygame.display.set_caption('Music-Analyzer')


#Define Colors
red = (255,0,0)

img_playPause_x_cordinate = int(screen_width/2)-35
img_playPause_y_cordinate = int(screen_height)-140
img_playPause_size = (70,70)

#Define Images
img_play = pygame.transform.scale(pygame.image.load("images/play.png"),img_playPause_size)
img_pause = pygame.transform.scale(pygame.image.load("images/pause.png"),img_playPause_size)


done = False

""" 1 means Play and 0 means pause"""
img_PlayPause_state = 1

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    txt_isPressed = myfont.render("Song: Bijay is Awesome",False,(0,0,0))

    isPressed = logic.togglePlayPause(screen_height,screen_width)
    if isPressed:
        img_PlayPause_state = img_PlayPause_state ^ 1
    if img_PlayPause_state == 1:
        screen.blit(img_play,(img_playPause_x_cordinate,img_playPause_y_cordinate))
    else:
        screen.blit(img_pause,(img_playPause_x_cordinate,img_playPause_y_cordinate))

    screen.blit(txt_isPressed,(400,400))
    pygame.display.flip()
    pygame.display.update()


