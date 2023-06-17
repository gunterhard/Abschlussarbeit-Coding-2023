# pyright: reportMissingImports = false, reportUndefinedVariable = false
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name:  	CommInterfaceMP_pp.py
# Class Name:  	CommInterface_pp.py
# Description:	
# Company:	    dieEntwickler Elektronik GmbH
# Author:	    Manfred PEIRLEITNER
# Date:		    2022/05/18
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from ..libraries_common import *;

# ----------------------------------------------------------------------------------------------------
# brief:        CommInterface_pp
# details:      
# param[in]:    ---
# param[out]:   ---
# ----------------------------------------------------------------------------------------------------
class CommInterface_pp( object ):

    # ----------------------------------------------------------------------------------------------------
    # brief:        read   
    # details:   
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------        
    def read( self, params ):
        logger.printLog("%s: CommInterface_pp" % inspect.currentframe().f_code.co_name );
        
        
    # ----------------------------------------------------------------------------------------------------
    # brief:        write    
    # details:   
    # param[in]:    params
    # param[in]:    value   to set
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------        
    def write( self, params, value ):
        logger.printLog("%s: CommInterface_pp" % inspect.currentframe().f_code.co_name );

        
    # ----------------------------------------------------------------------------------------------------
    # brief:        exec     
    # details:   
    # param[in]:    params
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------        
    def exec( self, params ):
        logger.printLog("%s: CommInterface_pp" % inspect.currentframe().f_code.co_name );
