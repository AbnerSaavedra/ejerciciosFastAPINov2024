import asyncio

async def task1():
    print("Tarea 1: Inicio")
    await asyncio.sleep(2)
    print("Tarea 1: Fin")

async def task2():
    print("Tarea 2: Inicio")
    await asyncio.sleep(1)
    print("Tarea 2: Fin")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
