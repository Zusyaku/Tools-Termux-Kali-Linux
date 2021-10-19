import time


def start(delay):
    while 1:
        print('\r[kuzuri-chan]: sleeping for %s seconds ' % delay, end=' ')
        if delay == 0:
            print()
            break
        time.sleep(1)
        delay -= 1

if __name__ == '__main__':
    import sys
    start(int(sys.argv[1]))
