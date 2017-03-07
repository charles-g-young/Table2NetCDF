'''
Parsing strategies for use with TableDataDesc.
Created on Mar 1, 2017

@author: cyoung
'''

from gov.noaa.gmd.table_2_netcdf.TableDataSet import GlobalAttribute
from gov.noaa.gmd.table_2_netcdf.TableDataSet import Variable
from gov.noaa.gmd.table_2_netcdf.TableDataSet import VariableAttribute

#Dummy strategies for use in unit tests where we don't need a real strategy.

class GlobalAttributeStrategyDummy():
    def parse(self, attributeName, header):
        return GlobalAttribute(attributeName, attributeName)

class HeaderStrategyDummy():
    def parse(self,file):
        return "dummy"

class VariableAttributeStrategyDummy():
    def parse(self, attributeName, header):
        return VariableAttribute(attributeName, attributeName)

class VariableStrategyDummy():
    def parse(self, variableName, header):
        return Variable(variableName, variableName)
