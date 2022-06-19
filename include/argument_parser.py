from argparse import ArgumentParser
from _version import __version__


def args_parser():
    parser = ArgumentParser(add_help=False)
    subparser = parser.add_subparsers(dest='command', help='python %(prog)s command -h')

    create_group = subparser.add_parser('create', help='Create options commands')
    load_group = subparser.add_parser('load', help='Load options commands')
    other_group = parser.add_argument_group(title='Other options')

    create_group.add_argument('--name', '-n', type=str, required=True, help='Set profile name')
    create_group.add_argument('--client-id', '-ci', type=int, required=True, help='Set application ID.')
    create_group.add_argument('--state', '-st', type=str, required=True, help='Set state.')
    create_group.add_argument('--details', '-d', type=str, required=True, help='Set details.')
    create_group.add_argument('--start', '-s', type=bool)
    create_group.add_argument('--end', '-e', type=int)
    create_group.add_argument('--large-image', '-limage', type=str, help='Set large image.')
    create_group.add_argument('--large-text', '-ltext', type=str, help='Set text for large image.')
    create_group.add_argument('--small-image', '-simage', type=str, help='Set small image.')
    create_group.add_argument('--small-text', '-stext', type=str, help='Set text for small image.')
    create_group.add_argument('--party', '-p', type=bool, help='Enabling party presence function.')
    create_group.add_argument('--party-size', '-ps', type=int, nargs='+', help='Set party size.')
    create_group.add_argument('--join', '-j', type=bool, help='Set true for create "Join" button.')

    load_group.add_argument('--name', '-n', type=str, required=True)

    other_group.add_argument('-v', '--version', action='version',
                             version=f'Caesium Rich Presence, version: {__version__}',
                             help="Show program's version and exit.")

    parser.add_argument('-h', '--help', action='help',
                        help='Show this help message and exit.')

    args = parser.parse_args()
    arg = vars(args)
    return arg
