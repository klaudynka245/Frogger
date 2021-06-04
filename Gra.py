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
    def __init__(self,img,scale,hit_box_algorithm: str = "Detailed"):
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
    def __init__(self,img,scale,hit_box_algorithm: str = "Detailed"):
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

class Lily(arcade.Sprite):
    def __init__(self,img,scale,hit_box_algorithm: str = "Detailed"):
        super().__init__(img,scale=scale)
        self.size=0
        self.speed = 0.5 + DIFFICULTY
    def update(self):
        super().update()
        if self.center_x > 720:
            self.center_x = -10
        self.center_x += self.speed

class Log(arcade.Sprite):
    def __init__(self,img,scale, hit_box_algorithm: str = "Detailed"):
        super().__init__(img,scale=scale)
        self.size=0
        self.speed = -(0.5 + DIFFICULTY)
    def update(self):
        super().update()
        if self.center_x < -50:
            self.center_x = 750
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
        self.lilies_list = arcade.SpriteList()
        self.logs_list = arcade.SpriteList()

        self.score = 0
        self.frog_sprite = Frog(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\frog.png",scale=0.18)
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

        self.lily1 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png",scale=0.15)
        self.lily1.center_x = 600
        self.lily1.center_y = 360
        self.lilies_list.append(self.lily1)

        self.lily2 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily2.center_x = 550
        self.lily2.center_y = 360
        self.lilies_list.append(self.lily2)

        self.lily3 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily3.center_x = 200
        self.lily3.center_y = 360
        self.lilies_list.append(self.lily3)

        self.lily4 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily4.center_x = 250
        self.lily4.center_y = 360
        self.lilies_list.append(self.lily4)

        self.lily5 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily5.center_x = 400
        self.lily5.center_y = 360
        self.lilies_list.append(self.lily5)

        self.lily6 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily6.center_x = 100
        self.lily6.center_y = 360
        self.lilies_list.append(self.lily6)

        self.lily7 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily7.center_x = 450
        self.lily7.center_y = 435
        self.lilies_list.append(self.lily7)

        self.lily8 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily8.center_x = 550
        self.lily8.center_y = 435
        self.lilies_list.append(self.lily8)

        self.lily9 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily9.center_x = 150
        self.lily9.center_y = 435
        self.lilies_list.append(self.lily9)

        self.lily10 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily10.center_x = 300
        self.lily10.center_y = 435
        self.lilies_list.append(self.lily10)

        self.lily11 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily11.center_x = 250
        self.lily11.center_y = 435
        self.lilies_list.append(self.lily11)

        self.lily12 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily12.center_x = 300
        self.lily12.center_y = 475
        self.lilies_list.append(self.lily12)

        self.lily13 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily13.center_x = 600
        self.lily13.center_y = 475
        self.lilies_list.append(self.lily13)

        self.lily14 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily14.center_x = 650
        self.lily14.center_y = 475
        self.lilies_list.append(self.lily14)

        self.lily15 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily15.center_x = 150
        self.lily15.center_y = 475
        self.lilies_list.append(self.lily15)

        self.lily16 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily16.center_x = 50
        self.lily16.center_y = 475
        self.lilies_list.append(self.lily16)

        self.lily17 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily17.center_x = 350
        self.lily17.center_y = 475
        self.lilies_list.append(self.lily17)

        self.lily18 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily18.center_x = 450
        self.lily18.center_y = 475
        self.lilies_list.append(self.lily18)

        self.lily19 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily19.center_x = 500
        self.lily19.center_y = 475
        self.lilies_list.append(self.lily19)

        self.log = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log.center_x = 380
        self.log.center_y = 365
        self.logs_list.append(self.log)

        self.log2 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log2.center_x = 545
        self.log2.center_y = 365
        self.logs_list.append(self.log2)

        self.log3 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log3.center_x = 100
        self.log3.center_y = 365
        self.logs_list.append(self.log3)

        self.log4 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log4.center_x = 380
        self.log4.center_y = 440
        self.logs_list.append(self.log4)

        self.log5 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log5.center_x = 550
        self.log5.center_y = 440
        self.logs_list.append(self.log5)

        self.log6 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log6.center_x = 280
        self.log6.center_y = 555
        self.logs_list.append(self.log6)

        self.log7 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log7.center_x = 50
        self.log7.center_y = 555
        self.logs_list.append(self.log7)

        self.log8 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log8.center_x = 580
        self.log8.center_y = 555
        self.logs_list.append(self.log8)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.car_list.draw()
        self.lilies_list.draw()
        self.logs_list.draw()
        self.frog_list.draw()


    def on_update(self, delta_time):
        self.frog_list.update()
        self.car_list.update()
        self.lilies_list.update()
        self.logs_list.update()
        if arcade.check_for_collision_with_list(self.frog_sprite,self.car_list):
            arcade.play_sound(self.crash_sound)
            self.frog_sprite.center_x = 350
            self.frog_sprite.center_y = 50
            self.lives -=1
        for lily in self.lilies_list:
            if arcade.check_for_collision(self.frog_sprite,lily):
                self.frog_sprite.center_x += lily.speed
        for log in self.logs_list:
            if arcade.check_for_collision(self.frog_sprite,log):
                self.frog_sprite.center_x += log.speed

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