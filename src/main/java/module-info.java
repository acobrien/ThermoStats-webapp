module org.datastructures.thermometernetwork {
    requires transitive javafx.controls;
    requires javafx.fxml;
	requires javafx.graphics;


    opens org.datastructures.thermometernetwork to javafx.fxml;
    exports org.datastructures.thermometernetwork;
}