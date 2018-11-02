#!/usr/bin/env python3

import sys
import os
src_img = 'cgi-bin/hellocam.jpg'

sys.stdout.write("Content-Type: image/png\n")
sys.stdout.write("Content-Length: {}\n".format(str(os.stat(src_img).st_size)))
sys.stdout.write("\n")
sys.stdout.flush()
with open(src_img, 'rb') as img_file:
    contents = img_file.read()
sys.stdout.buffer.write(contents)
