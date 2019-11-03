import pygame
import time

#initialize pygame and pygame.mixer(for audio)
pygame.init()
pygame.mixer.init(allowedchanges=0)

#load sfx
phone = pygame.mixer.Sound('files/audio.ogg')

#play sfx
#phone.play()

image = pygame.image.load("files/keyboard.png")

width=image.get_rect()[2]
height=image.get_rect()[3]

x = 5
y = 5

x_gap = 3
y_gap = 5

key_dim = 49

#define screen
screen = pygame.display.set_mode((width, height))
done = False

is_blue = True

clock = pygame.time.Clock()


#main loop
while not done:
        screen.fill((0,0,0))
        #SHOW BACKGROUND IMAGE 
        screen.blit(image, (0, 0))


        #check for event
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                is_blue = not is_blue
                        if event.key == pygame.K_UP:
                                y -= 1
                        if event.key == pygame.K_DOWN:
                                y += 1
                        if event.key == pygame.K_LEFT:
                                x -= 1
                        if event.key == pygame.K_RIGHT:
                                x += 1
                if event.type == pygame.QUIT:
                        done = True

        #change color variable 
        if is_blue: color = pygame.Color(0, 128, 255,10)
        else: color = pygame.Color(255, 100, 0,0)

        for j in range(4):
                for i in range(12):
                        #draw rectangle on screen                        
                        s = pygame.Surface((49,49))
                        s.set_alpha(50)
                        s.fill(color)
                        screen.blit(s,(x+i*(key_dim+x_gap),y+j*(key_dim+y_gap)))

                        #pygame.draw.rect(screen, color, pygame.Rect(x+i*(key_dim+x_gap), y+j*(key_dim+y_gap), 49, 49))


        #update view
        pygame.display.flip()
        
        #set framerate to 60
        clock.tick(60)