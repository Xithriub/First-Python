from tkinter import*
tk=Tk()
tk.geometry("440x240")
tk.title('AMOGUS')
tk.resizable(False, False)
tk['bg']='#FFF'
def button_press1(): print('Кнопка 1 нажата')
def button_press2(): print('Кнопка 2 нажата')
def button_press3(): print('Кнопка 3 нажата')
b1=Button(tk, text='Команда 1',command=button_press1,font=('Times New Roman',15))
b1.place(x=10,y=100,width=120,height=50)
b2=Button(tk, text='Команда 2',command=button_press2,font=('Times New Roman',15))
b2.place(x=155,y=100,width=120,height=50)
b3=Button(tk, text='Команда 3',command=button_press3,font=('Times New Roman',15))
b3.place(x=300,y=100,width=120,height=50)
lbl1=Label(tk, text='Начало!', bg='#FFF',font=('Times New Roman',21,'bold'))
lbl1.place(x=250,y=100,width=120,height=50)
tk.mainloop()

          
from pygame import choice
from copy import deepcopy
from random import choice, randrange

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
RES = 750, 940
FPS = 60

pygame.init()
sc = pygame.display.set_mode(RES)
game_sc = pygame.Surface(GAME_RES)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
field = [[0 for i in range(W)] for j in range(H)]

anim_count, anim_speed, anim_limit = 0, 60, 2000

bg = pygame.image.load('img/bg.jpg').convert()
game_bg = pygame.image.load('img/bg2.jpg').convert()

main_font = pygame.font.Font('font/font.ttf', 65)
font = pygame.font.Font('font/font.ttf', 45)

title_tetris = main_font.render('TETRIS', True, pygame.Color('red'))
title_score = font.render('score:', True, pygame.Color('white'))
title_record = font.render('record:', True, pygame.Color('white'))

get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}







