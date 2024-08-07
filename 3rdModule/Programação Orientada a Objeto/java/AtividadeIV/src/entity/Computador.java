public class Computador {
    public String marca;
    public String modelo;

    public Computador(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }
    public String getModelo() {
        return modelo;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String consultarMarca(){
        return marca;
    }

    public String consultarModelo(){
        return modelo;
    }
}