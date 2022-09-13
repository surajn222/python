import os
for subdir, dirs, files in os.walk('./'):
    for file in files:
      do some stuff
      print(file)