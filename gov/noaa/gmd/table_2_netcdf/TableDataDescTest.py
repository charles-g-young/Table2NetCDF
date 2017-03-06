'''
Created on Feb 28, 2017

@author: cyoung
'''

import os
import unittest
from gov.noaa.gmd.table_2_netcdf.TableDataDesc import TableDataDesc
from gov.noaa.gmd.table_2_netcdf.TableDataDesc import GlobalAttributeDesc
from gov.noaa.gmd.table_2_netcdf.TableDataDesc import GlobalAttributeStrategyDesc
from gov.noaa.gmd.table_2_netcdf import Properties

class TableDataDescTest(unittest.TestCase):

    XML_FILE=Properties.TEST_DATA_DIR+"/dummy-data-set.xml"
    STRATEGY_CLASS="gov.noaa.gmd.table_2_netcdf.Strategies.GlobalAttributeStrategyDummy"

    def test_init(self):
        print ("working dir ", os.getcwd())
        TableDataDesc(self.XML_FILE)

    def test_getGlobalAttributeDesc(self):
        #Actual
        tableDataDesc=TableDataDesc(self.XML_FILE)
        actual=tableDataDesc.getGlobalAttributeDesc("blee")

        #Expected
        globalAttributeStrategyDesc=GlobalAttributeStrategyDesc(self.STRATEGY_CLASS)
        expected=GlobalAttributeDesc("blee", "int", globalAttributeStrategyDesc)
        self.assertEqual(actual, expected)

    def test_getGlobalAttributeStrategyDesc(self):
        #Actual
        tableDataDesc=TableDataDesc(self.XML_FILE)
        actual=tableDataDesc.getGlobalAttributeStrategyDesc("blee")

        #Expected
        expected=GlobalAttributeStrategyDesc(self.STRATEGY_CLASS)
        self.assertEqual(actual, expected)

    def test_GlobalAttributeStrategy(self):
        #Actual
        tableDataDesc=TableDataDesc(self.XML_FILE)
        actual=tableDataDesc.getGlobalAttributeStrategyDesc("blee")
        value=actual.parse("blee", "a header string")

        #Expected
        self.assertEqual(value, "dummy")