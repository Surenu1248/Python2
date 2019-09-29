# 9.	Create a suitable object type and  check for file size of 0 bytes of the directory

import os

b = os.path.getsize("sample.xml")

if b == 0:
    print("File does'nt contains anything...(0 Bytes)")
else:
    print("File size is : %d" % b)
