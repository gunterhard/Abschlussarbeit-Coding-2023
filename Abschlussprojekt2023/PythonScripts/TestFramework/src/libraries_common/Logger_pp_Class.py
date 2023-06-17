# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name:  	Logger_Class.py
# Description:	class handling to log action, errors, results, ...
# Company:	    dieEntwickler Elektronik GmbH
# Author:	    Manfred PEIRLEITNER
# Date:		    2022/05/18
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import datetime, inspect, logging, os;

from ...constants import *;


# ----------------------------------------------------------------------------------------------------
# brief:        Logger_MP_pp
# details:      logging events
# param[in]:    ---
# param[out]:   ---
# ----------------------------------------------------------------------------------------------------
class Logger_MP_pp:
    

    """ ----------------------------------------------------------------------------------------------------
    \brief:	        constructor of Logger_MP	
    \details:	    init class variables
    \param[in]:	    ---
    \param[out]:    ---
    """
    def __init__( self ):
        """
        name contains:
            prefix "LogFile_"
            actual time
            postfix ".log"               
            file in the folder "TestBench/logFiles..."
        """
        self.start_Time = datetime.datetime.now( );
        fileTime        = datetime.datetime.now( ).strftime( STR_TIME_FORMAT_LF );
       
        fileNameLog             = STR_PREFIX_LOGFILE + fileTime + STR_POSTFIX_LOGFILE;
        self.filePathLogFile    = os.path.join( STR_PATH_LOGFILES, fileNameLog );
               
        self.printLog( );
        self.printLog( "Constructor of Logger ... logging results" );
        

   
    """ ----------------------------------------------------------------------------------------------------
    \brief:	        create_LogFile_For_Testrun	
    \details:	    method to create a logfile for the actual testrun
    \param[in]:	    ---
    \param[out]:    filePathLogFile
    """
    def create_LogFile_For_Testrun( self ):
        self.printLog( inspect.currentframe().f_code.co_name );
           
        return self.filePathLogFile;


    """ ----------------------------------------------------------------------------------------------------
    \brief:	        printLog	
    \details:	    class method to log the actual activity
    \               file in the folder "TestBench/LogFiles..."
    \param[in]:	    message  ... message concerning the actual activity
    \param[out]:    ---
    """
    def printLog( self, message = "" ):
        logging.basicConfig( filename = self.filePathLogFile, level = logging.INFO, format='%(asctime)s %(message)s' );
        logging.info( message );
        print("%s%s" % ( datetime.datetime.now().strftime( STR_TIME_FORMAT ), message ) );

     
    """ ----------------------------------------------------------------------------------------------------
    \brief:	        print_Duration_Testrun	
    \details:	    print the duration of the actual testrun
    \param[in]:	    ---
    \param[out]:    ---
    """
    def print_Duration_Testrun( self ):
        self.printLog( );
        duration = datetime.datetime.now() - self.start_Time;
        self.printLog( "%s: %s" % (inspect.currentframe().f_code.co_name, duration ) );


logger = Logger_MP_pp( );

if __name__ == '__main__':
    logger.printLog('%s self executed!' % __name__ );
else:
    logger.printLog('%s called by another module' % __name__ );