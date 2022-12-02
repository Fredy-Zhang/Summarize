import sys
import os

print("Dataset path: ", sys.argv[1])
files_num = 0
for (dir_path, dir_names, file_names) in os.walk(sys.argv[1]):
    files_num += len(file_names)
    print("--Directory path: ", dir_path, " --Directory name: ", dir_names, " --File number: ",len(file_names))

print("***Total Files number: ",files_num)
