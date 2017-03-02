'''
Created on Feb 28, 2017

@author: cyoung
'''

import os
import unittest
from TableDataDesc import TableDataDesc
from TableDataDesc import GlobalAttributeDesc
from TableDataDesc import GlobalAttributeStrategyDesc

class TableDataDescTest(unittest.TestCase):
    def test_init(self):
        print ("working dir ", os.getcwd())
        TableDataDesc("table-data-set.xml")

    def test_getGlobalAttributeDesc(self):
        #Actual
        tableDataDesc=TableDataDesc("table-data-set.xml")
        actual=tableDataDesc.getGlobalAttributeDesc("blee")

        #Expected
        globalAttributeStrategyDesc=GlobalAttributeStrategyDesc(
            "gov.noaa.gmd.table_2_netcdf.GlobalAttributeStrategy.StrategyDummy")
        expected=GlobalAttributeDesc("blee", "int", globalAttributeStrategyDesc)
        self.assertEqual(actual, expected)

    def test_getGlobalAttributeStrategyDesc(self):
        #Actual
        tableDataDesc=TableDataDesc("table-data-set.xml")
        actual=tableDataDesc.getGlobalAttributeStrategyDesc("blee")

        #Expected
        expected=GlobalAttributeStrategyDesc(
            "gov.noaa.gmd.table_2_netcdf.GlobalAttributeStrategy.StrategyDummy")
        self.assertEqual(actual, expected)

    def test_GlobalAttributeStrategy(self):
        #Actual
        tableDataDesc=TableDataDesc("table-data-set.xml")
        actual=tableDataDesc.getGlobalAttributeStrategyDesc("blee")
        value=actual.parse("blee", "a header string")

        #Expected
        self.assertEqual(value, "dummy")
