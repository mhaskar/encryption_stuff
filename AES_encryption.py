#!/usr/bin/python
from Crypto.Cipher import AES # import AES Chiper Algorithm
from termcolor import cprint #import cprint to print text with colors
from Crypto.Util import Counter #import Counter to use in CTR AES mode.
file_to_save = raw_input("[~]Please enter file name to save the cipher text >> ") #file to save the ciphertext
key = raw_input("[~]Please Enter the key (16 or 24 or 32 byte) >> ") #KEY
ctr=Counter.new(128) #counter length
mode = AES.MODE_CTR #Counter Mode
encryptor = AES.new(key, mode,counter=ctr) #Create a new AES cipher 
text = raw_input("[~]Please Enter your text >> ") #TEXT
ciphertext = encryptor.encrypt(text) #encrypt the data
try:
 f = open(file_to_save,"w") #open file to save
 f.write(ciphertext) # write chiper text to this file
 f.close() # close file
 cprint("[+]Chiper Text is saved to file {0}".format(file_to_save),"green")
except:
 cprint("[!]Error while writing to {0}".format(file_to_save),"red")
