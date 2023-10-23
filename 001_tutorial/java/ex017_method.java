public class ex017_method {

  public static void main(String[] args) {
    int x = 6;
    int y = 18;

    int z = add(x, y);

    System.out.println(z);
  }

  static int add(int x, int y) {
    int z = x + y;
    return z;
  }
}
