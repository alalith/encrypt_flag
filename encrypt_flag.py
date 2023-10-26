key = ""
flag = open('flag.txt', 'r').read()
enc_flag = ""
for i in range(len(flag)):
    enc_flag += chr(ord(flag[i]) ^ ord(key[(i % len(key))]))

open('enc_flag.txt','w').write(enc_flag)

