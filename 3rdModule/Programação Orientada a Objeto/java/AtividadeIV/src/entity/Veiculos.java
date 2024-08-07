public class Veiculos {
    private String tipo;
    private double odometro;

    public Veiculos(String tipo, double odometro) {
        this.tipo = tipo;
        this.odometro = odometro;
    }

    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public double getOdometro() {
        return odometro;
    }
    public void setOdometro(double odometro) {
        this.odometro = odometro;
    }

    public void acelerar(double distancia){
        odometro += distancia;
    }

    public void re(double distancia){
        odometro -= distancia;
    }

    public double consultarOdometro(){
        return odometro;
    }

    public String consultarTipo(){
        return tipo;
    }
}
