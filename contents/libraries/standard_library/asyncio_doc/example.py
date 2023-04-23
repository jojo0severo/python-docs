import asyncio


async def sleep_2():
    print("sleeping 2")
    await asyncio.sleep(2)
    print("done sleeping 2")


async def sleep_1():
    print("sleeping 1")
    await asyncio.sleep(1)
    print("done sleeping 1")


async def sequential():
    # Espera uma task depois a outra
    # Nota que os prints são intercalados
    await sleep_1()
    await sleep_2()


async def parallel():
    # Espera as duas tasks executarem em paralelo
    # Nota que os prints não são intercalados
    # pois as duas tasks são executadas em ""paralelo""
    # O que acontece é que a chamada asyncio.sleep devolve
    # o controle de volta pro loop de execução inves de bloquear a thread
    # ao devolver o controle pro loop, a proxima task é executada
    # e assim por diante
    # O resultado final dá a impressão que é paralelo
    # mas na verdade o código só disse pra biblioteca que ele não 
    # vai executar mais nada por um tempo (esperando IO) e ele pode 
    # fazer outras coisas enquanto isso
    await asyncio.gather(sleep_1(), sleep_2())


# Antiga forma de usar asyncio
# Pode ser util quando jã houve um loop executando na aplicacao
# Por exemplo em um servidor web (fastapi) que utiliza asyncio por baixo
# dos panos para atender as requisições de forma assincrona
# Nesse caso, o loop ja foi criado e não **deve** (pode) ser criado outro

# loop = asyncio.new_event_loop()
# loop.run_until_complete(sequential())
# loop.run_until_complete(parallel())
# loop.close()

# Nova forma de usar asyncio

asyncio.run(sequential())
asyncio.run(parallel())
