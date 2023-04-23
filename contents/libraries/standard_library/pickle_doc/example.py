import pickle

print("Dumps:")
print(pickle.dumps([1, 2, 3, "a", "b", "c"]))
print(pickle.dumps("hello"))
print(pickle.dumps(None))
print(pickle.dumps(True))

print("\nLoads:")
print(pickle.loads(pickle.dumps([1, 2, 3, "a", "b", "c"])))
print(pickle.loads(pickle.dumps("hello")))
print(pickle.loads(pickle.dumps(None)))
print(pickle.loads(pickle.dumps(True)))

print("\nPickling and unpickling a file:")
with open("example_dump.txt", "wb") as f:
    pickle.dump([1, 2, 3, "a", "b", "c"], f)

with open("example_load.txt", "rb") as f:
    print(pickle.load(f))

print("\nPickling and unpickling a file with a custom class:")
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyClass({self.x}, {self.y})"
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __getstate__(self):
        return self.x, self.y
    
    def __setstate__(self, state):
        self.x, self.y = state

with open("example_dump_class.txt", "wb") as f:
    pickle.dump(MyClass(1, 2), f)


with open("example_load_class.txt", "rb") as f:
    print(pickle.load(f))