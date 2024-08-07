package application;

import entity.Funcionario;
import entity.Gerente;
import entity.Motoboy;
import entity.Secretaria;

public class Main {
    public static void main(String[] args) {
        Funcionario objeFuncionario = new Funcionario("Maria", "98765432109", 1000);
        Funcionario objetoGerente = new Gerente("Carlos", "12345678901", 2000, 10);
        Funcionario objetoSecretaria = new Secretaria("Secretaria", "cpf", 1500, "12345");
        Funcionario objetoMotoboy = new Motoboy("Motoboy", "cpfMotoboy", 800, "7533155");
        System.out.println(objeFuncionario);
        System.out.println(objetoGerente);
        System.out.println(objetoSecretaria);
        System.out.println(objetoMotoboy);
        System.err.println("************");
        objeFuncionario.aumentarSalario(0.10);
        objetoGerente.aumentarSalario(0.10);
        objetoSecretaria.aumentarSalario(0.50);
        objetoMotoboy.aumentarSalario(1);
        System.out.println(objeFuncionario);
        System.out.println(objetoGerente);
        System.out.println(objetoSecretaria);
        System.out.println(objetoMotoboy);
    }
}
