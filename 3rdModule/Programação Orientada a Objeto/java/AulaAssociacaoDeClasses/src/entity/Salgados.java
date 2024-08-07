package entity;

public class Salgados {
    private String nome;
    private double calorias;
    private int quantidade;
    public Salgados(String nome, double calorias, int quantidade) {
        this.nome = nome;
        this.calorias = calorias;
        this.quantidade = quantidade;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getCalorias() {
        return calorias;
    }
    public void setCalorias(double calorias) {
        this.calorias = calorias;
    }
    public int getQuantidade() {
        return quantidade;
    }
    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }
}
