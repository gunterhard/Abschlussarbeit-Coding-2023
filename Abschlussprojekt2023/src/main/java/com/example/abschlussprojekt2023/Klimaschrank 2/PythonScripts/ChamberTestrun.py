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


# create an instance of:
#   - climate chamber
#
# climateChamber          = FDM_ClimateChamberClassMP( ipClimateChamber );
# temperature             = -25;

# climateChamber.getChamberTemperaturePV( );
# climateChamber.switchOnChamberManualRun( )
# climateChamber.setChamberTemperatureSP( temperature );
# climateChamber.getChamberTemperatureSP( );
# climateChamber.waitChamberTemperaturePV_Event( temperature );
# climateChamber.constChamberTemperaturePV( temperature, 45 );

# climateChamber.getChamberTemperaturePV( );
# climateChamber.getChamberTemperatureSP( );
# climateChamber.getChamberHumidityPV( );
# climateChamber.getChamberHumiditySP( );

# climateChamber.setChamberTemperatureSP( 26.4 );
# climateChamber.getChamberTemperatureSP(  );
# climateChamber.setChamberTemperatureSP( 70.4 );
# climateChamber.getChamberTemperatureSP(  );
# climateChamber.setChamberTemperatureSP( 0.0 );
# climateChamber.getChamberTemperatureSP(  );
# climateChamber.setChamberTemperatureSP( -34.5 );
# climateChamber.getChamberTemperatureSP(  );
# climateChamber.setChamberTemperatureSP( -23.4 );
# climateChamber.getChamberTemperatureSP(  );

# climateChamber.setChamberHumiditySP( 99.0 );
# climateChamber.getChamberHumiditySP(  );
# climateChamber.setChamberHumiditySP( 0.0 );
# climateChamber.getChamberHumiditySP(  );
# climateChamber.setChamberHumiditySP( 25.0 );
# climateChamber.getChamberHumiditySP(  );

# climateChamber.setCorrosionProtection( )

# climateChamber.waitChamberTemperaturePV_Event( 22.0 );

# climateChamber.setHumidityControl_ON( );

# climateChamber.setHumidityControl_OFF( );

# climateChamber.switchOnHumidityControl(  );
# climateChamber.getHumidityControlState( );


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   print the duration of the actual testrun
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logger.print_Duration_Testrun();
logger.printLog( "Finished Testprocedure" );