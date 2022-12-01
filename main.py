from random import randint
from time import sleep


class Tankas:
    coords_x, coords_y = 0, 0
    direction = 'N'
    shots = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    total_shots = 0
    target_x, target_y = randint(-5, 5), randint(-5, 5)
    while target_x == coords_x and target_y == coords_y:
        target_x, target_y = randint(-5, 5), randint(-5, 5)

    def generate_new_target(self):
        self.target_x, self.target_y = randint(-5, 5), randint(-5, 5)
        while self.target_x == self.coords_x and self.target_y == self.coords_y:
            self.target_x, self.target_y = randint(-5, 5), randint(-5, 5)
        return self.target_x, self.target_y

    def move(self, move_direction):
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

    def enemy_down(self):
        for i in range(10):
            print('Tank' + i*'-' + '>')
            sleep(0.2)
        print('Tank----------> BOOM')
        print('Enemy down')
        self.generate_new_target()
        print(f'New target spawned at {self.target_x}, {self.target_y}')

    def info(self):
        print(f'Tank facing {self.direction} direction')
        print(f'Tank coordinates are: {tank.coords_x}, {tank.coords_y}')
        print(f'Target coordinates are: {tank.target_x}, {tank.target_y}')
        print(f'Total shots fired: {self.total_shots}')
        print(f'Shots fired to directions: {self.shots}')

    def shoot(self):
        print('Shots fired')
        self.total_shots += 1
        self.shots[self.direction] += 1
        if self.coords_x == self.target_x or self.coords_y == self.target_y:
            if self.coords_x > self.target_x and self.direction == 'W':
                self.enemy_down()
            elif self.coords_x < self.target_x and self.direction == 'E':
                self.enemy_down()
            elif self.coords_y > self.target_y and self.direction == 'S':
                self.enemy_down()
            elif self.coords_y < self.target_y and self.direction == 'N':
                self.enemy_down()
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
        game = False
