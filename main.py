import sys
import database


def main(x):
    x = int(x)
    if x < 0 or x > 250:
        print('Invalid value of x')
        exit()
    else:
        database.save_to_db(x)


if __name__ == '__main__':
    main(sys.argv[1])
