import arcade

Screen_width=700
Screen_height=800
Screen_title='Frogger'
MOVEMENT_SPEED = 5

class Frog(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > Screen_width - 1:
            self.right = Screen_width - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > Screen_height - 1:
            self.top = Screen_height - 1

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.background=None
        self.frog_list=None
        self.frog_sprite=None
    def setup(self):
        self.background = arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\tło.png")
        self.frog_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()

        self.score = 0
        self.frog_sprite = Frog(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\frog.png")
        self.frog_sprite.center_x = 50
        self.frog_sprite.center_y = 50
        self.frog_list.append(self.frog_sprite)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, Screen_width, Screen_height, self.background)
        self.frog_list.draw()



    def on_update(self, delta_time):
        self.frog_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.frog_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.frog_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.frog_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.frog_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers: int):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.frog_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.frog_sprite.change_x = 0

def main():
    window=MyGame(Screen_width,Screen_height,Screen_title)
    window.setup()
    arcade.run()
main()