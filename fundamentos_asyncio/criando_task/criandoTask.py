import asyncio
from fundamentos_asyncio.util import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_for_three2 = asyncio.create_task(delay(15))
    print(type(sleep_for_three))
    print('continue')
    result = await sleep_for_three
    result = await sleep_for_three2
    print(result)
    print('final')
    for x in range(8):
        print(x)

asyncio.run(main())
