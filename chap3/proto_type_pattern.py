import copy


class WebSite:
    def __init__(self, name, domain, description, author, **kwargs):
        self.name = name
        self.domain = domain
        self.descriptiona = description
        self.author = author
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def _str__(self):
        summary = [f'Website "{self.name}"\n']
        infos = var(self).items()
        ordered_infos = sorted(infos)
        for attr, val in orderd_infos:
            if attr == "name":
                continue
            summary.append(f'{attr}:{val}')
        return ''.join(summary)

class Prototype:
    def __init__(self):
        self.objects=dict()
    def register(self,identifier,obj):
        self.objects[identifier]=obj
    def unregister(self,identifier):
        del self.objects[identifier]]
    def clone(self,identifier,**attrs):
        found=self.objects.get(identifier)
        if not found:
            raise ValueError(f"incorret object identifier {identifier}")
        obj=copy.deepcopy(found)
        for key in attrs:
            setattr(obj,key,attrs[key])
        return obj