import os
from . import TaskType
from .task import Task
from .performer import Performer


class BashTask(Task):
    def __init__(self, cmd):
        self.type = TaskType.BASH
        self.task = cmd

    @Task.task.setter
    def task(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{value!r} is not a bash command string')

        self._task = value


class Bash(Performer):
    def perform(self, task):
        if not isinstance(task, BashTask):
            raise ValueError(f'{task!r} is not a bash task')

        os.system(task.task)
