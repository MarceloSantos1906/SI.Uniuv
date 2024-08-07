package application;

import entity.CPF;
import entity.Pessoa;

public class Main {
    public static void main(String[] args) {
        Pessoa objetoPessoa = new Pessoa("Marcelo");
        CPF objetoCPF = new CPF("12345");
        System.out.println(objetoPessoa);
        objetoPessoa.associarCpf(objetoCPF);
        System.out.println(objetoPessoa);
    }
}
