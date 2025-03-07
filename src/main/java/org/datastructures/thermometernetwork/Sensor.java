package org.datastructures.thermometernetwork;

import java.util.*;
import java.util.Map.Entry;

public class Sensor {

    private final String sensorId;
    private final TreeMap<String, LinkedHashMap<String, Double>> dateMap = new TreeMap<>(new DateComparator());

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
        dateMap.put(date, new LinkedHashMap<>());
    }

    //Gets the LinkedHashMap of temps for the supplied date.
    public LinkedHashMap<String, Double> getDayMap(String date) {
        return dateMap.get(date);
    }
    
    //Gets stringified list of temps in map ONLY FOR READABILITY
    public LinkedHashSet getDayTimesAndTemps(LinkedHashMap<String, Double> dayMap) {
    	LinkedHashSet<String> dayTimesAndTemps = new LinkedHashSet<>();
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
        return sensorId;
        //REMOVED TEMPORARILY: ": " + dateMap.toString()
    }

}