public class Pessoas {
    private String nome;
    private double peso;

    public Pessoas(String nome, double peso) {
        this.nome = nome;
        this.peso = peso;
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

    public void caminhar(double distancia){
        peso -= distancia*0.05;
    }

    public void correr(double distancia){
        peso -= distancia*0.1;
    }

    public double consultarPeso(){
        return peso;
    }

    public String consultarNome(){
        return nome;
    }

}