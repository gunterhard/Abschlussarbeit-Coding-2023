package com.example.abschlussprojekt2023;

import javafx.application.Application;
import javafx.beans.binding.DoubleBinding;


import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.control.ToolBar;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.CornerRadii;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import java.io.File;
import java.io.IOException;

public class  Main extends Application {


    @Override
    public void start(Stage stage) throws IOException {
        VBox process = new VBox();
        VBox objects = new VBox();
        Objects obj = new Objects(process, objects);
        Python_Interpreter py_Ip = new Python_Interpreter();



       

        

        VBox status = new VBox();
        HBox group = new HBox();
        BorderPane root = new BorderPane();

        Scene scene = new Scene(root, 1200, 750, Color.LIGHTBLUE);

        // TOOLBAR
        ToolBar toolbar = new ToolBar();

        MenuBar menuBar = new MenuBar();

        Menu fileMenu = new Menu("Datei");
        // Dropdown Buttons
        MenuItem oeffnen = new MenuItem("Öffnen");
        MenuItem speichern = new MenuItem("Speichern");
        MenuItem loeschen = new MenuItem("Löschen");

        oeffnen.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Datei öffnen");
            File selectedFile = fileChooser.showOpenDialog(stage);
            if (selectedFile != null) {
                System.out.println("Datei ausgewählt: " + selectedFile.getName());
            }
        });

        fileMenu.getItems().addAll(oeffnen, speichern, loeschen);
        menuBar.getMenus().add(fileMenu);

        toolbar.getItems().add(menuBar);

        // Buttons für Play, Pause und Reset
        Button playButton = new Button("Play");
        Button pauseButton = new Button("️Pause");
        Button resetButton = new Button("️Reset");


        HBox buttonbox = new HBox(playButton, pauseButton, resetButton);
        buttonbox.setPadding(new Insets(5));


        // Action Handler für die Buttons hinzufügen
        playButton.setOnAction(e -> {
            System.out.println("Play Button geklickt");
            // Hier den Code für das Abspielen einfügen
        });

        pauseButton.setOnAction(e -> {
            System.out.println("Pause Button geklickt");
            // Hier den Code für das Anhalten einfügen
        });

        resetButton.setOnAction(e -> {
            System.out.println("Reset Button geklickt");
            // Hier den Code für das Zurücksetzen einfügen
        });

       


        root.setTop(toolbar);

        DoubleBinding spacePercent = scene.widthProperty().multiply(0.025);
        int space = spacePercent.intValue();
        CornerRadii radii = new CornerRadii(5);


        // Objects
        LoopStart obj_loopStart = new LoopStart(process, objects);
        obj_loopStart.initRectangle();



        LoopEnd obj_loopEnd = new LoopEnd(process,objects);
        obj_loopEnd.initRectangle();



        Temperature obj_temp = new Temperature(process, objects);
        obj_temp.initRectangle();



        Humidity obj_hum = new Humidity(process, objects);
        obj_hum.initRectangle();



        Delay obj_delay = new Delay(process, objects);
        obj_delay.initRectangle();


        // Status

        float temp_now = ;
        float hum_now = py_Ip.getChamberHumidityPV_NoLog;
        

        Label Temp = new Label("Temp:");
        Label temp_now_Label = new Label();
        Label Hum = new Label("Hum:");
        Label hum_now_Label = new Label ();
        Label Status = new Label("Status:");
        Label status_now = new Label();
        Label Position = new Label("Position:");
        Label pos_now = new Label();
        


        //Areas
        obj.objects.setSpacing(10);
        obj.objects.prefWidthProperty().bind(scene.widthProperty().multiply(0.20));
        obj.objects.prefHeightProperty().bind(scene.heightProperty().multiply(0.95));
        obj.objects.setBackground(new Background(new BackgroundFill(Color.GREY, radii, null)));
        obj.objects.setPadding(new Insets(10));


        obj.process.setSpacing(10);
        obj.process.prefWidthProperty().bind(scene.widthProperty().multiply(0.5));
        obj.process.prefHeightProperty().bind(scene.heightProperty().multiply(0.95));
        obj.process.setBackground(new Background(new BackgroundFill(Color.GREY, radii, null)));
        obj.process.setPadding(new Insets(10));
        obj.process.getChildren().addAll(buttonbox);
        buttonbox.setAlignment(Pos.BOTTOM_CENTER);

        status.setSpacing(10);
        status.prefWidthProperty().bind(scene.widthProperty().multiply(0.20));
        status.prefHeightProperty().bind(scene.heightProperty().multiply(0.90) );
        status.setBackground(new Background(new BackgroundFill(Color.GREY, radii, null)));
        status.setPadding(new Insets(10));
        status.getChildren().addAll(Status, Temp, Hum, Position);

        group.setSpacing(space);
        group.setPadding(new Insets(space));
        group.getChildren().addAll(obj.objects, obj.process, status);
        group.setAlignment(Pos.CENTER);

        root.setCenter(group);
        root.setBackground(new Background(new BackgroundFill(Color.LIGHTBLUE, radii, null)));
        stage.setScene(scene);


        stage.setTitle("Abschlussprojekt 2023");
        stage.show();
    }




    public static void main(String[] args) {
        launch();
    }
}

