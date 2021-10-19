from urllib.parse import urlparse

from bs4 import BeautifulSoup
from selenium.common import exceptions as SeleniumExceptions
from selenium import webdriver

from .exceptions import DriverNotFound, RequestBlocked
from . import config


class Scraper:
    """ Animeheaven do their best to prevent automated downloadings,
      so I have to find a workaround """
    
    __ABUSE_MSG = config.ANIMEHEAVEN_ABUSE_MSG
    __PHANTOMJS_INSTALL_MSG = 'npm -g install phantomjs-prebuilt'


    def __init__(self, anime:str):
        self.__anime = self.__convert_url(anime)
        self.__driver = self.__get_driver()

    def get(self, episode:str) -> list:
        """ return list of download links for given episode """

        url = f'{self.__anime}{episode}'
        self.__driver.get(url)
        source = self.__driver.page_source

        # check if website already blocked anime request,
        # will do nothing if not blocked, else raise Exception
        self.__is_blocked(source)

        soup = BeautifulSoup(source, 'html.parser')
        result = soup.find_all('source')
        # if search not found, return None
        return [ download['src'] for download in result ] if result else None


    def __get_driver(self) -> object:
        try:
            # TODO: PhantomJS is deprecated, will have to replace
            return webdriver.PhantomJS()
        except SeleniumExceptions.WebDriverException:
            raise DriverNotFound('PhantomJS not found in the system')

    def __is_blocked(self, html:str) -> bool:
        if html.find(self.__ABUSE_MSG) != -1:
            raise RequestBlocked
        return False

    def __convert_url(self, url:str) -> str:
        """convert anime overall preview url to episode url"""
        
        url = urlparse(url)
        return f'{url.scheme}://{url.netloc}/watch.php?{url.query}&e='
