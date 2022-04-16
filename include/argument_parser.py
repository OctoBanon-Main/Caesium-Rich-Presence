from argparse import ArgumentParser
from _version import __version__


def args_parser():
    parser = ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    create_group = subparser.add_parser('create')
    load_group = subparser.add_parser('load')
    other_group = parser.add_argument_group(title="Other options")

    create_group.add_argument('--name', '-n', type=str, required=True)
    create_group.add_argument('--client-id', '-ci', type=int, required=True)
    create_group.add_argument('--state', '-s', type=str, required=True)
    create_group.add_argument('--details', '-d', type=str, required=True)
    # create_group.add_argument('--start-timestamp', '-st', type=bool)
    # create_group.add_argument('--end-timestamp', '-et', type=int)
    create_group.add_argument('--large-image', '-li', type=str)
    create_group.add_argument('--large-text', '-lt', type=str)
    create_group.add_argument('--small-image', '-si', type=str)
    create_group.add_argument('--small-text', '-stext', type=str)

    load_group.add_argument('--name', '-n', type=str, required=True)

    other_group.add_argument('-v', '--version', action='version',
                             version="Simple Discord Rich Presence client, version: " + __version__)

    args = parser.parse_args()
    arg = vars(args)
    return arg
