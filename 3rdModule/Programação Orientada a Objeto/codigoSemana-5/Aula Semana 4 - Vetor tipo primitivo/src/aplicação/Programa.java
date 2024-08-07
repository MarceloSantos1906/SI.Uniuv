package aplicação;
import java.util.Scanner;

public class Programa {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Ler a altura de quantas pessoas ?");
		int pessoas = sc.nextInt();
		double[] vetor = new double[pessoas];
		for (int i = 0; i < pessoas; i++) {
			System.out.println("Digite a altura ?");
			vetor[i] = sc.nextDouble();
		}
		double soma = 0;
		for (int i = 0; i < pessoas; i++) {
			soma += vetor[i];
		}
		double media = soma / pessoas;
		System.out.println("Média altura " + String.format("%.2f", media));
		//System.out.printf("Média alturas: %.2f%n", media);
		sc.close();

	}

}
