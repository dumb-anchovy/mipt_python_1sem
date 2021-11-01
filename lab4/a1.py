import pygame
from pygame.draw import *
from random import randint
import os

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
speed = [randint(-20, 20), randint(-20, 20)]
score = 0

'''
Всё о шариках
'''

# создаем класс шариков
class Ball():
    def __init__(self, x=500, y=500, r=10):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        self.speed = [randint(-10, 10), randint(-10, 10)]

    def move(self): # описание движения
        if self.x - self.r < 0 or self.x + self.r > 1200:
            self.speed[0] = -self.speed[0]
            if self.x - self.r < 0:  # шарик ушел влево
                self.x = self.r
            if self.x + self.r > 1200:  # шарик ушел вправо
                self.x = 1200 - self.r
        if self.y - self.r < 0 or self.y + self.r > 900:
            self.speed[1] = -self.speed[1]
            if self.y - self.r < 0:  # шарик ушел наверх
                self.y = self.r
            if self.y + self.r > 900:  # шарик ушел вниз
                self.y = 900 - self.r
        self.x += self.speed[0]
        self.y += self.speed[1]
        circle(screen, self.color, (self.x, self.y), self.r)

# добавляем начальные шарики
balls = []
for i in range(10):
    ball = Ball()
    balls.append(ball)

'''
Всё о жабах
'''

# создаем массив изображений лягушек
froggies = []
for _, _, filenames in os.walk("./frogs"):
    for fn in filenames:
        print(fn)
        froggies.append(pygame.image.load("./frogs/"+fn))

# создаем класс жабок
class Frog():
    def __init__(self, x=500, y=500, r=10):
        self.x = randint(150, 1050)
        self.y = randint(150, 750)
        self.scale = 1
        self.i = 0
        self.image = froggies[0]
        self.speed = 0.01
        self.r = r
    def reduce_size(self):
        self.scale -= self.speed
        img = pygame.transform.rotozoom(self.image, 0, self.scale)
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.r = rect.height//2
        screen.blit(img, rect)
    def change_gif(self):
        self.i = (self.i + 1) % len(froggies)  # 0 ... 3
        self.image = froggies[self.i]

# добавляем массив жаб
frogs = []


'''
Всё о котах
'''

# создаем массив изображений с котами
kittens = []
for _, _, filenames in os.walk("./kits"):
    for fn in filenames:
        kittens.append(pygame.image.load("./kits/"+fn))

# описание класса котов
class Kit():
    def __init__(self, x=500, y=500, r=10):
        self.x = randint(150, 1050)
        self.y = randint(150, 750)
        self.scale = 1
        self.i = 0
        self.image = kittens[0]
        self.speed = 0.02
        self.r = r
    def reduce_size(self):
        self.scale -= self.speed
        img = pygame.transform.rotozoom(self.image, 0, self.scale)
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.r = rect.height//2
        screen.blit(img, rect)
    def change_gif(self):
        self.i = (self.i + 1) % len(kittens)  # 0 ... 3
        self.image = kittens[self.i]

# добавляем массив котов
cats = []


'''
Всё о хомяках
'''

# создаем массив изображений с хомяками
humsters = []
for _, _, filenames in os.walk("./humsters"):
    for fn in filenames:
        print(fn)
        humsters.append(pygame.image.load("./humsters/"+fn))

# создаем класс хомяков
class Humster():
    def __init__(self, x=500, y=500, r=10):
        self.x = randint(150, 1050)
        self.y = randint(150, 750)
        self.scale = 1
        self.i = 0
        self.image = humsters[0]
        self.speed = 0.05
        self.r = r
    def reduce_size(self):
        self.scale -= self.speed
        img = pygame.transform.rotozoom(self.image, 0, self.scale)
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.r = rect.height//2
        screen.blit(img, rect)
    def change_gif(self):
        self.i = (self.i + 1) % len(humsters)  # 0 ... 3
        self.image = humsters[self.i]

# добавляем массив хомяков
hums = []



pygame.display.update()
clock = pygame.time.Clock()

# timers
ball_timer = 0
change_frog_timer = 0
frog_birth_timer = 122
change_cat_timer = 0
cat_birth_timer = 231
change_hum_timer = 0
hum_birth_timer = 157
game_finishing_timer = 0

# some bools
finished = False
name_not_entered = True


name = ""

players_scores = {}

# font to display text
myfont = pygame.font.SysFont("monospace", 24)

while not finished:
    delta = clock.tick(FPS)  # количество миллисекунд прошедшее с предыдущего кадра
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
            pygame.quit()
            exit()
        elif name_not_entered and event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                if name:
                    name_not_entered = False
            elif event.key == pygame.K_BACKSPACE:
                if name:
                    name = name[:-1]
            else:
                name += pygame.key.name(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if (ball.x - event.pos[0]) ** 2 + (ball.y - event.pos[1]) ** 2 <= ball.r ** 2:
                    balls.remove(ball)
                    score += 1
            for frog in frogs:
                if (frog.x - event.pos[0]) ** 2 + (frog.y - event.pos[1]) ** 2 <= frog.r ** 2:
                    frogs.remove(frog)
                    score += 5
            for cat in cats:
                if (cat.x - event.pos[0]) ** 2 + (cat.y - event.pos[1]) ** 2 <= cat.r ** 2:
                    cats.remove(cat)
                    score += 10
            for hum in hums:
                if (hum.x - event.pos[0]) ** 2 + (hum.y - event.pos[1]) ** 2 <= hum.r ** 2:
                    hums.remove(hum)
                    score += 15

    pygame.display.update()
    screen.fill(BLACK)
    if name_not_entered:
        enter_name_text = myfont.render("Enter your name: " + name, 1, (255, 255, 255))
        screen.blit(enter_name_text, (250, 250))
    else:
        if game_finishing_timer >= 20000:
            # draw game overs
            for i in range(10):
                game_over_text = myfont.render("GAME OVER!", 1, (255, 255, 255))
                screen.blit(game_over_text, (randint(0, 300), randint(0, 900)))
            for i in range(10):
                game_over_text = myfont.render("GAME OVER!", 1, (255, 255, 255))
                screen.blit(game_over_text, (randint(800, 1200), randint(0, 900)))

            # draw current score
            enter_name_text = myfont.render(f"Current Score: {score}", 1, (255, 255, 255))
            screen.blit(enter_name_text, (500, 150))

            # work with high score
            with open('top.txt', 'r') as f:
                # считываем с файла
                for line in f:
                    splitted = line.split(' ')
                    players_scores[''.join(splitted[0:-1])] = int(splitted[-1])
                # обновляем инфу по нашему игроку
                if name in players_scores.keys():
                    players_scores[name] = max(players_scores[name], score)
                else:
                    players_scores[name] = score
            with open('top.txt', 'w') as f:
                # записать всё обратно
                sorted_players_scores = {k: v for k, v in sorted(players_scores.items(), reverse=True, key=lambda item: item[1])}
                for key, value in sorted_players_scores.items():
                    f.write(key + ' ' + str(value) + '\n')
            # вывести на экран
            y = 350
            high_score_text = myfont.render("High Score:", 1, (255, 255, 255))
            screen.blit(high_score_text, (500, 290))
            for num, (key, value) in enumerate(sorted_players_scores.items()):
                if num >= 10: break
                player_text = myfont.render(f"{num+1}. {key}: {value}", 1, (255, 255, 255))
                screen.blit(player_text, (500, y))
                y += 30
        else:
            ball_timer += delta # таймер для шаров
            change_frog_timer += delta  # таймер для изменения изображения лягушки
            change_cat_timer += delta  # таймер для изменения изображения кота
            change_hum_timer += delta  # таймер для изменения изображения хомыча
            frog_birth_timer += delta  # таймер для спавна новой жабы
            cat_birth_timer += delta  # таймер для спавна нового кота
            hum_birth_timer += delta  # таймер для спавна нового хомы
            game_finishing_timer += delta  # таймер для finishing game

            scoretext = myfont.render("Score = " + str(score), 1, (255, 255, 255))
            screen.blit(scoretext, (50, 100))
            for ball in balls: # катаем шары
                ball.move()
            if ball_timer >= 1000:
                ball = Ball()
                balls.append(ball)
                ball_timer = 0

            if change_frog_timer >= 20: # приколы с жабами
                for frog in frogs:
                    frog.change_gif()
                change_frog_timer = 0
            if frog_birth_timer >= 1500:
                frog = Frog()
                frogs.append(frog)
                frog_birth_timer = 0
            for frog in frogs:
                frog.reduce_size()
                if frog.r < 10:
                    frogs.remove(frog)

            if change_cat_timer >= 20: # приколы с котами
                for cat in cats:
                    cat.change_gif()
                change_cat_timer = 0
            if cat_birth_timer >= 2500:
                cat = Kit()
                cats.append(cat)
                cat_birth_timer = 0
            for cat in cats:
                cat.reduce_size()
                if cat.r < 10:
                    cats.remove(cat)

            if change_hum_timer >= 20: # приколы с хомами
                for hum in hums:
                    hum.change_gif()
                change_hum_timer = 0
            if hum_birth_timer >= 4000:
                hum = Humster()
                hums.append(hum)
                hum_birth_timer = 0
            for hum in hums:
                hum.reduce_size()
                if hum.r < 10:
                    hums.remove(hum)

pygame.quit()
