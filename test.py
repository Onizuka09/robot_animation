import  pygame
import time
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Blinking Eye Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define eye parameters
left_eye_center = (150, 200)
right_eye_center = (250, 200)
eye_radius = 50
pupil_radius = 20

# Define mouth parameters
mouth_rect = pygame.Rect(150, 270, 100, 50)
mouth_width = 3

def draw_eyes(open=True, look_direction="center"):
    if look_direction == "left":
        pupil_offset = (-25, 0)
    elif look_direction == "right":
        pupil_offset = (25, 0)
    else:  # center
        pupil_offset = (0, 0)
    
    if open:
        # Draw left eye open
        pygame.draw.circle(screen, BLACK, left_eye_center, eye_radius)
        pygame.draw.circle(screen, WHITE, left_eye_center, eye_radius - 5)
        pygame.draw.circle(screen, BLACK, (left_eye_center[0] + pupil_offset[0], left_eye_center[1] + pupil_offset[1]), pupil_radius)
        # Draw right eye open
        pygame.draw.circle(screen, BLACK, right_eye_center, eye_radius)
        pygame.draw.circle(screen, WHITE, right_eye_center, eye_radius - 5)
        pygame.draw.circle(screen, BLACK, (right_eye_center[0] + pupil_offset[0], right_eye_center[1] + pupil_offset[1]), pupil_radius)
    else:
        # Draw left eye closed
        pygame.draw.line(screen, BLACK, (left_eye_center[0] - eye_radius, left_eye_center[1]), (left_eye_center[0] + eye_radius, left_eye_center[1]),5 )
        # Draw right eye closed
        pygame.draw.line(screen, BLACK, (right_eye_center[0] - eye_radius, right_eye_center[1]), (right_eye_center[0] + eye_radius, right_eye_center[1]), 5)

def draw_eyebrows(expression="neutral"):
    if expression == "smiling":
        left_eyebrow_start = (110, 140)
        left_eyebrow_end = (190, 130)
        right_eyebrow_start = (210, 130)
        right_eyebrow_end = (290, 140)
    elif expression == "mad":
        left_eyebrow_start = (110, 130)
        left_eyebrow_end = (190, 140)
        right_eyebrow_start = (210, 140)
        right_eyebrow_end = (290, 130)
    elif expression == "excited":
        left_eyebrow_start = (110, 120)
        left_eyebrow_end = (190, 110)
        right_eyebrow_start = (210, 110)
        right_eyebrow_end = (290, 120)
    else:  # neutral
        left_eyebrow_start = (110, 140)
        left_eyebrow_end = (190, 140)
        right_eyebrow_start = (210, 140)
        right_eyebrow_end = (290, 140)
    
    pygame.draw.line(screen, BLACK, left_eyebrow_start, left_eyebrow_end, 5)
    pygame.draw.line(screen, BLACK, right_eyebrow_start, right_eyebrow_end, 5)

def draw_smiling_mouth(open=False):
    if open:
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(0), math.radians(180), mouth_width)
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(180), math.radians(360), mouth_width)
    else:
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(0), math.radians(180), mouth_width)

def draw_mad_mouth(open=False):
    if open:
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(180), math.radians(360), mouth_width)
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(0), math.radians(180), mouth_width)
    else:
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(180), math.radians(360), mouth_width)

def draw_neutral_mouth(open=False):
    pygame.draw.line(screen, BLACK, mouth_rect.topleft, mouth_rect.topright, mouth_width)

def draw_excited_mouth(open=False):
    if open:
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(0), math.radians(180), mouth_width)
        pygame.draw.arc(screen, BLACK, pygame.Rect(mouth_rect.left, mouth_rect.top, mouth_rect.width, mouth_rect.height * 2), math.radians(0), math.radians(180), mouth_width)
    else:
        pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(0), math.radians(180), mouth_width)

def talk(): 
    draw_smiling_mouth(True)
    time.sleep(0.3)
    draw_smiling_mouth(False) 
    time.sleep(0.3) 
def draw_face(act ="talk",expression= "neutral", eyes_open=True, look_direction="center", mouth_open=False):
    screen.fill(WHITE)
    draw_eyes(eyes_open, look_direction)
    draw_eyebrows(expression)
    if act == "talk":
        #talk()
        draw_smiling_mouth(mouth_open)
    elif act == "neutral":
        draw_neutral_mouth(mouth_open)
    elif act  == "excited":
        draw_excited_mouth(mouth_open)
    else:  # neutral
        draw_neutral_mouth(mouth_open)
   
    pygame.display.flip()


# Main loop
talking_time = 60 
stay_neutral= 10
talking_finished =False
running = True
blink_num = 2 
blink_cnt= 0 
start_time = time.time()
blink_interval = 3  # Time between blinks
last_blink_time = 0
last_openMouth= 0
eyes_open=True
mouth = True
eyes = True
blynk_period = 20
blynk_enabled =True
print(start_time)
blynk_f= False
looked = False 
looked_dir = "center"
last_look= 0
is_right=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Example usage: alternate between expressions and looking directions, with talking animation
    elapsed_time = time.time() -start_time 
    if ( ( elapsed_time  >  talking_time) and (not talking_finished))   :  
        talking_finished= True
        mouth= True
        start_time = time.time()
        elapsed_time =0
    
    if (not talking_finished):
        #if ( blink_cnt
        current_time = time.time()
        if ( current_time - blynk_period > 10):
            #eyes_open = True
            print("blynk finished")
            blynk_enabled = not blynk_enabled
            blink_cnt = 0
            blynk_period = current_time
        
        if (blynk_enabled and (blink_cnt< 4)) :
            if (current_time - last_blink_time > 0.5) and eyes_open :
                eyes_open = False 
                last_blink_time = current_time
            elif (current_time- last_blink_time > 0.1 ) and not eyes_open:
                eyes_open =True
                last_blink_time = current_time
                blynk_f = True
            if ( blynk_f): 
                blink_cnt = blink_cnt + 1
                blynk_f = False
        else:
            eyes_open = True
            looked_dir = "center"    
        """
        if not looked : 
            print("blynking .... ",blink_cnt )
            eyes_open = True
            current_time = time.time()
            if ( current_time - last_look > 0.3 )and  is_right:
                is_right = False
                last_look = current_time
            if ( is_right):
                looked_dir= "right"
            else:
                looked ="center"
         """
        if (current_time - last_openMouth > 0.3):  
            mouth= not mouth 
            last_openMouth= current_time
        
        draw_face(act = "talk" , expression="neutral", eyes_open=eyes_open, look_direction=looked_dir, mouth_open=mouth)
        #print(eyes_open) 
        #time.sleep(0.3) 
    #time.sleep(0.3)  # Mouth open duration
    else:
        if  elapsed_time > stay_neutral :
            talking_finished= False
            start_time =time.time()
        else :
            draw_face(act= "neutral", expression="talk", eyes_open=True, look_direction="center", mouth_open=True)

    #print(current_time,eyes_open)
    #draw_face(expression="neutral", eyes_open=True, look_direction="left", mouth_open=False)
    """
    draw_face(expression="mad", eyes_open=True, look_direction="right", mouth_open=True)
    time.sleep(0.3)  # Mouth open duration
    draw_face(expression="mad", eyes_open=True, look_direction="right", mouth_open=False)
    time.sleep(0.3)  # Mouth closed duration

    draw_face(expression="neutral", eyes_open=True, look_direction="center", mouth_open=True)
    time.sleep(0.3)  # Mouth open duration
    draw_face(expression="neutral", eyes_open=True, look_direction="center", mouth_open=False)
    time.sleep(0.3)  # Mouth closed duration

    draw_face(expression="excited", eyes_open=True, look_direction="center", mouth_open=True)
    time.sleep(0.3)  # Mouth open duration
    #draw_face(expression="excited", eyes_open=True, look_direction="center", mouth_open=False)
    #time.sleep(0.3)  # Mouth closed duration
    """

# Quit Pygame
pygame.quit()

