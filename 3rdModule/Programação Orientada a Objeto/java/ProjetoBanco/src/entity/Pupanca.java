package entity;

public class Pupanca {
    private String conta;
    private double saldo;

    public Pupanca(String conta, double saldo) {
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
        return "Pupanca [conta=" + conta + ", saldo=R$" + saldo + "]";
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
