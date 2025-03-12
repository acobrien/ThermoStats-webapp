package org.datastructures.thermometernetwork;

import java.util.TreeSet;

public class Thermostat {

    private final String name;
    private final TreeSet<Sensor> sensors = new TreeSet<>(new SensorComparator());

    public Thermostat(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public boolean addSensor(Sensor sensor) {
        return sensors.add(sensor);
    }

    public TreeSet<Sensor> getSensors() {
        return sensors;
    }

    public boolean addEntry(Sensor sensor, String timestamp, double temperature) {
        sensor.addTemperature(timestamp, temperature);
        return true;
    }

    @Override
    public String toString() {
        return("Thermostat: " + name + "\n");
    }

}