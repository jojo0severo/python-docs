from dataclasses import asdict, dataclass, field


@dataclass(frozen=True, kw_only=True)
class FrozenKwonly:
    x: int
    y: int = 10
    z: int = field(default=20, init=False)

    def __post_init__(self):
        object.__setattr__(self, "z", 30)


print(FrozenKwonly(x=1, y=2))
print(FrozenKwonly(x=1))

# Erro, kw_only
# print(FrozenKwonly(1))

# Erro, x is required
# print(FrozenKwonly(y=1))

# Erro, z is not allowed by init=False
# print(FrozenKwonly(x=1, z=10))

x = FrozenKwonly(x=10)

# Erro, frozen não permite alteração
# x.y += 1

print(asdict(x))
