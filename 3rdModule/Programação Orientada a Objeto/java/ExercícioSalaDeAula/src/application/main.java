package application;

import java.util.Scanner;
import entity.Banco;

public class main {
    public static void main(String[] args) {
    	boolean loop = true;
        Scanner scan = new Scanner(System.in);
        Banco conta1;
        System.out.print("Nome do titular: ");
        String nome = scan.nextLine();
        System.out.print("Numero da conta: ");
        int numeroDaConta = scan.nextInt();
        System.out.println("Deposito inicial? ");
        String depositoInicialString = scan.next().toLowerCase();
        if (depositoInicialString.equals("s") || depositoInicialString.equals("sim")) {
            System.out.println("Deposito inicial: ");
            double depositoInicial = scan.nextDouble();
            conta1 = new Banco(numeroDaConta, nome, depositoInicial);
        } else {
            conta1 = new Banco(numeroDaConta, nome);
        }
        System.out.println(conta1.toString());
        while (loop) {
            System.out.println("\nDepositando:");
            System.out.print("Valor para depositar: R$");
            double deposito = scan.nextDouble();
            conta1.Depositar(deposito);
            System.out.println(conta1.toString());

            System.out.println("\nSacando:");
            System.out.print("Valor para sacar: R$");
            double saque = scan.nextDouble();
            conta1.Sacar(saque);
            System.out.println(conta1.toString());

            System.out.println("\nTrocando nome do titular:");
            System.out.print("Novo nome do titular: ");
            nome = scan.next();
            conta1.NomeDoTitular(nome);
            System.out.println(conta1.toString());

            System.out.println("\nSair? ");
            String sair = scan.next().toLowerCase();
            if (sair.equals("s") || sair.equals("sair") || sair.equals("sim")) {
                loop = false;
            }
        }
        scan.close();
    }
}