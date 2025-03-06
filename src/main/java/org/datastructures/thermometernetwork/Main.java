package org.datastructures.thermometernetwork;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.*;
import javafx.geometry.Pos;
import javafx.stage.Stage;

public class Main extends Application {

    private static final ThermostatManager manager = new ThermostatManager();
    private final Button loadSaveBtn = new Button("Load Save");
    private final Button writeDataBtn = new Button("Write Data");
    private final TextField rawInputNameTxf = new TextField("example-input.txt");
    private final TextField outputSaveNameTxf = new TextField("example-output-save.csv");
    private final TextField inputSaveNameTxf = new TextField("example-input-save.csv");

    public static void main(String[] args) {
        launch(args);

        try {
            manager.loadSave("saveFile.csv");
            System.out.println(manager.toString());
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void start(Stage primaryStage) {
        Pane rootPane = buildGui();
        Scene scene = new Scene(rootPane, 1024, 768);
        scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
        primaryStage.setScene(scene);
        primaryStage.setTitle("Temperature Sensor Network");
        primaryStage.show();
    }

    private Pane buildGui() {
        GridPane root = new GridPane();
        root.setAlignment(Pos.CENTER);

        root.add(buildTitle(), 0, 0);
        root.add(buildReadWrite(), 0, 1);
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

    private Pane buildReadWrite() {
        VBox vBox = new VBox();
        vBox.setAlignment(Pos.CENTER);
        vBox.getStyleClass().add("h_or_v_box");

        HBox loadSaveHBox = new HBox();
        LoadSaveHandler loadSaveHandler = new LoadSaveHandler();
        loadSaveBtn.setOnAction(loadSaveHandler);
        loadSaveBtn.getStyleClass().add("button");
        loadSaveHBox.getChildren().addAll(loadSaveBtn, inputSaveNameTxf);

        HBox writeDataHBox = new HBox();
        WriteDataHandler writeDataHandler = new WriteDataHandler();
        writeDataBtn.setOnAction(writeDataHandler);
        writeDataBtn.getStyleClass().add("button");
        writeDataHBox.getChildren().addAll(writeDataBtn, rawInputNameTxf, outputSaveNameTxf);

        vBox.getChildren().addAll(loadSaveHBox, writeDataHBox);
        return vBox;
    }

    private class LoadSaveHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {

        }
    }

    private class WriteDataHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {

        }
    }

}