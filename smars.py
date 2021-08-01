from pyfirmata import Arduino
from time import sleep

bot = Arduino("/dev/tty.usbserial-110")
print("version - ", bot.get_firmata_version())

motor_a_pin = 10
motor_b_pin = 11
motor_a_speed_pin = 12
motor_b_speed_pin = 13

def forward(bot:Arduino):
    bot.digital[motor_a_pin].write(1)
    bot.digital[motor_b_pin].write(1)
    bot.digital[motor_a_speed_pin].write(1)
    bot.digital[motor_b_speed_pin].write(0)
    bot.pass_time(1)
    bot.digital[motor_a_pin].write(0)
    bot.digital[motor_b_pin].write(0)
    bot.digital[motor_a_speed_pin].write(0)
    bot.digital[motor_b_speed_pin].write(1)

def backward(bot:Arduino):
    bot.digital[motor_a_pin].write(1)
    bot.digital[motor_b_pin].write(1)
    bot.digital[motor_a_speed_pin].write(0)
    bot.digital[motor_b_speed_pin].write(1)
    bot.pass_time(1)
    bot.digital[motor_a_pin].write(0)
    bot.digital[motor_b_pin].write(0)
    bot.digital[motor_a_speed_pin].write(0)
    bot.digital[motor_b_speed_pin].write(1)

def left(bot:Arduino):
    bot.digital[motor_a_pin].write(1)
    bot.digital[motor_b_pin].write(1)
    bot.digital[motor_a_speed_pin].write(1)
    bot.digital[motor_b_speed_pin].write(1)
    bot.pass_time(1)
    bot.digital[motor_a_pin].write(0)
    bot.digital[motor_b_pin].write(0)
    bot.digital[motor_a_speed_pin].write(0)
    bot.digital[motor_b_speed_pin].write(0)

def right(bot:Arduino):
    bot.digital[motor_a_pin].write(1)
    bot.digital[motor_b_pin].write(1)
    bot.digital[motor_a_speed_pin].write(0)
    bot.digital[motor_b_speed_pin].write(0)
    bot.pass_time(1)
    bot.digital[motor_a_pin].write(0)
    bot.digital[motor_b_pin].write(0)
    bot.digital[motor_a_speed_pin].write(0)
    bot.digital[motor_b_speed_pin].write(0)

def stop(bot:Arduino):
    bot.digital[motor_a_pin].write(0)
    bot.digital[motor_b_pin].write(0)
    bot.digital[motor_a_speed_pin].write(0)
# bot.digital[4].write(1)
# sleep(0.1)
# bot.digital[4].write(0)
# sleep(0.1)
# bot.analog[4].write(100)
# sleep(0.1)
# bot.digital[4].write(0)

forward(bot=bot)
stop(bot=bot)
backward(bot=bot)
left(bot=bot)
right(bot=bot)