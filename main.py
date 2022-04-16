from sys import argv
from os import path, mkdir
from json import dump, load
from include import connect_rpc
from include import argument_parser


class Main:
    def __init__(self):
        self.params = argument_parser.args_parser()

    def create_profile(self):
        if not path.exists('profiles'):
            mkdir('profiles')
        else:
            pass

        with open(f'profiles/{self.params["name"]}.json', 'w') as f:
            self.params.pop("command")
            dump(self.params, f, indent=2)

    def load_profile(self):
        if not path.exists(f'profiles/{self.params["name"]}.json'):
            print("This profile is not exists")
            return

        with open(f'profiles/{self.params["name"]}.json') as json_file:
            profile = load(json_file)
            connect_rpc.connection_up(profile)


if __name__ == '__main__':
    main = Main()
    if argv[1] == 'create':
        main.create_profile()
    elif argv[1] == 'load':
        main.load_profile()
