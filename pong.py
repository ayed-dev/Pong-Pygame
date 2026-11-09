from pygame import *
from sys import exit

init()
clock = time.Clock()

class Game:
    def __init__(self):
        self.screen = display.set_mode((1920, 1080))
        self.player1 = Rect(500, 500, 25, 100)
        self.player1_1 = Rect(500, 500, 25, 33)
        self.player1_2 = Rect(500, 533, 25, 33)
        self.player1_3 = Rect(500, 566, 25, 33)

        self.player2 = Rect(1400, 500, 25, 100)

        self.player2_1 = Rect(1400, 500, 25, 33)
        self.player2_2 = Rect(1400, 533, 25, 33)
        self.player2_3 = Rect(1400, 566, 25, 33)
        
        self.ball = Rect(1920/2, 1080/2, 25, 25)
        self.player_speed = 10
        self.ball_speed = 15
        self.player1_score = 0
        self.player2_score = 0

    def update(self):
        self.font = font.Font(None, 50)
        self.text = self.font.render("Score : ", True, (255, 255, 255))
        self.text_score1= self.font.render(str(self.player1_score), True, ("blue"))
        self.text_score2= self.font.render(str(self.player2_score), True, ("red"))
        self.screen.fill("black")
        draw.rect(self.screen, ("blue"), self.player1)
        draw.rect(self.screen, ("red"), self.player2)
        draw.rect(self.screen, ("white"), self.ball)

        self.screen.blit(self.text, (900, 200)) 
        self.screen.blit(self.text_score1, (1025, 200))   
        self.screen.blit(self.text_score2, (1060, 200))     
         
game = Game()

def left():
     game.ball[0] -= game.ball_speed
def right():
     game.ball[0] += game.ball_speed
function_x = left

def move_ball_x():
        global function_x
        function_x()
    
        if game.ball.colliderect(game.player1):
             function_x = right

        elif game.ball.colliderect(game.player2):
           function_x = left

def up():
     game.ball[1] -= 10
def medium():
     game.ball[1] = game.ball[1]
def down():
     game.ball[1] += 10

function_y = medium

def move_ball_y():
        global  function_y
        if game.ball.colliderect(game.player1_1) or game.ball.colliderect(game.player2_1) :
            function_y = up
        if game.ball.colliderect(game.player1_2) or game.ball.colliderect(game.player2_2):
            function_y = medium
        if game.ball.colliderect(game.player1_3) or game.ball.colliderect(game.player2_3):
            function_y = down

def ball_up():
     global function_y
     if game.ball[1] <= 170:
         function_y = down
def ball_down():
     global function_y
     if game.ball[1] >= 800:
         function_y = up

def restart():
        global function_y
        game.player1 = Rect(500, 500, 25, 100)
        game.player1_1 = Rect(500, 500, 25, 33)
        game.player1_2 = Rect(500, 533, 25, 33)
        game.player1_3 = Rect(500, 566, 25, 33)

        game.player2 = Rect(1400, 500, 25, 100)

        game.player2_1 = Rect(1400, 500, 25, 33)
        game.player2_2 = Rect(1400, 533, 25, 33)
        game.player2_3 = Rect(1400, 566, 25, 33)

        game.ball = Rect(1920/2, 1080/2, 25, 25)
        function_y = medium

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()
    
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
        exit()
    if keys[K_SPACE]:
         restart()
   
    def move():
      if game.player1[1] > 170:
        if keys[K_a]:
            game.player1[1] -= game.player_speed
            game.player1_1[1] -= game.player_speed
            game.player1_2[1] -= game.player_speed
            game.player1_3[1] -= game.player_speed
        
      if game.player1[1] < 800:
        if keys[K_q]:
            game.player1[1] += game.player_speed

            game.player1_1[1] += game.player_speed
            game.player1_2[1] += game.player_speed
            game.player1_3[1] += game.player_speed

      if game.player2[1] > 170:
        if keys[K_p]:
            game.player2[1] -= game.player_speed

            game.player2_1[1] -= game.player_speed
            game.player2_2[1] -= game.player_speed
            game.player2_3[1] -= game.player_speed
    
      if game.player2[1] < 800:
        if keys[K_m]:
              game.player2[1] += game.player_speed

              game.player2_1[1] += game.player_speed
              game.player2_2[1] += game.player_speed
              game.player2_3[1] += game.player_speed
        
    
    move()
 
    game.update()
    move_ball_x()
    move_ball_y()
    function_y()
    ball_up()
    ball_down()

    if game.ball[0] <= 100:
        game.player2_score += 1
        restart()
    
    if game.ball[0] >= 1600:
        game.player1_score += 1
        restart()
    
    if game.player1_score == 10:
        game.player1_score = 0
        game.player2_score = 0

    if game.player2_score == 10:
        game.player1_score = 0
        game.player2_score = 0

    clock.tick(60)
    display.update()