# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:18:45 2019

@author: rutherfordw
"""

import unittest

class test(unittest.TestCase):
    
  def test_suite_height_calculator(self):
    '''test height calculator implementation'''
    test_inches=0
    test_feet=6
    test_height=((int(test_feet)*12)+ int(test_inches))
    self.assertEqual(test_height,72)                           # height calculator test case
  
  def test_suite_BMI_calculator(self):
    '''test BMI calculator implementation'''
    test_weight=100.0
    test_height=120.0
    test_BMI= float(((test_weight/(test_height ** 2)) * 703))
    self.assertEqual(test_BMI,4.881944444444444 )               # BMI calculator test case

  def main(self):
    '''calls all test cases'''
    self.test_suite_height_calculator       #test height calculator
    self.test_suite_BMI_calculator             #test BMI calculator

if __name__ == '__main__':
  unittest.main()     