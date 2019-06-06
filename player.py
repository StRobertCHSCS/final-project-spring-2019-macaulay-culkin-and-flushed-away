import arcade
import os

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Constants
movement_speed = 3
os.system("afplay gunload.aiff&")

class Zombie(arcade.Sprite):

    def update(self):
        self.center_x -= 1

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT

class Player():
    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.player_list = arcade.SpriteList
        self.player_sprite = arcade.Sprite("Soldier.gif")
        self.sound = arcade.load_sound("gunshot.wav")
        self.sound = arcade.load_sound("reload.wav")

    def draw(self):
        player_image = arcade.load_texture("Soldier.gif")
        scale = 0.4
        arcade.draw_texture_rectangle(self.position_x, self.position_y, scale * player_image.width,
                                      scale * player_image.height, player_image, 1)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.player = Player(100, 225, 0, 0)

    def on_draw(self):
        arcade.start_render()

        arcade.set_background_color(arcade.color.GRAY)
        arcade.draw_circle_filled(50, 599.9, 10, arcade.color.YELLOW)

        self.player.draw()

    def update(self, delta_time):
        self.player.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player.change_y = movement_speed
        if self.player.position_x >= 0 or self.player.position_x <= 800:
            if key == arcade.key.A:
                self.player.change_x = -movement_speed
        if key == arcade.key.S:
            self.player.change_y = -movement_speed
        if key == arcade.key.D:
            self.player.change_x = movement_speed
        if key == arcade.key.SPACE:
            os.system("afplay gunshot.wav&")
        if key == arcade.key.R:
            os.system("afplay reload.wav&")

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player.change_y = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0


def main():
    window = MyGame()
    arcade.run()


main()
