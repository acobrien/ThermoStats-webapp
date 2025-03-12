package org.datastructures.thermometernetwork;

import java.util.Comparator;

public class SensorComparator implements Comparator<Sensor> {
    @Override
    public int compare(Sensor s1, Sensor s2) {
        return s1.getSensorId().compareTo(s2.getSensorId());
    }
}
