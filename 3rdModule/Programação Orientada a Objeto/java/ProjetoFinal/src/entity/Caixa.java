package entity;

public class Caixa extends Funcionarios {
    private double caixa;
    public Caixa (String nome, int idade, double salario){
        super(nome, idade, salario);
        this.caixa = 0;
    }

    public double getCaixa() {
        return caixa;
    }

    public void setCaixa(double caixa) {
        this.caixa = caixa;
    }

    public void cobrar(double valor){
        this.caixa += this.caixa + valor;
    }
    @Override
    public String toString() {
        return super.toString() + "Caixa Atual= R$" + this.caixa;
    }

}
