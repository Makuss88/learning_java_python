package ex020_global;

import java.util.Random;

public class DiceRool {

  // global
  Random random;
  int number;

  DiceRool() {
    random = new Random();
    roll();
  }

  void roll() {
    number = random.nextInt(6) + 1;
    System.out.println(number);
  }
}
