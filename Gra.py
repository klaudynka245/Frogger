import arcade
import arcade.gui


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Frogger'
MOVEMENT_SPEED = 5
DIFFICULTY = 1
LIVES = 3


#class GameButton(arcade.gui.UIFlatButton):
#    def on_click(self):
#        game_view = GameView()
#        game_view.setup()
#        MyGame().window.show_view(game_view)
#        arcade.run()

#class InstructionButton(arcade.gui.UIFlatButton):
#    def on_click(self):
#        insview = InstructionView()
#        MyGame().show_view(insview)
#        arcade.run()

#class ExitButton(arcade.gui.UIFlatButton):
#    def on_click(self):
#        Menu.close()

#class MyView(arcade.View):
#    def __init__(self):
#        super().__init__()
#        self.ui_manager = UIManager()
#    def on_draw(self):
#        arcade.start_render()
#    def on_show_view(self):
#        self.setup()
#        arcade.set_background_color(arcade.color.BLACK)
#    def on_hide_view(self):
#        self.ui_manager.unregister_handlers()
#    def setup(self):
#        self.ui_manager.purge_ui_elements()
#        y_slot = self.window.height // 4
#        left_column_x = self.window.width // 4
#        right_column_x = 3 * self.window.width // 4

#        button = GameButton('Start Game', center_x=120, center_y= 300, width = 250)
#        self.ui_manager.add_ui_element(button)

#        button = InstructionButton('Instruction',center_x=120, center_y=100)
#        self.ui_manager.add_ui_element(button)

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
        super().__init__(img,scale=scale,hit_box_algorithm= "Detailed")
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
        super().__init__(img,scale=scale,hit_box_algorithm= "Detailed")
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
    def __init__(self,img,scale):
        super().__init__(img,scale=scale,hit_box_algorithm= "Detailed")
        self.size=0
        self.speed = 0.1 + DIFFICULTY
    def update(self):
        super().update()
        if self.center_x > 720:
            self.center_x = -10
        self.center_x += self.speed

class Log(arcade.Sprite):
    def __init__(self,img,scale):
        super().__init__(img,scale=scale,hit_box_algorithm= "Detailed")
        self.size=0
        self.speed = -(0.2 + DIFFICULTY)
    def update(self):
        super().update()
        if self.center_x < -70:
            self.center_x = 770
        self.center_x += self.speed

class Flower(arcade.Sprite):
    def __init__(self,img,scale):
        super().__init__(img,scale=scale)

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Menu', SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text('Click g to start the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text('Click i for the instruction', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 125,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text('Click l to see the leaderboard', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 175,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text('Click esc to exit', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 225,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
    def on_key_press(self, key, modifiers):
        if key == arcade.key.G:
            view = GameView()
            view.setup()
            self.window.show_view(view)
        elif key == arcade.key.I:
            view = InstructionView()
            self.window.show_view(view)


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_GREEN)
        arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instruction Screen", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=50, anchor_x='center')
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            menu_view = MenuView()
            self.window.show_view(menu_view)

class GameOverView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\gameover.jpg")
        arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT)
    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background=None
        self.frog_list=None
        self.frog_sprite=None
        self.lives = LIVES
        self.score = 0
    def setup(self):
        self.window.set_mouse_visible(False)
        self.background = arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\tło.png")
        self.crash_sound = arcade.load_sound(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\dźwięki\PiskOpon.mp3")
        self.gameover_sound = arcade.load_sound(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\dźwięki\GameOver.mp3")
        self.win_sound = arcade.load_sound(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\dźwięki\Wygrana.mp3")
        self.water_sound = arcade.load_sound(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\dźwięki\PluskWody.mp3")
        self.bell_sound = arcade.load_sound(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\dźwięki\Bell.mp3")

        self.frog_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()
        self.lilies_list = arcade.SpriteList()
        self.flowers_list = arcade.SpriteList()
        self.logs_list = arcade.SpriteList()

        self.time = 100
        self.score = 0
        self.frog_sprite = Frog(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\frog.png",scale=0.16)
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
        self.lily7.center_x = 50
        self.lily7.center_y = 435
        self.lilies_list.append(self.lily7)

        self.lily8 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily8.center_x = 500
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
        self.lily11.center_x = 600
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

        self.lily20 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily20.center_x = 500
        self.lily20.center_y = 550
        self.lilies_list.append(self.lily20)

        self.lily21 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily21.center_x = 300
        self.lily21.center_y = 550
        self.lilies_list.append(self.lily21)

        self.lily22 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily22.center_x = 100
        self.lily22.center_y = 550
        self.lilies_list.append(self.lily22)

        self.lily23 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily23.center_x = 150
        self.lily23.center_y = 550
        self.lilies_list.append(self.lily23)

        self.lily24 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily24.center_x = 250
        self.lily24.center_y = 550
        self.lilies_list.append(self.lily24)

        self.lily25 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily25.center_x = 650
        self.lily25.center_y = 550
        self.lilies_list.append(self.lily25)

        self.lily26 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily26.center_x = 650
        self.lily26.center_y = 625
        self.lilies_list.append(self.lily26)

        self.lily27 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily27.center_x = 150
        self.lily27.center_y = 625
        self.lilies_list.append(self.lily27)

        self.lily28 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily28.center_x = 400
        self.lily28.center_y = 625
        self.lilies_list.append(self.lily28)

        self.lily29 = Lily(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lisc.png", scale=0.15)
        self.lily29.center_x = 350
        self.lily29.center_y = 625
        self.lilies_list.append(self.lily29)

        self.log = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log.center_x = 280
        self.log.center_y = 365
        self.logs_list.append(self.log)

        self.log2 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log2.center_x = 645
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

        self.log9 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log9.center_x = 580
        self.log9.center_y = 630
        self.logs_list.append(self.log9)

        self.log10 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log10.center_x = 420
        self.log10.center_y = 630
        self.logs_list.append(self.log10)

        self.log11 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log11.center_x = 100
        self.log11.center_y = 630
        self.logs_list.append(self.log11)

        self.log12 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log12.center_x = 350
        self.log12.center_y = 705
        self.logs_list.append(self.log12)

        self.log13 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log13.center_x = 600
        self.log13.center_y = 705
        self.logs_list.append(self.log13)

        self.log14 = Log(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log14.center_x = 50
        self.log14.center_y = 705
        self.logs_list.append(self.log14)

        self.flower = Flower(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lils.png", scale=0.08)
        self.flower.center_x = 120
        self.flower.center_y = 708
        self.flowers_list.append(self.flower)

        self.flower2 = Flower(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lils.png", scale=0.08)
        self.flower2.center_x = 263
        self.flower2.center_y = 708
        self.flowers_list.append(self.flower2)

        self.flower3 = Flower(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lils.png", scale=0.08)
        self.flower3.center_x = 405
        self.flower3.center_y = 708
        self.flowers_list.append(self.flower3)

        self.flower4 = Flower(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lils.png", scale=0.08)
        self.flower4.center_x = 567
        self.flower4.center_y = 708
        self.flowers_list.append(self.flower4)




    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.car_list.draw()
        self.lilies_list.draw()
        self.logs_list.draw()
        self.flowers_list.draw()
        self.frog_list.draw()
        time = f"Time: {self.time:.02f}"
        arcade.draw_text(time, 570,760,arcade.color.WHITE,21)
        score = f"Score: {self.score}"
        arcade.draw_text(score, 20,760, arcade.csscolor.WHITE, 22)


    def on_update(self, delta_time):
        self.frog_list.update()
        self.car_list.update()
        self.lilies_list.update()
        self.logs_list.update()
        self.time -= delta_time
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

        if self.frog_sprite.center_y > 300:
            if not arcade.check_for_collision_with_list(self.frog_sprite,self.lilies_list):
                if not arcade.check_for_collision_with_list(self.frog_sprite,self.logs_list):
                    arcade.play_sound(self.water_sound)
                    self.lives -=1
                    self.frog_sprite.center_y = 50
                    self.frog_sprite.center_x = 350



        if self.time <= 0:
            self.lives -= 1
            self.frog_sprite.center_x = 350
            self.frog_sprite.center_y = 50
            self.time = 100

        flowers = 0
        for flower in self.flowers_list:
            if arcade.check_for_collision(self.frog_sprite,flower):
                flowers +=1
                self.score += self.time
                flower.append_texture(arcade.load_texture(r"C:\Users\Klaudia\Desktop\Gra\Gra_lista7\zdjeciadogry\lily.png"))
                flower.set_texture(1)
                arcade.play_sound(self.bell_sound)
                self.frog_sprite.center_x = 350
                self.frog_sprite.center_y = 50
        if flowers == 4:
            pass

        if self.lives == 0:
            view = GameOverView()
            self.window.show_view(view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.frog_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.frog_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.frog_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.frog_sprite.change_x = MOVEMENT_SPEED

        #elif key == arcade.key.ESCAPE:
        #    menu_view = MenuView()
        #    self.window.show_view(menu_view)

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.frog_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.frog_sprite.change_x = 0


def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    view = GameView()
    view.setup()
    window.show_view(view)
    arcade.run()
main()