'''

Given an table oriented text file with header and a TableDataDesc that describes the
file, make global attributes, variables, variable attributes and the table data
available.

Created on Feb 27, 2017

@author: cyoung
'''

from gov.noaa.gmd.table_2_netcdf.Util import Util
#from gov.noaa.gmd.table_2_netcdf.TableDataDesc import GlobalAttributeStrategyDesc

class DataSet:
    def  __init__ (self, inputFileName, dataSetDesc):
        self.inputFileName=inputFileName
        self.dataSetDesc=dataSetDesc
        self.file = open(inputFileName, "r", encoding="utf-8")
        headerStrategyDesc=dataSetDesc.getHeaderStrategyDesc()
        util=Util()
        c=util.getClass(headerStrategyDesc.getStrategyClassName())
        self.header=c.parse(self.file)
        
    def getAllGlobalAttributes(self):
        globalAttributeDescs=self.dataSetDesc.getAllGlobalAttributeDesc()
        globalAttributes=[]
        for d in globalAttributeDescs:
            globalAttributeStrategyDesc=d.getGlobalAttributeStrategyDesc()
            globalAttributes.append(globalAttributeStrategyDesc.parse(d.getAttributeName(),
                                    self.header))
        return globalAttributes

    def getAllVariables(self):
        variableDescs=self.dataSetDesc.getAllVariableDesc()
        variables=[]
        for d in variableDescs:
            variableStrategyDesc=d.getVariableStrategyDesc()
            variables.append(variableStrategyDesc.parse(d.getVariableName(),
                                    self.header))
        return variables

    def getGlobalAttribute(self, attributeName):
        pass
    def getVariable(self, variableName):
        pass
    def getVariableAttribute(self, variableName):
        pass

    def getAllVariableAttributes(self, variableName):
        variableAttributeDescs=self.dataSetDesc.getAllVariableAttributeDesc()
        variableAttributes=[]
        for d in variableAttributeDescs:
            variableAttributeStrategyDesc=d.getVariableAttributeStrategyDesc()
            variableAttributes.append(variableAttributeStrategyDesc.parse(d.getVariableName(),
                                    self.header))
        return variableAttributes

    def __eq__(self, other):
        if self.inputFileName != other.inputFileName:
            return False
        if self.dataSetDesc != other.dataSetDesc:
            return False
        return True

class GlobalAttribute:
    def  __init__ (self, name, value):
        self.name=name
        self.value=value
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def __eq__(self, other):
        if self.name != other.name:
            print(self.name+" "+"other.name")
            return False
        if self.value != other.value:
            print(self.value+" "+"other.value")
            return False
        return True

class Variable:
    def  __init__ (self, name, value):
        self.name=name
        self.value=value
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.value != other.value:
            return False
        return True

class VariableAttribute:
    def  __init__ (self, name, value):
        self.name=name
        self.value=value
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.value != other.value:
            return False
        return True

class Row:
    pass

class TableDataSet (DataSet):

    def  __init__ (self, inputFileName, tableDataDesc):
        super().__init__(inputFileName,tableDataDesc)
        self.tableDataDesc=tableDataDesc
        self.inputFileName=inputFileName

    def parse(self):
        pass
    
    def getRows(self):
        pass

    def __eq__(self, other):
        if self.inputFileName != other.inputFileName:
            return False
        if self.tableDataDesc != other.tableDataDesc:
            return False
        return True
    pass