"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"
FULL_SCREEN = True

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,FULL_SCREEN)

        arcade.set_background_color((20, 20, 20))

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass        

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()  