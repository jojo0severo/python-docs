import pathlib

p = pathlib.Path(__file__)
print("\nRaw path:")
print(p)

print("\nResolve:")
print(p.resolve())

print("\nParts:")
print(p.parts)

print("\Exists:")
print(p.exists())

print("\Is absolute:")
print(p.is_absolute())

print("\nName:")
print(p.name)

print("\nIs dir:")
print(p.is_dir())

print("\Absolute path:")
print(p.absolute())



print("\nGlob:")
another_p = p.parent
for child_path in another_p.glob("*"):
    print(child_path)