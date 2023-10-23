import java.util.ArrayList;

public class ex015_DoubleArrayList {

  public static void main(String[] args) {
    ArrayList<String> bakeList = new ArrayList<String>();

    bakeList.add("aaa");
    bakeList.add("bbb");
    bakeList.add("ccc");
        bakeList.add("ddd");


    ArrayList<String> makeList = new ArrayList<String>();

    makeList.add("doopa");
    makeList.add("eeee");
    makeList.add("giwno");

    ArrayList<String> drinkList = new ArrayList<String>();

    drinkList.add("mohito");
    drinkList.add("rum");
    drinkList.add("tequila");

    ArrayList<ArrayList<String>> list = new ArrayList<ArrayList<String>>();

    list.add(bakeList);
    list.add(makeList);
    list.add(drinkList);

    System.out.println(list);
  }
}
