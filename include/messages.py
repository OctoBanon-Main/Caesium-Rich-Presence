from os import system, name


def cleaner():
    system("cls" if name == "nt" else "clear")


def colorizer(r, g, b, text):
    return '\033[38;2;{};{};{}m{}\033[38;2;255;255;255m'.format(r, g, b, text)


# Errors
profile_not_exists_error = f'{colorizer(177, 0, 0, "[ERROR]")} Cant find profile with given name!'
profile_already_exists_error = f'{colorizer(177, 0, 0, "[ERROR]")} This profile already exists!'
unexpected_error_occurred = f'{colorizer(177, 0, 0, "[ERROR]")} Unexpected error occurred. Exiting...'

# Messages
arguments_missing = f'{colorizer(177, 0, 0, "[ERROR]")} No arguments provided. Run Caesium with \'help\' command ' \
                    f'to get arguments list.'
profile_created = f'{colorizer(0, 217, 145, "[LOG]")} Profile created!'
client_connected = f'{colorizer(0, 217, 145, "[LOG]")} Rich Presence client connected!'
option_start_enabled = f'{colorizer(0, 217, 145, "[LOG]")} Found "start" option, starting timer in presence.'
option_join_enabled = f'{colorizer(0, 217, 145, "[LOG]")} Found "join" option, creating fake "Join" button.'
option_party_enabled = f'{colorizer(0, 217, 145, "[LOG]")} Found "party" option.'
