import argparse
import time


from src.downloader import Downloader
from src.exceptions import RequestBlocked
from src.logger import Logger
from src.scraper import Scraper
from src import config, helper


# CONFIGS
LOGGER = Logger()
DOWNLOAD_PATH = config.DEFAULT_DOWNLOAD_PATH

class App:
    __FILE_FORMAT = '.mp4'
    __TIMEOUT = config.BLOCKED_TIMEOUT


    def __init__(self, anime_url:str, download_path:str):
        self.__scraper = Scraper(anime_url)
        self.__downloader = Downloader(download_path)

    def download(self, episode:str) -> bool:
        while True:
            try:
                LOGGER.info(f'downloading episode {episode}')
                
                # acquire list of downloadable video urls
                videos = self.__scraper.get(episode)
                break
            except RequestBlocked:
                LOGGER.error(f'request blocked by anime heaven for episode {episode}, going to try again in {self.__TIMEOUT} seconds')
                time.sleep(self.__TIMEOUT)

        if not videos:
            LOGGER.error(f'url not found for episode {episode}')
            return False

        filename = self.__get_filename(episode)
        # NOTE: use first download url only
        todownload = videos[0]
        self.__downloader.download(filename, todownload)        

        LOGGER.info(f'downloaded episode {episode}')
        return True

    def get_downloads(self) -> dict:
        return self.__downloader.get_downloads()

    def __get_filename(self, episode:str) -> str:
        return f'Episode-{episode}{self.__FILE_FORMAT}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--anime', help='add anime url', type=str)
    parser.add_argument('-e', '--episode', help='enter episode range (1-10) or just 1 to download single episode', type=str)
    parser.add_argument('-d', '--download', help='download path, by defult download to current directory', type=str)

    args = parser.parse_args()
    # terminal can automatically add escape sequences, so remove it
    anime = args.anime.replace('\\', '') if args.anime else args.anime

    # check if given anime url is valid
    if not helper.is_valid_anime(anime):
        print('Invalid anime url')
        print('I.e. http://animeheaven.eu/i.php?a=Bakuman.')
        exit(1)
    
    episodes = helper.get_episodes(args.episode)
    # check if given episode url is valid
    if not episodes:
        print('Invalid episode(s)')
        exit(1)

    # check if download path exists
    DOWNLOAD_PATH = args.download if args.download else DOWNLOAD_PATH

    LOGGER.info(f'Download path: {DOWNLOAD_PATH}')

    app = App(anime, DOWNLOAD_PATH)
    for ep in episodes:
        app.download(ep)
