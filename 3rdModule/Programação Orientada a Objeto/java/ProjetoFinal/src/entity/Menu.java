package entity;

import entity.enums.Comidas;

public class Menu{
    private Comidas comida;

    public Menu(Comidas comida) {
        this.comida = comida;
    }

    public Comidas getComida() {
        return comida;
    }

    public void setComida(Comidas comida) {
        this.comida = comida;
    }

    @Override
    public String toString() {
        return "Prato [comida=" + comida + "]";
    }
}
