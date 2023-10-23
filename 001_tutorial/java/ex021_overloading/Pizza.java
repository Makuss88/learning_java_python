package ex021_overloading;

public class Pizza {

  String a;
  String bread;
  String sos;

  Pizza(String a, String bread, String sos) {
    this.a = a;
    this.bread = bread;
    this.sos = sos;
  }

  Pizza(String a, String bread) {
    this.a = a;
    this.bread = bread;
  }
}
