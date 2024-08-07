package entity;

public class Gerente extends Funcionario {
    private double tempoDeEmpresa;

    public Gerente(String nome, String cpf, double salario, double tempoDeEmpresa) {
        super(nome, cpf, salario);
        this.tempoDeEmpresa = tempoDeEmpresa;
    }

    public double getTempoDeEmpresa() {
        return tempoDeEmpresa;
    }

    public void setTempoDeEmpresa(double tempoDeEmpresa) {
        this.tempoDeEmpresa = tempoDeEmpresa;
    }

    @Override
    public String toString() {
        return super.toString() + ", tempoDeEmpresa=" + tempoDeEmpresa;
    }

    @Override
    public void aumentarSalario(double porcentagem) {
        double bonus = ((this.tempoDeEmpresa / 2) / 100);
        super.aumentarSalario(porcentagem + bonus);
    }
}
