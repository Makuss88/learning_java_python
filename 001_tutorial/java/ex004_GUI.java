import javax.swing.JOptionPane;

public class ex004_GUI {

  public static void main(String[] args) {
    String name = JOptionPane.showInputDialog("show name");
    JOptionPane.showMessageDialog(null, "Hello " + name);

    int age = Integer.parseInt(JOptionPane.showInputDialog("show age"));
    JOptionPane.showMessageDialog(null, "Age " + age);

    double height = Double.parseDouble(
      JOptionPane.showInputDialog("show height")
    );
    JOptionPane.showMessageDialog(null, "Heigth " + height);
  }
}
