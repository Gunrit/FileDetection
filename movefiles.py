import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Use absolute paths to avoid errors
source = r"C:\Users\gunri\OneDrive\Desktop\WHJJ\segregation-main\segregate module"
destination = r"C:\Users\gunri\OneDrive\Desktop\WHJJ\Photos"

# File types dictionary
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Make sure source folder exists
if not os.path.exists(source):
    os.makedirs(source)

# Make sure destination folder exists
if not os.path.exists(destination):
    os.makedirs(destination)

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Only handle files, not directories
        if event.is_directory:
            return

        # Extract file extension
        _, extension = os.path.splitext(event.src_path)
        extension = extension.lower()  # make case-insensitive

        time.sleep(1)  # wait for file to be fully written

        for folder_name, extensions in dir_tree.items():
            if extension in extensions:
                filename = os.path.basename(event.src_path)
                print(f"File detected: {filename}")

                path1 = os.path.join(source, filename)
                path2 = os.path.join(destination, folder_name)
                path3 = os.path.join(path2, filename)

                # Create folder if it does not exist
                if not os.path.exists(path2):
                    os.makedirs(path2)

                # Move file
                try:
                    shutil.move(path1, path3)
                    print(f"Moved '{filename}' to '{path2}' successfully.")
                except Exception as e:
                    print(f"Error moving file {filename}: {e}")
                break


if __name__ == "__main__":
    event_handler = FileMovementHandler()
    observer = Observer()
    observer.schedule(event_handler, source, recursive=True)
    observer.start()
    print("Watching started on", source)
    try:
        while True:
            time.sleep(2)
            # Optional: print("Code is running")
    except KeyboardInterrupt:
        print("Stopping watchdog...")
        observer.stop()
    observer.join()
