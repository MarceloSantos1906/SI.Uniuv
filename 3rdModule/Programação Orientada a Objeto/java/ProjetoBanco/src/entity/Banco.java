package entity;

import java.util.ArrayList;
import java.util.List;

public class Banco {
    private String nome;
    private List<ContaCorrente> listaContaCorrentes;
    private List<Pupanca> listaPupancas;

    public Banco(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public List<ContaCorrente> getListaContaCorrentes() {
        return listaContaCorrentes;
    }

    public void setListaContaCorrentes(List<ContaCorrente> listaContaCorrentes) {
        this.listaContaCorrentes = listaContaCorrentes;
    }

    public List<Pupanca> getListaPupancas() {
        return listaPupancas;
    }

    public void setListaPupancas(List<Pupanca> listaPupancas) {
        this.listaPupancas = listaPupancas;
    }

    @Override
    public String toString() {
        return "Banco [nome=" + nome + ", listaContaCorrentes=" + listaContaCorrentes + ", listaPupancas="
                + listaPupancas + "]";
    }

    public void iniciarBanco() {
        listaContaCorrentes = new ArrayList<>();
        listaPupancas = new ArrayList<>();
    }

    public void abrirContaCorrente(String conta, double valor) {
        ContaCorrente objetoContaCorrente = new ContaCorrente(conta, valor);
        listaContaCorrentes.add(objetoContaCorrente);
    }

    public void abrirPoupanca(String conta, double valor) {
        Pupanca objetoPoupanca = new Pupanca(conta, valor);
        listaPupancas.add(objetoPoupanca);
    }

    public void encerrarContas() {
        listaContaCorrentes = null;
        listaPupancas = null;
    }
}
