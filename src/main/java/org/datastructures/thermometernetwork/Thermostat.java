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

}