import os
import logging
from .linker import Linker


def yield_tasks(srcs, srcdir, dstdir):
    for src in srcs:
        yield os.path.join(srcdir, src), os.path.join(dstdir, src)


class LinkerMarshall:
    def __init__(self, srcs, dstdir=os.getenv('HOME')):
        self.logger = logging.getLogger(__name__)
        self.srcs = srcs
        self.dstdir = dstdir

    def run(self, srcdir):
        Linker(yield_tasks(self.srcs, srcdir, self.dstdir)).run()
