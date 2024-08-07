package entity;

import java.util.ArrayList;
import java.util.List;

public class Chefes {
    private String nome;
    private int idade;
    private double salario;
    private List<Funcionarios> listaDeFuncionarios = new ArrayList<>();

    public Chefes(String nome, int idade, double salario) {
        this.nome = nome;
        this.idade = idade;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public List<Funcionarios> getListaDeFuncionarios() {
        return listaDeFuncionarios;
    }

    public void setListaDeFuncionarios(List<Funcionarios> listaDeFuncionarios) {
        this.listaDeFuncionarios = listaDeFuncionarios;
    }

    @Override
    public String toString() {
        return "Chefes [nome=" + nome + ", idade=" + idade + ", salario=" + salario + ", Funcionarios="
                + listaDeFuncionarios + "]";
    }

    public void contratar(Funcionarios funcionario) {
        listaDeFuncionarios.add(funcionario);
    }

    public void demitir(Funcionarios funcionarioParaDemitir) {
        listaDeFuncionarios.removeIf(funcionario -> funcionario.getNome().equals(funcionarioParaDemitir.getNome()));
    }

}