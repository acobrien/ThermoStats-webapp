package org.datastructures.thermometernetwork;

import java.text.SimpleDateFormat;
import java.util.*;
import java.io.*;

// For converting epoch to date/time


public class Main {

    /*
FORMAT: TIMESTAMP_24HR  TIMESTAMP_EPOCH  THERMOSTAT_NUM  SENSOR_TEMPS (IN ORDER)

INFO:
-Date is included in name of file
-Temp reading of -1 means sensor is offline or not in use

Thermostat 0 - East Side
-Sensor 0: HVAC Intake
-Sensor 1: Master Bedroom
-Sensor 2: Master Bathroom
-Sensor 3: Office
-Sensor 4: Ty's Bedroom
-Sensor 5: Luke's Bedroom
-Sensor 6: Sabry's Bedroom
-Sensor 7: Expansion (not in use)
-Sensor 8: Living Room
-Sensor 9: HVAC Supply
-Sensor 10: Average of 1,2,3,4,5,6,&8

Thermostat 1 - West Side
-Sensor 0: HVAC Intake
-Sensor 1: Brody's Bedroom
-Sensor 2: Kitchen
-Sensor 3: Den
-Sensor 4: Bar
-Sensor 5: Living Room
-Sensor 6: Expansion (not in use)
-Sensor 7: Expansion (not in use)
-Sensor 8: Outside
-Sensor 9: HVAC Supply
-Sensor 10: Average of 1,2,3,4,&5
     */

    private HashSet<Sensor> sensors = new HashSet<>();

    public static void main(String[] args) {
        try {
            saveNewData("dump-2025-03-02.txt", "saveFile");
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
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
        boolean even = false;
        //FIXME: Doesn't capture last bit of input; very weird
        while (in.hasNextLine()) {
            line = in.nextLine();
            tokens = line.split("[\t ]+"); //Splits on tabs, spaces or multiples of tabs/spaces. Works as expected.
            out.print(epochToDateTime(tokens[1]));
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
            if (even) {
                out.println();
                even = false;
            }
            else {
                even = true;
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