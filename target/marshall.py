import os
import abc
import itertools
from .target import Target
from .. import task


class Marshall(abc.ABCMe, Target, task.marshall.Marshall):
    @property
    @abc.abstractmethod
    def dstdir(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def srcs(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def cmds(self):
        raise NotImplementedError

    @task.marshall.Marshall.tasks
    def tasks(self):
        return itertools.chain(
            map(self.srcToLinkerTask, self.srcs),
            map(self.cmdToBashTask, self.cmds))

    def srcToLinkerTask(self, src):
        return task.linker.LinkerTask(
            src, os.path.join(self.dstdir, os.path.basename(src)))

    def cmdToBashTask(self, cmd):
        return task.bash.BashTask(cmd)

    def run(self):
        self.perform()
