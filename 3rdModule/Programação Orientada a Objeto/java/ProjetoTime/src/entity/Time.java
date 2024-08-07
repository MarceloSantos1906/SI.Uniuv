package entity;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Time {
    private String nome;
    private String anoFundacao;
    private int vitorias;
    private int derrotas;

    private List<Jogador> listaJogador = new ArrayList<>();
    public Time(String nome, String anoFundacao) {
        this.nome = nome;
        this.anoFundacao = anoFundacao;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getAnoFundacao() {
        return anoFundacao;
    }
    public void setAnoFundacao(String anoFundacao) {
        this.anoFundacao = anoFundacao;
    }
    public int getVitorias() {
        return vitorias;
    }
    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }
    public int getDerrotas() {
        return derrotas;
    }
    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }
    public List<Jogador> getListaJogador() {
        return listaJogador;
    }
    public void setListaJogador(List<Jogador> listaJogador) {
        this.listaJogador = listaJogador;
    }
    @Override
    public String toString() {
        return "Time [nome=" + nome + ", anoFundacao=" + anoFundacao + ", vitorias=" + vitorias + ", derrotas="
                + derrotas + ", listaJogador=" + listaJogador + "]";
    }


    public void escalarJogador(Jogador jogador){
        listaJogador.add(jogador);
    }

    public void aumentarSalario(Jogador jogador, double salario){
        jogador.setSalario(jogador.getSalario() + salario);
    }

    public void jogar(){
        Random random = new Random();
        int resultado = random.nextInt(2);
        if (resultado == 0){
            this.derrotas += 1;
        } else {
            this.vitorias += 1;
        }
    }

    public Time falir(){
        return null;
    }

}
