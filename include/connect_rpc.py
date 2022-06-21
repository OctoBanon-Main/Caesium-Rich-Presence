from include import messages
from secrets import token_hex
from time import time, sleep

try:
    from pypresence import Presence
except ImportError:
    messages.cleaner()
    print(messages.pypresence_import_error)
    exit()


def connection_up(profile: dict):
    presence = Presence(profile['client_id'], pipe=0, loop=None, handler=None)
    presence.connect()
    messages.cleaner()

    if profile['start']:
        profile['start'] = time()
        print(messages.parameter_start_enabled)

    if profile['join']:
        profile['join'] = token_hex(32)
        print(messages.parameter_join_enabled)

    if profile['party']:
        profile['party'] = token_hex(32)
        print(messages.parameter_party_enabled)

    try:
        print(messages.connection_up_message)
        while True:
            presence.update(state=profile['state'], details=profile['details'],
                            large_image=profile['large_image'],
                            large_text=profile['large_text'],
                            small_image=profile['small_image'],
                            small_text=profile['small_text'],
                            start=profile['start'],
                            end=profile['end'],
                            party_id=profile['party'],
                            party_size=profile['party_size'],
                            join=profile['join'])
            sleep(15)
    except ():
        print(messages.unexpected_error_occurred)
