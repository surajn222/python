import traceback
import sys
import logging

print("Format Exec----------------------------")
try:
    a = 1/0
except Exception:
    print(traceback.format_exc())
    # or
    print(sys.exc_info()[2])

# print("Exc Info----------------------------")
# try:
#     a = 1/0
# except Exception:
#     print('General exception noted.', exc_info=True)

print("String e----------------------------")
try:
    a = 1/0
except Exception as e:
    print(str(e))

print("sys exc info----------------------------")
try:
    a = 1/0
except Exception:
    print(sys.exc_info())