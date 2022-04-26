from os import system, name


def cleaner():
    system("cls" if name == "nt" else "clear")


def colorizer(r, g, b, text):
    return '\033[38;2;{};{};{}m{} \033[38;2;255;255;255m'.format(r, g, b, text)


# Errors
profile_not_exists_error = f'{colorizer(177, 0, 0, "[ERROR]")} This profile are not exists!'
profile_already_exists_error = f'{colorizer(177, 0, 0, "[ERROR]")} This profile already exists!'
unexpected_error_occurred = f'{colorizer(177, 0, 0, "[ERROR]")} Unexpected error occurred'

# Messages
profile_created_message = f'{colorizer(0, 217, 145, "[LOG]")} Profile created!'
connection_up_message = f'{colorizer(0, 217, 145, "[LOG]")} Rich Presence client connected!'
parameter_start_enabled = f'{colorizer(0, 217, 145, "[LOG]")} Parameter "start" enabled, starting timer in presence!'
parameter_join_enabled = f'{colorizer(0, 217, 145, "[LOG]")} Parameter "join" enabled, creating fake "Join" button!'
parameter_party_enabled = f'{colorizer(0, 217, 145, "[LOG]")} Parameter "party" enabled!'
