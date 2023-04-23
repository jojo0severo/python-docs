from enum import auto, Enum


class NotEnum:
    A = "a"
    B = "b"
    C = "c"


class IsEnum(Enum):
    A = "a"
    B = "b"
    C = "c"


class IsStrEnum(str, Enum):
    A = "a"
    B = "b"
    C = "c"


class IsAutoEnum(Enum):
    A = auto()
    B = auto()
    C = auto()


class IsAutoStrEnum(str, Enum):
    A = auto()
    B = auto()
    C = auto()



print("NotEnum: ", NotEnum.A)
print("IsEnum: ", IsEnum.A, IsEnum.A.name, IsEnum.A.value)
print("IsStrEnum: ", IsStrEnum.A,  IsStrEnum.A.name, IsStrEnum.A.value)
print("IsAutoEnum: ", IsAutoEnum.A, IsAutoEnum.A.name, IsAutoEnum.A.value)
print("IsAutoStrEnum: ", IsAutoStrEnum.A, IsAutoStrEnum.A.name, IsAutoStrEnum.A.value)
