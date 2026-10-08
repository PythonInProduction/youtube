async def main():
    ta = asyncio.create_task(fetch("a"))
    tb = asyncio.create_task(fetch("b"))
    a = await ta
    b = await tb
