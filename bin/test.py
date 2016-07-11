alphabet = 'abcdefghijklmnopqrstuvwxyz'
from threading import Thread

def func1():
    count = 0
    while True:
        print alphabet[count]
        if count == 25:
            count = 0
        else:
            count += 1

def func2():
    count = 0
    while True:
        print count
        if count == 25:
            count = 0
        else:
            count += 1

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()