'''

Given a table-oriented text data file, a descriptive XML file and an outputFile name
convert the text data file into a netCDF file.
Created on Feb 27, 2017

@author: cyoung
'''

import sys
from gov.noaa.gmd.table_2_netcdf.TableDataDesc import TableDataDesc
from gov.noaa.gmd.table_2_netcdf.TableDataSet import TableDataSet
from gov.noaa.gmd.table_2_netcdf.NetCDFWriter import NetCDFWriter

class Table2NetCDF :
  
    def  __init__ (self, inputFile, xmlFile, outputFile):
        self.inputFile=inputFile
        self.xmlFile=xmlFile
        self.outputFile=outputFile
        print ('inputFile ', self.inputFile)
        print ('xmlFile ', self.xmlFile)
        print ('outputFile ', self.outputFile)

    def convert (self):
        #Parse the XML file.
        tableDataDesc=TableDataDesc(self.xmlFile)
        tableDataDesc.parse()
        #Parse the data file.
        tableDataSet=TableDataSet(self.inputFile, tableDataDesc)
        tableDataSet.parse()
        #Write the netCDF file
        netCDFWriter=NetCDFWriter(tableDataSet, self.outputFile)
        netCDFWriter.write()

if __name__ == "__main__":
    table2NetCDF=Table2NetCDF(sys.argv[1],sys.argv[2],sys.argv[3])
    table2NetCDF.convert()
