#Video input parameters bitmap
# coding=utf-8
import common.func
def parameters(edid_table):
	print "  Basic display parameters. "
	if (int(edid_table[20],16) & 0x80 ):
		print "Digital"
		print ("bit depth : %s" %(bit_depth(edid_table_20 = edid_table[20])))
		print ("video_inferface : %s" %(video_interface(edid_table_20 = edid_table[20])))
		print ("screen H size : %d" %(screen_h_size( edid_table_21 =  edid_table[21])))
		print ("screen V size : %d" %(screen_v_size( edid_table_22 =  edid_table[22])))
		print ("screen Gamma : %d" %(screen_gamma( edid_table_23 =  edid_table[23])))
	else :
		print ("EDID version @@ : %s" %(screen_h_size( edid_table_21 =  edid_table[23])))

	print ("Supported features bitmap ")
	print ("  DPMS standby supported %s" %(dpms_standby_supported( edid_table_24 =  edid_table[24])))
	print ("  DPMS suspend supported %s" %(dpms_suspend_supported( edid_table_24 =  edid_table[24])))
	print ("  DPMS active-off  supported %s" %(dpms_active_off_supported( edid_table_24 =  edid_table[24])))
	print ("  Display type %s" %(display_type( edid_table_20 =  edid_table[20], edid_table_24 =  edid_table[24])))
	print ("  Standard sRGB colour space %s" %(standard_srgb_colour_space( edid_table_24 =  edid_table[24])))
	print ("  Preferred timing mode specified in descriptor block 1 %s" %(preferred_timing_mode_pecified_in_where( edid_table_24 =  edid_table[24])))
	print ("  Continuous timings with GTF or CVT %s" %(continuous_timings_with_gtf_or_cvt( edid_table_24 =  edid_table[24])))
#	print ("  DPMS active-off  supported" %(support_features_bitmap( edid_table_24 =  edid_table[24])))


def bit_depth(edid_table_20):
	bits = {
		000:"undefined",
		001:"6 bits per color",
		010:"8 bits per color",
		011:"10 bits per color",
		100:"12 bits per color",
		101:"14 bits per color",
		110:"16 bits per color",
		111:"reserved"
	}

	return bits.get(common.func.get_data_from_byte(byte = edid_table_20, low_bit = 4,high_bit =6 ))


def video_interface(edid_table_20):

	interface = {
	0000 : "undefined",
	0001 : "HDMIa",
	0010 : "HDMIb",
	0100 : "MDDI",
	0101 : "DisplayPort"
	}
	return interface.get(common.func.get_data_from_byte(byte = edid_table_20, low_bit = 0,high_bit = 3 ))

def screen_h_size(edid_table_21):
	#in centimetres (range 1-255). If vsize=0, landscape aspect ratio (range 1.00-3.54), datavalue = (AR×100)-99 (example: 16:9 = 79, 4:3 = 34)
	return int(common.func.get_data_from_byte(byte = edid_table_21, low_bit = 0,high_bit = 7 ),2)
def screen_v_size(edid_table_22):
	#in centimetres. If hsize=0, portrait aspect ratio (range 0.28-0.99), datavalue = (100/AR)-99 (example: 9:16 = 79, 3:4 = 34). If either byte is 0, screen size and aspect ratio are undefined (e.g. projector)
	return int(common.func.get_data_from_byte(byte = edid_table_22, low_bit = 0,high_bit = 7 ),2)
def screen_gamma(edid_table_23):
	#Display gamma, factory default (range 1.00–3.54), datavalue = (gamma×100)-100 = (gamma−1)×100. If 225, gamma is defined by DI-EXT block.
	return int(common.func.get_data_from_byte(byte = edid_table_23, low_bit = 0,high_bit = 7 ),2)

def dpms_standby_supported(edid_table_24):
	return common.func.get_data_from_byte(byte = edid_table_24, low_bit = 7,high_bit = 7 )

def dpms_suspend_supported(edid_table_24):
	return common.func.get_data_from_byte(byte = edid_table_24, low_bit = 6,high_bit = 6 )

def dpms_active_off_supported(edid_table_24):
	return common.func.get_data_from_byte(byte = edid_table_24, low_bit = 5,high_bit = 5 )

def display_type(edid_table_20, edid_table_24):
	digital_type = {
		00 : "RGB 4:4:4",
		01 : "RGB 4:4:4 + YCrCb 4:4:4",
		10 : "RGB 4:4:4 + YCrCb 4:2:2",
		11 : "RGB 4:4:4 + YCrCb 4:4:4 + YCrCb 4:2:2"
	}
	analog_type = {
		00 : "Monochrome or Grayscale",
		01 : "RGB color",
		10 : "Non-RGB color",
		11 : "Undefined"
	}
	displaytype = common.func.get_data_from_byte(byte = edid_table_24, low_bit = 3, high_bit = 4 )
	if( common.func.get_data_from_byte(byte = edid_table_20, low_bit = 7, high_bit = 7 ) == 1):
		return digital_type.get(displaytype)
	else:
		return analog_type.get(displaytype)

def standard_srgb_colour_space(edid_table_24):
	return common.func.get_data_from_byte(byte = edid_table_24, low_bit = 2,high_bit = 2 )

def preferred_timing_mode_pecified_in_where(edid_table_24):
	return common.func.get_data_from_byte(byte = edid_table_24, low_bit = 1,high_bit = 1 )

def continuous_timings_with_gtf_or_cvt(edid_table_24):
	return common.func.get_data_from_byte(byte = edid_table_24, low_bit = 0,high_bit = 0 )













def test(edid_table_21):
	low = 2
	print ("edid table 11 bit %s = %s" %( low, common.func.get_data_from_byte(byte = edid_table_21,low_bit=low)))
	low = 5
	print ("edid table 11 bit 5 = %s" %(common.func.get_data_from_byte(byte = edid_table_21,low_bit=low)))
	low =7
	high =7
	print ("edid table 11 bit %s~%s = %s" %(low, high, common.func.get_data_from_byte(byte = edid_table_21,low_bit=low, high_bit = high)))
	low = 2
	high =7
	print ("edid table 11 bit %s~%s = %s" %(low, high, common.func.get_data_from_byte(byte = edid_table_21,low_bit=low, high_bit = high)))
	print ("edid table 11 bit %s~%s = %s" %(low, high, common.func.get_data_from_byte(byte = edid_table_21,low_bit=low, high_bit = high)))
	print ("edid table 11 bit %s~%s = %s" %(low, high, common.func.get_data_from_byte(byte = edid_table_21,low_bit=low, high_bit = high)))
