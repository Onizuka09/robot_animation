import pygame 
import time 
import math 

pygame.init()  
screen = pygame.display.set_mode((400,400)) 
pygame.display.set_caption("Robot face animation") 

WHITE= (255,255,255) 
BLACK = (0,0,0) 


left_eye_center = (150,200) 
right_eye_center = (250,200) 

eye_radius = 50  
pupil_radius  = 20 

left_eyebrow_pos = [ (110,140) , (190,140) ] 

right_eyebrow_pos =  [ (150, 300), (250, 300) ] 


mouth_rect = pygame.Rect(150,270,100,50)
mouth_width = 5 
def draw_eyes(open=True):
    if open:
        # Draw left eye open
        pygame.draw.circle(screen, BLACK, left_eye_center, eye_radius)
        pygame.draw.circle(screen, WHITE, left_eye_center, eye_radius - 10)
        pygame.draw.circle(screen, BLACK, left_eye_center, pupil_radius)
        # Draw right eye open
        pygame.draw.circle(screen, BLACK, right_eye_center, eye_radius)
        pygame.draw.circle(screen, WHITE, right_eye_center, eye_radius - 10)
        pygame.draw.circle(screen, BLACK, right_eye_center, pupil_radius)
    else:
        # Draw left eye closed
        pygame.draw.line(screen, BLACK, (100, 200), (200, 200), 20)
        # Draw right eye closed
        pygame.draw.line(screen, BLACK, (200, 200), (300, 200), 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.circle(screen,BLACK,left_eye_center, eye_radius)
    pygame.draw.circle(screen, WHITE, left_eye_center, eye_radius -5 )
    pygame.draw.circle(screen, BLACK, left_eye_center, pupil_radius)


    pygame.draw.line (screen,BLACK ,left_eyebrow_pos[0], left_eyebrow_pos[1],5  )
    # looking left 
    
    pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(180), math.radians(360), mouth_width)
        
    pygame.display.flip()
pygame.quit() 
