#!/usr/bin/python3
import pygame
import time

#initialize pygame and pygame.mixer(for audio)
pygame.init()
pygame.mixer.init(allowedchanges=0)

sfx = pygame.mixer.music



#define fps
fps = 60
#load background image
image = pygame.image.load("files/keyboard.png")
#define window width to background image dimensions
width=image.get_rect()[2]
height=image.get_rect()[3]

#define window
window = pygame.display.set_mode(flags=pygame.FULLSCREEN)

w,h = pygame.display.get_surface().get_size()

param = w/width

# define offset of first key from border
x_margin = param * 5
y_margin = param * 5
#define gaps between keys
x_gap = param * 3
y_gap = param * 5
#define size of square keys
key_dim = param * 49

#define that we are not done jet
done = False

#Todo:rename
is_muted = False

color = pygame.Color(0, 128, 255)

#define how fast loop will be running 
clock = pygame.time.Clock()


myfont = pygame.font.SysFont("Noto Sans",int(param*9),True)


keys = {'1':(0,0),'2':(1,0),'3':(2,0),'4':(3,0),'5':(4,0),'6':(5,0),'7':(6,0),'8':(7,0),'9':(8,0),'0':(9,0),'ß':(10,0),'´':(11,0),
        'q':(0,1),'w':(1,1),'e':(2,1),'r':(3,1),'t':(4,1),'z':(5,1),'u':(6,1),'i':(7,1),'o':(8,1),'p':(9,1),'ü':(10,1),'+':(11,1),
        '^':(0,2),'a':(1,2),'s':(2,2),'d':(3,2),'f':(4,2),'g':(5,2),'h':(6,2),'j':(7,2),'k':(8,2),'l':(9,2),'ö':(10,2),'ä':(11,2),
        '<':(0,3),'y':(1,3),'x':(2,3),'c':(3,3),'v':(4,3),'b':(5,3),'n':(6,3),'m':(7,3),',':(8,3),'.':(9,3),'-':(10,3),'#':(11,3)}



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (color)                     
        self.image = pygame.Surface((key_dim,key_dim))
        self.image.set_alpha(0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.key = ''


    def update(self):
        if self.key :
                self.image.fill(self.color)
                self.image.set_alpha(128)
                self.rect = ((x_margin + keys[self.key][0]*(key_dim+x_gap),y_margin + keys[self.key][1]*(key_dim+y_gap)),(key_dim,key_dim))
        else:
                self.image.set_alpha(0)


player = Player()

dt_prev = 0

sounds = {'q':'phone','w':'door','e':'break','r':'durch_fr','t':'durch_sa','z':'inter...','u':'klass...','i':'somm...'}
#main loop
while not done:
        dt = clock.tick(fps) / 1000


        
        #make window black
        window.fill((0,0,0))

        #show background image

        window.blit(pygame.transform.scale(image,(int(param*width),int(param*height))), (0, 0))
        
        
        #write text
        for element in sounds:
                label = myfont.render(sounds[element],1,(255,255,255))

                window.blit(label, (  5 + x_margin + keys[element][0]*(key_dim + x_gap)  , param*30+y_margin + keys[element][1]*(key_dim + y_gap)  ))




        #change color variable 
        if is_muted: player.color = pygame.Color(0, 128, 255,10)
        else: player.color = pygame.Color(255, 100, 0,0)




        #check for event
       


        for event in pygame.event.get():
                #check for keypresses
                if event.type == pygame.QUIT:
                       done = True
                
                if event.type == pygame.KEYDOWN:
                     
                        if event.key == pygame.K_SPACE:
                               is_muted = not is_muted
                        
                        
                        if event.key == pygame.K_q:
                                player.key = "q"

                                sfx.load('files/phone_ring.ogg')
                                sfx.play(0)
                                
                        if event.key == pygame.K_w:
                                player.key = "w"

                                sfx.load('files/door_bell.ogg')
                                sfx.play(0)
                        if event.key == pygame.K_e:
                                player.key = "e"

                                sfx.load('files/break_bell.ogg')
                                sfx.play(0)
                              
                        if event.key == pygame.K_r:     
                                player.key = "r"

                                sfx.load('files/durchsage_freitag.ogg')
                                sfx.play(0)
                        if event.key == pygame.K_t:     
                                player.key = "t"

                                sfx.load('files/durchsage_samstag.ogg')
                                sfx.play(0)
                        if event.key == pygame.K_z:     
                                player.key = "z"

                                sfx.load('files/intermezzo_sommernachtstraum.ogg')
                                sfx.play(0)  
                        if event.key == pygame.K_u:     
                                player.key = "u"

                                sfx.load('files/klassenzimmerloops.ogg')
                                sfx.play(0)
                        if event.key == pygame.K_i:     
                                player.key = "i"

                                sfx.load('files/sommernachtstraum.ogg')
                                sfx.play(0)
                        # if event.key == pygame.K_o:     
                        #         player.key = "r"

                        #         sfx.load('files/durchsage_freitag.ogg')
                        #         sfx.play(0)
                        # if event.key == pygame.K_p:     
                        #         player.key = "r"

                        #         sfx.load('files/durchsage_freitag.ogg')
                        #         sfx.play(0)     
                        if event.key == pygame.K_ESCAPE:     
                                done = True

        if sfx.get_busy() == 0:
                if not is_muted:
                        player.key =  "" 
                if is_muted:
                        time.sleep(1)
                        player.key = ""   
                                  
        if is_muted and sfx.get_busy() == 1:
                sfx.pause()
        elif not is_muted :
                sfx.unpause()
        
       

        player.update()


        window.blit(player.image, player.rect)


        #set framerate to 60
        clock.tick(fps)

        #update view
        pygame.display.flip()
        
        
