public class Animais {
    private String tipo;
    private double peso;

    public Animais(String tipo, double peso) {
        this.tipo = tipo;
        this.peso = peso;
    }

    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public double getPeso() {
        return peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }

    public void alimentar(double quantidadeDeComida){
        peso += 0.003*quantidadeDeComida;
    }

    public void passear(double distancia){
        peso -= 0.05*distancia;
    }

    public double consultarPeso(){
        return peso;
    }

    public String consultarTipo(){
        return tipo;
    }
}
