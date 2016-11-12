#!/usr/bin/python

import binascii
from termcolor import cprint
from permutation import encryption
#transfer data to binary (ascii to hex) --> (hex to binary).
#generate N blocks of data , every block is 64-bit size.
encrypted_data = []
data = "Hi my name is Mohammad Askar , how are you ?"
hexed_data = binascii.hexlify(data)
binary_data = "{0:b}".format(int(hexed_data,16))
print binary_data
#################################### END OF TRANSFERRING DATA TO BINARY ####################################
cprint("Plain Text is : %s"%data,"blue")
print "+" * 60
print "total bits number :%s bits"%len(binary_data)
blocks = len(binary_data) / 64
from_index = 0
to_index = 64
cprint("[+]binary data blocks :","yellow")
for i in range(blocks):	
  data = binary_data[from_index:to_index]
  cprint("64-bit block num{0}      is : {1}".format(i+1,data),"green")
  cprint("64-bit encrypted block is : {0}".format(encryption(data)),"yellow")
  encrypted_data.append(data)
  from_index = from_index + 64
  to_index   = from_index + 64
last_index = to_index - 64
left_bits = binary_data[last_index:len(binary_data)] #binary data from last index to len
left_char = 64 - len(left_bits)

l = len(left_bits)
left_bits_data = str(binary_data[last_index:len(binary_data)]) + "1" * left_char #binary data from last index to len
last_padding_address = last_index + l
encrypted_data.append(left_bits_data) #add left bits data to the encrypted data list
print "64-bit block numf is      : {0}".format(left_bits_data)
print "64-bit encrypted block is : {0}".format(encryption(left_bits_data))
print "+" * 60
cprint("\t final block length : %s bits"%l,"red")
cprint("\t padding with       : %s bits"%left_char,"red")
cprint("\t last data value    : %s"%str(binary_data[last_index:len(binary_data)]),"red")
print "+" * 60
final_encrypted_data = "".join(encrypted_data)
cprint("[+]Final binary encrypted data : ","yellow")
cprint(final_encrypted_data,"green")
print "+" * 60
cprint("[+]Final hex encrypted data","yellow")
#print "".format(int(final_encrypted_data),)
print hex(int(final_encrypted_data,2)) 
print last_padding_address
padding_number = to_index - len(binary_data)
#################################### END OF BLOCKING AND PADDING ####################################
