package org.datastructures.thermometernetwork;

import java.util.*;
import java.io.*;
import java.text.SimpleDateFormat;

public class ThermostatManager {

    HashSet<Thermostat> thermostats = new HashSet<Thermostat>();

    public ThermostatManager() {
        // Intentionally empty
    }

    public boolean addThermostat(Thermostat thermostat) {
        return thermostats.add(thermostat);
    }

    public boolean addSensor(Thermostat thermostat, Sensor sensor) {
        return thermostat.addSensor(sensor);
    }

    // Only method that should have to change for compatibility with other systems
    // Writes to the save file in our format; does NOT create objects or add to internal data structure
    public static void saveNewData(String inFileName, String saveFileName) throws IOException {
        File inFile = new File(inFileName);
        File saveFile = new File(saveFileName);
        String line;
        String[] tokens;
        boolean even = true;

        try (Scanner in = new Scanner(inFile);
             FileWriter fileWriter = new FileWriter(saveFile, true);
             PrintWriter out = new PrintWriter(fileWriter)) {

            // Write metadata for thermostats/sensors if the save file is empty. Format:
            // thermostat1Name,sensor1name,sensor2name...\n
            // thermostat1Name,sensor1name,sensor2name...
            if (saveFile.length() == 0) {
                out.println("East Side,Master Bedroom,Master Bathroom,Office," +
                        "Ty's Bedroom,Luke's Bedroom,Sabry's Bedroom,Living Room\n" +
                        "West Side,Brody's Bedroom,Kitchen,Den,Bar,Living Room,Outside");
            }

            while (in.hasNextLine()) {
                line = in.nextLine();
                tokens = line.split("[\t ]+"); //Splits on tabs, spaces or multiples of tabs/spaces

                if (even) { // Only prints timestamp once per two lines of input
                    out.print(epochToDateTime(tokens[1]));
                }

                for (int i = 4; i < tokens.length; i++) {

                    if (tokens[2].equals("0")) { // East Side
                        switch (i) { // Ignores inactive sensors on East thermostat
                            case 4, 5, 6, 7, 8, 9, 11:
                                out.print("," + tokens[i]);
                                break;
                        }
                    }

                    else if (tokens[2].equals("1")) { // West Side
                        switch (i) { // Ignores inactive sensors on West thermostat
                            case 4, 5, 6, 7, 8, 11:
                                out.print("," + tokens[i]);
                                break;
                        }
                    }

                }// for-loop

                if (!even) { //Prints a \n once for every two lines of input
                    out.println();
                    even = true;
                }
                else {
                    even = false;
                }

            }// while-loop
        }// try-with-resources (automatically closes scanner and printWriter)
    }// method

    // Converts epoch to MM/DD/YYYY-hh:mm:ss
    public static String epochToDateTime(String epochTimestampStr) {
        double epochTimestamp = Double.parseDouble(epochTimestampStr);
        long epochMillis = (long) (epochTimestamp * 1000);
        Date date = new Date(epochMillis);// Create a Date object
        SimpleDateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy-HH:mm:ss");// Define the desired format
        return dateFormat.format(date);// Format the date and time
    }

    public void readSave(String saveFileName) throws IOException {
        File inFile = new File(saveFileName);
        String line;
        String[] firstDataLine;
        double temperature;
        String[] tokens;
        boolean isMetaData = true;

        try (Scanner in = new Scanner(inFile)) {

            //Reads metadata and creates Thermostat and Sensor objects
            while (in.hasNextLine()) {
                line = in.nextLine();
                tokens = line.split(",");

                // Regex pattern for the date/time format
                String dateTimeRegex = "^\\d{2}/\\d{2}/\\d{4}-\\d{2}:\\d{2}:\\d{2}$";

                if (isMetaData && !tokens[0].matches(dateTimeRegex)) { //This line is metadata
                    Thermostat thermostat = new Thermostat(tokens[0]);
                    addThermostat(thermostat);
                    for (int i = 1; i < tokens.length; i++) {
                        Sensor sensor = new Sensor(tokens[i]);
                        addSensor(thermostat, sensor); // Adds the current sensor to the current thermostat
                    }
                }

                else {
                    isMetaData = false;
                    //process real data. going to be aggravating I think.
                }
            }
        }
    }

}