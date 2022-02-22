from .periodic import Periodic

RUN_EVERY_SECONDS = 10


class Runner(Periodic):
    is_running = False

    def __init__(self):
        super().__init__(self.run, RUN_EVERY_SECONDS)

    async def run(self):
        print("now running ")
