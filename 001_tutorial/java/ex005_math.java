import java.util.Scanner;

public class ex005_math {

  public static void main(String[] args) {
    // double x = 3.14;
    // double y = 25;

    // double z = Math.max(x, y);
    // double z = Math.min(x, y);
    // double z = Math.abs(y);
    // double z = Math.sqrt(y);
    // double z = Math.round(x);
    // double z = Math.ceil(x);
    // double z = Math.floor(x);

    // System.out.println(z);

    double a;
    double b;
    double c;

    Scanner scanner = new Scanner(System.in);

    System.out.println("enter a: ");
    a = scanner.nextDouble();
    System.out.println("enter b: ");
    b = scanner.nextDouble();

    c = Math.sqrt((a * a) + (b * b));

    System.out.println(c);

    scanner.close();
  }
}
