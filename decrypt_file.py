#!/usr/bin/python3

import argparse

key = #PUT YOUR RECOVERED KEY HERE

parser = argparse.ArgumentParser(description='Decrypt .crypted files by ransomware')

parser.add_argument('-s', '--source_file', action='store', nargs="+", required=True, help="Crypted files (source files list)")
args = parser.parse_args()

for source_file in args.source_file:
    bf = open(source_file, "rb")
    nf = open(source_file + ".recovered", "wb")

    i = 0
    print("byte# bad key new str(new)")
    read_bytes = 0
    while read_bytes < 2048:
        bad_byte = bf.read(1)
        new_byte = (key[i] ^ ord(bad_byte))
        print(str(read_bytes) + " " + hex(ord(bad_byte)) + " " + hex(key[i]) + " " + hex(new_byte) + " " + str(new_byte) + " ")
        nf.write(bytes([new_byte]))
        i = i + 1
        if i > 254:
            i = 0
        read_bytes = read_bytes + 1

    while bad_byte:
        bad_byte = bf.read(1)
        nf.write(bad_byte)

    nf.close()
    bf.close()
