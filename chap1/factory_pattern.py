import json
import xml.etree.ElementTree as entree


class JsonDataExtractor:
    def __init__(self,filepath):
        self.data={}
        with open(filepath,mode="r",encoding="utf-8")as reader:
            self.data=json.load(f)

    @property
    def _parsed_data(self):
        return self.data
    
class XMLDataExtractor:
    def __init__(self,filepath):
        self.tree=etree.parse(filepath)
    @property
    def parsed_data(self):
        return self.tree
    
def dataextraction_factory(filepath):
    if filepath.endswith("json"):
        extractor=JsonDataExtractor
    elif filepath.endswith("xml"):
        extractor=XMLDataExtractor
    else:
        raise ValueError(f"cannot extract data from {filepath}")
    return extractor(filepath)

