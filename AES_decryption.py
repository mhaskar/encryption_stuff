#!/usr/bin/python
from Crypto.Cipher import AES
from termcolor import cprint
from Crypto.Util import Counter

file_to_read = raw_input("[~]Please enter file name to save the cipher text >> ") #file $
key = raw_input("[~]Please Enter the key (16 or 24 or 32 byte) >> ") #KEY
ctr=Counter.new(128) #counter length
mode = AES.MODE_CTR #Counter Mode
dec = AES.new(key, mode,counter=ctr)
f = open(file_to_read)
data = f.read()
f.close()
cprint("[+]Plain Text is : {0}".format(dec.decrypt(data)),"yellow")
