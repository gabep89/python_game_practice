import pgzrun
from random import randint

score = 0
game_over = False

apple = Actor("apple2")
strawberry = Actor("strawberry")
cherry = Actor("cherry")

def draw():
    screen.clear()
    apple.draw()
    strawberry.draw()
    cherry.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("FINAL SCORE: " + str(score), color="white", topleft=(10, 10), fontsize=60)

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def place_strawberry():
    strawberry.x = randint(10, 800)
    strawberry.y = randint(10, 600)

def place_cherry():
    cherry.x = randint(10, 800)
    cherry.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    
    if apple.collidepoint(pos):
        score = score + 1
        print("gawt heeeem!")
        place_apple()
        place_strawberry()
        place_cherry()
        
    else:
        print("You missed :'(")
        print("Final Score: " + str(score))
        game_over = True

pgzrun.go()
