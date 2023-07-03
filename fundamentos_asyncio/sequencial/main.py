import asyncio
# from util import delay


async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} second(s)')
    return delay_seconds

async def add_one(number: int) -> int:
    print('add_one')
    return number + 1

async def hello_world_message() -> str:
    print('TT')
    await delay(5)
    await add_one(3)
    return 'Hello World!'

async def main() -> None:
    message = await hello_world_message()
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)
asyncio.run(main())
