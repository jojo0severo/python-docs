## O que é o GIL?

O GIL é um mecanismo de sincronização que garante que apenas uma thread execute o código Python por vez. Isso é necessário porque o interpretador Python não é thread-safe, ou seja, não é seguro para múltiplas threads executarem o código Python ao mesmo tempo.

## Por que o GIL existe?

O GIL foi criado para evitar que o interpretador Python tenha que lidar com situações de concorrência. Isso é necessário porque o interpretador Python não é thread-safe, ou seja, não é seguro para múltiplas threads executarem o código Python ao mesmo tempo.