# normalmente é importado somente "import json" e utilizado "json.dump"
# mas para simplificar a vida foram explicitamente importandas as funcoes
from json import dumps, dump, load, loads 



# loads() converte uma string json para um objeto python
x = loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(x)

# load() carrega o json de um arquivo e converte para um objeto python
with open('example.json', 'r') as f:
    data = load(f)
print(data)

# dumps() converte um objeto python para uma string json
print(dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

# dump() converte um objeto python para uma string json e salva em um arquivo
with open('example_out.json', 'w') as f:
    dump(x, f)
