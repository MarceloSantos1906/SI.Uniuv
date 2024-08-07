package entity;

public class Beber {
    private String nome;
    private double teorAlcoolico;
    private int quantidade;
    public Beber(String nome, double teorAlcoolico, int quantidade) {
        this.nome = nome;
        this.teorAlcoolico = teorAlcoolico;
        this.quantidade = quantidade;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getTeorAlcoolico() {
        return teorAlcoolico;
    }
    public void setTeorAlcoolico(double teorAlcoolico) {
        this.teorAlcoolico = teorAlcoolico;
    }
    public int getQuantidade() {
        return quantidade;
    }
    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }
}
