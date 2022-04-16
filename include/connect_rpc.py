from pypresence import Presence
from time import time, sleep


def connection_up(profile: dict):
    presence = Presence(profile["client_id"], pipe=0, loop=None, handler=None)
    presence.connect()
    print("RPC Connected")
    while True:
        presence.update(state=profile["state"], details=profile["details"],
                        large_image=profile["large_image"],
                        large_text=profile["large_text"], small_image=profile["small_image"],
                        small_text=profile["small_text"])
        sleep(15)
