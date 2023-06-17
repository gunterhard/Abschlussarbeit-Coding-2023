# pyright: reportMissingImports = false, reportUndefinedVariable = false
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name:    FDM_ClimateChamber.py
# Class Name:   FDM_ClimateChamberClassMP
# Description:  
# Company:      dieEntwickler Elektronik GmbH
# Author:       Manfred PEIRLEITNER
# Date:         2023/01/10
# Revision:     ongoing
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import sqlite3

# Verbindung zur Datenbank herstellen oder erstellen
conn = sqlite3.connect('Abschlussprojekt_db.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()





from pyModbusTCP.client import ModbusClient;
import time;
import sys;

from ..libraries_common import *;
from ..libraries_devices import *;


MB_ADDR_TEMPERATURE_PV              = 1000;
MB_ADDR_HUMIDITY_PV                 = 1002;
MB_ADDR_TEMPERATURE_SP              = 2020;
MB_ADDR_HUMIDITY_SP                 = 2022;
MB_ADDR_MANUAL_RUN                  = 3500;
MB_ADDR_HUMIDITY_CONTROL            = 3503;

LIMIT_BINARY_COMPLEMENT             = 32767;
MAX_BINARY_VALUE                    = 65535;

MIN_TEMPERATURE_SP                  = -25.0;
MAX_TEMPERATURE_SP                  = 70.0;

MIN_HUMIDITY_SP                     = 10.0;
MAX_HUMIDITY_SP                     = 98.0;

CORROSION_PROTECTION_TEMPERATURE    = 60.0;
CORROSION_PROTECTION_HUMIDITY       = 10.0;


# ----------------------------------------------------------------------------------------------------
# brief:        FDM_ClimateChamberClassMP
# details:      
# param[in]:    
# param[out]:   ---
# ----------------------------------------------------------------------------------------------------
class FDM_ClimateChamberClassMP( object ):


    # ----------------------------------------------------------------------------------------------------
    # brief:        __init__
    # details:      
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def __init__( self, host ):

        logger.printLog( );
        logger.printLog( "Constructor of FDM_ClimateChamberMP ( %s ) Started" % host );

        idSlave             = 255;
        self.bytesRead      = 2;

        try:
            self.client = ModbusClient(
                host        = host,
                unit_id     = idSlave,
                auto_open   = True,
                auto_close  = True
            );

        except:
            logger.printLog( '%s: ... NOT CONNECTED ...' % inspect.currentframe( ).f_code.co_name );
            logger.printLog( '%s: Application will be terminated ... NOT CONNECTED!' % inspect.currentframe( ).f_code.co_name );
            sys.exit( );


        logger.printLog("Constructor of FDM_ClimateChamberMP ( %s ) Finished!" % host );


    # ----------------------------------------------------------------------------------------------------
    # brief:        __del__
    # details:      destructor of class
    # param[in]:    clode the opened comport
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def __del__( self ):
        #self.setChamberManualStopp_NoLog( );
        pass;
        

    # ----------------------------------------------------------------------------------------------------
    # brief:        convertReadingData  
    # details:      convert the data: 
    #                   ... 2er complement for negative values
    #                   ... values are returned without the comma ( 234 ... 23.4 )
    # param[in]:    data    as int value
    # param[out]:   data    as float value
    # ----------------------------------------------------------------------------------------------------
    def convertReadingData( self, data: int ) -> float:
        if( data > LIMIT_BINARY_COMPLEMENT ):
            data = -( MAX_BINARY_VALUE - data + 1 );
            
        result = data / 10;
        return result;        


    # ----------------------------------------------------------------------------------------------------
    # brief:        assertLimits  
    # details:      check the name of the calling function
    #               - if temperature setpoint, check allowed range of temperature   ( -25.0 ... +70.0 )
    #               - if humidity setpoint, chekc allowed range of the humidity     ( +10.0 ... +98.0 )
    # param[in]:    data    as float
    # param[out]:   data    float value within ranges
    # ----------------------------------------------------------------------------------------------------
    def assertLimits( self, data ):

        if( inspect.stack( )[ 1 ][ 3 ] == 'setChamberTemperatureSP' ):        
            if( data < MIN_TEMPERATURE_SP ):
                logger.printLog( '%s: Setpoint ( %s°C ) IS OUT OF RANGE' % ( inspect.currentframe().f_code.co_name, data ) );
                logger.printLog( '%s: TEMPERATURE IS SET TO %s°C' % ( inspect.currentframe().f_code.co_name, MIN_TEMPERATURE_SP ) );
                return MIN_TEMPERATURE_SP;
            elif( data > MAX_TEMPERATURE_SP ):
                logger.printLog( '%s: Setpoint ( %s°C ) IS OUT OF RANGE' % ( inspect.currentframe().f_code.co_name, data ) );
                logger.printLog( '%s: TEMPERATURE IS SET TO %s°C' % ( inspect.currentframe().f_code.co_name, MAX_TEMPERATURE_SP ) );
                return MAX_TEMPERATURE_SP;
            else:
                return data;

        elif( inspect.stack( )[ 1 ][ 3 ] == 'setChamberHumiditySP' ):      
            if( data < MIN_HUMIDITY_SP ):
                logger.printLog( '%s: Setpoint ( %s ) IS OUT OF RANGE' % ( inspect.currentframe().f_code.co_name, data ) );
                logger.printLog( '%s: PERCENTAGE IS SET TO %s' % ( inspect.currentframe().f_code.co_name, MIN_HUMIDITY_SP ) );
                return MIN_HUMIDITY_SP;
            elif( data > MAX_HUMIDITY_SP ):
                logger.printLog( '%s: Setpoint ( %s ) IS OUT OF RANGE' % ( inspect.currentframe().f_code.co_name, data ) );
                logger.printLog( '%s: PERCENTAGE IS SET TO %s' % ( inspect.currentframe().f_code.co_name, MAX_HUMIDITY_SP ) );
                return MAX_HUMIDITY_SP;
            else:
                return data;
        
        else:
            return data;
            

    # ----------------------------------------------------------------------------------------------------
    # brief:        getChamberTemperaturePV  
    # details:      get the process value for temperature of the climate chamber
    # param[in]:    ---
    # param[out]:   result  as float
    # ----------------------------------------------------------------------------------------------------
    def getChamberTemperaturePV( self ) -> float:
        register    = self.client.read_holding_registers( MB_ADDR_TEMPERATURE_PV, self.bytesRead );
        if register:
            temperature = self.convertReadingData( register[ 0 ] );
        else:
            logger.printLog( '%s: Reading Holding Register ERROR' %  inspect.currentframe().f_code.co_name );
            temperature    = 0.0; 

        logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, temperature ) );
        return temperature;


    # ----------------------------------------------------------------------------------------------------
    # brief:        getChamberTemperaturePV_NoLog  
    # details:      get the process value for temperature of the climate chamber
    # param[in]:    ---
    # param[out]:   result  as float
    # ----------------------------------------------------------------------------------------------------
    def getChamberTemperaturePV_NoLog( self ) -> float:
        register    = self.client.read_holding_registers( MB_ADDR_TEMPERATURE_PV, self.bytesRead );
        if register:
            return self.convertReadingData( register[ 0 ] );
        else:
            logger.printLog( '%s: Reading Holding Register ERROR' %  inspect.currentframe().f_code.co_name );
            return 0.0; 


    # ----------------------------------------------------------------------------------------------------
    # brief:        setChamberTemperatureSP  
    # details:      check allowed range for temperature
    # param[in]:    temperature as int/float
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def setChamberTemperatureSP( self, temperature ) -> None:
        temperature     = self.assertLimits( temperature );
        _temperature     = int( temperature * 10 );

        if( temperature < 0.0 ):
            _temperature    = MAX_BINARY_VALUE + 1 + _temperature;
        
            if( self.client.write_multiple_registers( MB_ADDR_TEMPERATURE_SP, [ _temperature, MAX_BINARY_VALUE ] ) ):
                logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, temperature ) );
            else:
                logger.printLog( '%s: Writing multiple Registers ERROR' %  inspect.currentframe().f_code.co_name );
        
        else:
            if( self.client.write_multiple_registers( MB_ADDR_TEMPERATURE_SP, [ _temperature, 0 ] ) ):
                logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, temperature ) );
            else:
                logger.printLog( '%s: Writing multiple Registers ERROR' %  inspect.currentframe().f_code.co_name );



    # ----------------------------------------------------------------------------------------------------
    # brief:        getChamberTemperatureSP  
    # details:      get the setpoint value of the chamber temperature
    #               value is an integer and must be divided by 10
    # param[in]:    ---
    # param[out]:   temperature setpoint as float
    # ----------------------------------------------------------------------------------------------------
    def getChamberTemperatureSP( self ) -> float:
        register    = self.client.read_holding_registers( MB_ADDR_TEMPERATURE_SP, self.bytesRead );
        if register:
            temperature = self.convertReadingData( register[ 0 ] );
        else:
            logger.printLog( '%s: Reading Holding Register ERROR' %  inspect.currentframe().f_code.co_name );
            temperature    = 0.0; 

        logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, temperature ) );
        return temperature;


    # ----------------------------------------------------------------------------------------------------
    # brief:        getChamberHumidityPV
    # details:      get the process value for humidity of the climate chamber
    # param[in]:    ---
    # param[out]:   result  as float
    # ----------------------------------------------------------------------------------------------------
    def getChamberHumidityPV( self ) -> float:
        register    = self.client.read_holding_registers( MB_ADDR_HUMIDITY_PV, self.bytesRead );
        if register:
            humidity    = self.convertReadingData( register[ 0 ] );
        else:
            logger.printLog( '%s: Reading Holding Register ERROR' %  inspect.currentframe().f_code.co_name );
            humidity    = 0.0; 

        logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, humidity ) );
        return humidity;


    # ----------------------------------------------------------------------------------------------------
    # brief:        getChamberHumidityPV_NoLog
    # details:      get the process value for humidity of the climate chamber
    #               not log entries in the *.log files
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def getChamberHumidityPV_NoLog( self ) -> float:
        register    = self.client.read_holding_registers( MB_ADDR_HUMIDITY_PV, self.bytesRead );
        if register:
            return self.convertReadingData( register[ 0 ] );
        else:
            logger.printLog( '%s: Reading Holding Register ERROR' %  inspect.currentframe().f_code.co_name );
            return 0.0; 


    # ----------------------------------------------------------------------------------------------------
    # brief:        setChamberHumiditySP  
    # details:      setpoint of humidity control as float ... converted to int ( factor 10 )
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def setChamberHumiditySP( self, humidity ) -> None:
        humidity    = self.assertLimits( humidity );
        _humidity   = int( humidity * 10 );
        
        if( self.client.write_multiple_registers( MB_ADDR_HUMIDITY_SP, [ _humidity, 0 ] ) ):
            logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, humidity ) );
        else:
            logger.printLog( '%s: Writing multiple Registers ERROR' %  inspect.currentframe().f_code.co_name );


    # ----------------------------------------------------------------------------------------------------
    # brief:        getChamberHumiditySP  
    # details:      get the setpoint of humidity control of the climate chamber
    # param[in]:    ---
    # param[out]:   setpoint of humidity control
    # ----------------------------------------------------------------------------------------------------
    def getChamberHumiditySP( self ) -> float:
        register    = self.client.read_holding_registers( MB_ADDR_HUMIDITY_SP, self.bytesRead );
        if register:
            humidity = self.convertReadingData( register[ 0 ] );
        else:
            logger.printLog( '%s: Reading Holding Register ERROR' %  inspect.currentframe().f_code.co_name );
            humidity    = 0.0; 

        logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, humidity ) );
        return humidity;


    # ----------------------------------------------------------------------------------------------------
    # brief:        switchOnChamberManualRun
    # details:      switch on the manual run of the climate chamber
    #               write a single bit at the specified register
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def switchOnChamberManualRun( self ) -> None:
        
        if( self.client.write_single_coil( MB_ADDR_MANUAL_RUN, True ) ):
            logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, True ) );
        else:
            logger.printLog( '%s: Writing Single Coil ERROR' %  inspect.currentframe().f_code.co_name );


    # ----------------------------------------------------------------------------------------------------
    # brief:        switchOffChamberManualRun
    # details:      switch off the manual run of the climate chamber
    #               write a single bit at the specified register
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def switchOffChamberManualRun( self ) -> None:
        
        if( self.client.write_single_coil( MB_ADDR_MANUAL_RUN, False ) ):
            logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, True ) );
        else:
            logger.printLog( '%s: Writing Single Coil ERROR' %  inspect.currentframe().f_code.co_name );


    # ----------------------------------------------------------------------------------------------------
    # brief:        getChamberManualStart  
    # details:      returns if the manual run of the climate chamber is active or not
    #               True    ... manual run is on
    #               False   ... manual run is off
    # param[in]:    ---
    # param[out]:   state as bool
    # ----------------------------------------------------------------------------------------------------
    def getChamberManualRunState( self ) -> None:
        register    = None;
        state       = False
        try:
            register    = self.client.read_coils( MB_ADDR_MANUAL_RUN, 1 );
            state       = register[ 0 ];
            logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, state ) );
        except Exception as exc:
            logger.printLog( '%s: Reading Single Coil ERROR: %s' % ( inspect.currentframe().f_code.co_name, exc ) );
        
        return state;
        

    # ----------------------------------------------------------------------------------------------------
    # brief:        switchOnHumidityControl  
    # details:      False   ... switch ON
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def switchOnHumidityControl( self ) -> None:
        
        if( self.client.write_single_coil( MB_ADDR_HUMIDITY_CONTROL, False ) ):
            logger.printLog( '%s' % inspect.currentframe().f_code.co_name );
        else:
            logger.printLog( '%s: Writing Single Coil ERROR' %  inspect.currentframe().f_code.co_name );


    # ----------------------------------------------------------------------------------------------------
    # brief:        switchOffHumidityControl  
    # details:      True    ... switch off
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def switchOffHumidityControl( self ) -> None:
        
        if( self.client.write_single_coil( MB_ADDR_HUMIDITY_CONTROL, True ) ):
            logger.printLog( '%s' % inspect.currentframe().f_code.co_name );
        else:
            logger.printLog( '%s: Writing Single Coil ERROR' %  inspect.currentframe().f_code.co_name );


    # ----------------------------------------------------------------------------------------------------
    # brief:        getHumidityControlState  
    # details:      True    ... state is OFF
    #               False   ... state is ON
    # param[in]:    ---
    # param[out]:   state if humidity control is activated
    # ----------------------------------------------------------------------------------------------------
    def getHumidityControlState( self ) -> None:
        register    = None;
        state       = False;
        try:
            register    = self.client.read_coils( MB_ADDR_HUMIDITY_CONTROL, 1 );
            state       = register[ 0 ];
            state       = not state;
            logger.printLog( '%s: %s' % ( inspect.currentframe().f_code.co_name, state ) );
        except Exception as exc:
            logger.printLog( '%s: Reading Single Coil ERROR: %s' % ( inspect.currentframe().f_code.co_name, exc ) );
        
        return state;

    
    # ----------------------------------------------------------------------------------------------------
    # brief:        switchOnChamberManualRun_NoLog  
    # details:      switch on the manual run of the climate chamber
    #               write a single bit at the specified register
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def switchOnChamberManualRun_NoLog( self ) -> None:
        self.client.write_single_coil( MB_ADDR_MANUAL_RUN, True );
    

    # ----------------------------------------------------------------------------------------------------
    # brief:        waitChamberTemperaturePV_Event  
    # details:      wait till the setpoint of the temperature is reached in the climate chamber
    #               check every ... seconds the actual process value of the temperature in the chamber
    # param[in]:    setpoint of the temperature as float value
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def waitChamberTemperaturePV_Event( self, SP ) -> None:
        idleTimeSecTemperatureEvent = 30;
        logger.printLog( '%s: expected temperature = %s' % ( inspect.currentframe().f_code.co_name, SP ) );
        self.setChamberTemperatureSP( SP );
        self.switchOnChamberManualRun( );
        PV  = self.getChamberTemperaturePV_NoLog( );

        if( SP < PV ):
            while( SP < PV ):
                logger.printLog( '%s: exp temp = %s, act temp = %s ( cooling )' % ( inspect.currentframe().f_code.co_name, SP, PV ) );
                time.sleep( idleTimeSecTemperatureEvent );
                PV = self.getChamberTemperaturePV_NoLog( );
        elif( SP > PV ):
            while( SP > PV ):
                logger.printLog( '%s: exp temp = %s, act temp = %s ( heating )' % ( inspect.currentframe().f_code.co_name, SP, PV ) );
                time.sleep( idleTimeSecTemperatureEvent );
                PV = self.getChamberTemperaturePV_NoLog( );

        self.switchOffChamberManualRun( );


    # ----------------------------------------------------------------------------------------------------
    # brief:        constChamberTemperaturePV  
    # details:      wait till the setpoint of the temperature is reached in the climate chamber
    #               check every ... seconds the actual process value of the temperature in the chamber
    # param[in]:    setpoint of the temperature as float value
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def constChamberTemperaturePV( self, SP, timeMinutes ) -> None:
        idleTime    = 30;
        actTime     = int( time.time( ) );
        stoppTime   = int( time.time( ) ) + ( 60 * timeMinutes );
        self.setChamberTemperatureSP( SP );
        self.switchOnChamberManualRun( );
        
        while( actTime < stoppTime ):
            minLeft     = int( ( stoppTime - actTime ) / 60 );
            secLeft     = int( ( stoppTime - actTime ) % 60 );
            logger.printLog( '%s to %s °C: %s min, %s sec left' % ( inspect.currentframe().f_code.co_name, SP, minLeft, secLeft ) );
            time.sleep( idleTime );
            actTime     = int( time.time( ) );
        
        self.switchOffChamberManualRun( );

    
    # ----------------------------------------------------------------------------------------------------
    # brief:        waitChamberHumidityPV_Event  
    # details:      wait till the setpoint of the humidity is reached in the climate chamber
    #               check every ... seconds the actual process value of the humidity in the chamber
    # param[in]:    setpoint of the humidity as float value
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def waitChamberHumidityPV_Event( self, SP ) -> None:
        idleTimeSecHumidityEvent    = 30;
        logger.printLog( '%s: expected humidity = %s' % ( inspect.currentframe().f_code.co_name, SP ) );
        self.setChamberHumiditySP( SP );
        self.switchOnChamberManualRun( );
        PV  = self.getChamberHumidityPV_NoLog( );

        if( SP < PV ):
            while( SP < PV ):
                logger.printLog( '%s: exp humidity = %s, act humidity = %s' % ( inspect.currentframe().f_code.co_name, SP, PV ) );
                time.sleep( idleTimeSecHumidityEvent );
                PV = self.getChamberHumidityPV_NoLog( );
        elif( SP > PV ):
            while( SP > PV ):
                logger.printLog( '%s: exp humidity = %s, act humidity = %s' % ( inspect.currentframe().f_code.co_name, SP, PV ) );
                time.sleep( idleTimeSecHumidityEvent );
                PV = self.getChamberHumidityPV_NoLog( );

        self.switchOffChamberManualRun( );


    # ----------------------------------------------------------------------------------------------------
    # brief:        setCorrosionProtection  
    # details:      Danger of corrosion:
    #               after operating at humidity > 70 % for a long period
    #               is necessary to dry the chamber before to turn it off.
    #               To do this, set the humidity to 10%, set the temperature
    #               to 60°C and let the unit operate for at least 2 hours
    #               After this period is possible to turn the chamber down
    #               actual time + 2 ( hours ) * 60 ( min ) * 60 ( sec )
    #               switch off the manual run, when the requirements are met
    # param[in]:    ---
    # param[out]:   ---
    # ----------------------------------------------------------------------------------------------------
    def setCorrosionProtection( self ) -> None:
        logger.printLog( '%s' % inspect.currentframe().f_code.co_name );

        actTime     = int( time.time( ) );
        stoppTime   = int( time.time( ) ) + ( 2 * 60  );
        
        self.setChamberTemperatureSP( CORROSION_PROTECTION_TEMPERATURE );
        self.setChamberHumiditySP( CORROSION_PROTECTION_HUMIDITY );
        self.switchOnChamberManualRun( );

        while( actTime < stoppTime ):
            minLeft     = int( ( stoppTime - actTime ) / 60 ); 
            logger.printLog( '%s: %s min left' % ( inspect.currentframe().f_code.co_name, minLeft  ) );
            time.sleep( 60 );
            actTime     = int( time.time( ) );
        
        self.switchOffChamberManualRun( );


# Aktuelles Datum und Uhrzeit erhalten
current_datetime = datetime.datetime.now()

# Datums- und Uhrzeitwert in das entsprechende Format konvertieren
formatted_datetime = current_datetime.strftime('%d-%m-%Y %H:%M:%S')

cursor.execute("INSERT INTO tests (name, date_time, temp, hum) VALUES (?, ?, ?, ?)", ('test1', current_datetime, temperature, humidity))

# Änderungen in der Datenbank speichern
conn.commit()

# Verbindung schließen
conn.close()