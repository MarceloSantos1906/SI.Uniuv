package entity;

public class Pessoas {
    private String nome;
    private double peso;
    private double teorAlcoolico;
    private double nivelDeDiversao;
    public Pessoas(String nome, double peso, double teorAlcoolico, double nivelDeDiversao) {
        this.nome = nome;
        this.peso = peso;
        this.teorAlcoolico = teorAlcoolico;
        this.nivelDeDiversao = nivelDeDiversao;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getPeso() {
        return peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }
    public double getTeorAlcoolico() {
        return teorAlcoolico;
    }
    public void setTeorAlcoolico(double teorAlcoolico) {
        this.teorAlcoolico = teorAlcoolico;
    }
    public double getNivelDeDiversao() {
        return nivelDeDiversao;
    }
    public void setNivelDeDiversao(double nivelDeDiversao) {
        this.nivelDeDiversao = nivelDeDiversao;
    }
    
    public void comer(){
        this.peso += (Salgados.getCalorias()) + getPeso();
        Salgados.setQuantidade((Salgados.getQuantidade) - 1);
    }

    @Override
    public String toString() {
        return "Pessoas [nome=" + nome + ", peso=" + peso + ", teorAlcoolico=" + teorAlcoolico + ", nivelDeDiversao="
                + nivelDeDiversao + "]";
    }
}
