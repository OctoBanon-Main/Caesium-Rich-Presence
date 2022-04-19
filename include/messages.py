from os import system


def cleaner():
    system("cls||clear")


def colorizer(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


# Errors
profile_not_exists_error = colorizer(177, 0, 0, "[ERROR]") + "This profile is not exists!"

# Messages
profile_created_message = colorizer(0, 217, 145, "[LOG]") + "Profile created!"
connection_up_message = colorizer(0, 217, 145, "[LOG]") + "Rich Presence client connected!"
