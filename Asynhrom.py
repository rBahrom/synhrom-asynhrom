import asyncio
from  datetime import datetime


async def async_1():
    await asyncio.sleep(3)
    print('Asynchrom 1')


async def async_2():
    await asyncio.sleep(1)
    print('Asynchrom 2')


async def async_3():
    await asyncio.sleep(4)
    print('Asynchrom 3')


async def async_4():
    await asyncio.sleep(6)
    print('Asynchrom 4')


async def async_5():
    await asyncio.sleep(2)
    print('Asynchrom 5')


async def async_6():
    await asyncio.sleep(8)
    print('Asynchrom 6')


async def async_7():
    await asyncio.sleep(5)
    print('Asynchrom 7')


async def async_8():
    await asyncio.sleep(0)
    print('Asynchrom 8')


async def one():
    print(datetime.now())
    await asyncio.gather(async_1(), async_2(), async_3(), async_4(), async_5(), async_6(), async_7(), async_8())
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(one())
