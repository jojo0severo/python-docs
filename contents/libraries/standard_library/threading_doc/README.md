## threading

Provém funcionalidades para interagir com threads em python.
Não é tão útil quanto o multiprocessing devido ao GIL, mas ainda assim é útil quando o gargalo do código é a I/O (requisições, time.sleep, leitura de arquivo, etc).