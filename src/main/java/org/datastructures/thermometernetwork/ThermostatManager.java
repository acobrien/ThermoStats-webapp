package org.datastructures.thermometernetwork;

import java.util.HashSet;

public class ThermostatManager {

    HashSet<Thermostat> thermostats = new HashSet<Thermostat>();

    public ThermostatManager() {
        // Intentionally empty
    }

    public boolean addThermostat(Thermostat thermostat) {
        return thermostats.add(thermostat);
    }

    public boolean addSensor(Thermostat thermostat, Sensor sensor) {
        return thermostat.addSensor(sensor);
    }

}
