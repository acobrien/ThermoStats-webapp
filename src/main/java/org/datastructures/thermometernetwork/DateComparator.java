package org.datastructures.thermometernetwork;

import java.util.Comparator;

public class DateComparator implements Comparator<String> {

    //Date format: MM/DD/YYYY
    @Override
    public int compare(String date1, String date2) {
        int month1 = Integer.parseInt(date1.substring(0, 2));
        int day1 = Integer.parseInt(date1.substring(3, 5));
        int year1 = Integer.parseInt(date1.substring(6));

        int month2 = Integer.parseInt(date2.substring(0, 2));
        int day2 = Integer.parseInt(date2.substring(3, 5));
        int year2 = Integer.parseInt(date2.substring(6));

        if (year1 != year2) {
            return Integer.compare(year1, year2);
        }

        // Years must be equal, compare months
        if (month1 != month2) {
            return Integer.compare(month1, month2);
        }

        // Years and months must be equal, compare days
        return Integer.compare(day1, day2);
    }

}