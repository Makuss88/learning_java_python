package ex025_OOP;

public class Friend {

  String name;
  // int numberOfFriends; - its Wrong!!!!
  static int numberOfFriends;

  Friend(String name) {
    this.name = name;
    numberOfFriends++;
  }
}
