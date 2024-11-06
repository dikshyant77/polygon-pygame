import pygame

pygame.init()
window =pygame.display.set_mode((650,650))
window.fill((255,255,255))

GREEN = (0,255,0)
trianglepoints = [(325, 100), (200, 400), (450, 400)] 
pygame.draw.polygon(window, GREEN, trianglepoints)
pygame.display.update()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.flip()

pygame.quit()