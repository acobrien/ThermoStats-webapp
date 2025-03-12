package org.datastructures.thermometernetwork;

import java.util.LinkedHashSet;

public class Thermostat {

    private final String name;
    private final LinkedHashSet<Sensor> sensors = new LinkedHashSet<>();

    public Thermostat(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public boolean addSensor(Sensor sensor) {
        return sensors.add(sensor);
    }

    public LinkedHashSet<Sensor> getSensors() {
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