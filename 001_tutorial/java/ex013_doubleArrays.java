public class ex013_doubleArrays {

  public static void main(String[] args) {
    String[][] cars = {
      { "opel_1", "toyota_1", "Polonez_1" },
      { "opel_2", "toyota_2", "Polonez_2" },
      { "opel_3", "toyota_3", "Polonez_3" },
    };

    for (int i = 0; i < cars.length; i++) {
      System.out.println();
      for (int j = 0; j < cars[i].length; j++) {
        System.out.print(cars[i][j] + " ");
      }
    }
  }
}
