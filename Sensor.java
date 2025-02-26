import java.util.*;

public class Sensor {

    String name;
    private TreeMap<String, ArrayList<Double>> dataMap;

    public Sensor(String name) {
        this.name = name;
        this.dataMap = new TreeMap<>();
    }
}