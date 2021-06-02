import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Frogger'
MOVEMENT_SPEED = 5
LEFT_LIMIT = 0
DIFFICULTY = 1
LIVES = 3


class Frog(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Carleft(arcade.Sprite):
    def __init__(self,img,scale):
        super().__init__(img,scale=scale)
        self.size=0
        self.speed = -(2 + DIFFICULTY)
    def update(self):
        super().update()
        if self.center_x < 0:
            self.center_x = 5
            self.speed *= -1
            self.append_texture(
                arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkieprawo.png"))
            self.set_texture(1)
        elif self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
            self.speed *= -1
            self.append_texture(
                arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkie.png"))
            self.set_texture(2)
        self.center_x += self.speed

class Carright(arcade.Sprite):
    def __init__(self,img,scale):
        super().__init__(img,scale=scale)
        self.size=0
        self.speed = 2 + DIFFICULTY
    def update(self):
        super().update()
        if self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
            self.speed *= -1
            self.append_texture(
                arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkie.png"))
            self.set_texture(1)
        elif self.center_x < 0:
            self.append_texture(
                arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkieprawo.png"))
            self.set_texture(2)
            self.center_x = 5
            self.speed *= -1

        self.center_x += self.speed

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.background=None
        self.frog_list=None
        self.frog_sprite=None
        self.lives = LIVES
    def setup(self):
        self.background = arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\tło.png")
        self.crash_sound = arcade.load_sound(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\dźwięki\PiskOpon.mp3")

        self.frog_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()

        self.score = 0
        self.frog_sprite = Frog(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\frog.png",scale=0.3)
        self.frog_sprite.center_x = 350
        self.frog_sprite.center_y = 50
        self.frog_list.append(self.frog_sprite)

        self.car_left_sprite = Carleft(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkie.png",scale=0.3)
        self.car_left_sprite.center_x = 650
        self.car_left_sprite.center_y = 220
        self.car_list.append(self.car_left_sprite)

        self.car_left_sprite2 = Carleft(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkie.png",scale=0.3)
        self.car_left_sprite2.center_x = 250
        self.car_left_sprite2.center_y = 180
        self.car_list.append(self.car_left_sprite2)

        self.car_right_sprite = Carright(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkieprawo.png",scale=0.3)
        self.car_right_sprite.center_x = 30
        self.car_right_sprite.center_y = 150
        self.car_list.append(self.car_right_sprite)

        self.car_right_sprite2 = Carright(
            r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\autoszybkieprawo.png", scale=0.3)
        self.car_right_sprite2.center_x = 450
        self.car_right_sprite2.center_y = 120
        self.car_list.append(self.car_right_sprite2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.frog_list.draw()
        self.car_list.draw()



    def on_update(self, delta_time):
        self.frog_list.update()
        self.car_list.update()
        if arcade.check_for_collision_with_list(self.frog_sprite,self.car_list):
            arcade.play_sound(self.crash_sound)
            self.frog_sprite.center_x = 350
            self.frog_sprite.center_y = 50
            self.lives -=1


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
    window=MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    arcade.run()
main()