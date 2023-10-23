import java.util.Scanner;

public class ex009_logical {

  public static void main(String[] args) {
    // int temp = 35;
    // if (temp >= 30) {
    //   System.out.println("HOT");
    // } else if (temp >= 25 && temp <= 35) {
    //   System.out.println("WARM");
    // } else {
    //   System.out.println("COLD");
    // }

    Scanner scanner = new Scanner(System.in);

    System.out.println("write p or s");
    String game = scanner.next();

    if (game.equals("p") || game.equals("s")) {
      System.out.println("OKEY!");
    } else {
      System.out.println("NO!!!!!!!");
    }

    scanner.close();
  }
}
