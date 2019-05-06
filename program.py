


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------------------------')
    print('----------WIZARD DAME APP---------------')
    print('----------------------------------------')
    print()

def game_loop():

    while True:

        cmd = input('Do you [a]ttack, [r]runaway, or [l]ook around? ')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('lookaround')
        else:
            print('Ok, exiting game.... bye !')
            break


if __name__ == '__main__':
    main()
