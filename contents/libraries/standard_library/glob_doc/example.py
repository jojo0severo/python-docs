from glob import glob


for path in glob("../*/*.py"):
    print(path)
