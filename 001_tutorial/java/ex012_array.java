// import java.util.Arrays;

public class ex012_array {

  public static void main(String[] args) {
    // String[] cars = new String[] { "opel", "toyota", "Polonez" };
    // cars[0] = "mustang";

    // System.out.println(cars[cars.length - 1]);
    // System.out.println(Arrays.toString(cars));

    String[] cars = new String[3];
    cars[0] = "opel";
    cars[1] = "tyota";
    cars[2] = "polonez";
    for (int i = 0; i < cars.length; i++) {
      System.out.println(cars[i]);
    }
  }
}
