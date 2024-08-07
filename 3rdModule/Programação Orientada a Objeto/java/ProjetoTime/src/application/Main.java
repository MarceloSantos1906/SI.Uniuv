package application;

import entity.Jogador;
import entity.Time;

public class Main {
    public static void main(String[] args) {
        Jogador objetoJogador1 = new Jogador("Neymar", 30, "987654", "Atacante", 10000);
        Jogador objetoJogador2 = new Jogador("Bento", 24, "123456", "Goleiro", 2000);

        Time objetoTime1 = new Time("Brasil", "1930");

        objetoTime1.escalarJogador(objetoJogador1);
        objetoTime1.escalarJogador(objetoJogador2);
        for(int i = 0; i > 100; i++){
            objetoTime1.jogar();
        }
        System.out.println(objetoTime1);

    }
}
