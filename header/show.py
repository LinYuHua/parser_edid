def info(edid_table):
	print "head info"

	print ("Manufacturer ID : %s%s%s" %(manufact_id_first_letter(edid_table[8]),manufact_id_second_letter(str1 = edid_table[8], str2 = edid_table[9]),manufact_id_third_letter(edid_table[9])))
	print ("Manufacturer product code : %s%s" %(edid_table[11],edid_table[10]))
	print ("Serial number : %s%s%s%s" %(edid_table[15],edid_table[14],edid_table[13],edid_table[12]))
	print ("Week of manufacture : %d" %(int(edid_table[16],16)))
	print ("Year of manufacture : %d" %(1990 + int(edid_table[17],16)))
	print ("EDID version : %s" %(edid_table[18]))
	print ("EDID revision: %s" %(edid_table[19]))

def manufact_id_first_letter(str):
	first_letter = 0x7c
	str = (first_letter & (int(str,16)))>>2
	return chr(str+0x40)
	#return chr(int(str,16)+0x40)
	#return bin(int(str,16))[2:]

def manufact_id_second_letter(str1, str2):
	second_letter_byte_8 = 0x03
	second_letter_byte_9 = 0xe0
	str1 = (second_letter_byte_8 & (int(str1,16)))<<3
	str2 = (second_letter_byte_9 & (int(str2,16)))>>5
        str = str1+str2
	return chr(str+0x40)
	#return chr(int(str,16)+0x40)
	#return bin(int(str,16))[2:]

def manufact_id_third_letter(str):
	third_letter = 0x1f
	str = third_letter & (int(str,16))
	return chr(str+0x40)
	#return chr(int(str,16)+0x40)
	#return bin(int(str,16))[2:]
