package org.datastructures.thermometernetwork;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.text.SimpleDateFormat;
import java.util.*;
import java.io.*;

public class Main extends Application {

    private HashSet<Sensor> sensors = new HashSet<>();

    public static void main(String[] args) {
        launch(args);
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

    // Only method that should have to change for compatibility with other systems
    // Writes to the save file in our format; does NOT create objects or add to internal data structure
    public static void saveNewData(String inFileName, String saveFileName) throws IOException {
        File inFile = new File(inFileName);
        File saveFile = new File(saveFileName);
        Scanner in = new Scanner(inFile);
        FileWriter fileWriter = new FileWriter(saveFile, true);
        PrintWriter out = new PrintWriter(fileWriter);
        String line;
        String[] tokens;
        boolean even = true;
        //FIXME: Doesn't capture last bit of input; very weird
        while (in.hasNextLine()) {
            line = in.nextLine();
            tokens = line.split("[\t ]+"); //Splits on tabs, spaces or multiples of tabs/spaces. Works as expected.
            if (even) {
                out.print(epochToDateTime(tokens[1]));
            }
            //Goes through every temp, on every line
            for (int i = 4; i < tokens.length; i++) {

                if (tokens[2].equals("0")) { // East Side
                    switch (i) {
                        case 4:
                            out.print(",MasterBed:" + tokens[4]);
                            break;
                        case 5:
                            out.print(",MasterBath:" + tokens[5]);
                            break;
                        case 6:
                            out.print(",Office:" + tokens[6]);
                            break;
                        case 7:
                            out.print(",TyBed:" + tokens[7]);
                            break;
                        case 8:
                            out.print(",LukeBed:" + tokens[8]);
                            break;
                        case 9:
                            out.print(",SabryBed:" + tokens[9]);
                            break;
                        case 11: // 10 not in use
                            out.print(",LivingRm:" + tokens[11]);
                            break;
                    }// switch
                }// if
                else if (tokens[2].equals("1")) { // West Side
                    switch (i) {
                        case 4:
                            out.print(",BrodyBed:" + tokens[4]);
                            break;
                        case 5:
                            out.print(",Kitchen:" + tokens[5]);
                            break;
                        case 6:
                            out.print(",Den:" + tokens[6]);
                            break;
                        case 7:
                            out.print(",Bar:" + tokens[7]);
                            break;
                        case 8:
                            out.print(",LivingRm:" + tokens[8]);
                            break;
                        case 11: // 9 & 10 not in use
                            out.print(",Outside," + tokens[11]);
                            break;
                    }// switch
                }// else if
            }// for-loop
            if (!even) {
                out.println();
                even = true;
            }
            else {
                even = false;
            }
        }// while-loop
    }// method

    // Converts epoch to MM/DD/YYYY-hh:mm:ss
    public static String epochToDateTime(String epochTimestampStr) {
        double epochTimestamp = Double.parseDouble(epochTimestampStr);
        long epochMillis = (long) (epochTimestamp * 1000);
        // Create a Date object from the epoch milliseconds
        Date date = new Date(epochMillis);
        // Define the desired date and time format
        SimpleDateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy-HH:mm:ss");
        // Format the date and time and return it as a string
        return dateFormat.format(date);
    }

    public void readSave(File file) throws IOException {
        //read saved data
    }

}