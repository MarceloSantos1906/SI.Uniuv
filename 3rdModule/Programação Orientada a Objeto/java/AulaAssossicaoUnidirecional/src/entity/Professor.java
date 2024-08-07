package entity;

import java.util.ArrayList;
import java.util.List;

import entity.enums.Titulacao;

public class Professor {
    private String nome;
    private String formacao;
    private Titulacao titulacao;
    private int idade;
    private List<Aluno> listaDeAlunos = new ArrayList<>();

    public Professor(String nome, String formacao, Titulacao titulacao, int idade) {
        this.nome = nome;
        this.formacao = formacao;
        this.titulacao = titulacao;
        this.idade = idade;
    }
    public void associarAluno(Aluno aluno) {
        listaDeAlunos.add(aluno);
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getFormacao() {
        return formacao;
    }
    public void setFormacao(String formacao) {
        this.formacao = formacao;
    }
    public Titulacao getTitulacao() {
        return titulacao;
    }
    public void setTitulacao(Titulacao titulacao) {
        this.titulacao = titulacao;
    }
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }
    public List<Aluno> getListaDeAlunos() {
        return listaDeAlunos;
    }
    public void setListaDeAlunos(List<Aluno> listaDeAlunos) {
        this.listaDeAlunos = listaDeAlunos;
    }

    @Override
    public String toString() {
        return "Professor [nome=" + nome + ", formacao=" + formacao + ", titulacao=" + titulacao + ", idade=" + idade
                + ", listaDeAlunos=" + listaDeAlunos + "]";
    }
}
