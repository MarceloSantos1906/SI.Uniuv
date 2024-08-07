package application;

import java.util.Scanner;

import entity.Produto;

public class main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Produto produto1 = new Produto("Produto1", 5, 0);
        boolean loop = true;
        while (loop) {
            System.out.println("\nEstoque atual:");
            System.out.println(produto1.toString() + produto1.valorTotalEstoque());

            System.out.println("\nDeseja adicionar, remover Produtos ou mudar o preço do produto1? \n1 - Adicionar \n2 - Remover \n3 - Mudar preço \n4 - Sair");
            String resposta = scan.next();
            if (resposta.equals("1")) {
                System.out.println("Quantas Uniades do Produto1 deseja adicionar? ");
                int quantidade = scan.nextInt();
                produto1.adicionarProduto(quantidade);
            } else if (resposta.equals("2")) {
                int quantidade = (produto1.getQuantidade());
                if (quantidade >= 1) {
                    System.out.println("Quantas Uniades do Produto1 deseja remover? ");
                    quantidade = scan.nextInt();
                    int quantidadeTemporaria = ((produto1.getQuantidade() - quantidade));
                    if (quantidadeTemporaria >= 0) {
                        produto1.removerProduto(quantidade);
                    } else {
                        System.out.println("Não a produtos suficientes para serem removidos.");
                    }
                } else {
                    System.out.println("Não a produtos suficientes para serem removidos.");
                }
            } else if (resposta.equals("3")) {
                System.out.println("Qual o novo preço do Produto1? ");
                double preco = scan.nextDouble();
                if (preco >= 0) {
                    produto1.mudarPreco(preco);
                } else {
                    System.out.println("Preço invalido - Preço negativo ou igual a 0.");
                }
            } else if (resposta.equals("4")){
                loop = false;
            }
        }
        scan.close();
    }
}
