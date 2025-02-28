module org.datastructures.thermometernetwork {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.datastructures.thermometernetwork to javafx.fxml;
    exports org.datastructures.thermometernetwork;
}