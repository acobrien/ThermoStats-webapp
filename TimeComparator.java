import java.util.Comparator;

public class TimeComparator implements Comparator<String> {

    //24-hour time format: "HH:MM:SS"
    @Override
    public int compare(String date1, String date2) {
        int hour1 = Integer.parseInt(date1.substring(0, 2));
        int minute1 = Integer.parseInt(date1.substring(3, 5));
        int second1 = Integer.parseInt(date1.substring(6));

        int hour2 = Integer.parseInt(date2.substring(0, 2));
        int minute2 = Integer.parseInt(date2.substring(3, 5));
        int second2 = Integer.parseInt(date2.substring(6));

        if (hour1 != hour2) {
            return Integer.compare(hour1, hour2);
        }

        //Hours must be equal, compare minutes
        if (minute1 != minute2) {
            return Integer.compare(minute1, minute2);
        }

        //Hours and minutes must be equal, compare seconds
        return Integer.compare(second1, second2);
    }

}