package application;

import entity.Banco;

public class Main {
    public static void main(String[] args) {
        Banco objetoBanco = new Banco("xy");
        objetoBanco.iniciarBanco();
        objetoBanco.abrirContaCorrente("12345", 200);
        System.out.println(objetoBanco);
        objetoBanco.getListaContaCorrentes().get(0).depositar(800);
        System.out.println(objetoBanco);
        objetoBanco.encerrarContas();
        System.out.println(objetoBanco);
        objetoBanco = null;
        System.out.println(objetoBanco);
    }
}
