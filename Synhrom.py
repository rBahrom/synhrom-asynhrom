import time
from datetime import datetime


def synhrom_1():
    time.sleep(2)
    print('Synhrom 1')


def synhrom_2():
    time.sleep(2)
    print('Synhrom 2')


def synhrom_3():
    time.sleep(2)
    print('Synhrom 3')


def synhrom_4():
    time.sleep(2)
    print('Synhrom 4')
    synhrom_8()


def synhrom_5():
    time.sleep(2)
    print('Synhrom 5')


def synhrom_6():
    time.sleep(2)
    print('Synhrom 6')


def synhrom_7():
    time.sleep(2)
    print('Synhrom 7')


def synhrom_8():
    time.sleep(2)
    print('Synhrom 8')


def synhrom():
    print(datetime.now())
    print(synhrom_1())
    print(synhrom_2())
    print(synhrom_3())
    print(synhrom_4())
    print(synhrom_5())
    print(synhrom_6())
    print(synhrom_7())
    print(synhrom_8())
    print(datetime.now())


if __name__ == '__main__':
    synhrom()
