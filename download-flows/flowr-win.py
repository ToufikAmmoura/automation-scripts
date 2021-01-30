# !python3
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

PATH = "C:\\Users\\toufi\\Downloads" 

def on_created(event):
    print(f"{event.src_path} has been created!")
    os.system(f"move {event.src_path} C:\\Users\\toufi\\OneDrive\\Documenten")

def on_deleted(event):
    print(f"Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"{event.src_path} has been modified")
    os.system(f"move {event.src_path} C:\\Users\\toufi\\OneDrive\\Documenten")

def on_moved(event):
    print(f"someone moved {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    # event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(my_event_handler, PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()