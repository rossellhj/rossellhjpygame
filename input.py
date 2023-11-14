import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Input Example")


font = pygame.font.Font(None, 36)

# Create a text input field
text = ""
text_input_rect = pygame.Rect(100, 100, 400, 50)
active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), text_input_rect, 2)
    if active:
        pygame.draw.rect(screen, (200, 200, 200), text_input_rect)

    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (text_input_rect.x + 5, text_input_rect.y + 5))

    pygame.display.flip()
