package org.datastructures.thermometernetwork;

import java.util.Comparator;

public class ThermostatComparator implements Comparator<Thermostat> {
    @Override
    public int compare(Thermostat t1, Thermostat t2) {
        return t1.getName().compareTo(t2.getName());
    }
}