package org.datastructures.thermometernetwork;

import java.util.*;

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
    public LinkedHashMap<String, Double> getDay(String date) {
        return dateMap.get(date);
    }

}