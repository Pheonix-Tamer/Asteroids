import pygame
import pygame_gui
import pygame_gui.elements.ui_text_box
import pygame_gui.ui_manager
from constants import * # NOQA
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Starting Info
    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}") 
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    # Initialise Pygame and its surface
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    
    ui_manager = pygame_gui.UIManager(screen_size)
    
    # Groups Declaration
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    # declare a clock object and instantiate the player in the centre of the screen
    clock = pygame.time.Clock()
    dt = 0 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    score = 0

    score_text = pygame_gui.elements.ui_text_box.UITextBox(
        html_text=f"Score: <effect id=score_effect>{score}</effect>",
        relative_rect=pygame.Rect(10, 10, 200, 50),
        manager=ui_manager
    )
    

    # Main Game Loop
    while(True):
        # Event Checks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # Check for the UI manager to update the UI
            ui_manager.process_events(event)
        
        # for obj in updatable:
        #     obj.update(dt)
        updatable.update(dt)
        ui_manager.update(dt)
        
        # Check for collisions between an asteroid and a player
        for ast in asteroids:
            if ast.collisionCheck(player):
                print("Game Over!")
                print(f"Your Score was: {score}")
                pygame.QUIT
                quit()
            # Check for a collision between a shot and an asteroid.
            for shot in shots:
                if ast.collisionCheck(shot):
                    ast.split()
                    shot.kill()
                    score += 1
                    score_text.set_text(f"Score: <effect id=score_effect>{score}</effect>")
                    score_text.set_active_effect(pygame_gui.TEXT_EFFECT_EXPAND_CONTRACT, effect_tag="score_effect")

            
        screen.fill("black")

        # drawable.draw(screen) # This will be for a later thing when we add image and Rect
        for obj in drawable:
            obj.draw(screen)
        
        ui_manager.draw_ui(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()