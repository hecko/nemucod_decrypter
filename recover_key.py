#!/usr/bin/python3

import sys

# good file is the same file from backups
good_file = "DSC05334.JPG.original"
bad_file = "DSC05334.JPG.crypted"

key = []

gf = open(good_file, "rb")
bf = open(bad_file, "rb")

i = 0
good_byte = gf.read(1)
bad_byte  = bf.read(1)

print("byte# good bad key")
while i < 600:
    key.append(ord(good_byte) ^ ord(bad_byte))
    print(str(i) + " " + hex(ord(good_byte)) + " " + hex(ord(bad_byte)) + " " + hex(key[i]))
    bad_byte = bf.read(1)
    good_byte = gf.read(1)
    i = i+1

i = 0
print("KEY: ")
print('key = (', end="")
while i < 255:
    if key[i] == key[i+255]:
        print(hex(key[i]) + ", ", end="")
    else:
        print("Failed to find decryption key!")
        sys.exit(1)
    i = i + 1
print(')')
print()
gf.close()
bf.close()
