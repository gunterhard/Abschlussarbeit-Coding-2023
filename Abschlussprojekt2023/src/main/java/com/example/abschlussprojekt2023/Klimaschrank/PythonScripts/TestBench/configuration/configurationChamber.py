#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name:    configuration.py
# Description:  
# Company:      dieEntwickler Elektronik GmbH
# Author:       Manfred PEIRLEITNER
# Date:         2023/01/10
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   define 'fileUTFileNames': path and filename of the file including all testfile names to execute 
#   define 'pathUnitTests':   path of the folder where all files to execute are stored
#   define 'stoppOnFailure':  if the test procedure should stopp when an error occurs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fileUTFileNames     = "TestBench/TESTCASES_CALL.py";
pathUnitTests       = r"TestBench/TestCollection/UnitTests/";
stoppOnFailure      = False;

ipClimateChamber    = '192.168.0.41';

