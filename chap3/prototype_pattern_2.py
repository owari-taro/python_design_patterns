from typing import Dict
import copy


class WebSite:
    def __init__(self, name, domain, description, author, **kwargs):
        self.name = name
        self.domain = domain
        self.description = description
        self.author = author
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        summary = [f"Website {self.name}"]
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == "name":
                continue
            summary.append(f"{attr}:{val}\n")
        return "".join(summary)


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f"incorrect object identifer:{identifier}")
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])
        return obj


def copy_itself(original_obj,**attrs):
    copied=copy.deepcopy(original_obj)
    for key in attrs:
        setattr(obj,key,attrs[key])
    return copied


class Person:
    def __init__(self,**kwargs):
        print(kwargs)