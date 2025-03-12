package org.datastructures.thermometernetwork;

import java.util.*;

public class Sensor {

    private final String sensorId;
    private final TreeMap<String, TreeMap<String, Double>> dateMap = new TreeMap<>(new DateComparator());

    public Sensor(String sensorId) {
        this.sensorId = sensorId;
    }

    public void addTemperature(String timestamp, double temperature) {
        String date = timestamp.substring(0, 10);
        String time = timestamp.substring(11);
        if (dateMap.containsKey(date)) {
            dateMap.get(date).put(time, temperature);
            return;
        }
        dateMap.put(date, new TreeMap<>(new TimeComparator()));
    }

    //Gets the TreeMap of temps for the supplied date.
    public TreeMap<String, Double> getDayMap(String date) {
        return dateMap.get(date);
    }
    
    //Gets stringified list of temps in map ONLY FOR READABILITY
    public TreeSet<String> getDayTimesAndTemps(TreeMap<String, Double> dayMap) {
    	TreeSet<String> dayTimesAndTemps = new TreeSet<>();
    	dayMap.forEach((key, value)  -> {
    		String combo = key + " : " + value;
    		dayTimesAndTemps.add(combo);
    	});
    	return dayTimesAndTemps;  
    }
    
    public Set<String> getDates(){
    	return dateMap.keySet();
    }

    @Override
    public String toString() {
        return "Sensor: " + sensorId;
    }

}