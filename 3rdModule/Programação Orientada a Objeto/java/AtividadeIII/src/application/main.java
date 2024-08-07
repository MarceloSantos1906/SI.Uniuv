public class main {
    public static void main(String[] args){
        System.out.println("Criando os objetos com seus valores iniciais:");
        Conta conta1 = new Conta("123-4", 1000.00);
        System.out.println("Nº da Conta: " + conta1.consultarConta() + "\nSaldo: " + conta1.consultarSaldo() + "\n");

        Conta conta2 = new Conta("567-8", 5000.00);
        System.out.println("Nº da Conta: " + conta2.consultarConta() + "\nSaldo: " + conta2.consultarSaldo() + "\n");

        System.out.println("Debitar conta1 e creditar conta2:");
        conta1.debitar(100.00);
        System.out.println("Nº da Conta: " + conta1.consultarConta() + "\nSaldo: " + conta1.consultarSaldo() + "\n");

        conta2.creditar(500.00);
        System.out.println("Nº da Conta: " + conta2.consultarConta() + "\nSaldo: " + conta2.consultarSaldo() + "\n");
    }
}
