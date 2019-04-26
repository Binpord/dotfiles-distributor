import os
import errno
import enum
from .task import Task
from .performer import Performer
from .linker import LinkerTask, Linker
from .bash import BashTask, Bash


@enum.unique
class TaskType(enum.Enum):
    LINK = 'link'
    BASH = 'bash'


class BackendedPerformer(Performer):
    def __init__(self, backends):
        self.backends = backends

    def perform(self, task):
        if not isinstance(task, Task):
            raise ValueError(f'{task!r} is not a task')

        self.backends[task.type].perform(task)


class Marshall(Performer):
    def __init__(self, dotfiles):
        if not os.path.isdir(dotfiles):
            raise FileNotFoundError(
                errno.ENOENT, errno.strerror(errno.ENOENT), dotfiles)

        self.dotfiles = dotfiles
        self.performer = BackendedPerformer({
            TaskType.LINK: Linker(),
            TaskType.BASH: Bash(),
        })

    def perform(self, task):
        task = self.parse_task(task)
        self.performer.perform(task)

    def parse_task(self, task):
        if 'type' not in task or 'task' not in task:
            raise ValueError(f'{task} is not a valid task')

        type, task = task['type'], task['task']
        if type == TaskType.LINK:
            src, dst = task.get('src'), task.get('dst')
            if src is None or dst is None:
                raise ValueError(f'{task!r} is not a valid linker task')

            return LinkerTask(os.path.join(self.dotfiles, src),
                              os.path.expandvars(dst))
        elif type == TaskType.BASH:
            cmd = task.get('cmd')
            if cmd is None:
                raise ValueError(f'{task!r} is not a valid bash task')

            return BashTask(cmd)
        else:
            raise ValueError(f'{type} is not a task type')
