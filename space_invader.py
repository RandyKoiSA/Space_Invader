import pygame
import hub


def run_game():
    """ Main game structure that runs the whole program. """

    # Initialize pygame
    pygame.init()

    # Set up the window
    game_hub = hub.Hub()
    pygame.display.set_caption(game_hub.WINDOW_TITLE)

    while True:
        """ Game loop, as long as this true the game will run. """
        # Clear Screen
        game_hub.main_screen.fill(game_hub.BG_COLOR)

        # Decide what screen to display
        game_hub.displayscreen()

        # Display the screen onto the window
        pygame.display.flip()
        game_hub.CLOCK.tick(60)

if __name__ == '__main__':
    run_game()
