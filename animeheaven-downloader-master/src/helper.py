from urllib.parse import urlparse

def is_valid_anime(anime:str) -> bool:
    url = urlparse(anime)
    if not (url.scheme and url.netloc and url.path and url.query):
        return False
    return True

def get_episodes(ep:str) -> list:
    # check if episode numbers are valid
    try:
        episodes = [int(episode) for episode in ep.split('-')]
    except ValueError:
        return False
    # check either range or not
    if not episodes or len(episodes) > 2:
        return False

    # if in range, generage episode numbers from x-y inclusive`
    return episodes if len(episodes) == 1 else [ep for ep in range(episodes[0], episodes[1] + 1)]
