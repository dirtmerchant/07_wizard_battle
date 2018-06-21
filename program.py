from actors import Wizard, Creatures


def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------')
    print('    Wizard Game App')
    print('-----------------------')
    print()


def game_loop():
    creatures = [
        Creatures(),
        Creatures(),
        Creatures(),
        Creatures(),
        Creatures(),
    ]

    hero = Wizard()

    while True:

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('Ok Exiting game. Bye.')
            break


if __name__ == '__main__':
    main()
