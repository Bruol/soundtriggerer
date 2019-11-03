import pygame


pygame.init()
pygame.mixer.init(allowedchanges=0)



phone = pygame.mixer.Sound('files/audio.ogg')
phone.play()

pygame.init()
screen = pygame.display.set_mode((500, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()