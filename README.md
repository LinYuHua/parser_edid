#Parser_edid
Read EDID the first 128bytes and shows on the screen.

---------------------------
the edid structure
---------------------------
refer 
https://en.wikipedia.org/wiki/Extended_Display_Identification_Data


---------------------------
How to paly
---------------------------
1. python Main.py to launch

2. select a din file.

---------------------------
Main func
---------------------------
common.func.get_data_from_byte(byte,  low_bit, high_bit =0)

Parameter:
 byte : the bin code
 low_bit & High_bit : get bits from low_bit to high_bit
 
Ouput:
 a string "11011"  etc...
---------------------------
ex:   
  get byte3 bit 2 \- 5.  
      common.func.get_data_from_byte(byte =byte3,  low_bit =2, high_bit =5)  
  get byte3 bit 7.  
      common.func.get_data_from_byte(byte =byte3,  low_bit =7, high_bit =7)  
  get byte3 bit 0 \- 7.  
      common.func.get_data_from_byte(byte =byte3,  low_bit =0, high_bit =7)  
  

P.s.
NO error handler
Not all data can be show
No GUI
Little-endian.


