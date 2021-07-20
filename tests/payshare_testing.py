import sys

file = __file__.replace('\\','/')
top_folder = "/".join(file.split('/')[:-2])

sys.path.append(top_folder)