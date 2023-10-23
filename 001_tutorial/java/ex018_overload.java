public class ex018_overload {

  public static void main(String[] args) {
    int result = add(1, 2, 6, 8, 7);
    System.out.println(result);
  }

  static int add(int x, int y) {
    int z = x + y;
    return z;
  }

  static int add(int x, int y, int c) {
    int z = x + y + c;
    return z;
  }

  static int add(int x, int y, int c, int d) {
    int z = x + y + c + d;
    return z;
  }

  static int add(int x, int y, int c, int d, int e) {
    int z = x + y + c + d + e;
    return z;
  }
}
