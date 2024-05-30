import pygame
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

def draw_eyes(open=True):
    if open:
        # Draw left eye open
        pygame.draw.circle(screen, BLACK, left_eye_center, eye_radius)
        pygame.draw.circle(screen, WHITE, left_eye_center, eye_radius - 5)
        pygame.draw.circle(screen, BLACK, left_eye_center, pupil_radius)
        # Draw right eye open
        pygame.draw.circle(screen, BLACK, right_eye_center, eye_radius)
        pygame.draw.circle(screen, WHITE, right_eye_center, eye_radius - 5)
        pygame.draw.circle(screen, BLACK, right_eye_center, pupil_radius)
    else:
        # Draw left eye closed
        pygame.draw.line(screen, BLACK, (100, 200), (200, 200), 5)
        # Draw right eye closed
        pygame.draw.line(screen, BLACK, (200, 200), (300, 200), 5)

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
    else:  # neutral
        left_eyebrow_start = (110, 140)
        left_eyebrow_end = (190, 140)
        right_eyebrow_start = (210, 140)
        right_eyebrow_end = (290, 140)
    
    pygame.draw.line(screen, BLACK, left_eyebrow_start, left_eyebrow_end, 5)
    pygame.draw.line(screen, BLACK, right_eyebrow_start, right_eyebrow_end, 5)

def draw_smiling_mouth():
    pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(0), math.radians(180), mouth_width)

def draw_mad_mouth():
    pygame.draw.arc(screen, BLACK, mouth_rect, math.radians(180), math.radians(360), mouth_width)

def draw_neutral_mouth():
    pygame.draw.line(screen, BLACK, mouth_rect.topleft, mouth_rect.topright, mouth_width)

def draw_face(expression="neutral", eyes_open=True):
    screen.fill(WHITE)
    draw_eyes(eyes_open)
    draw_eyebrows(expression)
    if expression == "smiling":
        draw_smiling_mouth()
    elif expression == "mad":
        draw_mad_mouth()
    else:  # neutral
        draw_neutral_mouth()
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """
    # Example usage: alternate between expressions
    draw_face(expression="smiling", eyes_open=True)
    time.sleep(0.5)  # Eye open duration
    draw_face(expression="smiling", eyes_open=False)
    time.sleep(0.1)  # Blink duration

    draw_face(expression="mad", eyes_open=True)
    time.sleep(0.5)  # Eye open duration
    draw_face(expression="mad", eyes_open=False)
    time.sleep(0.1)  # Blink duration
    """
    draw_face(expression="neutral", eyes_open=True)
    time.sleep(0.5)  # Eye open duration
    draw_face(expression="neutral", eyes_open=False)
    time.sleep(0.1)  # Blink duration

# Quit Pygame
pygame.quit()

