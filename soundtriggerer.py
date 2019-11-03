import pygame
import time

#initialize pygame and pygame.mixer(for audio)
pygame.init()
pygame.mixer.init(allowedchanges=0)




#load sfx
phone = pygame.mixer.Sound('files/audio.ogg')

#play sfx
#phone.play()



#load background image
image = pygame.image.load("files/keyboard.png")


#define window width to background image dimensions
width=image.get_rect()[2]
height=image.get_rect()[3]

# define offset of first key from border
x = 5
y = 5

#define gaps between keys
x_gap = 3
y_gap = 5

#define size of square keys
key_dim = 49

#define window
window = pygame.display.set_mode((width, height))

#define that we are not done jet
done = False

#Todo:rename
is_blue = True

#define how fast loop will be running 
clock = pygame.time.Clock()


keys = {'1':(1,1),'2':(2,1),'3':(3,1),'4':(4,1),'5':(5,1),'6':(6,1),'7':(7,1),'8':(8,1),'9':(9,1),'0':(10,1),'ß':(11,1),'´':(12,1),
        'q':(1,2),'w':(2,2),'e':(3,2),'r':(4,2),'t':(5,2),'z':(6,2),'u':(7,2),'i':(8,2),'o':(9,2),'p':(10,2),'ü':(11,2),'+':(12,2),
        '^':(1,3),'a':(2,3),'s':(3,3),'d':(4,3),'f':(5,3),'g':(6,3),'h':(7,3),'j':(8,3),'k':(9,3),'l':(10,3),'ö':(11,3),'ä':(12,3),
        '<':(1,4),'y':(2,4),'x':(3,4),'c':(4,4),'v':(5,4),'b':(6,4),'n':(7,4),'m':(8,4),',':(9,4),'.':(10,4),'-':(11,4),'#':(12,4),}


#main loop
while not done:

        #make window black
        window.fill((0,0,0))

        #show background image
        window.blit(image, (0, 0))


        #check for event
        for event in pygame.event.get():
                #check for keypresses
                if event.type == pygame.KEYDOWN:
                        #move squares
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
                        #draw rectangle on window                        
                        s = pygame.Surface((49,49))
                        s.set_alpha(50)
                        s.fill(color)
                        window.blit(s,(x+i*(key_dim+x_gap),y+j*(key_dim+y_gap)))

                        #pygame.draw.rect(window, color, pygame.Rect(x+i*(key_dim+x_gap), y+j*(key_dim+y_gap), 49, 49))


        #update view
        pygame.display.flip()
        
        #set framerate to 60
        clock.tick(60)