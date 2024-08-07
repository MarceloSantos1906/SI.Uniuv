package application;

import java.util.Scanner;

import entity.Funcionario;

public class main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("\nNome: ");
        String nome = scan.nextLine();
        System.out.print("Salario: R$");
        double salario = scan.nextDouble();
        System.out.print("Taxa: R$");
        double taxa = scan.nextDouble();

        Funcionario funcionario1 = new Funcionario(nome, salario, taxa);
        System.out.println(funcionario1.toString() + funcionario1.salarioLiquido());
        
        System.out.print("\nAumentar salario em: R$");
        double aumentarSalario = scan.nextDouble();
        funcionario1.aumentarSalario(aumentarSalario);
        System.out.println(funcionario1.toString() + funcionario1.salarioLiquido());
    }
}
