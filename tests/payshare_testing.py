import sys

file = __file__.replace('\\','/')
source_folder = "/".join(file.split('/')[:-2]) + "/source"


sys.path.append(source_folder)