#!/usr/bin/python3
import os

key = os.environ['SECRET_KEY']

flag = open('flag.txt', 'r').read().strip()
enc_flag = ""
i = 0
while i < len(flag):
    enc_flag += format(int(flag[i:i+2], 16) ^ ord(key[i//2 % len(key)]), '02x')
    i += 2

open('enc_flag.txt','w').write(enc_flag)


