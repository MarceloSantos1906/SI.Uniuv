package entity;

public class Banco {
    private String nomeDoTitular;
    private int numeroDaConta;

    private double saldo;
    public Banco(int numeroDaConta, String nomeDoTitular, double saldo) {
        this.numeroDaConta = numeroDaConta;
        this.nomeDoTitular = nomeDoTitular;
        this.saldo = saldo;
    }
    public Banco(int numeroDaConta, String nomeDoTitular) {
        this.nomeDoTitular = nomeDoTitular;
        this.numeroDaConta = numeroDaConta;
    }
    public int getNumeroDaConta() {
        return numeroDaConta;
    }
    public String getNomeDoTitular() {
        return nomeDoTitular;
    }
    public void setNomeDoTitular(String nomeDoTitular) {
        this.nomeDoTitular = nomeDoTitular;
    }
    public double isSaldo() {
        return saldo;
    }
    private void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void NomeDoTitular(String nome){
        setNomeDoTitular(nome);
    }

    public void Depositar(double valor){
        setSaldo(isSaldo() + valor);
    }

    public void Sacar(double valor){
        setSaldo(isSaldo() - (valor + 5.0));
    }

    public String toString(){
        return "\nNumero da conta: " + getNumeroDaConta() + "\nNome do titular: " + getNomeDoTitular() + "\nSaldo: " + isSaldo();
    }

}
