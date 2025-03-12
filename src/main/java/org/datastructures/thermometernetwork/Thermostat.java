package org.datastructures.thermometernetwork;

import java.util.LinkedHashSet;

public class Thermostat {

    private final String thermostatId;
    private final LinkedHashSet<Sensor> sensors = new LinkedHashSet<>();

    public Thermostat(String thermostatId) {
        this.thermostatId = thermostatId;
    }

    public boolean addSensor(Sensor sensor) {
        return sensors.add(sensor);
    }

    public boolean addTemperature(Sensor sensor, String timestamp, double temperature) {
        sensor.addTemperature(timestamp, temperature);
        return true;
    }

    public LinkedHashSet<Sensor> getSensors() {
        return sensors;
    }

    public String getThermostatId() {
        return thermostatId;
    }

    @Override
    public String toString() {
        return thermostatId;
    }

}