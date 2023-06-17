#!/usr/bin/python3
# pyright: reportMissingImports = false, reportUndefinedVariable = false
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name:  	ChamberTestrun.py
# Description:	 
# Company:	    dieEntwickler Elektronik GmbH
# Author:	    Manfred PEIRLEITNER
# Date:		    2023/01/18
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from TestBench.configuration import *;
from TestFramework.src.libraries_common import *;
from TestFramework.src.libraries_devices import *;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# create logfile: name containing:
# prefix "LogFile_" + actual time + postfix ".log"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filePath       = logger.create_LogFile_For_Testrun( );
logger.printLog( "Beginning with Testprocedure" );


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logger.printLog( );
logger.printLog( "Perform test specification here!!!" );
logger.printLog( os.path.realpath( __file__ ) );
input( );
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   print the duration of the actual testrun
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logger.print_Duration_Testrun();
logger.printLog( "Finished Testprocedure" );