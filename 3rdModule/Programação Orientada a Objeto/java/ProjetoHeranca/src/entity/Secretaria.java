package entity;

public class Secretaria extends Funcionario{
    private String senha;

    public Secretaria(String nome, String cpf, double salario, String senha) {
        super(nome, cpf, salario);
        this.senha = senha;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    @Override
    public String toString() {
        return super.toString() + ", senha=" + senha;
    }
}
