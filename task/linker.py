import os
import logging
import errno
from . import TaskType
from .task import Task
from .performer import Performer


class LinkerTask(Task):
    def __init__(self, src, dst):
        self.type = TaskType.LINK
        self.task = (src, dst)

    @Task.task.setter
    def task(self, value):
        if len(value) != 2:
            raise ValueError(f'{value!r} is not a linker task')

        self._task = value


class Linker(Performer):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def perform(self, task):
        src, dst = task
        self.link(src, dst)

    def link(self, src, dst):
        self.check_src(src)
        self.prepare_dst(dst)
        self.do_link(src, dst)

    def check_src(self, src):
        if not os.path.isfile(src):
            self.logger.error('Failed to find {}'.format(src))
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), src)

    def prepare_dst(self, dst):
        if not os.path.exists(dst):
            self.logger.info('Creating directories for {}'.format(dst))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
        elif os.path.isfile(dst):
            self.logger.info('File {} already exists'.format(dst))
            self.replace_dst(dst)

    def replace_dst(self, dst):
        dstdst = '{}.pre-dotfiles-distributor'.format(dst)
        self.logger.info('Moving {} to {}'.format(dst, dstdst))
        if os.path.isfile(dstdst):
            os.remove(dstdst)

        os.replace(dst, dstdst)

    def do_link(self, src, dst):
        self.logger.info('Linking {} to {}'.format(src, dst))
        os.link(src, dst)
