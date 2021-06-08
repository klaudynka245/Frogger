import arcade



SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Frogger'
MOVEMENT_SPEED = 4
DIFFICULTY = 1
LIVES = 3
ListOfPoints = []
with open("Leaderboard.txt", 'r') as f:
    for line in f.readlines():
        ListOfPoints.append(float(line))
ListOfPoints.sort(reverse=True)

HardListOfPoints = []
with open("HardLeaderBoard.txt", 'r') as f:
    for line in f.readlines():
        HardListOfPoints.append(float(line))
HardListOfPoints.sort(reverse=True)

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
                arcade.load_texture(r".\zdjeciadogry\autoszybkieprawo.png"))
            self.set_texture(1)
        elif self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
            self.speed *= -1
            self.append_texture(
                arcade.load_texture(r".\zdjeciadogry\autoszybkie.png"))
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
                arcade.load_texture(r".\zdjeciadogry\autoszybkie.png"))
            self.set_texture(1)
        elif self.center_x < 0:
            self.append_texture(
                arcade.load_texture(r".\zdjeciadogry\autoszybkieprawo.png"))
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

class Torpedo(arcade.Sprite):
    def __init__(self,img,scale):
        super().__init__(img,scale=scale,hit_box_algorithm= "Detailed")
        self.size=0
        self.speed = 0.1 + DIFFICULTY/2
    def follow(self,player):
        if self.center_y < player.center_y:
            self.center_y += min(self.speed, player.center_y - self.center_y)
        elif self.center_y > player.center_y:
            self.center_y -= min(self.speed, self.center_y - player.center_y)
        if self.center_x < player.center_x:
            self.center_x += min(self.speed, player.center_x - self.center_x)
        elif self.center_x > player.center_x:
            self.center_x -= min(self.speed, self.center_x - player.center_x)

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_draw(self):
        arcade.start_render()
        logo = arcade.load_texture(r".\zdjeciadogry\logo.png")
        arcade.draw_lrwh_rectangle_textured(-45,250,800,600,logo)
        arcade.draw_text('Press G to start the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text('Press I for the instruction', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text('Press L to see the leaderboard', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text('Press A to read about the author', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press ESC to quit", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200,
                         arcade.color.WHITE, font_size=20, anchor_x='center')

    def on_key_press(self, key, modifiers):
        if key == arcade.key.G:
            view = ChoiceView()
            self.window.show_view(view)
        elif key == arcade.key.I:
            view = InstructionView()
            self.window.show_view(view)
        elif key == arcade.key.L:
            view = LeaderboardView()
            self.window.show_view(view)
        elif key == arcade.key.A:
            view = AuthorView()
            self.window.show_view(view)
        elif key == arcade.key.ESCAPE:
            self.window.close()

class AuthorView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("About the author", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.WHITE, font_size=40, anchor_x='center')
        arcade.draw_text("Hi! My name's Klaudia,", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text("I'm an Applied Mathematics student", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text("The game you're about to play", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2, arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text("was made for the programming course purposes.", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 50, arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text("I hope you'll enjoy it! :)", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 100, arcade.color.WHITE, font_size=20, anchor_x='center')
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            view = MenuView()
            self.window.show_view(view)


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
        arcade.set_viewport(0,SCREEN_WIDTH-1,0,SCREEN_HEIGHT-1)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instruction Screen", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=50, anchor_x='center')
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            menu_view = MenuView()
            self.window.show_view(menu_view)


class ChoiceView(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Press E to choose the easy mode', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,arcade.color.WHITE,
                         font_size=40,anchor_x='center')
        arcade.draw_text('Press H to choose the hard mode', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-50, arcade.color.WHITE,
                         font_size=40, anchor_x='center')
    def on_key_press(self, key, modifiers):
        if key == arcade.key.E:
            gameview = GameView()
            gameview.setup()
            self.window.show_view(gameview)
        elif key == arcade.key.H:
            gameview = HardGameView()
            gameview.setup()
            self.window.show_view(gameview)
        elif key == arcade.key.ESCAPE:
            view = MenuView()
            self.window.show_view(view)

class PauseView(arcade.View):
    def __init__(self,gameview):
        super().__init__()
        self.game_view = gameview
    def on_show_view(self):
        arcade.set_background_color(arcade.color.COOL_GREY)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('PAUSED',SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, arcade.color.DARK_GREEN,
                         font_size=50, anchor_x='center')
        arcade.draw_text('Press r to return to the game', SCREEN_WIDTH/2,SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text('Press Enter to reset the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2-30,
                         arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text('Press Esc to return to the menu', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 70,
                         arcade.color.WHITE, font_size=20, anchor_x='center')

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:
            game = GameView()
            game.setup()
            self.window.show_view(game)
        elif key == arcade.key.ESCAPE:
            menu = MenuView()
            self.window.show_view(menu)

class LeaderboardView(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_draw(self):
        arcade.start_render()

        arcade.draw_line(150,100,150,660,arcade.color.WHITE)
        arcade.draw_line(350, 100, 350, 660, arcade.color.WHITE)
        arcade.draw_line(550, 100, 550, 660, arcade.color.WHITE)
        arcade.draw_line(70, 650, 580, 650, arcade.color.WHITE)
        arcade.draw_text('1.', 100, 600, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('2.', 100, 550, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('3.', 100, 500, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('4.', 100, 450, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('5.', 100, 400, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('6.', 100, 350, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('7.', 100, 300, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('8.', 100, 250, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('9.', 100, 200, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('10.', 100, 150, arcade.color.WHITE,
                         font_size=25, anchor_x='center')
        arcade.draw_text('HARD', 450, 650, arcade.color.WHITE,
                         font_size=30, anchor_x='center')
        arcade.draw_text('EASY', 250, 650, arcade.color.WHITE,
                         font_size=30, anchor_x='center')
        arcade.draw_text('BEST SCORES', 350, 700, arcade.color.WHITE,
                         font_size=50, anchor_x='center')
        i = 0
        for points in ListOfPoints:
            arcade.draw_text(f'{points}', 250, 600 - i*50 , arcade.color.WHITE,
                            font_size=25, anchor_x='center')
            i +=1

        z = 0
        for points in HardListOfPoints:
            arcade.draw_text(f'{points}', 450, 600 - z * 50, arcade.color.WHITE,
                             font_size=25, anchor_x='center')
            z += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            menu = MenuView()
            self.window.show_view(menu)

class HardPauseView(arcade.View):
    def __init__(self,gameview):
        super().__init__()
        self.game_view = gameview
    def on_show_view(self):
        arcade.set_background_color(arcade.color.COOL_GREY)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('PAUSED',SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, arcade.color.DARK_GREEN,
                         font_size=50, anchor_x='center')
        arcade.draw_text('Press R to return to the game', SCREEN_WIDTH/2,SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text('Press Enter to reset the game', SCREEN_WIDTH/2, SCREEN_HEIGHT/2-30,
                         arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text('Press Esc to return to the menu', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 70,
                         arcade.color.WHITE, font_size=20, anchor_x='center')

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:
            game = HardGameView()
            game.setup()
            self.window.show_view(game)
        elif key == arcade.key.ESCAPE:
            menu = MenuView()
            self.window.show_view(menu)

class GameOverView(arcade.View):

    def __init__(self):
        super().__init__()
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('GAME OVER',SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, arcade.color.WHITE,
                         font_size=50, anchor_x='center')
        arcade.draw_text('Click to start again', SCREEN_WIDTH/2,SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=40, anchor_x='center')

class HardGameOverView(arcade.View):

    def __init__(self):
        super().__init__()
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_mouse_press(self, x, y, button, modifiers):
        game_view = HardGameView()
        game_view.setup()
        self.window.show_view(game_view)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('GAME OVER',SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, arcade.color.WHITE,
                         font_size=50, anchor_x='center')
        arcade.draw_text('Click to start again', SCREEN_WIDTH/2,SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=40, anchor_x='center')


class WinView(arcade.View):

    def __init__(self,gameview):
        super().__init__()
        self.game_view = gameview
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('You won!',SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, arcade.color.WHITE,
                         font_size=50, anchor_x='center')
        arcade.draw_text(f'Your score: {round(self.game_view.score,2)}', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=40, anchor_x='center')
        arcade.draw_text('Click to start again', SCREEN_WIDTH/2,SCREEN_HEIGHT/2-50,
                         arcade.color.WHITE, font_size=40, anchor_x='center')

class HardWinView(arcade.View):

    def __init__(self,gameview):
        super().__init__()
        self.game_view = gameview
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
    def on_mouse_press(self, x, y, button, modifiers):
        game_view = HardGameView()
        game_view.setup()
        self.window.show_view(game_view)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('You won!',SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, arcade.color.WHITE,
                         font_size=50, anchor_x='center')
        arcade.draw_text(f'Your score: {self.game_view.score}', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=40, anchor_x='center')
        arcade.draw_text('Click to start again', SCREEN_WIDTH/2,SCREEN_HEIGHT/2-50,
                         arcade.color.WHITE, font_size=40, anchor_x='center')



class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background=None
        self.frog_list=None
        self.frog_sprite=None
        self.lives = LIVES
        self.score = 0
        self.flowers = 0
    def setup(self):
        self.window.set_mouse_visible(False)
        self.background = arcade.load_texture(r".\zdjeciadogry\tło.png")
        self.crash_sound = arcade.load_sound(r".\dźwięki\PiskOpon.mp3")
        self.gameover_sound = arcade.load_sound(r".\dźwięki\GameOver.mp3")
        self.win_sound = arcade.load_sound(r".\dźwięki\Wygrana.mp3")
        self.water_sound = arcade.load_sound(r".\dźwięki\PluskWody.mp3")
        self.bell_sound = arcade.load_sound(r".\dźwięki\Bell.mp3")

        self.frog_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()
        self.lilies_list = arcade.SpriteList()
        self.flowers_list = arcade.SpriteList()
        self.logs_list = arcade.SpriteList()

        self.time = 100
        self.score = 0
        self.frog_sprite = Frog(r".\zdjeciadogry\frog.png",scale=0.16)
        self.frog_sprite.center_x = 350
        self.frog_sprite.center_y = 50
        self.frog_list.append(self.frog_sprite)

        self.lives_img = arcade.load_texture(r".\zdjeciadogry\frog.png")

        self.car_left_sprite = Carleft(r".\zdjeciadogry\autoszybkie.png",scale=0.3)
        self.car_left_sprite.center_x = 650
        self.car_left_sprite.center_y = 220
        self.car_list.append(self.car_left_sprite)

        self.car_left_sprite2 = Carleft(r".\zdjeciadogry\autoszybkie.png",scale=0.3)
        self.car_left_sprite2.center_x = 250
        self.car_left_sprite2.center_y = 180
        self.car_list.append(self.car_left_sprite2)

        self.car_right_sprite = Carright(r".\zdjeciadogry\autoszybkieprawo.png",scale=0.3)
        self.car_right_sprite.center_x = 30
        self.car_right_sprite.center_y = 150
        self.car_list.append(self.car_right_sprite)

        self.car_right_sprite2 = Carright(r".\zdjeciadogry\autoszybkieprawo.png", scale=0.3)
        self.car_right_sprite2.center_x = 450
        self.car_right_sprite2.center_y = 120
        self.car_list.append(self.car_right_sprite2)

        self.lily1 = Lily(r".\zdjeciadogry\lisc.png",scale=0.15)
        self.lily1.center_x = 600
        self.lily1.center_y = 360
        self.lilies_list.append(self.lily1)

        self.lily2 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily2.center_x = 550
        self.lily2.center_y = 360
        self.lilies_list.append(self.lily2)

        self.lily3 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily3.center_x = 200
        self.lily3.center_y = 360
        self.lilies_list.append(self.lily3)

        self.lily4 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily4.center_x = 250
        self.lily4.center_y = 360
        self.lilies_list.append(self.lily4)

        self.lily5 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily5.center_x = 400
        self.lily5.center_y = 360
        self.lilies_list.append(self.lily5)

        self.lily6 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily6.center_x = 100
        self.lily6.center_y = 360
        self.lilies_list.append(self.lily6)

        self.lily7 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily7.center_x = 50
        self.lily7.center_y = 435
        self.lilies_list.append(self.lily7)

        self.lily8 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily8.center_x = 500
        self.lily8.center_y = 435
        self.lilies_list.append(self.lily8)

        self.lily9 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily9.center_x = 150
        self.lily9.center_y = 435
        self.lilies_list.append(self.lily9)

        self.lily10 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily10.center_x = 300
        self.lily10.center_y = 435
        self.lilies_list.append(self.lily10)

        self.lily11 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily11.center_x = 600
        self.lily11.center_y = 435
        self.lilies_list.append(self.lily11)

        self.lily12 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily12.center_x = 300
        self.lily12.center_y = 475
        self.lilies_list.append(self.lily12)

        self.lily13 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily13.center_x = 600
        self.lily13.center_y = 475
        self.lilies_list.append(self.lily13)

        self.lily14 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily14.center_x = 650
        self.lily14.center_y = 475
        self.lilies_list.append(self.lily14)

        self.lily15 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily15.center_x = 150
        self.lily15.center_y = 475
        self.lilies_list.append(self.lily15)

        self.lily16 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily16.center_x = 50
        self.lily16.center_y = 475
        self.lilies_list.append(self.lily16)

        self.lily17 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily17.center_x = 350
        self.lily17.center_y = 475
        self.lilies_list.append(self.lily17)

        self.lily18 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily18.center_x = 450
        self.lily18.center_y = 475
        self.lilies_list.append(self.lily18)

        self.lily19 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily19.center_x = 500
        self.lily19.center_y = 475
        self.lilies_list.append(self.lily19)

        self.lily20 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily20.center_x = 500
        self.lily20.center_y = 550
        self.lilies_list.append(self.lily20)

        self.lily21 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily21.center_x = 300
        self.lily21.center_y = 550
        self.lilies_list.append(self.lily21)

        self.lily22 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily22.center_x = 100
        self.lily22.center_y = 550
        self.lilies_list.append(self.lily22)

        self.lily23 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily23.center_x = 150
        self.lily23.center_y = 550
        self.lilies_list.append(self.lily23)

        self.lily24 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily24.center_x = 250
        self.lily24.center_y = 550
        self.lilies_list.append(self.lily24)

        self.lily25 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily25.center_x = 650
        self.lily25.center_y = 550
        self.lilies_list.append(self.lily25)

        self.lily26 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily26.center_x = 650
        self.lily26.center_y = 625
        self.lilies_list.append(self.lily26)

        self.lily27 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily27.center_x = 150
        self.lily27.center_y = 625
        self.lilies_list.append(self.lily27)

        self.lily28 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily28.center_x = 400
        self.lily28.center_y = 625
        self.lilies_list.append(self.lily28)

        self.lily29 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily29.center_x = 350
        self.lily29.center_y = 625
        self.lilies_list.append(self.lily29)

        self.log = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log.center_x = 280
        self.log.center_y = 365
        self.logs_list.append(self.log)

        self.log2 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log2.center_x = 645
        self.log2.center_y = 365
        self.logs_list.append(self.log2)

        self.log3 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log3.center_x = 100
        self.log3.center_y = 365
        self.logs_list.append(self.log3)

        self.log4 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log4.center_x = 380
        self.log4.center_y = 440
        self.logs_list.append(self.log4)

        self.log5 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log5.center_x = 550
        self.log5.center_y = 440
        self.logs_list.append(self.log5)

        self.log6 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log6.center_x = 280
        self.log6.center_y = 555
        self.logs_list.append(self.log6)

        self.log7 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log7.center_x = 50
        self.log7.center_y = 555
        self.logs_list.append(self.log7)

        self.log8 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log8.center_x = 580
        self.log8.center_y = 555
        self.logs_list.append(self.log8)

        self.log9 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log9.center_x = 580
        self.log9.center_y = 630
        self.logs_list.append(self.log9)

        self.log10 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log10.center_x = 420
        self.log10.center_y = 630
        self.logs_list.append(self.log10)

        self.log11 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log11.center_x = 100
        self.log11.center_y = 630
        self.logs_list.append(self.log11)

        self.log12 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log12.center_x = 350
        self.log12.center_y = 705
        self.logs_list.append(self.log12)

        self.log13 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log13.center_x = 600
        self.log13.center_y = 705
        self.logs_list.append(self.log13)

        self.log14 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log14.center_x = 50
        self.log14.center_y = 705
        self.logs_list.append(self.log14)

        self.flower = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
        self.flower.center_x = 120
        self.flower.center_y = 708
        self.flowers_list.append(self.flower)

        self.flower2 = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
        self.flower2.center_x = 263
        self.flower2.center_y = 708
        self.flowers_list.append(self.flower2)

        self.flower3 = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
        self.flower3.center_x = 405
        self.flower3.center_y = 708
        self.flowers_list.append(self.flower3)

        self.flower4 = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
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

        for live in range(self.lives):
            arcade.draw_lrwh_rectangle_textured(20 + 50*live,2,40,40,self.lives_img)


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


        for flower in self.flowers_list:
            if arcade.check_for_collision(self.frog_sprite,flower):
                self.flowers += 1
                self.score += round(self.time,1)
                flower.append_texture(arcade.load_texture(r".\zdjeciadogry\lily.png"))
                flower.set_texture(1)
                arcade.play_sound(self.bell_sound)
                self.frog_sprite.center_x = 350
                self.frog_sprite.center_y = 50
                self.time += 10
        if self.flowers == 4:
            self.score += self.lives * 100
            arcade.play_sound(self.win_sound)
            view = WinView(self)
            self.window.show_view(view)

            with open("Leaderboard.txt", 'w') as f:
                ListOfPoints[-1] = round(self.score)
                ListOfPoints.sort(reverse=True)
                Strlist = [str(point)+'\n' for point in ListOfPoints]
                f.writelines(Strlist)

        if self.lives == 0:
            arcade.play_sound(self.gameover_sound)
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

        elif key == arcade.key.ESCAPE:
            paused_view = PauseView(self)
            self.window.show_view(paused_view)

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.frog_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.frog_sprite.change_x = 0


class HardGameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background=None
        self.frog_list=None
        self.frog_sprite=None
        self.lives = LIVES
        self.score = 0
        self.flowers = 0
    def setup(self):
        self.window.set_mouse_visible(False)
        self.background = arcade.load_texture(r".\zdjeciadogry\tło.png")
        self.crash_sound = arcade.load_sound(r".\dźwięki\PiskOpon.mp3")
        self.gameover_sound = arcade.load_sound(r".\dźwięki\GameOver.mp3")
        self.win_sound = arcade.load_sound(r".\dźwięki\Wygrana.mp3")
        self.water_sound = arcade.load_sound(r".\dźwięki\PluskWody.mp3")
        self.bell_sound = arcade.load_sound(r".\dźwięki\Bell.mp3")

        self.frog_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()
        self.lilies_list = arcade.SpriteList()
        self.flowers_list = arcade.SpriteList()
        self.logs_list = arcade.SpriteList()

        self.time = 100
        self.score = 0
        self.frog_sprite = Frog(r".\zdjeciadogry\frog.png",scale=0.16)
        self.frog_sprite.center_x = 350
        self.frog_sprite.center_y = 50
        self.frog_list.append(self.frog_sprite)

        self.lives_img = arcade.load_texture(r".\zdjeciadogry\frog.png")

        self.car_left_sprite = Carleft(r".\zdjeciadogry\autoszybkie.png",scale=0.3)
        self.car_left_sprite.center_x = 650
        self.car_left_sprite.center_y = 240
        self.car_list.append(self.car_left_sprite)

        self.car_left_sprite2 = Carleft(r".\zdjeciadogry\autoszybkie.png",scale=0.3)
        self.car_left_sprite2.center_x = 250
        self.car_left_sprite2.center_y = 215
        self.car_list.append(self.car_left_sprite2)

        self.car_right_sprite = Carright(r".\zdjeciadogry\autoszybkieprawo.png",scale=0.3)
        self.car_right_sprite.center_x = 30
        self.car_right_sprite.center_y = 190
        self.car_list.append(self.car_right_sprite)

        self.car_right_sprite2 = Carright(
            r".\zdjeciadogry\autoszybkieprawo.png", scale=0.3)
        self.car_right_sprite2.center_x = 450
        self.car_right_sprite2.center_y = 150
        self.car_list.append(self.car_right_sprite2)

        self.car_right_sprite3 = Carright(r".\zdjeciadogry\autoszybkieprawo.png", scale=0.3)
        self.car_right_sprite3.center_x = 250
        self.car_right_sprite3.center_y = 115
        self.car_list.append(self.car_right_sprite3)

        self.lily1 = Lily(r".\zdjeciadogry\lisc.png",scale=0.15)
        self.lily1.center_x = 600
        self.lily1.center_y = 360
        self.lilies_list.append(self.lily1)

        self.lily2 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily2.center_x = 550
        self.lily2.center_y = 360
        self.lilies_list.append(self.lily2)

        self.lily3 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily3.center_x = 200
        self.lily3.center_y = 360
        self.lilies_list.append(self.lily3)

        self.lily4 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily4.center_x = 250
        self.lily4.center_y = 360
        self.lilies_list.append(self.lily4)

        self.lily5 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily5.center_x = 400
        self.lily5.center_y = 360
        self.lilies_list.append(self.lily5)

        self.lily6 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily6.center_x = 100
        self.lily6.center_y = 360
        self.lilies_list.append(self.lily6)

        self.lily7 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily7.center_x = 50
        self.lily7.center_y = 435
        self.lilies_list.append(self.lily7)

        self.lily8 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily8.center_x = 500
        self.lily8.center_y = 435
        self.lilies_list.append(self.lily8)

        self.lily9 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily9.center_x = 150
        self.lily9.center_y = 435
        self.lilies_list.append(self.lily9)

        self.lily10 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily10.center_x = 300
        self.lily10.center_y = 435
        self.lilies_list.append(self.lily10)

        self.lily11 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily11.center_x = 600
        self.lily11.center_y = 435
        self.lilies_list.append(self.lily11)

        self.lily13 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily13.center_x = 600
        self.lily13.center_y = 475
        self.lilies_list.append(self.lily13)

        self.lily14 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily14.center_x = 650
        self.lily14.center_y = 475
        self.lilies_list.append(self.lily14)

        self.lily15 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily15.center_x = 150
        self.lily15.center_y = 475
        self.lilies_list.append(self.lily15)

        self.lily17 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily17.center_x = 350
        self.lily17.center_y = 475
        self.lilies_list.append(self.lily17)

        self.lily19 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily19.center_x = 500
        self.lily19.center_y = 475
        self.lilies_list.append(self.lily19)

        self.lily20 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily20.center_x = 500
        self.lily20.center_y = 550
        self.lilies_list.append(self.lily20)

        self.lily21 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily21.center_x = 300
        self.lily21.center_y = 550
        self.lilies_list.append(self.lily21)

        self.lily23 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily23.center_x = 150
        self.lily23.center_y = 550
        self.lilies_list.append(self.lily23)

        self.lily24 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily24.center_x = 250
        self.lily24.center_y = 550
        self.lilies_list.append(self.lily24)

        self.lily25 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily25.center_x = 650
        self.lily25.center_y = 550
        self.lilies_list.append(self.lily25)

        self.lily26 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily26.center_x = 650
        self.lily26.center_y = 625
        self.lilies_list.append(self.lily26)

        self.lily27 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily27.center_x = 150
        self.lily27.center_y = 625
        self.lilies_list.append(self.lily27)

        self.lily28 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily28.center_x = 400
        self.lily28.center_y = 625
        self.lilies_list.append(self.lily28)

        self.lily29 = Lily(r".\zdjeciadogry\lisc.png", scale=0.15)
        self.lily29.center_x = 350
        self.lily29.center_y = 625
        self.lilies_list.append(self.lily29)

        self.log = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log.center_x = 280
        self.log.center_y = 365
        self.logs_list.append(self.log)

        self.log2 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log2.center_x = 645
        self.log2.center_y = 365
        self.logs_list.append(self.log2)

        self.log4 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log4.center_x = 380
        self.log4.center_y = 440
        self.logs_list.append(self.log4)

        self.log5 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log5.center_x = 550
        self.log5.center_y = 440
        self.logs_list.append(self.log5)

        self.log7 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log7.center_x = 50
        self.log7.center_y = 555
        self.logs_list.append(self.log7)

        self.log8 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log8.center_x = 580
        self.log8.center_y = 555
        self.logs_list.append(self.log8)

        self.log10 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log10.center_x = 420
        self.log10.center_y = 630
        self.logs_list.append(self.log10)

        self.log11 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log11.center_x = 100
        self.log11.center_y = 630
        self.logs_list.append(self.log11)

        self.log13 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log13.center_x = 600
        self.log13.center_y = 705
        self.logs_list.append(self.log13)

        self.log14 = Log(r".\zdjeciadogry\kłoda2.png", scale=0.2)
        self.log14.center_x = 50
        self.log14.center_y = 705
        self.logs_list.append(self.log14)

        self.flower = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
        self.flower.center_x = 120
        self.flower.center_y = 708
        self.flowers_list.append(self.flower)

        self.flower2 = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
        self.flower2.center_x = 263
        self.flower2.center_y = 708
        self.flowers_list.append(self.flower2)

        self.flower3 = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
        self.flower3.center_x = 405
        self.flower3.center_y = 708
        self.flowers_list.append(self.flower3)

        self.flower4 = Flower(r".\zdjeciadogry\lils.png", scale=0.08)
        self.flower4.center_x = 567
        self.flower4.center_y = 708
        self.flowers_list.append(self.flower4)

        self.torpedo = Torpedo(r".\zdjeciadogry\torpeda.png",scale=0.1)
        self.torpedo.center_x = 200
        self.torpedo.center_y = -100
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.car_list.draw()
        self.lilies_list.draw()
        self.logs_list.draw()
        self.flowers_list.draw()
        self.torpedo.draw()
        self.frog_list.draw()
        time = f"Time: {self.time:.02f}"
        arcade.draw_text(time, 570,760,arcade.color.WHITE,21)
        score = f"Score: {self.score}"
        arcade.draw_text(score, 20,760, arcade.csscolor.WHITE, 22)

        for live in range(self.lives):
            arcade.draw_lrwh_rectangle_textured(20 + 50*live,2,40,40,self.lives_img)


    def on_update(self, delta_time):
        self.frog_list.update()
        self.car_list.update()
        self.lilies_list.update()
        self.logs_list.update()
        self.torpedo.follow(self.frog_sprite)
        self.time -= delta_time
        if arcade.check_for_collision_with_list(self.frog_sprite,self.car_list):
            arcade.play_sound(self.crash_sound)
            self.frog_sprite.center_x = 350
            self.frog_sprite.center_y = 50
            self.lives -=1
            self.torpedo.center_x = 300
            self.torpedo.center_y = -100
        for lily in self.lilies_list:
            if arcade.check_for_collision(self.frog_sprite,lily):
                self.frog_sprite.center_x += lily.speed
        for log in self.logs_list:
            if arcade.check_for_collision(self.frog_sprite,log):
                self.frog_sprite.center_x += log.speed

        if self.frog_sprite.center_y > 300:
            if not arcade.check_for_collision_with_list(self.frog_sprite,self.lilies_list) and not arcade.check_for_collision_with_list(self.frog_sprite,self.logs_list):
                arcade.play_sound(self.water_sound)
                self.lives -=1
                self.frog_sprite.center_y = 50
                self.frog_sprite.center_x = 350
                self.torpedo.center_y = -100



        if self.time <= 0:
            self.lives -= 1
            self.frog_sprite.center_x = 350
            self.frog_sprite.center_y = 50
            self.time = 100


        for flower in self.flowers_list:
            if arcade.check_for_collision(self.frog_sprite,flower):
                self.flowers += 1
                self.score += round(self.time,1)
                flower.append_texture(arcade.load_texture(r".\zdjeciadogry\lily.png"))
                flower.set_texture(1)
                arcade.play_sound(self.bell_sound)
                self.frog_sprite.center_x = 350
                self.frog_sprite.center_y = 50
                self.torpedo.center_y = -100
                self.torpedo.center_x = 200
                self.time += 10
        if self.flowers == 4:
            self.score += self.lives * 100
            arcade.play_sound(self.win_sound)
            view = HardWinView(self)
            self.window.show_view(view)
            with open("HardLeaderBoard.txt", 'w') as f:
                HardListOfPoints[-1] = round(self.score)
                HardListOfPoints.sort(reverse=True)
                HardStrlist = [str(point) + '\n' for point in HardListOfPoints]
                f.writelines(HardStrlist)

        if self.lives == 0:
            arcade.play_sound(self.gameover_sound)
            view = HardGameOverView()
            self.window.show_view(view)

        if arcade.check_for_collision(self.frog_sprite,self.torpedo):
            self.lives -=1
            self.frog_sprite.center_x = 350
            self.frog_sprite.center_y = 50
            self.torpedo.center_x = 350
            self.torpedo.center_y = -100

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.frog_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.frog_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.frog_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.frog_sprite.change_x = MOVEMENT_SPEED

        elif key == arcade.key.ESCAPE:
            paused_view = HardPauseView(self)
            self.window.show_view(paused_view)

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.frog_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.frog_sprite.change_x = 0




def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    view = MenuView()
    window.show_view(view)
    arcade.run()
main()