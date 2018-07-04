'''
Created on 1 Jul. 2018

@author: Danny
'''
import unittest
import os
from HtmlTestRunner import HTMLTestRunner
from LoginPage import LoginPage


# get the directory path to output report file
dir = os.getcwd()

# get all tests from LoginPage class
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginPage)

# create a test suite
test_suite = unittest.TestSuite(login_test)

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(output='example_suite')

# run the suite using HTMLTestRunner
runner.run(test_suite)