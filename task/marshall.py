import os
import errno
from . import TaskType
from .task import Task
from .performer import Performer
from .linker import LinkerTask, Linker
from .bash import BashTask, Bash


class BackendedPerformer(Performer):
    def __init__(self, backends):
        self.backends = backends

    def perform(self, task):
        if not isinstance(task, Task):
            raise ValueError(f'{task!r} is not a task')

        self.backends[task.type].perform(task)


class Marshall(Performer):
    def __init__(self, dotfiles, skip_bash):
        if not os.path.isdir(dotfiles):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), dotfiles)

        self.dotfiles = dotfiles
        self.skip_bash = skip_bash
        self.performer = BackendedPerformer({
            TaskType.LINK: Linker(),
            TaskType.BASH: Bash(),
        })

    def perform(self, task):
        task = self.parse_task(task)
        self.performer.perform(task)

    def parse_task(self, task):
        type, task = task['type'], task['task']
        type = TaskType[type.upper()]
        if type == TaskType.LINK:
            src, dst = task['src'], task['dst']
            return LinkerTask(os.path.join(self.dotfiles, src),
                              os.path.expandvars(dst))
        elif type == TaskType.BASH and not self.skip_bash:
            return BashTask(task['cmd'])
