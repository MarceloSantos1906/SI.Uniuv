package entity;

public class Clientes {
    private String nome;

    public Clientes(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Clientes [nome=" + nome + "]";
    }

    public void pedirPrato(Prato prato, Caixa funcionario) {
        funcionario.cobrar(prato.getPreco());
    }
}
