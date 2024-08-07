package application;

import java.util.Scanner;
import entity.Retangulo;

public class main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Largura do retangulo: ");
        double largura = scan.nextDouble();
        System.out.println("Altura do retangulo: ");
        double altura = scan.nextDouble();
        Retangulo retangulo1 = new Retangulo(largura, altura);
        System.out.println(retangulo1.toString());
    }
}
