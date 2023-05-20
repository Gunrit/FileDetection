import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source="segregate module"
destination="Photos"
dir_tree = { "Image_Files": ['.jpg','.jpeg', '.png', '.gif', '.jfif'],
 "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
  "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
   "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event)
    name,extension = os.path.splittext(event.src_path)
    time.sleep(1)
    for i,j in dir_3.items():
        time.sleep(1)
        ifextension in j:
            filename = os.path.basename(event.src_path)
            print("Files downloaded")
            path1=source + '/' +filename
             path2=destination + '/' +i 
             path3=destination + '/' +i + "/" +filename
             if os.path.exists(path2):
                  shutil.move(path1,path3)
                  print('files moved succsesfully') 
             else: os.makedirs(path2)
                   shutil.move(path1,path3) 
                   print('files moved succsesfully')
                   time.sleep(1)
EventHandler=FileMovementHandler()
observer=Observer()
observer.schedule(EventHandler,source,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Code is running")
except KeyboardInterrupt:
    print("Watchdog stopped")
    observer.stop()      

