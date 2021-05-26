import json
from xml.etree import ElemenTree as etree

from abc import ABCMeta, abstractmethod


class Character(ABCMeta):
    @abstractmethod
    def interact_with(self):
        pass


class Extractor(ABCMeta):
    @abstractmethod
    def parsed_data(self):
        pass


class JSONDataExtractor(Extractor):
    def __init__(self, filepath):
        self._data = dict()
        with open(filepath, "r", encoding="utf-8")as reader:
            self._data = json.load(reader)

    @property
    def parsed_data(self):
        return self._data


class XMLDataExtractor(Extractor):
    def __init__(self, filepath):
        self._tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self._tree
