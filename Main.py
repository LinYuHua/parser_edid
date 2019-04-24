import header.show
import basic.display
import chromaticity.coordinates
import established.timing
import standard.timing
import detailed.timing
import read.edid
import common.func

table = read.edid.openfile()
#print(table)

header.show.info(table)
basic.display.parameters(table)
chromaticity.coordinates.info(table)
standard.timing.information(table)
established.timing.bitmap(table)
standard.timing.information(table)
detailed.timing.descriptor(table)#include standard timing information
