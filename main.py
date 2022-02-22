import asyncio
from lib.runner import Runner

files_dir = "~/sample-stl-data/"


async def test():
    print("I run")


def main():
    runner = Runner()
    loop = asyncio.new_event_loop()

    loop.create_task(runner.start())
    loop.run_forever()


main()
