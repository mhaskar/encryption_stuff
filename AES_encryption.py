#!/usr/bin/python
from Crypto.Cipher import AES
from termcolor import cprint
from Crypto.Util import Counter
file_to_save = raw_input("[~]Please enter file name to save the cipher text >> ") #file to save the ciphertext
key = raw_input("[~]Please Enter the key (16 or 24 or 32 byte) >> ") #KEY
ctr=Counter.new(128) #counter length
mode = AES.MODE_CTR #Counter Mode
encryptor = AES.new(key, mode,counter=ctr) #Create new AES object 
text = raw_input("[~]Please Enter your text >> ") #TEXT
ciphertext = encryptor.encrypt(text) #encrypt the data
try:
 f = open(file_to_save,"w")
 f.write(ciphertext)
 f.close()
 cprint("[+]Chiper Text is saved to file {0}".format(file_to_save),"green")
except:
 cprint("[!]Error while writing to {0}".format(file_to_save),"red")
