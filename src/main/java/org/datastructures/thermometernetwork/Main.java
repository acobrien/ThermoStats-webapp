package org.datastructures.thermometernetwork;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.*;
import javafx.geometry.Pos;
import javafx.stage.Stage;

public class Main /*extends Application*/ {

    static ThermostatManager manager = new ThermostatManager();

    public static void main(String[] args) {
        //launch(args); launches the gui

        //testing
        try {
            //manager.saveNewData("dump-2025-03-02.txt", "saveFile.csv");
            manager.readSave("saveFile.csv");
            System.out.println(manager.toString());
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

//    @Override
//    public void start(Stage primaryStage) {
//        Pane rootPane = buildGui();
//        Scene scene = new Scene(rootPane, 1024, 768);
//        scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
//        primaryStage.setScene(scene);
//        primaryStage.setTitle("Temperature Sensor Network");
//        primaryStage.show();
//    }

    private Pane buildGui() {
        GridPane root = new GridPane();
        root.setAlignment(Pos.CENTER);

        root.add(buildTitle(), 0, 0);
        //Examples:
        //root.add(buildDataEntryRow(), 0, 1);
        //root.add(buildDisplayRow(), 0, 2);
        return root;
    }

    private Pane buildTitle() {
        VBox vBox = new VBox();
        vBox.setAlignment(Pos.CENTER);
        vBox.getStyleClass().add("h_or_v_box");

        Label title = new Label("Temperature Sensor Network");
        title.setStyle("-fx-font-size: 40pt; -fx-font-weight: bold; " +
                "-fx-text-fill: rgba(152, 255, 152, 0.75); -fx-padding: 10px;");

        vBox.getChildren().add(title);
        return vBox;
    }

}