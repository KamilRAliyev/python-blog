import os

from reader.compressed import gzipped, bzipped

EXTENTION_MAP = {
    ".bz2": bzipped.opener,
    ".gz": gzipped.opener
}


class Reader:
    def __init__(self, filename):
        self.filename = filename
        extension = os.path.splitext(filename)[1]
        # if extension is in map, will be used one of them, else it will use just open func
        opener = EXTENTION_MAP.get(extension, open)
        self.f = open(self.filename, "rt")

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
