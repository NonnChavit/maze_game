#create a Maze game!

from pygame import *

window_width = 700
window_height = 500
window = display.set_mode( (window_width, window_height) )

class Character():
    def __init__(self, filename, x, y, w, h):
        self.img = transform.scale(image.load(filename),(w,h))
        self.x = x
        self.y = y
    def draw (self):
        window.blit(self.img,(self.x,self.y))



bg = transform.scale(image.load("background.png"), (window_width, window_height))
player1 = Character("sprite1.png", 200, 300, 50, 50)
player2 = Character("sprite2.png", 250, 350, 50, 50)
player2 = Character("treasure.png", 250, 350, 50, 50)

game = True

while game:
 
    
    window.blit(bg,(0,0))

    player1.draw()
    player2.draw()

   

    keys_pressed = key.get_pressed()
    if keys_pressed[K_w] and player1.y > 0:
        player1.y -= 2 
    if keys_pressed[K_s] and player1.y < 420:
        player1.y += 2
    if keys_pressed[K_d] and player1.x < 615:
        player1.x += 2
    if keys_pressed[K_a] and player1.x > 0:
        player1.x -= 2 


    if keys_pressed[K_UP] and player2.y > 0:
        player2.y -= 2
    if keys_pressed[K_DOWN] and player2.y < 420:
        player2.y += 2
    if keys_pressed[K_LEFT] and player2.x > 0:
        player2.x -= 2
    if keys_pressed[K_RIGHT] and player2.x < 615:
        player2.x += 2 


    

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()