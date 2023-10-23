import java.util.Scanner;

public class ex002_scanner {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("what is your name: ");
    String name = scanner.nextLine();
    System.out.println("what is your age: ");
    int age = scanner.nextInt();
    scanner.nextInt(); // VERY IMPORNANT
    System.out.println("what is your food: ");
    String food = scanner.nextLine();

    System.out.println("Hey " + name);
    System.out.println("Age " + age);
    System.out.println("food " + food);
    scanner.close();
  }
}
