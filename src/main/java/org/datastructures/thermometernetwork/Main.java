package org.datastructures.thermometernetwork;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;

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
    private final Button wipeSaveBtn = new Button("Wipe Save");
    private final Button loadDataBtn = new Button("Add Data");
    private final Button analysisBtn = new Button("Analysis");
    private final Button storageBtn = new Button("Storage");
    private final TextField rawInputNameTxf = new TextField("example-input.txt");
    private final TextField outputSaveNameTxf = new TextField("example-output-save.csv");
    private final TextField inputSaveNameTxf = new TextField("example-input-save.csv");
    private final TextField loadDataNameTxf = new TextField("example-input-save.csv");
    private final ListView<Sensor> sensors = new ListView<>();
	private final ListView<Thermostat> thermostats = new ListView<>();
	private final ListView<String> dates = new ListView<>();
	private final ListView<String> timesAndTemps = new ListView<>();
	private Thermostat currThermostat;
	private Sensor currSensor;
	private String currDate;
	private String saveFileName = "";
	private final Label startErrorOutput = new Label();
	private final Label listsErrorOutput = new Label();
	private final Stage mainStage = new Stage();

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
    	mainStage.setMinWidth(1024);
    	mainStage.setMinHeight(768);
    	primaryStage = mainStage;
        Pane rootPane = buildStartGui();
        Scene scene = new Scene(rootPane, 1024, 768);
        scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
        primaryStage.setScene(scene);
        primaryStage.setTitle("ThermoStats - Temperature Sensor Network");
        primaryStage.show();
    }

    private Pane buildStartGui() {
        GridPane root = new GridPane();
        root.setAlignment(Pos.CENTER);

        root.add(buildStartTitle(), 0, 0);
        root.add(buildStartReadWrite(), 0, 1);
        root.add(buildStartOutput(), 0, 2);
        return root;
    }

    private Pane buildStartTitle() {
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
    
    private Pane buildStartOutput() {
        VBox vBox = new VBox();
        vBox.setAlignment(Pos.TOP_CENTER);
        vBox.getStyleClass().add("h_or_v_box");
        
        startErrorOutput.setContentDisplay(ContentDisplay.TOP);
        
        startErrorOutput.setStyle("-fx-font-size: 12pt; -fx-font-weight: bold; " +
                "-fx-text-fill: rgba(255, 0, 0, .75); -fx-padding: 10px;");
        
        vBox.getChildren().add(startErrorOutput);
        return vBox;
    }

    private Pane buildStartReadWrite() {
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
    
    private Pane buildListsGui() {
    	GridPane root = new GridPane();
    	root.setAlignment(Pos.CENTER);
    	root.getStyleClass().add("grid");
    	
    	VBox vBox = new VBox();
        vBox.setAlignment(Pos.BOTTOM_CENTER);
        vBox.getStyleClass().add("h_or_v_box");
        
        HBox listsHBox = new HBox();
		listsHBox.setAlignment(Pos.CENTER);
    	
		listsHBox.getChildren().addAll(buildThermostatsEntry());
		populateThermostatsEntry();
		thermostats.setOnMouseClicked(new ThermostatsClickedEvent());
		listsHBox.getChildren().addAll(buildSensorsEntry());
		listsHBox.getChildren().addAll(buildDatesEntry());
		listsHBox.getChildren().addAll(buildTimeAndTempEntry());
		
		vBox.getChildren().addAll(listsHBox);
		vBox.getChildren().addAll(buildListsButtons());
		
		listsErrorOutput.setStyle("-fx-font-size: 12pt; -fx-font-weight: bold; " +
                "-fx-text-fill: rgba(255, 0, 0, .75); -fx-padding: 10px;");
		vBox.getChildren().addAll(listsErrorOutput);
		
		root.add(vBox, 0, 0);
        
        return root;
    }
    
    private Pane buildListsButtons() {
    	HBox buttonsHBox = new HBox();
		buttonsHBox.setAlignment(Pos.CENTER);
		
        AnalysisHandler analysisHandler = new AnalysisHandler();
        analysisBtn.setOnAction(analysisHandler);
        analysisBtn.getStyleClass().add("button");
        buttonsHBox.getChildren().addAll(analysisBtn);
        
        WipeSaveHandler wipeSaveHandler = new WipeSaveHandler();
        wipeSaveBtn.setOnAction(wipeSaveHandler);
        wipeSaveBtn.getStyleClass().add("button");
        buttonsHBox.getChildren().addAll(wipeSaveBtn);
        
        LoadDataHandler loadDataHandler = new LoadDataHandler();
        loadDataBtn.setOnAction(loadDataHandler);
        loadDataBtn.getStyleClass().add("button");
        buttonsHBox.getChildren().addAll(loadDataBtn, loadDataNameTxf);
       
        return buttonsHBox;
    }
    
    private Pane buildAnalysisGui() {
        GridPane root = new GridPane();
        root.setAlignment(Pos.CENTER);
        
        root.add(buildAnalysisComingSoon(), 0, 0);
        root.add(buildAnalysisButtons(), 0, 1);
        
        return root;
    }
    
    private Pane buildAnalysisComingSoon() {
        VBox vBox = new VBox();
        vBox.setAlignment(Pos.TOP_CENTER);
        vBox.getStyleClass().add("h_or_v_box");
        
        Image comingSoonImage = new Image(getClass().getResourceAsStream("ComingSoon.png"));
        ImageView imageView = new ImageView();
        imageView.setImage(comingSoonImage);
        
        Label comingSoonLabel = new Label("Analysis, graphs, and more functionality will be added for problem two!", imageView);
        comingSoonLabel.setContentDisplay(ContentDisplay.TOP);
        
        comingSoonLabel.setStyle("-fx-font-size: 15pt; -fx-font-weight: bold; " +
                "-fx-text-fill: rgba(152, 255, 152, .50); -fx-padding: 10px;");
        
        vBox.getChildren().add(comingSoonLabel);
        return vBox;
    }
    
    private Pane buildAnalysisButtons() {
    	HBox buttonsHBox = new HBox();
		buttonsHBox.setAlignment(Pos.CENTER);
        StorageHandler storageHandler = new StorageHandler();
        storageBtn.setOnAction(storageHandler);
        storageBtn.getStyleClass().add("button");
        buttonsHBox.getChildren().addAll(storageBtn);
        
        return buttonsHBox;
    }

    private class LoadSaveHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
        	Label label = new Label("Unable to locate file: Please enter in the correct pathway.");
        	label.setStyle("-fx-font-size: 8pt; -fx-font-weight: bold; " +
                    "-fx-text-fill: rgba(152, 255, 152, .50); -fx-padding: 10px;");
        	
        	try {
				manager.loadSave(inputSaveNameTxf.getText());
				saveFileName = inputSaveNameTxf.getText();
				startErrorOutput.setText("");
				Pane rootPane = buildListsGui();
	            Scene scene = new Scene(rootPane, 1024, 768);
	            scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
	            mainStage.setScene(scene);
	            mainStage.show();
			}
			catch (IOException e) {
				startErrorOutput.setText("Unable to locate save file: Please enter in correct file name/location");
			}
        }
    }

    private class WriteDataHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
			try {
				manager.writeToSave(rawInputNameTxf.getText(), outputSaveNameTxf.getText());
				startErrorOutput.setText("");
			}
			catch (IOException e) {
				startErrorOutput.setText("Unable to locate files: Please enter in correct file names/locations");
			}
        }
    }
    
    private class WipeSaveHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
        	try {
				manager.wipeSave(saveFileName);
				thermostats.getItems().clear();
				sensors.getItems().clear();
				dates.getItems().clear();
				timesAndTemps.getItems().clear();
			}
			catch (IOException e) {
				e.printStackTrace();
			}
        	
        }
    }
    
    private class LoadDataHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
        	//BUG: CALLED INDEX OUT OF BOUNDS ON WRITETOSAVE WITH MUTLIPLE TEXTFILES: CURRENTLY BROKEN
        	try {
        		manager.writeToSave(loadDataNameTxf.getText(), saveFileName);
        		manager.loadSave(saveFileName);
				populateThermostatsEntry();
				listsErrorOutput.setText("");
			}
			catch (IOException e) {
				listsErrorOutput.setText("Currently broken... try again later lol");
			}
        	
        }
    }
    
    private class AnalysisHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
        	Pane rootPane = buildAnalysisGui();
            Scene scene = new Scene(rootPane, 1024, 768);
            scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
            mainStage.setScene(scene);
            mainStage.show();
        }
    }
    
    private class StorageHandler implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
        	Pane rootPane = buildListsGui();
            Scene scene = new Scene(rootPane, 1024, 768);
            scene.getStylesheets().add(getClass().getResource("application-styling.css").toExternalForm());
            mainStage.setScene(scene);
            mainStage.show();
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