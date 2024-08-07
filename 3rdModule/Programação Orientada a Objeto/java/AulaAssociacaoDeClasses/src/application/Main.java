package application;

import entity.Pessoas;
import entity.Salgados;

public class Main {
    public static void main(String[] args) {
        Pessoas pessoa1 = new Pessoas("tset", 60, 0, 0);
        Salgados salgado1 = new Salgados("salgado1", 3.5, 10);
        System.out.println(pessoa1);
        pessoa1.comer(salgado1);
        System.out.println(pessoa1);
    }
}
