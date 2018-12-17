import pygame

def togglePlayPause(screen_height,screen_width):
    current_mouse_position = pygame.mouse.get_pos()
    print(current_mouse_position)

    a = int(screen_width/2)-35
    b = int(screen_height)-140

    if(current_mouse_position[0] >= a and current_mouse_position[0] <= a+70) and (current_mouse_position[1] >=b and current_mouse_position[1] <=b+70):
        if pygame.mouse.get_pressed()[0]:
            return True

    return False

