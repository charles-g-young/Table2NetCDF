'''

Given an table oriented text file with header and a TableDataDesc that describes the
file, make global attributes, variables, variable attributes and the table data
available.

Created on Feb 27, 2017

@author: cyoung
'''

import gov.noaa.gmd.table_2_netcdf.TableDataDesc

class DataSet :
    def  __init__ (self, inputFile, dataSetDesc):
        self.inputFile=inputFile
        self.dataSetDesc=dataSetDesc
    def getVariable(self, variableName):
        pass
    def getAllVariables(self):
        pass

class Variable :
    def  __init__ (self, name, value):
        self.name=name
        self.value=value
    def getName(self):
        return self.name
    def getValue(self):
        return self.value

class TableDataSet (DataSet):

    def  __init__ (self, inputFile, tableDataDesc):
        self.tableDataDesc=tableDataDesc
        self.inputFile=inputFile

    def parse(self):
        pass

class TableDataDesc :
    pass

class Row :
    pass