import java.util.Scanner;

public class ex011_manyFor {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int rows;
    int columns;
    String symbol;

    System.out.println("enter rows: ");
    rows = scanner.nextInt();
    System.out.println("enter cols: ");
    columns = scanner.nextInt();
    System.out.println("enter symbol: ");
    symbol = scanner.next();

    for (int i = 1; i <= rows; i++) {
      System.out.println();
      for (int j = 1; j <= columns; j++) {
        System.out.print(symbol);
      }
    }

    scanner.close();
  }
}
