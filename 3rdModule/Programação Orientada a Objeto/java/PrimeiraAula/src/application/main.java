package application;
import entidade.Triangulo;

public class main {
    public static void main(String[] args) {
        Triangulo objTrianguloX = new Triangulo(3, 4, 5);
        Triangulo objTrianguloY = new Triangulo(7.5, 4.5, 4.02);
        double area = objTrianguloX.area();
        System.out.println(String.format("%.2f", area));

        area = objTrianguloY.area();
        System.out.println(String.format("%.2f", area));

        System.out.println(objTrianguloX.toString());
        System.err.println(objTrianguloX);
    }
}
