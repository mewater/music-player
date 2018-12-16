import pygame

pygame.init()

infoObject = pygame.display.Info()
screen_heignt = infoObject.current_h
screen_width = infoObject.current_w
screen = pygame.display.set_mode((screen_width,screen_heignt))
screen.fill((255,255,255))
pygame.display.set_caption('Music-Analyzer')


#Define Colors
red = (255,0,0)

img_playPause_x_cordinate = int(screen_width/2)-35
img_playPause_y_cordinate = int(screen_heignt)-140
img_playPause_size = (70,70)

#Define Images
img_play = pygame.transform.scale(pygame.image.load("images/play.png"),img_playPause_size)
img_pause = pygame.transform.scale(pygame.image.load("images/pause.png"),img_playPause_size)


done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(img_play,(img_playPause_x_cordinate,img_playPause_y_cordinate))
    pygame.display.flip()


