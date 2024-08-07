package entity;

public class Pessoa {
    private String nome;
    private CPF cpf;

    public Pessoa(String nome) {
        this.nome = nome;
    }

    public void associarCpf(CPF cpf) {
        this.cpf = cpf;
        cpf.setPessoa(this);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public CPF getCpf() {
        return cpf;
    }

    public void setCpf(CPF cpf) {
        this.cpf = cpf;
    }

    @Override
    public String toString() {
        return "Pessoa [nome=" + nome + ", cpf=" + this.cpf + "]";
    }
}
