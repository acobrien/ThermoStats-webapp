package org.datastructures.thermometernetwork;

import java.util.HashSet;

public class Thermostat {

    private final String name;
    private final HashSet<Sensor> sensors = new HashSet<>();

    public Thermostat(String name) {
        this.name = name;
    }

    public boolean addSensor(Sensor sensor) {
        return sensors.add(sensor);
    }

    public HashSet<Sensor> getSensors() {
        return sensors;
    }

    public boolean addEntry(Sensor sensor, String timestamp, double temperature) {
        sensor.addTemperature(timestamp, temperature);
        return true;
    }

    @Override
    public String toString() {
        StringBuilder msg = new StringBuilder("Thermostat: " + name + ", Sensors:\n");
        for (Sensor sensor : sensors) {
            msg.append(sensor.toString()).append("\n");
        }
        return msg + "\n";
    }

}