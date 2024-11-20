import asyncio

async def say_hello():
    print("Hola")
    await asyncio.sleep(1)
    print("Mundo")

async def main():
    await say_hello()

asyncio.run(main())