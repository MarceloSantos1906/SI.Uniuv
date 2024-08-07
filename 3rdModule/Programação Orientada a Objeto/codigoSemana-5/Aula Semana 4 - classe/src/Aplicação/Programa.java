package Aplicação;

import java.util.Scanner;

import entidades.Pessoas;

public class Programa {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite a quantidade de pessoas: ");
		int pessoas = sc.nextInt();
		Pessoas[] vetorPessoas = new Pessoas[pessoas];
		for (int i = 0; i < vetorPessoas.length; i++) {
			sc.nextLine();
			System.out.println("Digite o nome: ");
			String nome = sc.nextLine();
			System.out.println("Digite a idade: ");
			int idade = sc.nextInt();
			vetorPessoas[i] = new Pessoas(nome, idade);
		}
		double soma = 0;
		for (int i = 0; i < vetorPessoas.length; i++) {
			soma += vetorPessoas[i].getIdade();
		}
		double media = soma / vetorPessoas.length;
		System.out.printf("Média idade = %.2f%n", media);
		sc.close();

	}

}
