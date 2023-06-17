#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pyright: reportMissingImports = false, reportUndefinedVariable = false
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name:    constants_general.py
# Description:  
# Company:      dieEntwickler Elektronik GmbH
# Author:       Manfred PEIRLEITNER
# Date:         2023/01/10
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os;

MISSING                                 = "MISSING_ELEMENT";
PATH_DIRECTORY_ADDS                     = os.path.abspath( os.getcwd( ) ) + "/TestBench/adds/";
UNDEFINED                               = "UNDEFINED";
UNITTESTING_IDLE                        = "UNITTESTING IS IDLE FOR:";
UNITTESTING_PROGRESS                    = "UNITTESTING IS IN PROGRESS";

STR_ACT_TIME_STAMP                      = "Actual time stamp: ";
STR_START_TIME_TEST                     = "StartTime of testrun: ";

STR_STARTED                             = "Started!";
STR_FINISHED                            = "Finished!";

STR_FAILED                              = "FAILED";

STR_INPUT_FORMAT                        = "Your input: {0}";


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# format the time 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
STR_TIME_FORMAT                         = "%d.%m.%Y %H:%M:%S ";
STR_TIME_FORMAT_MS                      = "%d.%m.%Y %H:%M:%S.%f";
STR_TIME_FORMAT_LF                      = "%Y%m%d_%H%M%S";

STR_FLOAT_FORMAT                        = "{:0.8f}";

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# settings for file attributes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
STR_PATH_LOGFILES                       = r"TestBench\logFiles";
STR_PATH_BU_SCRIPTS                     = r"TestBench\backup_Scripts";
STR_PATH_RESOURCES                      = r"TestBench\resources";
STR_PATH_LOGGING_CONF                   = r'TestBench\logging.conf';

STR_PREFIX_LOGFILE                      = "logFile_";
STR_POSTFIX_LOGFILE                     = ".log";