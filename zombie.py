import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_ZOMBIE = 0.8
ZOMBIE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Zombie(arcade.Sprite):

    def update(self):
        self.center_x -= 1

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.zombie_list = None

    def setup(self):

        # Sprite lists
        self.zombie_list = arcade.SpriteList()

        for i in range(ZOMBIE_COUNT):

            zombie = Zombie("zombie.py", SPRITE_SCALING_ZOMBIE)

            # Position the zombie
            zombie.center_x = random.randrange(SCREEN_WIDTH)
            zombie.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the zombie to the lists
            self.zombie_list.append(zombie)


    def on_draw(self):
        arcade.start_render()
        self.zombie_list.draw()


def main(self):
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
