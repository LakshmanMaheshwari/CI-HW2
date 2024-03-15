import pygame
import random
import math

# Initialize Pygame
pygame.init()
pygame.mixer.init()
# Set up the screen
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 50
NUM_NUCLEI = 200
NUCLEUS_RADIUS = 10
ELECTRON_RADIUS = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.music.load("CanYouHearTheMusic.mp3")
pygame.display.set_caption("Nuclear Fission Simulation")

class Nucleus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hit = False
        self.color = RED

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), NUCLEUS_RADIUS)

class Electron:
    def __init__(self, x, y, vx, vy, init_nuc):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.inside_nucleus = init_nuc

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > WIDTH:
            self.vx = -self.vx
        if self.y < 0 or self.y > HEIGHT:
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), ELECTRON_RADIUS)

# Generate random nuclei
nuclei1 = [Nucleus(random.randint(0, WIDTH//2), random.randint(0, HEIGHT//2)) for _ in range(NUM_NUCLEI//4)]
nuclei2 = [Nucleus(random.randint(WIDTH//2, WIDTH), random.randint(0, HEIGHT//2)) for _ in range(NUM_NUCLEI//4)]
nuclei3 = [Nucleus(random.randint(0, WIDTH//2), random.randint(HEIGHT//2, HEIGHT)) for _ in range(NUM_NUCLEI//4)]
nuclei4 = [Nucleus(random.randint(WIDTH//2, WIDTH), random.randint(HEIGHT//2, HEIGHT)) for _ in range(NUM_NUCLEI//4)]
nuclei1d = nuclei1.copy()
nuclei2d = nuclei2.copy()
nuclei3d = nuclei3.copy()
nuclei4d = nuclei4.copy()
n1 = [i for i in range(len(nuclei1))]
n2 = [i for i in range(len(nuclei2))]
n3 = [i for i in range(len(nuclei3))]
n4 = [i for i in range(len(nuclei4))]

electrons = []
pygame.mixer.music.play()

running = True
while running and pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not electrons:
            x, y = pygame.mouse.get_pos()
            magnitudex = random.randint(4,5)*0.2
            signx = random.randint(1,2)
            magnitudey = random.randint(4,5)*0.2
            signy = random.randint(1,2)
            electrons.append(Electron(x, y, ((-1)**signx)*magnitudex, ((-1)**signy)*magnitudey, False))

    # Check for collisions with nuclei
    for electron in electrons[:]:
        electron.move()
        hit = False
        if 0 <= electron.x < WIDTH//2 and 0 <= electron.y < HEIGHT//2:
            for i in n1:
                nucleus = nuclei1[i]
                distance = math.sqrt((electron.x - nucleus.x)**2 + (electron.y - nucleus.y)**2)
                if distance < NUCLEUS_RADIUS + ELECTRON_RADIUS:
                    # Remove collided electron
                    hit = True
                    
                    if not(electron.inside_nucleus) and not(nucleus.hit):
                        nucleus.hit = True
                        nuclei1d[i].color = PINK
                        # nuclei1.pop(i)
                        n1.remove(i)

                        electrons.remove(electron)
                    
                    # Emit 3 new electrons from the nucleus
                        for _ in range(3):
                            #new_electron_x = 
                            #new_electron_y = 
                            new_electron = Electron(nucleus.x, nucleus.y, random.uniform(-0.3, 0.3), random.uniform(-0.3, 0.3), True)
                            electrons.append(new_electron)
                        break
        elif WIDTH//2 <= electron.x <= WIDTH and 0 <= electron.y < HEIGHT//2:
            for i in n2:
                nucleus = nuclei2[i]
                distance = math.sqrt((electron.x - nucleus.x)**2 + (electron.y - nucleus.y)**2)
                if distance < NUCLEUS_RADIUS + ELECTRON_RADIUS:
                    # Remove collided electron
                    hit = True
                    
                    if not(electron.inside_nucleus) and not(nucleus.hit):
                        nucleus.hit = True
                        nuclei2d[i].color = PINK
                        # nuclei2.pop(i)
                        n2.remove(i)
                        electrons.remove(electron)
                    
                    # Emit 3 new electrons from the nucleus
                        for _ in range(3):
                            #new_electron_x = 
                            #new_electron_y = 
                            new_electron = Electron(nucleus.x, nucleus.y, random.uniform(-0.3, 0.3), random.uniform(-0.3, 0.3), True)
                            electrons.append(new_electron)
                        break
        elif 0 <= electron.x < WIDTH//2 and HEIGHT//2 <= electron.y <= HEIGHT:
            for i in n3:
                nucleus = nuclei3[i]
                distance = math.sqrt((electron.x - nucleus.x)**2 + (electron.y - nucleus.y)**2)
                if distance < NUCLEUS_RADIUS + ELECTRON_RADIUS:
                    # Remove collided electron
                    hit = True
                    
                    
                    if not(electron.inside_nucleus) and not(nucleus.hit):
                        nucleus.hit = True
                        nuclei3d[i].color = PINK
                        # nuclei3.pop(i)
                        n3.remove(i)
                        electrons.remove(electron)
                    
                    # Emit 3 new electrons from the nucleus
                        for _ in range(3):
                            #new_electron_x = 
                            #new_electron_y = 
                            new_electron = Electron(nucleus.x, nucleus.y, random.uniform(-0.3, 0.3), random.uniform(-0.3, 0.3), True)
                            electrons.append(new_electron)
                        break
        elif WIDTH//2 <= electron.x <= WIDTH and HEIGHT//2 <= electron.y <= HEIGHT:
            for i in n4:
                nucleus = nuclei4[i]
                distance = math.sqrt((electron.x - nucleus.x)**2 + (electron.y - nucleus.y)**2)
                if distance < NUCLEUS_RADIUS + ELECTRON_RADIUS:
                    # Remove collided electron
                    hit = True
                    
                    if not(electron.inside_nucleus) and not(nucleus.hit):
                        nucleus.hit = True

                        nuclei4d[i].color = PINK
                        # nuclei4.pop(i)
                        n4.remove(i)
                        electrons.remove(electron)
                    
                    # Emit 3 new electrons from the nucleus
                        for _ in range(3):
                            #new_electron_x = 
                            #new_electron_y = 
                            new_electron = Electron(nucleus.x, nucleus.y, random.uniform(-0.3, 0.3), random.uniform(-0.3, 0.3), True)
                            electrons.append(new_electron)
                        break
            
        
        if hit == False:
            electron.inside_nucleus = False

    screen.fill(WHITE)
    for nucleus in nuclei1d:
        nucleus.draw()
    for nucleus in nuclei2d:
        nucleus.draw()
    for nucleus in nuclei3d:
        nucleus.draw()
    for nucleus in nuclei4d:
        nucleus.draw()
    for electron in electrons:
        electron.draw()

    
    pygame.display.flip()

pygame.quit()
