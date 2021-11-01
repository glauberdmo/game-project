"""
Platformer Game
"""

import arcade
import arcade.gui
from Interface.OptionsDialog import OptionsDialog

# Constants
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Platformer"
FULL_SCREEN = False

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,FULL_SCREEN)
        arcade.set_background_color((20, 20, 20))

        self.textOptions =[]
        self.NavigationBox = None
        self.shape_list = None
        self.textBox = None
        
        

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.textOptions.append("Start Game")
        self.textOptions.append("Options")
        self.textOptions.append("Exit")

        self.NavigationBox = OptionsDialog(self.textOptions, 300,500,600,100,10)

        print(self.NavigationBox.get_colors())
        self.shape = arcade.create_rectangles_filled_with_colors(self.NavigationBox.get_points(),self.NavigationBox.get_colors())
        
        self.shape_list = arcade.ShapeElementList()
        self.shape_list.append(self.shape)

        self.textBox = arcade.gui.UIInputText(0,0,300,100,text_color=arcade.color.WHITE)
    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here
        self.shape_list.draw()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()  