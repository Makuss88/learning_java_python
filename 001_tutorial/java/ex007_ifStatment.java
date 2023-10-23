public class ex007_ifStatment {

  public static void main(String[] args) {
    int age = 58;
    if (age >= 75) {
      System.out.println("senior");
    } else if (age >= 18) {
      System.out.println("adult");
    } else if (age >= 13) {
      System.out.println("teen");
    } else {
      System.out.println("child");
    }
  }
}
