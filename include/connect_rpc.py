from pypresence import Presence
from include import messages
from time import time, sleep
from os import system


def connection_up(profile: dict):
    presence = Presence(profile["client_id"], pipe=0, loop=None, handler=None)
    presence.connect()

    if profile["start"]:
        profile["start"] = time()

    messages.cleaner()
    print(messages.connection_up_message)

    while True:
        presence.update(state=profile["state"], details=profile["details"],
                        large_image=profile["large_image"],
                        large_text=profile["large_text"], small_image=profile["small_image"],
                        small_text=profile["small_text"], start=profile["start"], end=profile["end"])
        sleep(15)
