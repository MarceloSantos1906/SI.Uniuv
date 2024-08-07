package entity;

import java.util.ArrayList;
import java.util.List;

public class Prato {
    private double preco;
    private List<Menu> comidaNoPrato = new ArrayList<>();

    public Prato(double preco) {
        this.preco = preco;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    @Override
    public String toString() {
        return "Prato [comidaNoPrato=" + comidaNoPrato + "]";
    }

    public void adicionarComida(Menu comida){
        this.comidaNoPrato.add(comida);
    }


}
