package org.datastructures.thermometernetwork;

import java.io.IOException;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ContentDisplay;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.SelectionMode;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
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
    private ListView<Sensor> sensors = new ListView<>();
	private ListView<Thermostat> thermostats = new ListView<>();
	private ListView<String> dates = new ListView<>();
	private ListView<String> timesAndTemps = new ListView<>();
	private Thermostat currThermostat;
	private Sensor currSensor;
	private String currDate;
	//private String currTimeAndTemp;
	private Stage mainStage = new Stage();

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
    	primaryStage = mainStage;
        Pane rootPane = buildStartGui();
        Scene scene = new Scene(rootPane, 1024, 768);
        scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
        primaryStage.setScene(scene);
        primaryStage.setTitle("Temperature Sensor Network");
        primaryStage.show();
    }

    private Pane buildStartGui() {
        GridPane root = new GridPane();
        root.setAlignment(Pos.CENTER);

        root.add(buildTitle(), 0, 0);
        root.add(buildReadWrite(), 0, 1);
        //root.add(buildDisplayRow(), 0, 2);
        return root;
    }
    
    private Pane buildListsGui() {
    	GridPane root = new GridPane();
    	
    	root.getStyleClass().add("grid");
    	
		root.add(buildThermostatsEntry(), 0, 0);
		populateThermostatsEntry();
		thermostats.setOnMouseClicked(new ThermostatsClickedEvent());
		
		root.add(buildSensorsEntry(), 1, 0);
		root.add(buildDatesEntry(), 2, 0);
		root.add(buildTimeAndTempEntry(), 3, 0);
        return root;
    }

    private Pane buildTitle() {
        VBox vBox = new VBox();
        vBox.setAlignment(Pos.TOP_CENTER);
        vBox.getStyleClass().add("h_or_v_box");
        
        Image logo = new Image(getClass().getResourceAsStream("ThermostatsLogo.png"));
        ImageView logoView = new ImageView();
        logoView.setImage(logo);
        
        Label title = new Label("Project By: Luke Fisher, Aidan O'Brien, Cody Hyers, Jason Ackerman Jr, and Meet Patel", logoView);
        title.setContentDisplay(ContentDisplay.TOP);
        
        title.setStyle("-fx-font-size: 8pt; -fx-font-weight: bold; " +
                "-fx-text-fill: rgba(152, 255, 152, .50); -fx-padding: 10px;");
        
        vBox.getChildren().add(title);
        return vBox;
    }

    private Pane buildReadWrite() {
        VBox vBox = new VBox();
        vBox.setAlignment(Pos.BOTTOM_CENTER);
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
        	try {
				manager.loadSave("saveFile.csv");
			} catch (IOException e) {	
				e.printStackTrace();
			}
        	Pane rootPane = buildListsGui();
            Scene scene = new Scene(rootPane, 1024, 768);
            scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
            mainStage.setScene(scene);
            mainStage.show();
        }
    }

    private class WriteDataHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {

        }
    }
    
    private Pane buildThermostatsEntry() {
		thermostats.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
		thermostats.setPrefHeight(500);
		thermostats.setPrefWidth(250);
		VBox vBox = new VBox();
		vBox.getStyleClass().add("h_or_v_box");
		Label lbl = new Label("Thermostats\nFormat: ID");
		lbl.getStyleClass().add("label");
		vBox.getChildren().add(lbl);
		vBox.getChildren().addAll(thermostats);
		return vBox;
	}
	
	private Pane buildSensorsEntry() {
		sensors.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
		sensors.setPrefHeight(500);
		sensors.setPrefWidth(250);
		VBox vBox = new VBox();
		vBox.getStyleClass().add("h_or_v_box");
		Label lbl = new Label("Sensors\nFormat: ID");
		lbl.getStyleClass().add("label");
		vBox.getChildren().add(lbl);
		vBox.getChildren().addAll(sensors);
		return vBox;
	}
	
	private Pane buildDatesEntry() {
		dates.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
		dates.setPrefHeight(500);
		dates.setPrefWidth(250);
		VBox vBox = new VBox();
		vBox.getStyleClass().add("h_or_v_box");
		Label lbl = new Label("Dates\nFormat: Date");
		lbl.getStyleClass().add("label");
		vBox.getChildren().add(lbl);
		vBox.getChildren().add(dates);
		return vBox;
	}
	
	private Pane buildTimeAndTempEntry() {
		timesAndTemps.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
		timesAndTemps.setPrefHeight(500);
		timesAndTemps.setPrefWidth(250);
		VBox vBox = new VBox();
		vBox.getStyleClass().add("h_or_v_box");
		Label lbl = new Label("Time and Temp\nFormat: Time : Temp");
		lbl.getStyleClass().add("label");
		vBox.getChildren().add(lbl);
		vBox.getChildren().add(timesAndTemps);
		return vBox;
	}
	
	private void populateThermostatsEntry() {
		thermostats.getItems().clear();
		thermostats.getItems().addAll(manager.getThermostats());
	}
	
	private void populateSensorsEntry(Thermostat t) {
		sensors.getItems().clear();
		sensors.getItems().addAll(t.getSensors());
		sensors.setOnMouseClicked(new SensorsClickedEvent());
		
	}
	
	private void populateDatesEntry(Sensor s) {
		dates.getItems().clear();
		if (s != null) {
			dates.getItems().addAll(s.getDates());
		}
		dates.setOnMouseClicked(new DatesClickedEvent());
	}
	
	@SuppressWarnings("unchecked")
	private void populateTimeAndTempsEntry(Sensor s, String date) {
		timesAndTemps.getItems().clear();
		if (s != null) {
			timesAndTemps.getItems().addAll(s.getDayTimesAndTemps(s.getDayMap(date)));
		}
		dates.setOnMouseClicked(new DatesClickedEvent());
	}
    
    public class ThermostatsClickedEvent implements EventHandler<MouseEvent> {

		@Override
		public void handle(MouseEvent event) {
			currThermostat = thermostats.getSelectionModel().getSelectedItem();
			timesAndTemps.getItems().clear();
			if (currThermostat != null) {
				populateSensorsEntry(currThermostat);
				populateDatesEntry(null);
			}
		}
	}
	
	public class SensorsClickedEvent implements EventHandler<MouseEvent> {

		@Override
		public void handle(MouseEvent event) {
			currSensor = sensors.getSelectionModel().getSelectedItem();
			timesAndTemps.getItems().clear();
			if (currThermostat != null && currSensor !=  null) {
				populateDatesEntry(currSensor);
			}
		}
	}
	
	public class DatesClickedEvent implements EventHandler<MouseEvent> {

		@Override
		public void handle(MouseEvent event) {
			currDate = dates.getSelectionModel().getSelectedItem();
			if (currThermostat != null && currSensor !=  null && currDate != null) {
				populateTimeAndTempsEntry(currSensor, currDate);
			}
		}
	}

}