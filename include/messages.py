from os import system


def cleaner():
    system('cls||clear')


def colorizer(r, g, b, text):
    return '\033[38;2;{};{};{}m{} \033[38;2;255;255;255m'.format(r, g, b, text)


# Errors
profile_not_exists_error = colorizer(177, 0, 0, '[ERROR]') + 'This profile are not exists!'
profile_already_exists_error = colorizer(177, 0, 0, '[ERROR]') + 'This profile already exists!'
unexpected_error_occurred = colorizer(177, 0, 0, '[ERROR]') + 'Unexpected error occurred'

# Messages
profile_created_message = colorizer(0, 217, 145, '[LOG]') + 'Profile created!'
connection_up_message = colorizer(0, 217, 145, '[LOG]') + 'Rich Presence client connected!'
parameter_start_enabled = colorizer(0, 217, 145, '[LOG]') + 'Parameter "start" enabled, starting timer in presence!'
parameter_join_enabled = colorizer(0, 217, 145, '[LOG]') + 'Parameter "join" enabled, creating fake "Join" button!'
parameter_party_enabled = colorizer(0, 217, 145, '[LOG]') + 'Parameter "party" enabled!'