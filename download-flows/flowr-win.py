# !python3
import os
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

PATH = "C:\\Users\\toufi\\Downloads" 

def on_created(event):
    print(f"{event.src_path} has been created!")
    # os.system(f"move {event.src_path} C:\\Users\\toufi\\OneDrive\\Documenten")

def on_deleted(event):
    print(f"Someone deleted {event.src_path}!")

def on_moved(event):
    print(f"someone moved {event.src_path} to {event.dest_path}")

class MyHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        print(f"{event.src_path} has been modified")
        os.system(f"move {event.src_path} C:\\Users\\toufi\\OneDrive\\Documenten")

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