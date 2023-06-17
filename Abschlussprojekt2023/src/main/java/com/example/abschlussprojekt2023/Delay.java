package com.example.abschlussprojekt2023;

import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;



public class Delay extends Objects{


    public Delay(VBox process, VBox objects) {
        super(process, objects);
    }



    @Override
    public void initRectangle() {

        super.initRectangle();
        rectangle.setFill(Color.GOLD);
        droppedrectangle.setFill(Color.GOLD);
        process.getChildren().addAll(droppedrectangle);
        
    
        
    }
    @Override
    public void openInputDialog(){
        super.openInputDialog();
        dialog.setTitle("Zeit eingeben in Minuten");
        dialog.setHeaderText("Zeit in Minuten:");
        
    }



}

