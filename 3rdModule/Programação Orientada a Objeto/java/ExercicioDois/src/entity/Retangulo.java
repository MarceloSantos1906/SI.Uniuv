package entity;

public class Retangulo {
    double largura;
    double altura;
    public Retangulo(double largura, double altura) {
        this.largura = largura;
        this.altura = altura;
    }
    public double getLargura() {
        return largura;
    }
    public double getAltura() {
        return altura;
    }

    public double area(){
        double area = getAltura() * getLargura();
        return area;
    }

    public double perimetro(){
        double perimetro = (2 * getAltura()) + (2 * getLargura());
        return perimetro;
    }

    public double diagonal(){
        double diagonal = Math.sqrt((getAltura() * getAltura()) + (getLargura() * getLargura()));
        return diagonal;
    }

    public String toString(){
        return "Area: " + area() + "\nPerimetro: " + perimetro() + "\nDiagonal: " + diagonal();
    }
    
}
