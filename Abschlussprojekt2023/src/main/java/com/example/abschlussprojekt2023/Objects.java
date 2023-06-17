package com.example.abschlussprojekt2023;

import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.scene.Node;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Dialog;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.scene.shape.Rectangle;
import javafx.scene.input.ClipboardContent;
import javafx.scene.input.DragEvent;
import javafx.scene.input.Dragboard;
import javafx.scene.input.MouseButton;

import javafx.scene.input.TransferMode;




public class Objects extends Node {

    protected Rectangle rectangle;
    protected Rectangle droppedrectangle = new Rectangle();

    protected  VBox process;
    protected  VBox objects;



    public Objects(VBox process, VBox objects) {

        this.process = process;
        this.objects  = objects;
    }


    public void initRectangle() {

        rectangle = new Rectangle();
        rectangle.setX(50);
        rectangle.setY(50);
        rectangle.setWidth(200);
        rectangle.setHeight(50);

        
        objects.getChildren().add(rectangle);
        

        

        }
    

   

    public Rectangle getRectangle() {
        return rectangle;
    }

    public void setRectangle(Rectangle rectangle) {
        this.rectangle = rectangle;
    }

   




    private void openInputDialog() {
        Dialog<Double> dialog = new Dialog<>();
        dialog.setTitle("Zahlenwert eingeben");
        dialog.setHeaderText("Geben Sie einen Zahlenwert ein:");

        TextField inputField = new TextField();
        dialog.getDialogPane().setContent(inputField);
        String x = inputField.getText();
        int new_int = Integer.parseInt(x);

        dialog.getDialogPane().getButtonTypes().addAll(ButtonType.OK, ButtonType.CANCEL);
        dialog.setResultConverter(buttonType -> {
            if (buttonType == ButtonType.OK) {
                String inputText = inputField.getText();
                try {
                    double value = Double.parseDouble(inputText);
                    return value;
                } catch (NumberFormatException e) {
                    showAlert("Fehler", "Ungültige Eingabe", "Bitte geben Sie eine gültige Zahl ein.");
                }
            }
            return null;
        });

        dialog.showAndWait().ifPresent(result -> {
            // Speichern des Zahlenwerts für das ausgewählte Rechteck
            droppedrectangle.getProperties().put("Value", result);
            showAlert("Erfolgreich", "Zahlenwert gespeichert", "Der Zahlenwert wurde erfolgreich gespeichert.");
        });
    }

    private void showAlert(String title, String header, String content) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(header);
        alert.setContentText(content);
        alert.showAndWait();
    }
}






