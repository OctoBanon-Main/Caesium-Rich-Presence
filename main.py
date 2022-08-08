from sys import argv
from os import path, mkdir
from json import dump, load
try:
    from include import connect_rpc, argument_parser, messages
except ModuleNotFoundError:
    print("Looks like pypresence not installed. Install it via pip.")
    exit(0)


class Main:
    def __init__(self):
        """Class can't be used in another modules."""
        if len(argv) == 1:
            print(messages.arguments_missing)
            exit(0)
        self.params = argument_parser.args_parser()

    def create_profile(self):
        if not path.exists('profiles'):
            mkdir('profiles')

        if path.exists(f'profiles/{self.params["name"]}.json'):
            print(messages.profile_already_exists_error)
            return

        with open(f'profiles/{self.params["name"]}.json', 'w') as f:
            self.params.pop('command')
            self.params.pop('name')
            dump(self.params, f, indent=4)

            print(messages.profile_created)

    def load_profile(self):
        if not path.exists(f'profiles/{self.params["name"]}.json'):
            print(messages.profile_not_exists_error)
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
