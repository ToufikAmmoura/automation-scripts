# !python3
import os
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

PATH = "C:\\Users\\toufi\\Downloads" 

class MyHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        command = f"python choosr-win.py {event.src_path}"
        os.system(command)

if __name__ == "__main__":
    patterns = ["*.pdf", "*tex"]
    ignore_patterns = ["*.part"]
    ignore_directories = False
    case_sensitive = True
    
    my_event_handler = MyHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    observer = Observer()
    observer.schedule(my_event_handler, PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()