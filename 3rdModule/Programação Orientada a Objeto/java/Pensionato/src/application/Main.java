package application;

import java.util.Scanner;

import entity.Pensionato;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Quantos quartos serao alugados?");
        int quantidadeDeAlunos = scan.nextInt();
        Pensionato[] vetorAlunos = new Pensionato[10];
        for (int i = 0; i < quantidadeDeAlunos; i++){
            scan.nextLine();
            System.out.print("\nDigite o nome do aluno: ");
            String nome = scan.nextLine();
            System.out.print("Digite o email de " + nome + ": ");
            String email = scan.nextLine();
            System.out.print("Digite o quarto que " + nome + " deseja: ");
            int numeroQuarto = scan.nextInt();
            vetorAlunos[numeroQuarto] = new Pensionato(nome, email, numeroQuarto);
        }
        System.out.println();
        for (int i = 0; i < 10; i++){
            if (vetorAlunos[i] != null){
                System.out.println(vetorAlunos[i].toString());
            }
        }
        scan.close();
    }
}
