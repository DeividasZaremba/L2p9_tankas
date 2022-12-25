from turtle import *
speed(70)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b*3)
    b -= 1

# import pyautogui as pag
# import random
# import time
#
# while True:
#     x = random.randint(600, 700)
#     y = random.randint(200, 600)
#     pag.moveTo(x,y,0.5)
#     time.sleep(3)

# import random
# lower = 'abcdefghijklmnopqrstuvwxyz'
# upper = lower.upper()
# symbols = '!@#$%^&*()-'
# numbers = '1234567890'
# all = lower + upper + symbols + numbers
#
# length = 10
#
# password = ''
# for _ in range(length):
#     password = ''.join([password, random.choice(all)])
#
# print(password)
