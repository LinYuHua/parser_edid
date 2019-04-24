def get_data_from_byte(byte ,low_bit = 0,high_bit = 0, font = 'HEX'):
	bits = {
	        0 : 0x1,
                1 : 0x2,
                2 : 0x4,
                3 : 0x8,
                4 : 0x10,
                5 : 0x20,
                6 : 0x40,
                7 : 0x80
	}
	if low_bit > 7 or low_bit < 0 : return 0
	if high_bit > 7 or high_bit < 0 : return 0
	processing=int(byte,16)
	print ("hex : %s " %(format(processing,'#010b')))
	if high_bit == 0 or (high_bit == low_bit):
#		print "bits value is %s" %( bits.get(low_bit))
		if  (processing & bits.get(low_bit)) == 0 :
			return 0
		else:
			return 1
	elif high_bit < low_bit:
		return  format((processing >> high_bit),'#010b')[(10-(low_bit-high_bit+1)):]
	else:
		#print (">> %s = %s" %( low_bit, format((processing >> low_bit),'#010b')))
		#print ("<< %s + 2 = %s" %( high_bit, format((processing >> low_bit),'#010b')[(10-(high_bit-low_bit+1)):]))
		return  (format((processing >> low_bit),'#010b')[(10-(high_bit-low_bit+1)):])
		return  int(format((processing >> low_bit),'#010b')[(10-(high_bit-low_bit+1)):])
