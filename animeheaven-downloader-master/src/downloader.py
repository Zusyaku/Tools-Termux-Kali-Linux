import time
import os
import urllib.request


class Downloader:
    def __init__(self, directory:str):
        """ directory: where to store downloads """

        self.__directory = self.__exists(directory)
        self.__downloads = {}  # to store downloaded path with episode number

        # download progress timer
        self.__start_time = None
        self.__current_download = None


    def download(self, name:str, url:str):
        path = f'{self.get_path()}/{name}'
        self.__current_download = name

        # download
        urllib.request.urlretrieve(url, path, self.__progress_hook)
        
        if not os.path.exists(path):
            raise IOError(f'File {name} missing in directory {self.get_path()}\
                            path: {path}')
        self.__downloads[name] = path

    def get_path(self) -> str:
        return self.__directory

    def get_downloads(self) -> dict:
        return self.__downloads


    def __exists(self, directory:str) -> str:
        """ check if directory exists, else create one """

        if not os.path.isdir(directory):
            os.makedirs(directory)
        return f'{os.path.dirname( os.path.abspath(directory) )}/{directory.split("/")[-1]}'

    def __progress_hook(self, count:int, block_size:int, total_size:int):
        """ download progress hook
            https://blog.shichao.io/2012/10/04/progress_speed_indicator_for_urlretrieve_in_python.html """

        # count = 0; download starts
        if count == 0:
            self.__start_time = time.time()
            return

        duration = time.time() - self.__start_time
        downloaded = int(count * block_size)
        speed = int(downloaded / (1024 * duration))
        percent = int(count * block_size * 100 / total_size)

        # convert file size to mb for print
        downloaded_mb = f'{downloaded / (1024 * 1024):.2f}'
        total_size_mb = f'{total_size / (1024 * 1024):.2f}'

        # convert speed to mb or gb
        if len(str(speed)) < 4:
            speed_str = f'{speed:10} KB/s'
        elif len(str(speed)) >= 4 and len(str(speed)) < 7:
            speed_mb = f'{(speed / 1024):.2f} MB/s'
            speed_str = f'{speed_mb:10}'
        else:
            speed_gb = f'{(speed / 1024 / 1024):.2f} GB/s'
            speed_str = f'{speed_gb:10}'

        if percent < 100:
            print(f'{self.__current_download.ljust(20)} Percent: {percent}% {downloaded_mb.rjust(12)}/{total_size_mb} MB {speed_str}', end='\r')
        else:
            # go to newline
            print(f'{self.__current_download.ljust(20)} Percent: {percent}% {downloaded_mb.rjust(12)}/{total_size_mb} MB {speed_str}')
