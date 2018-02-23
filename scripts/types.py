import json


class Media(object):
    __slots__ = ('publisher', 'title', 'month', 'day', 'year', 'video', 'url')

    def __init__(self, g):
        self.publisher = g[0]
        self.title = g[1]
        self.month = g[2]
        self.day = g[3]
        self.year = g[4]
        self.video = True if g[5].find('video') >= 0 else False
        self.url = g[6]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def build_media(g):
    return {
        'publisher': g[0],
        'title': g[1],
        'month': g[2],
        'day': g[3],
        'year': g[4],
        'video': True if g[5].find('video') >= 0 else False,
        'url': g[6],
    }
