import enum


@enum.unique
class TaskType(enum.Enum):
    LINK = enum.auto()
    BASH = enum.auto()
