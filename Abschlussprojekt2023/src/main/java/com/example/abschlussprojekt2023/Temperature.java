package com.example.abschlussprojekt2023;

import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;


public class Temperature extends Set {


    public Temperature(VBox process, VBox objects) {
        super(process, objects);
    }

    @Override
    public void initRectangle() {

        super.initRectangle();
        rectangle.setFill(Color.DARKGREEN);
        droppedrectangle.setFill(rectangle.getFill());
      
    }

    
}
