from .periodic import Periodic
from .db import db
import os

# 600 seconds is every 10 minutes
RUN_EVERY_SECONDS = 600

EXTENSIONS_TO_CHECK = ["stl", "zip"]


class FileRunner(Periodic):
    """
    Scans all files in a directory and stores them to be scanned
    later by the StlRunner and ZipRunner
    """

    file_dir = ""
    is_running = False

    def __init__(self, file_dir):
        super().__init__(self.run, RUN_EVERY_SECONDS)
        self.file_dir = os.path.expanduser(file_dir)
        self.table = db.create_table(
            "file_queue", primary_id="path", primary_type=db.types.text
        )

    async def run(self):
        print("Running FileRunner")
        self.scan_dir(self.file_dir)
        print("End FileRunner")

    def scan_dir(self, dir):
        for entry in os.scandir(dir):
            if entry.is_file():
                try:
                    ext = entry.name.split(".")[-1]
                    if ext in EXTENSIONS_TO_CHECK and self.table is not None:
                        existing_record = self.table.find_one(path=entry.path)
                        if not existing_record:
                            self.table.insert(dict(path=entry.path, pending=True))
                except Exception:
                    print("Could not add", entry.path)
            else:
                self.scan_dir(entry)
