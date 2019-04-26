import enum


@enum.unique
class TaskType(enum.Enum):
    LINK = 'link'
    BASH = 'bash'
