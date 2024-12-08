import pygame
from constants import * # NOQA
from player import Player

def main():
    # Starting Info
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 
    
    # Initialise Pygame and its surface
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Groups Declaration
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # declare a clock object and instantiate the player in the centre of the screen
    clock = pygame.time.Clock()
    dt = 0 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        screen.fill("black")

        # drawable.draw(screen) # This will be for a later thing when we add image and Rect
        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()