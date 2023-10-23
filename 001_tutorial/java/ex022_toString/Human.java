package ex022_toString;

public class Human {

  String name;
  int age;
  double height;

  Human(String name, int age, double height) {
    this.name = name;
    this.age = age;
    this.height = height;
  }

  void eat() {
    System.out.println(this.name + " mniam mniam");
  }

  @Override
  public String toString() {
    return (
      "{" +
      "name='" +
      name +
      "'" +
      ", age='" +
      age +
      "'" +
      ", height='" +
      height +
      "'" +
      "}"
    );
  }
}
