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
