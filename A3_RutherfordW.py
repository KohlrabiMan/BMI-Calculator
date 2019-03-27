# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:58:53 2019

@author: rutherfordw
"""


class BMI(object):

  def __init__(self):
    '''global value holder'''
    self.weight=100.0              #placeholder values
    self.feet=6
    self.inches=0
    self.height=120.0

  def weight_prompt(self):
    '''ask for weight'''
    print("Starting BMI Calculator...")
    self.weight=raw_input("How much do you weigh (lbs)?")
    pass
    
  
  def weight_limit_check(self):
    ''' Check for appropriate weight.'''
    if float(self.weight) >= 1400.0 or float(self.weight) <= 4.6:             # maximum and minimum weight recorded from humans 
      print("weight limit breached user must weigh between 4.7 & 1400lbs")
      self.weight_prompt()                             #Lucia Zarate weighed 4.7lbs & Jon Brower Minnoch weighed ~1400lbs
    else:
      pass
      
  def weight_input_format_check(self):
    '''Make sure weight is integer or float string'''
    value_exception=0                                 #exception counter
    try:
      float(self.weight)
    except ValueError:                               # exception catcher not a float
      value_exception += 1
    try:
      int(self.weight)
    except ValueError:                              # exception catcher not a int
      value_exception += 1
    if value_exception >= 2:                       # if neither send back to weight prompt
      print("invalid characters detected")
      self.weight_prompt()
    else:
      pass
      
  def height_prompt1(self):
    '''start height prompt ask for intial feet'''
    print("How tall are you?")
    self.feet=raw_input("How many feet")
    pass
      
  def height_prompt2(self):
    '''ask for inches to go with feet in height'''
    self.inches=raw_input("and how many inches?")
    pass
  
  def feet_checker(self):
    '''makes sure that an appropriate amount of feet was given'''
    if int(self.feet) <=0 or int(self.feet) > 8:
      print ("height limit breached user must be between 1&9ft")
      self.height_prompt1()   # shortest human Chandra Bahadur Dangi 1'9
    else:
      pass
      
  def inch_checker(self):
    '''makes sure that an appropriate amount of inches was given'''
    if int(self.inches) <0 or int(self.inches) > 11: 
      print ("invalid inch amount input")                         # tallest human Robert Pershing Wadlow 8'11
      self.height_prompt1()                                       # redo height prompt
    else:
      pass
 
      
  def feet_input_format_check(self):
    '''Make sure feet is integer string'''
    value_exception=0                             #error counter
    try:
      int(self.feet)
    except ValueError:                          # exception catch into earlier height prompt
      value_exception += 1
    if value_exception >= 1:
      print("invalid characters detected")
      self.height_prompt1()
    else:
      pass
      
  def inch_input_format_check(self):
    '''Make sure inches is integer string'''
    value_exception=0                        #error counter
    try:
      int(self.inches)
    except ValueError:                    #exception catcher into earlier height prompt recursion
      value_exception += 1
    if value_exception >= 1:
      print("invalid characters detected")
      self.height_prompt1()
    else:
      pass
      
  def height_calculator(self):
    '''Concert feet & inches of height to just inches for the imperial BMI calculator'''
    self.height=((int(self.feet) * 12) + int(self.inches))                     #imperial height formula
    pass 
  
  def BMI_calculator(self):
    '''calculate BMI using imperial measurements via BMI equation then give a prompt to restart the program'''
    BMI= ((float(self.weight))/((int(self.height) ** 2)) * 703)    #imperial BMI equation
    print("Your BMI is " + str(BMI))                              #print BMI
    restart=raw_input("to restart press r or to quit press q:")       #restart or end prompt
    if restart == "r":
      self.main()
    elif restart == "q":
      pass


  def main(self):
    '''call functions'''
    self.weight_prompt()               #ask for weight
    self.weight_limit_check()          #check weight amount make sure it is not too much or too little
    self.weight_input_format_check()   #make sure it is either an integer or float
    self.height_prompt1()              # ask for feet of height
    self.height_prompt2()               #ask for inches of height
    self.feet_checker()                 #check feet amount make sure it is not too much or too little
    self.inch_checker()                 # check inches amount make sure it is not too much or too little
    self.feet_input_format_check()     #make sure it is an integer
    self.inch_input_format_check()     #make sure it is an integer
    self.height_calculator()            #convert feet and inches to only inches
    self.BMI_calculator()              #calculate BMI given height & weight 
    
if __name__ == '__main__':            # calls main
  objName = BMI()          
  objName.main()
  
