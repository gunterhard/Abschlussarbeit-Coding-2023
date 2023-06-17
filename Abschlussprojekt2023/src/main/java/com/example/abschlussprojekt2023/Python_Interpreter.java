import org.python.util.PythonInterpreter;
import org.python.core.PyInstance;

public class Python_Interpreter {

    private PythonInterpreter interpreter;

    public Python_Interpreter() {
        interpreter = new PythonInterpreter();
    }

    public void execfile(String fileName) {
        interpreter.execfile(fileName);
    }

    public PyInstance createClass(String className, String opts) {
        return (PyInstance) interpreter.eval(className, + "(" + opts + ")");
    }

    public static void main(String[] args) {
        Python_Interpreter ie = new Python_Interpreter();

        ie.execfile("FDM_ClimateChamber.py");

  
      PyInstance hello = ie.createClass("FDM_ClimateChamberClassMP", "None");  

      hello.invoke("run");  

        PyInstance FDM = ie.createClass("FDM_ClimateChamberClassMP", "object");
        
       /* 
        FDM.invoke("convertReadingData( data: int )");
        
        FDM.invoke("assertLimits( data )");

        FDM.invoke("getChamberTemperaturePV");
        
        FDM.invoke("getChamberTemperaturePV_NoLog");

        FDM.invoke("setChamberTemperatureSP( temperature )");

        FDM.invoke("getChamberTemperatureSP( self )");

        FDM.invoke("getChamberHumidityPV ");

        FDM.invoke("getChamberHumidityPV_NoLog( self )");

        FDM.invoke("setChamberHumiditySP( self, humidity )");

        FDM.invoke("getChamberHumiditySP( self )");

        FDM.invoke("switchOnChamberManualRun( self )");

        FDM.invoke("switchOffChamberManualRun( self )");

        FDM.invoke("getChamberManualRunState( self )");

        FDM.invoke("switchOnHumidityControl( self )");

        FDM.invoke("switchOffHumidityControl( self )");

        FDM.invoke("getHumidityControlState( self )");

        FDM.invoke("switchOnChamberManualRun_NoLog( self )");

        FDM.invoke("waitChamberTemperaturePV_Event( self, SP )");

        FDM.invoke("constChamberTemperaturePV( self, SP, timeMinutes )");

        FDM.invoke("waitChamberHumidityPV_Event( self, SP )");

        FDM.invoke("setCorrosionProtection( self )");

        */


    }
}