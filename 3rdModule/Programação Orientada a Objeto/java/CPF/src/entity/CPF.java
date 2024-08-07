package entity;

public class CPF {
    private String cpf;
    private Pessoa pessoa;

    public CPF(String cpf) {
        this.cpf = cpf;
    }

    public String getcpf() {
        return cpf;
    }

    public void setcpf(String cpf) {
        this.cpf = cpf;
    }

    public Pessoa getPessoa() {
        return pessoa;
    }

    public void setPessoa(Pessoa pessoa) {
        this.pessoa = pessoa;
    }

    @Override
    public String toString() {
        return cpf;
    }
    

}