# pyright: reportMissingImports = false, reportUndefinedVariable = false
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name:    UnitAssert_pp_Class.py
# Class Name:   UnitAssertMP_pp
# Description:
# Company:      dieEntwickler Elektronik GmbH
# Author:       Manfred PEIRLEITNER
# Date:         2021/07/29
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import inspect;

import numpy as np;
from TestFramework.src.libraries_common import *;

EMPTY_ARG       = "EMPTY_ARGUMENT";
NOT_VALID_ARG   = "NOT_VALID_ARGUMENT";
OKAY            = "OK";

# ----------------------------------------------------------------------------------------------------
# brief:        UnitAssertMP_pp
# details:      
# param[in]:    ---
# param[out]:   ---
# ----------------------------------------------------------------------------------------------------
class UnitAssertSimpleMP_Class:

    unitName        = "UnitAssertMP_pp";
    unitDescr       = "Library with test functions (assertEquals, assertTrue, ...";
    version         = 1.1;
    company         = "dieEntwickler Elektronik GmbH";
    unitDate        ="July 2021 - ???";
    author          = "Manfred PEIRLEITNER"
    
    # ----------------------------------------------------------------------------------------------------
    #\brief:         __init__
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ---------------------------------------------------------------------------------------------------- 
    def __init__( self ):
        logger.printLog( "Constructor of UnitAssertMP_pp %s" % STR_STARTED );
        
        logger.printLog( "Constructor of UnitAssertMP_pp %s" % STR_FINISHED );
        

    # ----------------------------------------------------------------------------------------------------
    #\brief:            __del__
    #\details:      
    #\param[in]:        ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def __del__( self ):
        pass;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         printDescription
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------

    def printDescription( self ):
        
        logger.printLog( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" );
        logger.printLog( "INFORMATION ABOUT THE USED ASSERT-UNIT" );
        logger.printLog( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" );
        logger.printLog( "Name of the Unit: \t\t {0}".format( self.unitName ) );
        logger.printLog( "Unit Description: \t\t {0}".format( self.unitDescr) );
        logger.printLog( "Version of the Unit: \t {0}".format( self.version ) );
        logger.printLog( "Company created: \t\t {0}".format( self.company ) );
        logger.printLog( "Date of creation: \t\t {0}".format( self.unitDate) );
        logger.printLog( "Author of the Unit: \t {0}".format( self.author) );
        logger.printLog( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" );
        logger.printLog( );


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertFirstArgLowerOrEQ
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertFirstArgLowerOrEQ( self, expression1 = None, expression2 = None ):
        
        # Initialize returnValue
        
        errorReturn = "NOT_LOWER_NOT_EQUAL";

        # Check that the arguments are not empty
        # Check that the arguments are not empty
        if( ( expression1 == None ) and ( expression2 == None ) ):
            returnValue = "EMPTY_ARGS for BOTH EXPRESSIONS";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression1 == None ):
            returnValue = "EMPTY_ARGS for EXPRESSION 1";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        if( expression2 == None ):
            returnValue = "EMPTY_ARGS for EXPRESSION 2";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        

        # Check if arguments are of the same type
        if( type( expression1 ) != type ( expression2 ) ):
            returnValue = "Type MISMATCH: type of expression 1 = {0}, type of expression 2 = {1}".format( type( expression1 ), type( expression2 ) );
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        
        if( isinstance( expression1, str ) or isinstance( expression2, str ) ):
            returnValue = "Type STRING ... not possible to compare for lower or higher";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;


        # Evaluate expressions, then check if result are equal
        if( expression1 <= expression2 ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;

        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
        return errorReturn;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertSecondArgHigher
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertSecondArgHigher( self, expression1 = None, expression2 = None ):
        
        errorReturn = "NOT_HIGHER";

        # Check that the arguments are not empty
        # Check that the arguments are not empty
        if( ( expression1 == None ) and ( expression2 == None ) ):
            returnValue = "EMPTY_ARGS for BOTH EXPRESSIONS";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression1 == None ):
            returnValue = "EMPTY_ARGS for EXPRESSION 1";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        if( expression2 == None ):
            returnValue = "EMPTY_ARGS for EXPRESSION 2";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        

        # Check if arguments are of the same type
        if( type( expression1 ) != type ( expression2 ) ):
            returnValue = "Type MISMATCH: type of expression 1 = {0}, type of expression 2 = {1}".format( type( expression1 ), type( expression2 ) );
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        
        if( isinstance( expression1, str ) or isinstance( expression2, str ) ):
            returnValue = "Type STRING ... not possible to compare for lower or higher";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        # Evaluate expressions, then check if result are equal
        if( expression1 < expression2 ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;

        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
        return errorReturn;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertEquals
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertEquals( self, expression1 = None, expression2 = None ):
        
        # Initialize returnValue
        errorReturn = "NOT_EQUAL";

        # Check that the arguments are not empty
        if( ( expression1 == None ) and ( expression2 == None ) ):
            returnValue = "EMPTY_ARGS for BOTH EXPRESSIONS";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression1 == None ):
            returnValue = "EMPTY_ARGS for EXPRESSION1";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression2 == None ):
            returnValue = "EMPTY_ARGS for EXPRESSION2";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
    
        try:
            expression1 = str( expression1 );
            expression2 = str( expression2 );
        except:
            returnValue = "Type MISMATCH: type of expression 1 = {0}, type of expression 2 = {1}".format( type( expression1 ), type( expression2 ) );
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        # Check if arguments are of the same type
        #if( type( expression1 ) != type ( expression2 ) ):
        #    returnValue = "Type MISMATCH: type of expression 1 = {0}, type of expression 2 = {1}".format( type( expression1 ), type( expression2 ) );
        #    logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
        #    return returnValue;

        # Evaluate expressions, then check if result are equal 
        if( expression1 != expression2 ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
            return errorReturn;

        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
        return OKAY;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertEQUALS
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertEQUALS( self, expression1 = None, expression2 = None ):
        return self.assertEquals( expression1, expression2 );


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertEqualsList
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertEqualsList( self, expression1 = None, expression2 = None ):
        
        errorReturn = "NOT_EQUAL '{0}', '{1}'";
        
        # Check that the arguments are not empty
        if( ( expression1 == None ) and ( expression2 == None ) ):
            returnValue = "EMPTY_ARGS_for_both_expressions";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression1 == None ):
            returnValue = "EMPTY_ARG_for_EXPRESSION1";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression2 == None ):
            returnValue = "EMPTY_ARG_for_EXPRESSION2";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        # Compare the lists
        if( set( expression1 ) != set( expression2 ) ):
            returnValue = errorReturn.format( expression1, expression2);
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
        return OKAY;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertEqualsArray
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertEqualsArray( self, expression1 = None, expression2 = None ):
        
        # set error return value to default
        errorReturn = "NOT_EQUAL'{0}', '{1}'";

        # Check that the arguments are not empty
        if( ( expression1 == None ) and ( expression2 == None ) ):
            returnValue = "EMPTY_ARGS for both expressions";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression1 == None ):
            returnValue = "EMPTY_ARG for EXPRESSION1";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression2 == None ):
            returnValue = "EMPTY_ARG for EXPRESSION2";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        
        expression1 = np.array( expression1 );
        expression2 = np.array( expression2 );

        if( np.array_equiv( expression1, expression2 ) ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;
        else:
            returnValue = errorReturn.format( expression1, expression2 );
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertEqualsReal
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertEqualsReal( self, expression1 = None, expression2 = None, range = None ):
        # set error return value to default
        errorReturn = "NOT_EQUALS_REAL ";
        
        #   Check that the arguments are not empty
        if( expression1 == None ):
            returnValue = "EMPTY_ARG for EXPRESSION1";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return False;
        elif( expression2 == None ):
            returnValue = "EMPTY_ARG for EXPRESSION2";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return False;
        elif( range == None ):
            returnValue = "EMPTY_ARG for Range";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return False;

        #   evaluate expression1
        if( ( not isinstance( expression1 , int ) ) and ( not isinstance( expression1, float ) ) ):
            try:
                expression1 = int( expression1 );
            except:
                try:
                    expression1 = float( expression1 );
                except:
                    returnValue = "NO_Float_NO_Integer ({0})".format( expression1 );
                    logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
                    return False;

        #   evaluate expression2
        if( ( not isinstance( expression2, int ) ) and ( not isinstance( expression2, float ) ) ):
            try:
                expression2 = int( expression2 );
            except:
                try:
                    expression2 = float( expression2 );
                except:
                    returnValue = "NO_Float_NO_Integer ({0})".format( expression2 );
                    logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
                    return False;

        #   evaluate expression3
        if( ( not isinstance( range, int ) ) and ( not isinstance( range, float ) ) ):
            try:
                range = int( range );
            except:
                try:
                    range = float( range );
                except:
                    returnValue = "NO_Float_NO_Integer ({0})".format( range );
                    logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
                    return False;

        if( range >= abs( expression1 - expression2) ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return True;
        else:
            returnValue = errorReturn + "Expression 1 = {0}, Expression 2 = {1}, Range = {2}".format( expression1, expression2, range );
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return False;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertEqualsREAL
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertEqualsREAL(self, expression1 = None, expression2 = None, range = None ):
        return self.assertEqualsReal( expression1, expression2, range );


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertTrueOrFalse
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertTrueOrFalse( self, expression = None ):
        
        # set error return value to default 
        errorReturn = "True_OR_False_expected";
        #Check that the arguments are not empty

        if( expression == None ):
            returnValue = EMPTY_ARG;
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if ( isinstance( expression, bool ) ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;
        else:
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
            return errorReturn;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertFalse
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertFalse( self, expression = None ):  
        #Check that the arguments are not empty
        if( expression == None ):
           returnValue = EMPTY_ARG;
           logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
           return returnValue;

        # set error return value to default 
        errorReturn = "NOT_False-False_expected:";

        if ( not isinstance( expression, bool ) ):
            returnValue = "No_Boolean-Boolean-expected";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression == False ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;

        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
        return errorReturn;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertFALSE
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertFALSE( self, expression = None ):
        return self.assertFalse( expression );


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertTrue
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertTrue( self, expression = None ):  
        #Check that the arguments are not empty
        if( expression == None ):
           returnValue = EMPTY_ARG;
           logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
           return returnValue;

        # set error return value to default 
        errorReturn = "NOT_True-True_expected";
    
        if ( not isinstance( expression, bool ) ):
            returnValue = "No_Boolean-Boolean_expected";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression == True ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;
        
        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
        return errorReturn;


# ----------------------------------------------------------------------------------------------------
    #\brief:         assertTRUE
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertTRUE( self, expression = None ):
        return self.assertTrue( expression );


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertNotEquals
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertNotEquals( self, expression1 = None, expression2 = None ):

        # set error return value to default "EQUAL - NOT EQUAL expected"
        errorReturn = "EQUAL-NOT_EQUAL_expected";

        # Check that the arguments are not empty
        if( expression1 == None ):
            returnValue = "EMPTY_ARG_for_EXPRESSION1";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        elif( expression2 == None ):
            returnValue = "EMPTY_ARG_for_EXPRESSION2";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        # check if either argument is of integer type; mustn't compare integers
        # with doubles
        if( isinstance( expression1, int ) ):
            if ( not isinstance( expression2, int ) ):
                returnValue = "ARG_MISMATCH_(Integer-NO_Integer)";
                logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
                return returnValue;
        if( isinstance( expression2, int ) ):
            if ( not isinstance( expression1, int ) ):
                returnValue = "ARG_MISMATCH_(NO_Integer-Integer)";
                logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
                return returnValue;

        if( expression1 == expression2):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
            return errorReturn;

        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
        return OKAY;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertNOTEquals
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertNOTEquals( self, expression1 = None, expression2 = None ):
        return self.assertNotEquals( expression1, expression2 );



    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertXOrY
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertXOrY( self, expression = None, X = None, Y = None ):  
        
        #Check that the arguments are not empty
        if( expression == None ):
            returnValue = EMPTY_ARG;
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        elif( X == None ):
            returnValue = "EMPTY_ARG_for_X";
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;
        elif( Y == None ):
            returnValue = "EMPTY_ARG_for_Y";
            return returnValue;
    
        # Evaluate expression, then check if result is X
        if( expression == X ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;

        # Evaluate expression, then check if result is X
        if( expression == Y ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
            return OKAY;

        returnValue = "Expression_{0}_is_NOT_{1}_and_NOT_{2}".format( expression, X, Y );
        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
        return returnValue;



    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertNotNull
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertNotNull( self, expression = str( ) ):
        # Initialize returnValue
        errorReturn = "None";
    
        # Check that the arguments are not empty
        if( expression == str( ) ):
            returnValue = "Empty_Argument"
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, returnValue ) );
            return returnValue;

        if( expression == None ):
            logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, errorReturn ) );
            return errorReturn;

        logger.printLog("%s: %s" % ( inspect.currentframe().f_code.co_name, OKAY ) );
        return OKAY;


    # ----------------------------------------------------------------------------------------------------
    #\brief:         assertNOTNull
    #\details:   
    #\   
    #\param[in]:     ---
    #\param[out]:    ---
    # ----------------------------------------------------------------------------------------------------
    def assertNOTNull( self, expression = None ):
        return self.assertNotNull( expression );
