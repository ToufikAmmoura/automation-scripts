# !python3
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PATH = "C:\\Users\\toufi\\Downloads" 
DESTINATION = "C:\\Users\\toufi\\OneDrive\\Documenten"

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(PATH):
            src = f"{PATH}\\{filename}"
            new = f"{DESTINATION}\\{filename}"
            os.rename(src, new)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()