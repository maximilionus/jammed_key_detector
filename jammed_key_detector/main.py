from argparse import ArgumentParser


def run():
    argparser = ArgumentParser(
        description='JKD CLI Toolkit'
    )
    argparser.add_argument('--no-gui', '-T', dest='disable_gui', action='store_true',
                           help='disable gui for this application and use the terminal version')

    args = argparser.parse_args()

    if args.disable_gui:
        # TODO: Start app without GUI
        pass
    else:
        # TODO: Initialize GUI
        pass


if __name__ == '__main__':
    run()
