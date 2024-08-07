package entity;

import java.util.ArrayList;
import java.util.List;

import entity.enums.Comidas;

public class Chef extends Funcionarios {
    private List<Menu> listaMenu = new ArrayList<>();
    private List<Prato> listaPrato = new ArrayList<>();

    public Chef(String nome, int idade, double salario) {
        super(nome, idade, salario);
    }

    @Override
    public String toString() {
        return super.toString();
    }

    public void adicionarMenu(entity.enums.Comidas comida) {
        Menu obejetoMenu = new Menu(comida);
        listaMenu.add(obejetoMenu);
    }

    public void montarPrato(double preco){
        Prato objetoPrato01 = new Prato(preco);

    }
}
