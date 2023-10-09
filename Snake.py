from tkinter import *
import random

# Game settings constants are below
GAME_WIDTH = 900
GAME_HEIGHT = 700
SPEED = 50
SPACE_FOOD = 25
SNAKE_BODY = 3
SNAKE_COLOR = '#006400'
FOOD_COLOR = '#ff0000'
BACKGROUND = '#808080'


class Snake:

    def __init__(self):
        self.body_size = SNAKE_BODY
        self.coordinates = []
        self.squares = []

        for i in range(0, SNAKE_BODY):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_FOOD, y + SPACE_FOOD, fill=SNAKE_COLOR, tags='serpent')
            self.squares.append(square)

class Food:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_FOOD) - 1) * SPACE_FOOD
        y = random.randint(0, (GAME_HEIGHT/SPACE_FOOD) - 1) * SPACE_FOOD
        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_FOOD, y + SPACE_FOOD, fill=FOOD_COLOR, tags='food')




def turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_FOOD
    elif direction == 'down':
        y += SPACE_FOOD
    elif direction == 'left':
        x -= SPACE_FOOD
    elif direction == 'right':
        x += SPACE_FOOD

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_FOOD, y + SPACE_FOOD, fill=SNAKE_COLOR, tags='serpent')
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score: {}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if collision(snake):
        gameover()
    else:
        window.after(SPEED, turn, snake, food)


def movement(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for SNAKE_BODY in snake.coordinates[1:]:
        if x == SNAKE_BODY[0] and y == SNAKE_BODY[1]:
            return True

    return False

def gameover():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tags='gameover')

window = Tk()

window.title("The Serpent")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=('consolas', 22))
label.pack()

canvas = Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

win_width = window.winfo_width()
win_height = window.winfo_height()
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

x = int((screen_w/2) - (win_width/2))
y = int((screen_h/2) - (win_height/2))

window.geometry(f"{win_width}x{win_height}+{x}+{y}")

window.bind('<Left>', lambda event: movement('left'))
window.bind('<Right>', lambda event: movement('right'))
window.bind('<Up>', lambda event: movement('up'))
window.bind('<Down>', lambda event: movement('down'))


snake = Snake()
food = Food()
turn(snake, food)




window.mainloop()