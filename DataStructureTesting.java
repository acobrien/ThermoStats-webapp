import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class DataStructureTesting {

    /*
    Possible data format:
    sensorID,MM/DD/YYYY-HH:MM:SS,temp\n

    Example:
    sensorA,02/26/2025-13:12:30,75.31
    sensorA,02/26/2025-13:13:00,75.29
    */

    //Based on slide 4 of the presentation:
    private HashMap<String, TreeMap<String, ArrayList<Double>>> hashmap = new HashMap<>();

    //Other idea:
    private HashMap<String, LinkedHashMap<String, Double>> hashmap2 = new HashMap<>();

    public static void main(String[] args) {
        //do stuff
    }

    public void readData(File file) throws FileNotFoundException {
        Scanner reader = new Scanner(file);
        String line;
        String[] tokens;
        String sensorId;
        String date;
        double temperature;
        while (reader.hasNextLine()) {
            line = reader.nextLine();
            tokens = line.split(",");
            sensorId = tokens[0];
            date = tokens[1];
            temperature = Double.parseDouble(tokens[2]);
        }
    }

}