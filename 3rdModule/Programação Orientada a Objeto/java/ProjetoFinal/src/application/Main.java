package application;

import entity.enums.Comidas;
import entity.Caixa;
import entity.Chef;
import entity.Chefes;
import entity.Clientes;
import entity.Funcionarios;
import entity.Menu;
import entity.Motoboy;
import entity.Prato;
import entity.Zelador;

public class Main {
    public static void main(String[] args) {
        Chefes objetoChefes01 = new Chefes("Chefe 01", 58, 16000);
        System.out.println(objetoChefes01);
        Funcionarios objetoChef01 = new Chef("Chef", 30, 3000);
        Funcionarios objetoCaixa01 = new Caixa("Caixa", 23, 1200);
        Funcionarios objetoZelador01 = new Zelador("Zelador", 45, 1300);
        objetoChefes01.contratar(objetoChef01);
        objetoChefes01.contratar(objetoCaixa01);
        objetoChefes01.contratar(objetoZelador01);
        System.out.println(objetoChefes01);
        objetoChef01.adicionarMenu(Comidas.ARROZ);
        objetoChef01.adicionarMenu(Comidas.CARNE);
        objetoChef01.adicionarMenu(Comidas.FEIJAO);
        objetoChef01.montarPrato(13);
    }
}
