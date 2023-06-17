package com.example.abschlussprojekt2023;

import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;

public class LoopStart extends Loops {


    public LoopStart(VBox process, VBox objects) {
        super(process, objects);
    }

    @Override
    public void initRectangle() {

        super.initRectangle();
        rectangle.setFill(Color.DARKBLUE);
        droppedrectangle.setFill(Color.DARKBLUE);
    }




}

