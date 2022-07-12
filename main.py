from sys import argv
from os import path, mkdir
from json import dump, load
from include import connect_rpc, argument_parser, messages


class Main:
    def __init__(self):
        """This class can't used in another modules."""
        self.params = argument_parser.args_parser()

    def create_profile(self):
        if not path.exists('profiles'):
            mkdir('profiles')

        if path.exists(f'profiles/{self.params["name"]}.json'):
            messages.cleaner()
            print(messages.profile_already_exists_error)
            return

        with open(f'profiles/{self.params["name"]}.json', 'w') as f:
            self.params.pop('command')
            self.params.pop('name')
            dump(self.params, f, indent=4)

            messages.cleaner()
            print(messages.profile_created_message)

    def load_profile(self):
        if not path.exists(f'profiles/{self.params["name"]}.json'):
            messages.cleaner()
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
