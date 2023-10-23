public class ex001_temp {

  public static void main(String[] args) {
    String x = "water";
    String y = "solid";
    String temp;

    temp = x;
    x = y;
    y = temp;

    System.out.println("x: " + x);
    System.out.println("y: " + y);
  }
}
