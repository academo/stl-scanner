import asyncio
from lib.file_runner import FileRunner


# TODO move this to a config file
files_dir = "~/sample-stl-data/"


async def test():
    print("I run")


def main():
    runner = FileRunner(files_dir)
    loop = asyncio.new_event_loop()

    loop.create_task(runner.start())

    try:
        loop.run_forever()
    except Exception:
        pass


main()
