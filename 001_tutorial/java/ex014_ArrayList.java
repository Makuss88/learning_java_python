import java.util.ArrayList;

public class ex014_ArrayList {

  public static void main(String[] args) {
    ArrayList<String> list = new ArrayList<String>();

    list.add("dupa");
    list.add("dupaaa");
    list.add("dupaaaaaaaa");

    list.set(0, "pika");
    list.remove(2);
    list.clear();

    for (int i = 0; i < list.size(); i++) {
      System.out.println(list.get(i));
    }
  }
}
