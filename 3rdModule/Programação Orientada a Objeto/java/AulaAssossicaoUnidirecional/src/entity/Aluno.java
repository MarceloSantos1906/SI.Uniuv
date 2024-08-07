package entity;

import java.util.ArrayList;
import java.util.List;

public class Aluno {
    private String nome;
    private String matricula;
    private int idade;
    private List<Professor> listaDeProfessores = new ArrayList<>();

    public Aluno(String nome, String matricula, int idade) {
        this.nome = nome;
        this.matricula = matricula;
        this.idade = idade;
    }
    public void associarProfessor(Professor professor) {
        listaDeProfessores.add(professor);
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getMatricula() {
        return matricula;
    }
    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }
    public List<Professor> getListaDeProfessores() {
        return listaDeProfessores;
    }

    public void setListaDeProfessores(List<Professor> listaDeProfessores) {
        this.listaDeProfessores = listaDeProfessores;
    }

    @Override
    public String toString() {
        return "Alunos [nome=" + nome + ", matricula=" + matricula + ", idade=" + idade + ", listaDeProfessores="
                + listaDeProfessores + "]";
    }
}
