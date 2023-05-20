import os
import shutil
path="Photos"
print("before copying the files")
print(os.listdir(path))
print("after copying the files")
source="segregate module"
destination="Photos"
copyfiles=shutil.copy(source,destination)
print(os.listdir(path))
