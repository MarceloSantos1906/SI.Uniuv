package entity;

public class ContaCorrente {
    private String conta;
    private double saldo;

    public ContaCorrente(String conta, double saldo) {
        this.conta = conta;
        this.saldo = saldo;
    }

    public String getConta() {
        return conta;
    }

    public void setConta(String conta) {
        this.conta = conta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    @Override
    public String toString() {
        return "ContaCorrente [conta=" + conta + ", saldo=R$" + saldo + "]";
    }

    public void depositar(double valor) {
        this.saldo += valor;
    }

    public void sacar(double valor) {
        this.saldo -= valor;
    }

    public void extrato() {
        System.out.println("*** Banco xy ***");
        System.out.println("*** saldo: R$" + this.saldo + " ***");
    }
}
