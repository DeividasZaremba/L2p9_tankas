from random import randint
from time import sleep
import pickle
from os import path
import operator

scoreboard = {}
if path.exists('scoreboard.pkl'):
    with open('scoreboard.pkl', 'rb') as pickle_file:
        scoreboard = pickle.load(pickle_file)


class Tankas:
    coords_x, coords_y = 0, 0
    direction = 'N'
    shots = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    total_shots = 0
    target_x, target_y = randint(-5, 5), randint(-5, 5)
    while target_x == coords_x and target_y == coords_y:
        target_x, target_y = randint(-5, 5), randint(-5, 5)
    score = 100
    tankist_name = input('Enter your name: ')

    def generate_new_target(self):
        self.target_x, self.target_y = randint(-5, 5), randint(-5, 5)
        while self.target_x == self.coords_x and self.target_y == self.coords_y:
            self.target_x, self.target_y = randint(-5, 5), randint(-5, 5)
        return self.target_x, self.target_y

    def move(self, move_direction):
        tank.score -= 10
        if move_direction == 'N':
            self.coords_y += 1
        if move_direction == 'S':
            self.coords_y -= 1
        if move_direction == 'E':
            self.coords_x += 1
        if move_direction == 'W':
            self.coords_x -= 1
        self.direction = move_direction
        return

    def enemy_down_north(self):
        print('/\\')
        for i in range(5):
            print('|')
            sleep(0.2)
        print('Tank')
        print('BOOM')
        print('>>>>>  Enemy down  <<<<<')
        self.score += 100
        self.generate_new_target()
        print(f'New target spawned at {self.target_x}, {self.target_y}')

    def enemy_down_west(self):
        for i in range(5):
            print('<' + i * '-' + 'Tank')
            sleep(0.2)
        print('BOOM <----- Tank')
        print('>>>>>  Enemy down  <<<<<')
        self.score += 100
        self.generate_new_target()
        print(f'New target spawned at {self.target_x}, {self.target_y}')

    def enemy_down_south(self):
        print('Tank')
        sleep(0.2)
        for i in range(5):
            print('|')
            sleep(0.2)
        print('\/')
        print('BOOM')
        print('>>>>>  Enemy down  <<<<<')
        self.score += 100
        self.generate_new_target()
        print(f'New target spawned at {self.target_x}, {self.target_y}')

    def enemy_down_east(self):
        for i in range(5):
            print('Tank' + i * '-' + '>')
            sleep(0.2)
        print('Tank -----> BOOM')
        print('>>>>>  Enemy down  <<<<<')
        self.score += 100
        self.generate_new_target()
        print(f'New target spawned at {self.target_x}, {self.target_y}')


    def info(self):
        tank.score -= 10
        print(f'Tank facing {self.direction} direction')
        print(f'Tank coordinates are: {tank.coords_x}, {tank.coords_y}')
        print(f'Target coordinates are: {tank.target_x}, {tank.target_y}')
        print(f'Total shots fired: {self.total_shots}')
        print(f'Shots fired to directions: {self.shots}')


    def shoot(self):
        print('Shots fired')
        tank.score -= 10
        self.total_shots += 1
        self.shots[self.direction] += 1
        if self.coords_x == self.target_x or self.coords_y == self.target_y:
            if self.coords_x > self.target_x and self.direction == 'W':
                self.enemy_down_west()
            elif self.coords_x < self.target_x and self.direction == 'E':
                self.enemy_down_east()
            elif self.coords_y > self.target_y and self.direction == 'S':
                self.enemy_down_south()
            elif self.coords_y < self.target_y and self.direction == 'N':
                self.enemy_down_north()
        else:
            for i in range(10):
                print('Tank' + i * '-' + '>')
                sleep(0.2)
            print('Tank----------> Missed')


tank = Tankas()
game = True
print(f'Tank coordinates are: {tank.coords_x}, {tank.coords_y}')
print(f'Target coordinates are: {tank.target_x}, {tank.target_y}')

while game:
    if tank.score > 0:
        print(f'Current score: [{tank.score}]')
        action = input('Move: N - north; W - west; S - south; E - east; shoot; info; stopgame: ').upper()
        print('-------------------------------')
        if action == 'N' or action == 'W' or action == 'S' or action == 'E':
            tank.move(action)
        elif action == 'SHOOT':
            tank.shoot()
        elif action == 'INFO':
            tank.info()
        elif action == 'STOPGAME':
            print('Game finished')
            scoreboard[tank.tankist_name] = tank.score
            sorted_scoreboard = sorted(scoreboard.items(), key=operator.itemgetter(1), reverse=True)
            with open('Scoreboard.pkl', 'wb') as pickle_file:
                pickle.dump(scoreboard, pickle_file)
            print('Scoreboard:')
            for k, v in sorted_scoreboard:
                print(f'{v: >5} -> {k: <15}')
            game = False
    else:
        print('You ran out of points.')
        print('Game over')
        game = False
