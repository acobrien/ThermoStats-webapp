import java.util.*;

public class Sensor {

    private final String name;
    private final TreeMap<String, TreeMap<String, Double>> dayMap;

    public Sensor(String name) {
        this.name = name;
        this.dayMap = new TreeMap<String, TreeMap<String, Double>>(new DayComparator());
    }

    public void addTemperature(String day, String time, double temperature) {
        if (!dayMap.containsKey(day)) {
            dayMap.put(day, new TreeMap<String, Double>(new TimeComparator()));
        }
        dayMap.get(day).put(time, temperature);
    }

    //Gets the TreeMap of temps for a day.
    public TreeMap<String, Double> getDay(String day) {
        return dayMap.get(day);
    }

}