import asyncio

import aiohttp


async def example_one_call():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org") as response:
            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])

            html = await response.text()
            print("Body:", html[:15], "...")


async def example_many_calls():
    async with aiohttp.ClientSession() as session:
        html = await asyncio.gather(
            *[session.get("http://python.org") for _ in range(10)]
        )
        print(html)


loop = asyncio.get_event_loop()
print("Example one call:")
loop.run_until_complete(example_one_call())
print("Example many calls:")
loop.run_until_complete(example_many_calls())
