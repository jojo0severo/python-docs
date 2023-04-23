## multiprocessing

A biblioteca multiprocessing do python permite que você execute várias tarefas simultaneamente em um programa. Isso é feito usando processos, que são instâncias separadas de um programa Python. Cada processo tem seu próprio espaço de endereçamento, então, por exemplo, duas variáveis com o mesmo nome em processos diferentes não são a mesma variável.


A biblioteca burla a ideia do GIL (Global Interpreter Lock) do Python, que impede que mais de uma thread seja executada ao mesmo tempo. O GIL é necessário para que o interpretador Python seja seguro, mas ele pode ser um problema quando se deseja executar várias tarefas simultaneamente. A biblioteca multiprocessing permite que você execute várias tarefas simultaneamente, mesmo que o seu programa seja escrito em Python.