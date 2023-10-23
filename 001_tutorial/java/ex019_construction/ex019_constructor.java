package ex019_construction;

public class ex019_constructor {

  public static void main(String[] args) {
    Human elo = new Human("grzes", 34, 182.3);

    System.out.println(elo.name);
    System.out.println(elo.age);
    System.out.println(elo.height);
    elo.eat();

    System.out.println(elo);
  }
}
