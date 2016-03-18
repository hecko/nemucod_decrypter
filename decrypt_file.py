#!/usr/bin/python3

import argparse

key = (0x59, 0x6a, 0x55, 0x34, 0x4e, 0x44, 0x6b, 0x77, 0x4e, 0x6a, 0x49, 0x79, 0x4f, 0x54, 0x67, 0x7a, 0x5a, 0x6a, 0x63, 0x35, 0x4d, 0x7a, 0x64, 0x6b, 0x59, 0x7a, 0x45, 0x7a, 0x4d, 0x7a, 0x59, 0x33, 0x4e, 0x44, 0x5a, 0x6a, 0x4f, 0x54, 0x45, 0x35, 0x4d, 0x32, 0x52, 0x42, 0x65, 0x6c, 0x5a, 0x74, 0x57, 0x6a, 0x4a, 0x53, 0x4e, 0x45, 0x77, 0x79, 0x56, 0x33, 0x70, 0x42, 0x4d, 0x6b, 0x52, 0x71, 0x51, 0x6c, 0x46, 0x45, 0x62, 0x45, 0x46, 0x4b, 0x56, 0x6d, 0x70, 0x4e, 0x64, 0x33, 0x52, 0x73, 0x57, 0x6b, 0x70, 0x42, 0x65, 0x45, 0x78, 0x74, 0x51, 0x58, 0x56, 0x4e, 0x52, 0x33, 0x42, 0x71, 0x54, 0x56, 0x46, 0x50, 0x54, 0x32, 0x39, 0x49, 0x53, 0x54, 0x52, 0x48, 0x56, 0x44, 0x45, 0x30, 0x62, 0x6e, 0x68, 0x72, 0x5a, 0x33, 0x4a, 0x52, 0x52, 0x57, 0x35, 0x76, 0x53, 0x45, 0x6b, 0x32, 0x52, 0x48, 0x6c, 0x46, 0x52, 0x6c, 0x6f, 0x78, 0x59, 0x30, 0x68, 0x46, 0x55, 0x56, 0x4e, 0x61, 0x63, 0x54, 0x4e, 0x31, 0x5a, 0x6b, 0x52, 0x34, 0x63, 0x56, 0x70, 0x75, 0x4d, 0x46, 0x4e, 0x6e, 0x52, 0x6b, 0x74, 0x35, 0x54, 0x31, 0x70, 0x34, 0x64, 0x57, 0x52, 0x45, 0x53, 0x48, 0x46, 0x54, 0x62, 0x33, 0x6c, 0x6a, 0x4e, 0x45, 0x68, 0x74, 0x55, 0x31, 0x4a, 0x79, 0x56, 0x45, 0x46, 0x6f, 0x52, 0x45, 0x6c, 0x57, 0x61, 0x30, 0x46, 0x34, 0x64, 0x54, 0x4e, 0x47, 0x53, 0x55, 0x39, 0x54, 0x57, 0x6c, 0x56, 0x46, 0x5a, 0x30, 0x56, 0x56, 0x64, 0x58, 0x64, 0x47, 0x65, 0x6a, 0x6c, 0x48, 0x54, 0x44, 0x46, 0x4a, 0x56, 0x31, 0x6f, 0x7a, 0x53, 0x57, 0x35, 0x46, 0x52, 0x30, 0x45, 0x31, 0x51, 0x55, 0x68, 0x78, 0x53, 0x46, 0x70, 0x4a, 0x59, 0x32, 0x35, 0x61, 0x55, 0x31, 0x64, )

parser = argparse.ArgumentParser(description='Decrypt .crypted files by ransomware')

parser.add_argument('-s', '--source_file', action='store', nargs="+", required=True, help="Crypted file (source file)")
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