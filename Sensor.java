import java.util.*;

public class Sensor {

    private String name;
    private TreeMap<String, LinkedHashMap<String, Double>> dayMap;

    public Sensor(String name) {
        this.name = name;
        this.dayMap = new TreeMap<>();
    }

    public void addTemperature(String day, String time, double temperature) {
        if (!dayMap.containsKey(day)) {
            dayMap.put(day, new LinkedHashMap<String, Double>());
        }
        dayMap.get(day).put(time, temperature);
    }

    //Gets the LinkedHashMap of temps for a day.
    public LinkedHashMap<String, Double> getDay(String day) {
        return dayMap.get(day);
    }

}