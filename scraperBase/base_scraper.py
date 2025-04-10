from abc import ABC, abstractmethod
from scraperBase.scraper_exporter import BaseExporter
from scraperBase.scraper_core import *
from typing import List

class BaseScraper(ABC):
    def __init__(self, url: str, exporters: List[BaseExporter] = None):
        self.__url = url
        self.__html = ""
        self.__data = {}
        self.__exporters = exporters

    def _fetch_html(self):
        self.__html = fetch_html(self.__url)

    @abstractmethod
    def _parse(self):
        pass

    @abstractmethod
    def _clean(self):
        pass

    def export(self, data):
        for exporter in self.__exporters:
            exporter.export(data)

    def run(self):
        self._fetch_html()
        self._parse()
        clean_data = self._clean()
        return clean_data