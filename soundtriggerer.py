import pygame
import time

#initialize pygame and pygame.mixer(for audio)
pygame.init()
pygame.mixer.init(allowedchanges=0)


#define fps
fps = 60

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
x_margin = 5
y_margin = 5

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

color = pygame.Color(0, 128, 255)

#define how fast loop will be running 
clock = pygame.time.Clock()



keys = {'1':(0,0),'2':(1,0),'3':(2,0),'4':(3,0),'5':(4,0),'6':(5,0),'7':(6,0),'8':(7,0),'9':(8,0),'0':(9,0),'ß':(10,0),'´':(11,0),
        'q':(0,1),'w':(1,1),'e':(2,1),'r':(3,1),'t':(4,1),'z':(5,1),'u':(6,1),'i':(7,1),'o':(8,1),'p':(9,1),'ü':(10,1),'+':(11,1),
        '^':(0,2),'a':(1,2),'s':(2,2),'d':(3,2),'f':(4,2),'g':(5,2),'h':(6,2),'j':(7,2),'k':(8,2),'l':(9,2),'ö':(10,2),'ä':(11,2),
        '<':(0,3),'y':(1,3),'x':(2,3),'c':(3,3),'v':(4,3),'b':(5,3),'n':(6,3),'m':(7,3),',':(8,3),'.':(9,3),'-':(10,3),'#':(11,3)}



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
                                    
        self.image = pygame.Surface((49,49))
        self.image.set_alpha(128)
        self.image.fill(color)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.key = ''


    def update(self):
        if self.key:
                self.rect.move_ip((x_margin + keys[self.key][0]*(key_dim*x_gap),y_margin + keys[self.key][1]*(key_dim*y_gap)))
                print(keys[self.key])




player = Player()




#main loop
while not done:
        dt = clock.tick(fps) / 1000
        #make window black
        window.fill((0,0,0))

        #show background image
        window.blit(image, (0, 0))



        #change color variable 
        if is_blue: color = pygame.Color(0, 128, 255,10)
        else: color = pygame.Color(255, 100, 0,0)


        #check for event
        for event in pygame.event.get():
                #check for keypresses
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        
                        #move squares
                        if event.key == pygame.K_SPACE:
                                is_blue = not is_blue
                        if event.key == pygame.K_q:
                                player.key = "q"
                        if event.key == pygame.K_w:
                                player.key = "w"
                        #if event.key == pygame.K_e:
                              
                        #if event.key == pygame.K_r:
                                  
                        

        player.update()


        window.blit(player.image, player.rect)


        #set framerate to 60
        clock.tick(fps)


        #update view
        pygame.display.flip()
        
        