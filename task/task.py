from . import TaskType
import abc


class Task(abc.ABCMeta):
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value not in TaskType:
            raise ValueError(f'Task {value} is not one of TaskType enum')

        self._type = value

    @property
    def task(self):
        return self._task

    @task.setter
    @abc.abstractmethod
    def task(self, value):
        raise NotImplementedError
