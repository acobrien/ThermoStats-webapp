package org.datastructures.thermometernetwork;

import java.util.*;

public class Sensor {

    private final String sensorId;
    private final TreeMap<String, TreeMap<String, Double>> dateMap;

    public Sensor(String sensorId) {
        this.sensorId = sensorId;
        this.dateMap = new TreeMap<>(new DateComparator());
    }

    public void addTemperature(String date, String time, double temperature) {
        if (!dateMap.containsKey(date)) {
            dateMap.put(date, new TreeMap<>(new TimeComparator()));
        }
        dateMap.get(date).put(time, temperature);
    }

    //Gets the TreeMap of temps for the supplied date.
    public TreeMap<String, Double> getDay(String date) {
        return dateMap.get(date);
    }

}